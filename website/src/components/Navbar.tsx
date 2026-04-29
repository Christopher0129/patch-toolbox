import { useState, useCallback } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Shield,
  Globe,
  Menu,
  X,
  ChevronDown,
  Bug,
  Wrench,
  ExternalLink,
  Star,
} from 'lucide-react';
import { useTranslation, LANGUAGE_NAMES, type Language } from '@/i18n/LanguageContext';

const languages: Language[] = ['en', 'zh', 'fr', 'ja', 'ko'];
const langCodes: Record<Language, string> = {
  en: 'EN',
  zh: '中',
  fr: 'FR',
  ja: '日',
  ko: 'KO',
};

export default function Navbar() {
  const { t, lang, setLang } = useTranslation();
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [categoriesOpen, setCategoriesOpen] = useState(false);
  const [langOpen, setLangOpen] = useState(false);

  const isActive = useCallback(
    (path: string) => location.pathname === path,
    [location],
  );

  const closeAll = () => {
    setCategoriesOpen(false);
    setLangOpen(false);
    setMobileOpen(false);
  };

  return (
    <>
      <nav
        className="fixed top-0 left-0 right-0 z-50 h-16 border-b border-border-subtle"
        style={{ backgroundColor: 'rgba(10,14,23,0.85)', backdropFilter: 'blur(12px)' }}
      >
        <div className="mx-auto flex h-full max-w-[1200px] items-center justify-between px-6">
          {/* Left: Brand */}
          <Link to="/" className="flex items-center gap-2 text-text-primary hover:opacity-90">
            <Shield className="h-6 w-6 text-accent-blue" />
            <span className="font-mono text-base font-medium tracking-tight">
              {t('navbar.brand') as string}
            </span>
          </Link>

          {/* Center: Nav Links (desktop) */}
          <div className="hidden items-center gap-1 md:flex">
            <NavLink to="/" active={isActive('/')}>
              {t('navbar.home') as string}
            </NavLink>

            {/* Categories Dropdown */}
            <div className="relative">
              <button
                onClick={() => setCategoriesOpen(!categoriesOpen)}
                className="flex items-center gap-1 rounded-md px-3 py-2 text-sm text-text-secondary transition-colors hover:text-text-primary"
              >
                {t('navbar.categories') as string}
                <ChevronDown
                  className={`h-4 w-4 transition-transform ${categoriesOpen ? 'rotate-180' : ''}`}
                />
              </button>
              <AnimatePresence>
                {categoriesOpen && (
                  <motion.div
                    initial={{ opacity: 0, y: -8 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -8 }}
                    transition={{ duration: 0.2, ease: 'easeOut' }}
                    className="absolute left-0 top-full mt-2 w-64 overflow-hidden rounded-lg border border-border-subtle bg-bg-surface shadow-xl"
                  >
                    <div className="p-2">
                      <DropdownItem
                        icon={<Shield className="h-4 w-4 text-accent-blue" />}
                        label={t('navbar.networkSecurity') as string}
                        badge="452"
                        to="/network-security"
                        onClick={closeAll}
                      />
                      <DropdownItem
                        icon={<Bug className="h-4 w-4 text-accent-orange" />}
                        label={t('navbar.systemVulnerabilities') as string}
                        badge="OS"
                        to="/system-vulnerabilities"
                        onClick={closeAll}
                      />
                      <DropdownItem
                        icon={<Wrench className="h-4 w-4 text-accent-green" />}
                        label={t('navbar.systemTroubleshooting') as string}
                        badge="Solutions"
                        to="/system-troubleshooting"
                        onClick={closeAll}
                      />
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            <NavLink to="/about" active={isActive('/about')}>
              {t('navbar.about') as string}
            </NavLink>
            <NavLink to="/contributing" active={isActive('/contributing')}>
              {t('navbar.contributing') as string}
            </NavLink>
          </div>

          {/* Right: Language + GitHub */}
          <div className="hidden items-center gap-3 md:flex">
            {/* Language Switcher */}
            <div className="relative">
              <button
                onClick={() => setLangOpen(!langOpen)}
                className="flex items-center gap-1.5 rounded-md px-2 py-1.5 text-xs font-medium text-text-muted transition-colors hover:text-text-primary"
              >
                <Globe className="h-4 w-4" />
                <span>{langCodes[lang]}</span>
              </button>
              <AnimatePresence>
                {langOpen && (
                  <motion.div
                    initial={{ opacity: 0, y: -8 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -8 }}
                    transition={{ duration: 0.2, ease: 'easeOut' }}
                    className="absolute right-0 top-full mt-2 w-44 overflow-hidden rounded-lg border border-border-subtle bg-bg-surface shadow-xl"
                  >
                    <div className="p-1">
                      {languages.map((l) => (
                        <button
                          key={l}
                          onClick={() => {
                            setLang(l);
                            setLangOpen(false);
                          }}
                          className={`flex w-full items-center gap-2 rounded-md px-3 py-2 text-left text-sm transition-colors ${
                            lang === l
                              ? 'bg-bg-elevated text-accent-blue'
                              : 'text-text-secondary hover:bg-bg-elevated hover:text-text-primary'
                          }`}
                        >
                          <span
                            className={`h-full w-0.5 rounded-full ${lang === l ? 'bg-accent-blue' : 'bg-transparent'}`}
                            style={{ height: '16px' }}
                          />
                          <span>{LANGUAGE_NAMES[l]}</span>
                        </button>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            <a
              href="https://github.com/Christopher0129/patch-toolbox"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-1.5 rounded-md border border-border-active px-3 py-1.5 text-xs font-medium text-text-secondary transition-all hover:border-text-muted hover:text-text-primary"
            >
              <Star className="h-3.5 w-3.5" />
              Star
            </a>
          </div>

          {/* Mobile hamburger */}
          <button
            className="flex items-center text-text-secondary md:hidden"
            onClick={() => setMobileOpen(!mobileOpen)}
          >
            {mobileOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>
      </nav>

      {/* Mobile Drawer */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, x: '100%' }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: '100%' }}
            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            className="fixed inset-y-0 right-0 z-[60] w-72 border-l border-border-subtle bg-bg-surface pt-16 shadow-2xl md:hidden"
          >
            <div className="flex flex-col gap-1 p-4">
              <MobileLink to="/" onClick={closeAll}>
                {t('navbar.home') as string}
              </MobileLink>
              <MobileLink to="/network-security" onClick={closeAll}>
                {t('navbar.networkSecurity') as string}
              </MobileLink>
              <MobileLink to="/system-vulnerabilities" onClick={closeAll}>
                {t('navbar.systemVulnerabilities') as string}
              </MobileLink>
              <MobileLink to="/system-troubleshooting" onClick={closeAll}>
                {t('navbar.systemTroubleshooting') as string}
              </MobileLink>
              <MobileLink to="/about" onClick={closeAll}>
                {t('navbar.about') as string}
              </MobileLink>
              <MobileLink to="/contributing" onClick={closeAll}>
                {t('navbar.contributing') as string}
              </MobileLink>

              <div className="my-4 border-t border-border-subtle" />

              <p className="px-3 py-2 text-xs font-medium uppercase tracking-wider text-text-muted">
                Language / 语言
              </p>
              {languages.map((l) => (
                <button
                  key={l}
                  onClick={() => {
                    setLang(l);
                    closeAll();
                  }}
                  className={`flex items-center gap-2 rounded-md px-3 py-2 text-left text-sm transition-colors ${
                    lang === l
                      ? 'bg-bg-elevated text-accent-blue'
                      : 'text-text-secondary hover:bg-bg-elevated hover:text-text-primary'
                  }`}
                >
                  <span
                    className={`h-4 w-0.5 rounded-full ${lang === l ? 'bg-accent-blue' : 'bg-transparent'}`}
                  />
                  {LANGUAGE_NAMES[l]}
                </button>
              ))}

              <div className="my-4 border-t border-border-subtle" />

              <a
                href="https://github.com/Christopher0129/patch-toolbox"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-text-secondary transition-colors hover:text-text-primary"
              >
                <ExternalLink className="h-4 w-4" />
                {t('navbar.github') as string}
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Backdrop for mobile */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="fixed inset-0 z-[55] bg-black/50 md:hidden"
            onClick={() => setMobileOpen(false)}
          />
        )}
      </AnimatePresence>
    </>
  );
}

function NavLink({
  to,
  active,
  children,
}: {
  to: string;
  active: boolean;
  children: React.ReactNode;
}) {
  return (
    <Link
      to={to}
      className={`relative rounded-md px-3 py-2 text-sm transition-colors ${
        active ? 'text-text-primary' : 'text-text-secondary hover:text-text-primary'
      }`}
    >
      {children}
      {active && (
        <span className="absolute bottom-0 left-3 right-3 h-px bg-accent-blue" />
      )}
    </Link>
  );
}

function MobileLink({
  to,
  onClick,
  children,
}: {
  to: string;
  onClick: () => void;
  children: React.ReactNode;
}) {
  const location = useLocation();
  const active = location.pathname === to;
  return (
    <Link
      to={to}
      onClick={onClick}
      className={`rounded-md px-3 py-2 text-sm transition-colors ${
        active
          ? 'bg-bg-elevated text-accent-blue'
          : 'text-text-secondary hover:bg-bg-elevated hover:text-text-primary'
      }`}
    >
      {children}
    </Link>
  );
}

function DropdownItem({
  icon,
  label,
  badge,
  to,
  onClick,
}: {
  icon: React.ReactNode;
  label: string;
  badge: string;
  to: string;
  onClick: () => void;
}) {
  return (
    <Link
      to={to}
      onClick={onClick}
      className="flex items-center gap-3 rounded-md px-3 py-2.5 text-sm text-text-secondary transition-colors hover:bg-bg-elevated hover:text-text-primary"
    >
      {icon}
      <span className="flex-1">{label}</span>
      <span className="rounded bg-bg-elevated px-1.5 py-0.5 text-[10px] font-medium text-text-muted">
        {badge}
      </span>
    </Link>
  );
}
