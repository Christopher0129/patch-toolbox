import { createContext, useContext, useState, useCallback, useEffect, type ReactNode } from 'react';

export type Language = 'zh' | 'en' | 'fr' | 'ja' | 'ko';

interface LanguageContextType {
  lang: Language;
  setLang: (lang: Language) => void;
  t: (key: string) => string | Record<string, unknown>;
}

const LanguageContext = createContext<LanguageContextType | null>(null);

const STORAGE_KEY = 'patch-toolbox-lang';

const LANGUAGE_NAMES: Record<Language, string> = {
  zh: '中文',
  en: 'English',
  fr: 'Français',
  ja: '日本語',
  ko: '한국어',
};

function detectBrowserLanguage(): Language {
  const browserLang = typeof navigator !== 'undefined' ? navigator.language : 'en';
  const code = browserLang.split('-')[0];
  if (code === 'zh') return 'zh';
  if (code === 'fr') return 'fr';
  if (code === 'ja') return 'ja';
  if (code === 'ko') return 'ko';
  return 'en';
}

function getInitialLanguage(): Language {
  if (typeof window !== 'undefined') {
    const stored = localStorage.getItem(STORAGE_KEY) as Language | null;
    if (stored && ['zh', 'en', 'fr', 'ja', 'ko'].includes(stored)) {
      return stored;
    }
  }
  return detectBrowserLanguage();
}

const translationCache: Record<Language, Record<string, unknown>> = {
  zh: {},
  en: {},
  fr: {},
  ja: {},
  ko: {},
};

async function loadTranslations(lang: Language): Promise<Record<string, unknown>> {
  if (translationCache[lang] && Object.keys(translationCache[lang]).length > 0) {
    return translationCache[lang];
  }
  try {
    const module = await import(`./locales/${lang}.json`);
    translationCache[lang] = module.default as Record<string, unknown>;
    return translationCache[lang];
  } catch {
    const fallback = await import('./locales/en.json');
    translationCache[lang] = fallback.default as Record<string, unknown>;
    return translationCache[lang];
  }
}

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Language>(getInitialLanguage);
  const [translations, setTranslations] = useState<Record<string, unknown>>({});

  useEffect(() => {
    let cancelled = false;
    loadTranslations(lang).then((data) => {
      if (!cancelled) setTranslations(data);
    });
    return () => { cancelled = true; };
  }, [lang]);

  const setLang = useCallback((newLang: Language) => {
    setLangState(newLang);
    if (typeof window !== 'undefined') {
      localStorage.setItem(STORAGE_KEY, newLang);
    }
  }, []);

  const t = useCallback(
    (key: string): any => {
      const parts = key.split('.');
      let value: unknown = translations;
      for (const part of parts) {
        if (value && typeof value === 'object' && part in value) {
          value = (value as Record<string, unknown>)[part];
        } else {
          return key;
        }
      }
      if (typeof value === 'string') return value;
      if (value && typeof value === 'object') return value as Record<string, unknown>;
      return key;
    },
    [translations],
  );

  return (
    <LanguageContext.Provider value={{ lang, setLang, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const ctx = useContext(LanguageContext);
  if (!ctx) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return ctx;
}

export function useTranslation() {
  return useLanguage();
}

export { LANGUAGE_NAMES };
