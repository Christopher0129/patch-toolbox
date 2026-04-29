import { Link } from 'react-router-dom';
import { Shield, Github, ExternalLink } from 'lucide-react';
import { useTranslation, LANGUAGE_NAMES, type Language } from '@/i18n/LanguageContext';

const languages: Language[] = ['en', 'zh', 'fr', 'ja', 'ko'];

export default function Footer() {
  const { t, lang, setLang } = useTranslation();

  return (
    <footer className="border-t border-border-subtle bg-bg-base">
      <div className="mx-auto max-w-[1200px] px-6 py-16">
        <div className="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-4">
          {/* Column 1: Project */}
          <div className="space-y-4">
            <div className="flex items-center gap-2 text-text-primary">
              <Shield className="h-5 w-5 text-accent-blue" />
              <span className="font-mono text-sm font-medium">patch-toolbox</span>
            </div>
            <p className="text-sm leading-relaxed text-text-secondary">
              {t('footer.description') as string}
            </p>
            <a
              href="https://github.com/Christopher0129/patch-toolbox"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-sm text-accent-blue transition-colors hover:text-accent-cyan"
            >
              <Github className="h-4 w-4" />
              github.com/Christopher0129/patch-toolbox
            </a>
          </div>

          {/* Column 2: Categories */}
          <div className="space-y-4">
            <h4 className="text-xs font-medium uppercase tracking-wider text-text-muted">
              {t('footer.categories') as string}
            </h4>
            <ul className="space-y-2.5">
              <li>
                <Link
                  to="/network-security"
                  className="text-sm text-text-secondary transition-colors hover:text-text-primary"
                >
                  {t('navbar.networkSecurity') as string}
                </Link>
              </li>
              <li>
                <Link
                  to="/system-vulnerabilities"
                  className="text-sm text-text-secondary transition-colors hover:text-text-primary"
                >
                  {t('navbar.systemVulnerabilities') as string}
                </Link>
              </li>
              <li>
                <Link
                  to="/system-troubleshooting"
                  className="text-sm text-text-secondary transition-colors hover:text-text-primary"
                >
                  {t('navbar.systemTroubleshooting') as string}
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Resources */}
          <div className="space-y-4">
            <h4 className="text-xs font-medium uppercase tracking-wider text-text-muted">
              {t('footer.resources') as string}
            </h4>
            <ul className="space-y-2.5">
              <li>
                <Link
                  to="/about"
                  className="text-sm text-text-secondary transition-colors hover:text-text-primary"
                >
                  {t('footer.architecture') as string}
                </Link>
              </li>
              <li>
                <Link
                  to="/contributing"
                  className="text-sm text-text-secondary transition-colors hover:text-text-primary"
                >
                  {t('navbar.contributing') as string}
                </Link>
              </li>
              <li>
                <a
                  href="https://github.com/Christopher0129/patch-toolbox/blob/main/LICENSE"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 text-sm text-text-secondary transition-colors hover:text-text-primary"
                >
                  {t('footer.license') as string}
                  <ExternalLink className="h-3 w-3" />
                </a>
              </li>
            </ul>
          </div>

          {/* Column 4: Language */}
          <div className="space-y-4">
            <h4 className="text-xs font-medium uppercase tracking-wider text-text-muted">
              {t('footer.language') as string}
            </h4>
            <div className="grid grid-cols-2 gap-2">
              {languages.map((l) => (
                <button
                  key={l}
                  onClick={() => setLang(l)}
                  className={`rounded-md px-3 py-2 text-left text-sm transition-colors ${
                    lang === l
                      ? 'bg-bg-elevated text-accent-blue'
                      : 'text-text-secondary hover:bg-bg-elevated hover:text-text-primary'
                  }`}
                >
                  {LANGUAGE_NAMES[l]}
                </button>
              ))}
            </div>
            <a
              href="https://github.com/Christopher0129/patch-toolbox"
              target="_blank"
              rel="noopener noreferrer"
              className="mt-2 inline-flex items-center gap-1.5 rounded-md border border-border-active px-3 py-1.5 text-xs text-text-secondary transition-colors hover:border-text-muted hover:text-text-primary"
            >
              <Github className="h-3.5 w-3.5" />
              Star
            </a>
          </div>
        </div>
      </div>

      {/* Bottom bar */}
      <div className="border-t border-border-subtle">
        <div className="mx-auto flex max-w-[1200px] flex-col items-center justify-between gap-2 px-6 py-4 sm:flex-row">
          <p className="text-xs text-text-muted">
            MIT License | {t('footer.maintainedBy') as string}
          </p>
          <p className="text-xs text-text-muted">{t('footer.tagline') as string}</p>
        </div>
      </div>
    </footer>
  );
}
