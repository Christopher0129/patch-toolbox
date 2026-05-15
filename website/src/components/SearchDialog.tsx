import { useState, useEffect, useRef, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, X, FileText, Shield, Bug, Wrench, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useTranslation } from '@/i18n/LanguageContext';
import { loadSearchIndex } from '@/lib/search';
import { cn } from '@/lib/utils';

/* ─── Types ─── */
interface SearchHit {
  slug: string;
  title: string;
  category: string;
  keywords: string;
}

const CATEGORY_META: Record<string, { icon: React.ReactNode; route: string; color: string }> = {
  'network-security': {
    icon: <Shield className="h-3.5 w-3.5" />,
    route: '/network-security',
    color: 'text-accent-blue',
  },
  'system-vulnerabilities': {
    icon: <Bug className="h-3.5 w-3.5" />,
    route: '/system-vulnerabilities',
    color: 'text-accent-orange',
  },
  'system-troubleshooting': {
    icon: <Wrench className="h-3.5 w-3.5" />,
    route: '/system-troubleshooting',
    color: 'text-accent-green',
  },
};

interface SearchDialogProps {
  open: boolean;
  onClose: () => void;
}

export default function SearchDialog({ open, onClose }: SearchDialogProps) {
  const { t } = useTranslation();
  const [query, setQuery] = useState('');
  const [index, setIndex] = useState<SearchHit[]>([]);
  const [loaded, setLoaded] = useState(false);
  const [selectedIdx, setSelectedIdx] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  // Load search index
  useEffect(() => {
    if (open && !loaded) {
      loadSearchIndex()
        .then((data: SearchHit[]) => {
          setIndex(data);
          setLoaded(true);
        })
        .catch(() => {});
    }
  }, [open, loaded]);

  // Focus input when dialog opens
  useEffect(() => {
    if (open) {
      // Small delay to let the animation start
      const t = setTimeout(() => inputRef.current?.focus(), 100);
      return () => clearTimeout(t);
    }
  }, [open]);

  // Reset selection when results change
  useEffect(() => {
    setSelectedIdx(0);
  }, [query]);

  // Filter results
  const results = (() => {
    if (!query.trim()) return index.slice(0, 50);
    const q = query.toLowerCase();
    return index
      .filter(
        (hit) =>
          hit.title.toLowerCase().includes(q) ||
          hit.keywords.toLowerCase().includes(q) ||
          hit.slug.toLowerCase().includes(q),
      )
      .slice(0, 100);
  })();

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        setSelectedIdx((prev) => Math.min(prev + 1, results.length - 1));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setSelectedIdx((prev) => Math.max(prev - 1, 0));
      } else if (e.key === 'Enter' && results[selectedIdx]) {
        e.preventDefault();
        const hit = results[selectedIdx];
        const meta = CATEGORY_META[hit.category];
        if (meta) {
          onClose();
          // Navigate - we use window.location to force a full page refresh for the anchor
          window.location.href = meta.route;
        }
      } else if (e.key === 'Escape') {
        onClose();
      }
    },
    [results, selectedIdx, onClose],
  );

  // Format title for display (remove slug prefix noise)
  const formatTitle = (title: string) => {
    // If it looks like a CVE, make it stand out
    if (/^CVE-\d{4}/.test(title) || /^GHSA-/.test(title) || /^EDB-/.test(title)) {
      return title;
    }
    return title.length > 60 ? title.slice(0, 60) + '…' : title;
  };

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          className="fixed inset-0 z-[80] flex items-start justify-center pt-[15vh]"
          style={{ backgroundColor: 'rgba(0,0,0,0.7)', backdropFilter: 'blur(4px)' }}
          onClick={onClose}
        >
          <motion.div
            initial={{ opacity: 0, scale: 0.96, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.96, y: -10 }}
            transition={{
              duration: 0.2,
              ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
            }}
            onClick={(e) => e.stopPropagation()}
            className="w-full max-w-[640px] overflow-hidden rounded-2xl border border-border-subtle bg-bg-surface shadow-2xl"
          >
            {/* Search Input */}
            <div className="flex items-center gap-3 border-b border-border-subtle px-5 py-4">
              <Search className="h-5 w-5 shrink-0 text-text-muted" />
              <input
                ref={inputRef}
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={t('searchDialog.placeholder') as string}
                className="flex-1 bg-transparent text-base text-text-primary outline-none placeholder:text-text-muted"
              />
              <kbd className="hidden shrink-0 rounded-md border border-border-subtle bg-bg-elevated px-2 py-0.5 text-[11px] text-text-muted sm:inline-block">
                ESC
              </kbd>
              <button
                onClick={onClose}
                className="shrink-0 rounded-md p-1 text-text-muted hover:bg-bg-elevated hover:text-text-primary sm:hidden"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            {/* Results */}
            <div className="max-h-[60vh] overflow-y-auto">
              {results.length === 0 ? (
                <div className="flex flex-col items-center py-20 text-text-muted">
                  <Search className="h-10 w-10 mb-3 opacity-50" />
                  <p className="text-sm">{t('searchDialog.noResults') as string}</p>
                  <p className="mt-1 text-xs">{t('searchDialog.noResultsHint') as string}</p>
                </div>
              ) : (
                <ul className="py-2">
                  {results.map((hit, idx) => {
                    const meta = CATEGORY_META[hit.category] || {
                      icon: <FileText className="h-3.5 w-3.5" />,
                      route: '#',
                      color: 'text-text-muted',
                    };
                    const isSelected = idx === selectedIdx;
                    return (
                      <li key={hit.slug}>
                        <Link
                          to={meta.route}
                          onClick={onClose}
                          className={cn(
                            'flex items-center gap-3 px-5 py-3 text-sm transition-colors',
                            isSelected
                              ? 'bg-bg-elevated'
                              : 'hover:bg-bg-elevated/60',
                          )}
                        >
                          <span className={cn('shrink-0', meta.color)}>
                            {meta.icon}
                          </span>
                          <div className="min-w-0 flex-1">
                            <span className="block truncate text-text-primary">
                              {formatTitle(hit.title)}
                            </span>
                            <span className="mt-0.5 block truncate text-[11px] text-text-muted">
                              {hit.slug}
                            </span>
                          </div>
                          <span
                            className={cn(
                              'shrink-0 rounded px-1.5 py-0.5 text-[10px] font-medium capitalize',
                              meta.color,
                            )}
                            style={{
                              backgroundColor: isSelected
                                ? 'rgba(59,130,246,0.1)'
                                : 'rgba(100,116,139,0.1)',
                            }}
                          >
                            {hit.category.replace(/-/g, ' ')}
                          </span>
                          <ArrowRight
                            className={cn(
                              'h-3.5 w-3.5 shrink-0 text-text-muted transition-opacity',
                              isSelected ? 'opacity-100' : 'opacity-0',
                            )}
                          />
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              )}

              {/* Footer hint */}
              <div className="flex items-center gap-4 border-t border-border-subtle px-5 py-3 text-xs text-text-muted">
                <span className="flex items-center gap-1">
                  <kbd className="rounded border border-border-subtle bg-bg-elevated px-1.5 py-0.5 text-[10px]">↑↓</kbd>
                  <span>{t('searchDialog.navigate') as string}</span>
                </span>
                <span className="flex items-center gap-1">
                  <kbd className="rounded border border-border-subtle bg-bg-elevated px-1.5 py-0.5 text-[10px]">↵</kbd>
                  <span>{t('searchDialog.open') as string}</span>
                </span>
                <span className="flex items-center gap-1">
                  <kbd className="rounded border border-border-subtle bg-bg-elevated px-1.5 py-0.5 text-[10px]">ESC</kbd>
                  <span>{t('searchDialog.close') as string}</span>
                </span>
              </div>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
