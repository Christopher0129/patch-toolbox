import { useState, useEffect, useRef, memo } from 'react';
import { Link } from 'react-router-dom';
import { motion, useInView } from 'framer-motion';
import {
  Shield,
  Bug,
  Wrench,
  Database,
  GitCommit,
  RefreshCw,
  ChevronDown,
  FileText,
  ExternalLink,
  Star,
} from 'lucide-react';
import { useTranslation } from '@/i18n/LanguageContext';
import { loadStats, loadCategories, loadEntries } from '@/lib/content';

/* ------------------------------------------------------------------ */
/*  Matrix Rain Canvas (isolated, memoized)                            */
/* ------------------------------------------------------------------ */
const MatrixRainCanvas = memo(function MatrixRainCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animRef = useRef<number>(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let w = 0;
    let h = 0;
    const particles: { x: number; y: number; speed: number; char: string; size: number }[] = [];
    const chars = '01CVE-';

    const resize = () => {
      w = canvas.width = canvas.offsetWidth;
      h = canvas.height = canvas.offsetHeight;
    };
    resize();
    window.addEventListener('resize', resize);

    for (let i = 0; i < 50; i++) {
      particles.push({
        x: Math.random() * w,
        y: Math.random() * h,
        speed: 0.5 + Math.random() * 1,
        char: chars[Math.floor(Math.random() * chars.length)],
        size: 10 + Math.random() * 8,
      });
    }

    const draw = () => {
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = 'rgba(59,130,246,0.06)';
      ctx.font = '14px "JetBrains Mono", monospace';
      for (const p of particles) {
        p.y += p.speed;
        if (p.y > h) {
          p.y = -20;
          p.x = Math.random() * w;
        }
        ctx.fillText(p.char, p.x, p.y);
      }
      animRef.current = requestAnimationFrame(draw);
    };
    animRef.current = requestAnimationFrame(draw);

    return () => {
      cancelAnimationFrame(animRef.current);
      window.removeEventListener('resize', resize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', zIndex: 1, pointerEvents: 'none' }}
    />
  );
});

/* ------------------------------------------------------------------ */
/*  Typewriter Hook                                                    */
/* ------------------------------------------------------------------ */
function useTypewriter(text: string, speed = 40, startDelay = 0) {
  const [display, setDisplay] = useState('');
  const [done, setDone] = useState(false);
  const indexRef = useRef(0);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    setDisplay('');
    setDone(false);
    indexRef.current = 0;
    if (timerRef.current) clearTimeout(timerRef.current);

    timerRef.current = setTimeout(() => {
      const tick = () => {
        if (indexRef.current < text.length) {
          setDisplay(text.slice(0, indexRef.current + 1));
          indexRef.current += 1;
          timerRef.current = setTimeout(tick, speed);
        } else {
          setDone(true);
        }
      };
      tick();
    }, startDelay);

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [text, speed, startDelay]);

  return { display, done };
}

/* ------------------------------------------------------------------ */
/*  Count-Up Hook                                                    */
/* ------------------------------------------------------------------ */
function useCountUp(target: number, duration = 1500, start = false) {
  const [value, setValue] = useState(0);
  const rafRef = useRef<number>(0);
  const startTimeRef = useRef<number | null>(null);

  useEffect(() => {
    if (!start) return;
    setValue(0);
    startTimeRef.current = null;

    const animate = (ts: number) => {
      if (startTimeRef.current === null) startTimeRef.current = ts;
      const elapsed = ts - startTimeRef.current;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(Math.floor(eased * target));
      if (progress < 1) {
        rafRef.current = requestAnimationFrame(animate);
      }
    };
    rafRef.current = requestAnimationFrame(animate);

    return () => cancelAnimationFrame(rafRef.current);
  }, [target, duration, start]);

  return value;
}

/* ------------------------------------------------------------------ */
/*  Stat Item                                                        */
/* ------------------------------------------------------------------ */
function StatItem({
  icon,
  value,
  suffix,
  label,
  start,
}: {
  icon: React.ReactNode;
  value: number;
  suffix?: string;
  label: string;
  start: boolean;
}) {
  const count = useCountUp(value, 1500, start);
  return (
    <div className="flex flex-col items-center gap-1 px-4 py-2">
      <div className="mb-1 text-text-muted">{icon}</div>
      <span className="font-mono text-2xl font-bold text-accent-cyan md:text-3xl">
        {count.toLocaleString()}
        {suffix && <span className="text-lg">{suffix}</span>}
      </span>
      <span className="text-xs font-medium uppercase tracking-wider text-text-muted">{label}</span>
    </div>
  );
}

/* ------------------------------------------------------------------ */
/*  Terminal Block                                                   */
/* ------------------------------------------------------------------ */
const TerminalBlock = memo(function TerminalBlock({
  lines,
  startTyping,
}: {
  lines: { text: string; color: string }[];
  startTyping: boolean;
}) {
  const [visibleCount, setVisibleCount] = useState(0);
  const [cursorVisible, setCursorVisible] = useState(true);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (!startTyping) return;
    setVisibleCount(0);
    if (timerRef.current) clearTimeout(timerRef.current);

    const reveal = (idx: number) => {
      if (idx <= lines.length) {
        setVisibleCount(idx);
        timerRef.current = setTimeout(() => reveal(idx + 1), 60);
      }
    };
    reveal(1);

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [startTyping, lines.length]);

  useEffect(() => {
    const interval = setInterval(() => setCursorVisible((v) => !v), 530);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="overflow-hidden rounded-lg border border-[#30363D] bg-[#0D1117]">
      {/* macOS-style header */}
      <div className="flex items-center gap-2 border-b border-[#30363D] px-4 py-2">
        <span className="h-3 w-3 rounded-full bg-[#FF5F56]" />
        <span className="h-3 w-3 rounded-full bg-[#FFBD2E]" />
        <span className="h-3 w-3 rounded-full bg-[#27C93F]" />
        <span className="ml-2 text-xs text-text-muted font-mono">last_sync.log</span>
      </div>
      <div className="border-l-[3px] border-accent-blue px-4 py-4 font-mono text-[13px] leading-relaxed">
        {lines.slice(0, visibleCount).map((line, i) => (
          <div key={i} className="whitespace-pre-wrap" style={{ color: line.color }}>
            {line.text}
          </div>
        ))}
        <span
          className="inline-block h-4 w-2 align-middle"
          style={{
            backgroundColor: cursorVisible ? '#22C55E' : 'transparent',
            marginLeft: 2,
          }}
        />
      </div>
    </div>
  );
});

/* ------------------------------------------------------------------ */
/*  HOME PAGE                                                          */
/* ------------------------------------------------------------------ */
export default function Home() {
  const { t, lang } = useTranslation();
  const heroRef = useRef<HTMLDivElement>(null);

  // Fetch live stats from generated static data
  const [liveEntryCount, setLiveEntryCount] = useState(3300);
  useEffect(() => {
    loadStats().then((s) => {
      if (s?.totalEntries) setLiveEntryCount(s.totalEntries);
    }).catch(() => {});
  }, []);
  const statsRef = useRef<HTMLDivElement>(null);
  const categoriesRef = useRef<HTMLDivElement>(null);
  const liveDataRef = useRef<HTMLDivElement>(null);
  const severityRef = useRef<HTMLDivElement>(null);
  const formatsRef = useRef<HTMLDivElement>(null);
  const ctaRef = useRef<HTMLDivElement>(null);

  const statsInView = useInView(statsRef, { once: true, margin: '-10%' });
  const categoriesInView = useInView(categoriesRef, { once: true, margin: '-20%' });
  const liveDataInView = useInView(liveDataRef, { once: true, margin: '-20%' });
  const severityInView = useInView(severityRef, { once: true, margin: '-20%' });
  const formatsInView = useInView(formatsRef, { once: true, margin: '-20%' });
  const ctaInView = useInView(ctaRef, { once: true, margin: '-20%' });

  /* Typewriter text based on language */
  const headlineText =
    lang === 'zh'
      ? '您的安全知识指挥中心'
      : lang === 'fr'
        ? 'Votre Centre de Commande de Connaissances Sécurité'
        : lang === 'ja'
          ? 'あなたのセキュリティ知識コマンドセンター'
          : lang === 'ko'
            ? '당신의 보안 지식 명령 센터'
            : 'Your Security Knowledge Command Center';

  const { display: headline, done: headlineDone } = useTypewriter(headlineText, 40, 200);

  const subtitleText =
    lang === 'zh'
      ? '3000+ 精选漏洞 · SQLite + Markdown · 每日从 NVD、Exploit-DB、GitHub 安全公告等更新'
      : lang === 'fr'
        ? "3000+ vulnérabilités sélectionnées · SQLite + Markdown · Mises à jour quotidiennes depuis NVD, Exploit-DB, GitHub Advisories, et plus"
        : lang === 'ja'
          ? '3000+ 厳選脆弱性 · SQLite + Markdown · NVD、Exploit-DB、GitHub Advisories などから毎日更新'
          : lang === 'ko'
            ? '3000+ 선별된 취약점 · SQLite + Markdown · NVD, Exploit-DB, GitHub Advisories 등에서 매일 업데이트'
            : '3,000+ curated vulnerabilities · SQLite + Markdown · Daily updated from NVD, Exploit-DB, GitHub Advisories, and more';

  const badgeText =
    lang === 'zh'
      ? '自动化安全漏洞与系统故障知识库'
      : lang === 'fr'
        ? 'Base de Connaissances de Sécurité Automatisée'
        : lang === 'ja'
          ? '自動化セキュリティ知識ベース'
          : lang === 'ko'
            ? '자동화 보안 지식 베이스'
            : 'Automated Security Knowledge Base';

  /* Terminal lines */
  const terminalLines = [
    { text: '[2026-04-27 03:00:01] INFO: Starting daily sync...', color: '#64748B' },
    { text: '[2026-04-27 03:00:15] INFO: NVD feed processed: 142 new CVEs', color: '#3B82F6' },
    { text: '[2026-04-27 03:00:42] INFO: Exploit-DB updated: 8 new entries', color: '#3B82F6' },
    { text: '[2026-04-27 03:01:03] INFO: GitHub Advisories: 3 new GHSA', color: '#3B82F6' },
    { text: '[2026-04-27 03:01:30] INFO: CISA KEV catalog checked', color: '#3B82F6' },
    { text: `[2026-04-27 03:02:01] SUCCESS: ${t('liveData.syncComplete') as string}`, color: '#22C55E' },
    { text: `[2026-04-27 03:02:01] INFO: ${t('liveData.markdownRegenerated') as string}`, color: '#3B82F6' },
    { text: `[2026-04-27 03:02:01] INFO: ${t('liveData.sqliteUpdated') as string}`, color: '#3B82F6' },
  ];

  /* Severity data */
  const severityData = [
    { label: t('severity.critical') as string, pct: 12, color: '#EF4444', desc: t('severity.criticalDesc') as string },
    { label: t('severity.high') as string, pct: 28, color: '#F97316', desc: t('severity.highDesc') as string },
    { label: t('severity.medium') as string, pct: 45, color: '#F59E0B', desc: t('severity.mediumDesc') as string },
    { label: t('severity.unrated') as string, pct: 15, color: '#64748B', desc: t('severity.unratedDesc') as string },
  ];

  const containerVariants = {
    hidden: {},
    visible: { transition: { staggerChildren: 0.08 } },
  };
  const itemVariants = {
    hidden: { opacity: 0, y: 30 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] } },
  };

  return (
    <>
      {/* ============ HERO ============ */}
      <section
        ref={heroRef}
        className="relative flex min-h-[100dvh] items-center justify-center overflow-hidden"
        style={{ background: 'linear-gradient(180deg, #0A0E17 0%, #0F172A 50%, #111827 100%)' }}
      >
        {/* Subtle hex grid overlay */}
        <div
          className="pointer-events-none absolute inset-0 opacity-[0.03]"
          style={{
            backgroundImage:
              'url("data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M30 0l25.98 15v30L30 60 4.02 45V15z\' fill=\'none\' stroke=\'%233B82F6\' stroke-width=\'1\'/%3E%3C/svg%3E")',
            backgroundSize: '60px 60px',
          }}
        />

        {/* Hero glow pulse */}
        <div
          className="pointer-events-none absolute inset-0 animate-hero-glow-pulse"
          style={{
            background: 'radial-gradient(ellipse at 50% 0%, rgba(59,130,246,0.15) 0%, transparent 60%)',
          }}
        />

        {/* Matrix rain */}
        <MatrixRainCanvas />

        <div className="relative z-10 mx-auto flex max-w-[800px] flex-col items-center px-6 text-center">
          {/* Badge */}
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] as [number, number, number, number], delay: 0.2 }}
          >
            <span className="inline-flex items-center gap-2 rounded-full border border-border-subtle px-4 py-1.5 text-xs font-medium uppercase tracking-[0.1em] text-text-muted">
              <Shield className="h-3.5 w-3.5 text-accent-blue" />
              {badgeText}
            </span>
          </motion.div>

          {/* Headline with typewriter */}
          <h1 className="mt-6 font-heading text-4xl font-bold leading-tight tracking-tight text-text-primary md:text-6xl lg:text-7xl">
            {headline}
            <span className="animate-cursor-blink ml-1 inline-block h-[0.8em] w-2 align-middle bg-accent-green" />
          </h1>

          {/* Subtitle */}
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={headlineDone ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            className="mt-6 max-w-[640px] text-lg leading-relaxed text-text-secondary"
          >
            {subtitleText}
          </motion.p>

          {/* CTA Buttons */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={headlineDone ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number], delay: 0.3 }}
            className="mt-8 flex flex-wrap items-center justify-center gap-4"
          >
            <a
              href="#categories"
              className="rounded-lg bg-accent-blue px-6 py-3 text-sm font-medium text-white transition-all hover:scale-[1.02] hover:bg-[#2563EB]"
            >
              {t('hero.exploreDatabase') as string}
            </a>
            <a
              href="https://github.com/Christopher0129/patch-toolbox"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg border border-border-active px-6 py-3 text-sm font-medium text-text-secondary transition-all hover:border-text-muted hover:text-text-primary"
            >
              {t('hero.viewOnGithub') as string}
            </a>
            <Link
              to="/about"
              className="text-sm text-text-muted transition-colors hover:text-text-primary"
            >
              {t('hero.readArchitecture') as string}
            </Link>
          </motion.div>

          {/* Live Stats Ticker */}
          <motion.div
            ref={statsRef}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.8, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            className="mt-12 flex flex-wrap items-center justify-center gap-2 rounded-xl border border-border-subtle bg-bg-surface px-6 py-5 md:gap-0"
          >
            <StatItem
              icon={<Database className="h-5 w-5" />}
              value={3154}
              label={t('hero.stats.totalEntries') as string}
              start={statsInView}
            />
            <div className="hidden h-10 w-px bg-border-subtle md:block" />
            <StatItem
              icon={<Shield className="h-5 w-5" />}
              value={452}
              label={t('hero.stats.networkSecurity') as string}
              start={statsInView}
            />
            <div className="hidden h-10 w-px bg-border-subtle md:block" />
            <StatItem
              icon={<GitCommit className="h-5 w-5" />}
              value={63}
              label={t('hero.stats.commits') as string}
              start={statsInView}
            />
            <div className="hidden h-10 w-px bg-border-subtle md:block" />
            <div className="flex flex-col items-center gap-1 px-4 py-2">
              <div className="mb-1 text-text-muted">
                <RefreshCw className="h-5 w-5" />
              </div>
              <span className="font-mono text-2xl font-bold text-accent-cyan md:text-3xl">
                {t('hero.stats.dailyUpdates') as string}
              </span>
              <span className="text-xs font-medium uppercase tracking-wider text-text-muted">
                {t('hero.stats.dailyUpdates') as string}
              </span>
            </div>
          </motion.div>
        </div>

        {/* Scroll indicator */}
        <motion.div
          className="absolute bottom-8 left-1/2 z-10 -translate-x-1/2"
          animate={{ y: [0, 8, 0] }}
          transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
        >
          <div className="flex flex-col items-center gap-1 text-text-muted">
            <span className="text-xs">{t('hero.scrollToExplore') as string}</span>
            <ChevronDown className="h-4 w-4" />
          </div>
        </motion.div>
      </section>

      {/* ============ CATEGORIES ============ */}
      <section id="categories" className="relative py-24 md:py-32" style={{ background: '#0A0E17' }}>
        <div
          className="pointer-events-none absolute inset-0 opacity-[0.04]"
          style={{
            background: 'radial-gradient(ellipse at 50% 0%, rgba(59,130,246,0.3) 0%, transparent 60%)',
          }}
        />
        <div className="relative mx-auto max-w-[1200px] px-6">
          {/* Section Header */}
          <motion.div
            ref={categoriesRef}
            initial={{ opacity: 0, y: 20 }}
            animate={categoriesInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            className="mx-auto mb-16 max-w-[640px] text-center"
          >
            <span className="text-xs font-medium uppercase tracking-[0.1em] text-accent-blue">
              {t('categories.label') as string}
            </span>
            <h2 className="mt-3 font-heading text-3xl font-bold text-text-primary md:text-5xl">
              {t('categories.title') as string}
            </h2>
            <p className="mt-4 text-lg text-text-secondary">
              {t('categories.description') as string}
            </p>
          </motion.div>

          {/* Category Cards */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate={categoriesInView ? 'visible' : 'hidden'}
            className="grid grid-cols-1 gap-6 md:grid-cols-3"
          >
            {/* Network Security */}
            <motion.div variants={itemVariants}>
              <Link
                to="/network-security"
                className="group flex h-full flex-col rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:-translate-y-1 hover:border-accent-blue hover:shadow-[0_0_20px_rgba(59,130,246,0.08)]"
              >
                <div className="mb-4 flex items-center justify-between">
                  <Shield className="h-12 w-12 text-accent-blue transition-transform duration-300 group-hover:scale-110" />
                  <div className="flex gap-1.5">
                    <span className="rounded bg-[rgba(239,68,68,0.15)] px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wider text-accent-red">
                      CRITICAL
                    </span>
                    <span className="rounded bg-[rgba(249,115,22,0.15)] px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wider text-accent-orange">
                      HIGH
                    </span>
                    <span className="rounded bg-[rgba(245,158,11,0.15)] px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wider text-accent-amber">
                      MED
                    </span>
                  </div>
                </div>
                <h3 className="font-heading text-xl font-medium text-text-primary">
                  {t('categories.networkSecurity.title') as string}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-text-secondary">
                  {t('categories.networkSecurity.description') as string}
                </p>
                <p className="mt-4 text-xs text-text-muted">
                  452 {t('categories.networkSecurity.stats') as string}
                </p>
                <span className="mt-auto inline-flex items-center gap-1 pt-6 text-sm text-text-muted transition-colors group-hover:text-accent-blue">
                  {t('categories.networkSecurity.cta') as string}
                  <ExternalLink className="h-3.5 w-3.5" />
                </span>
              </Link>
            </motion.div>

            {/* System Vulnerabilities */}
            <motion.div variants={itemVariants}>
              <Link
                to="/system-vulnerabilities"
                className="group flex h-full flex-col rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:-translate-y-1 hover:border-accent-orange hover:shadow-[0_0_20px_rgba(249,115,22,0.08)]"
              >
                <div className="mb-4 flex items-center justify-between">
                  <Bug className="h-12 w-12 text-accent-orange transition-transform duration-300 group-hover:scale-110" />
                  <div className="flex gap-1.5">
                    <span className="rounded bg-[rgba(59,130,246,0.15)] px-2 py-0.5 text-[10px] font-medium text-accent-blue">
                      Windows
                    </span>
                    <span className="rounded bg-[rgba(59,130,246,0.15)] px-2 py-0.5 text-[10px] font-medium text-accent-blue">
                      Linux
                    </span>
                    <span className="rounded bg-[rgba(59,130,246,0.15)] px-2 py-0.5 text-[10px] font-medium text-accent-blue">
                      macOS
                    </span>
                  </div>
                </div>
                <h3 className="font-heading text-xl font-medium text-text-primary">
                  {t('categories.systemVulnerabilities.title') as string}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-text-secondary">
                  {t('categories.systemVulnerabilities.description') as string}
                </p>
                <p className="mt-4 text-xs text-text-muted">
                  {t('categories.systemVulnerabilities.stats') as string}
                </p>
                <span className="mt-auto inline-flex items-center gap-1 pt-6 text-sm text-text-muted transition-colors group-hover:text-accent-orange">
                  {t('categories.systemVulnerabilities.cta') as string}
                  <ExternalLink className="h-3.5 w-3.5" />
                </span>
              </Link>
            </motion.div>

            {/* System Troubleshooting */}
            <motion.div variants={itemVariants}>
              <Link
                to="/system-troubleshooting"
                className="group flex h-full flex-col rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:-translate-y-1 hover:border-accent-green hover:shadow-[0_0_20px_rgba(34,197,94,0.08)]"
              >
                <div className="mb-4 flex items-center justify-between">
                  <Wrench className="h-12 w-12 text-accent-green transition-transform duration-300 group-hover:scale-110" />
                </div>
                <h3 className="font-heading text-xl font-medium text-text-primary">
                  {t('categories.systemTroubleshooting.title') as string}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-text-secondary">
                  {t('categories.systemTroubleshooting.description') as string}
                </p>
                <p className="mt-4 text-xs text-text-muted">
                  {t('categories.systemTroubleshooting.stats') as string}
                </p>
                <span className="mt-auto inline-flex items-center gap-1 pt-6 text-sm text-text-muted transition-colors group-hover:text-accent-green">
                  {t('categories.systemTroubleshooting.cta') as string}
                  <ExternalLink className="h-3.5 w-3.5" />
                </span>
              </Link>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* ============ LIVE DATA / TERMINAL ============ */}
      <section className="relative border-l-[3px] border-accent-blue bg-bg-surface py-20 md:py-24">
        <div className="mx-auto max-w-[1200px] px-6">
          <div className="grid grid-cols-1 items-center gap-12 lg:grid-cols-2">
            {/* Left: Text */}
            <motion.div
              ref={liveDataRef}
              initial={{ opacity: 0, x: -30 }}
              animate={liveDataInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            >
              <span className="text-xs font-medium uppercase tracking-[0.1em] text-accent-cyan">
                {t('liveData.label') as string}
              </span>
              <h2 className="mt-3 font-heading text-3xl font-bold text-text-primary md:text-4xl">
                {t('liveData.title') as string}
              </h2>
              <p className="mt-4 text-lg text-text-secondary">
                {t('liveData.description') as string}
              </p>

              {/* Data source pills */}
              <div className="mt-6 flex flex-wrap gap-2">
                {['NVD', 'Exploit-DB', 'GitHub Advisories', 'CISA KEV', 'Stack Exchange', 'Reddit', 'V2EX'].map(
                  (src) => (
                    <span
                      key={src}
                      className="rounded-md border border-border-subtle bg-bg-base px-3 py-1 text-xs font-medium text-text-muted"
                    >
                      {src}
                    </span>
                  ),
                )}
              </div>
            </motion.div>

            {/* Right: Terminal */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={liveDataInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            >
              <TerminalBlock lines={terminalLines} startTyping={liveDataInView} />
            </motion.div>
          </div>
        </div>
      </section>

      {/* ============ SEVERITY DISTRIBUTION ============ */}
      <section className="relative bg-bg-base py-20 md:py-24">
        <div className="mx-auto max-w-[1200px] px-6">
          {/* Header */}
          <motion.div
            ref={severityRef}
            initial={{ opacity: 0, y: 20 }}
            animate={severityInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5 }}
            className="mb-12 text-center"
          >
            <span className="text-xs font-medium uppercase tracking-[0.1em] text-accent-blue">
              {t('severity.label') as string}
            </span>
            <h2 className="mt-3 font-heading text-3xl font-bold text-text-primary md:text-4xl">
              {t('severity.title') as string}
            </h2>
          </motion.div>

          {/* Stat Cards */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate={severityInView ? 'visible' : 'hidden'}
            className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4"
          >
            {severityData.map((s) => (
              <motion.div
                key={s.label}
                variants={itemVariants}
                className="rounded-xl border border-border-subtle bg-bg-surface p-6"
              >
                <SeverityStat pct={s.pct} color={s.color} label={s.label} desc={s.desc} start={severityInView} />
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* ============ FORMATS SHOWCASE ============ */}
      <section
        className="relative py-20 md:py-24"
        style={{ background: 'linear-gradient(180deg, #0A0E17 0%, #0F172A 50%, #111827 100%)' }}
      >
        <div className="mx-auto max-w-[1200px] px-6">
          <motion.div
            ref={formatsRef}
            initial={{ opacity: 0, y: 20 }}
            animate={formatsInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5 }}
            className="mb-12 text-center"
          >
            <span className="text-xs font-medium uppercase tracking-[0.1em] text-accent-cyan">
              {t('formats.label') as string}
            </span>
            <h2 className="mt-3 font-heading text-3xl font-bold text-text-primary md:text-4xl">
              {t('formats.title') as string}
            </h2>
          </motion.div>

          <div className="grid grid-cols-1 gap-6 md:grid-cols-2">
            {/* SQLite Card */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={formatsInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
              className="rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:border-border-active hover:shadow-[0_0_20px_rgba(6,182,212,0.08)]"
            >
              <Database className="h-10 w-10 text-accent-cyan" />
              <h3 className="mt-4 font-heading text-xl font-medium text-text-primary">
                {t('formats.sqlite.title') as string}
              </h3>
              <p className="mt-2 text-sm text-text-secondary">
                {t('formats.sqlite.description') as string}
              </p>
              <div className="mt-4 overflow-hidden rounded-lg border border-[#30363D] bg-[#0D1117] px-4 py-3">
                <pre className="font-mono text-[11px] leading-relaxed text-text-secondary">
                  <span className="text-accent-purple">SELECT</span>{' '}
                  <span className="text-accent-cyan">cve_id</span>,{' '}
                  <span className="text-accent-cyan">severity</span>,{' '}
                  <span className="text-accent-cyan">cvss_score</span>
                  {'\n'}
                  <span className="text-accent-purple">FROM</span>{' '}
                  <span className="text-accent-cyan">vulnerabilities</span>
                  {'\n'}
                  <span className="text-accent-purple">WHERE</span>{' '}
                  <span className="text-accent-cyan">severity</span> ={' '}
                  <span className="text-accent-green">&apos;CRITICAL&apos;</span>
                  {'\n'}
                  <span className="text-accent-purple">ORDER BY</span>{' '}
                  <span className="text-accent-cyan">cvss_score</span>{' '}
                  <span className="text-accent-purple">DESC</span>;
                </pre>
              </div>
              <div className="mt-3 flex flex-wrap gap-2">
                {['network-security.db', 'system-vulnerabilities.db', 'system-troubleshooting.db'].map((f) => (
                  <span key={f} className="text-xs text-text-muted font-mono">
                    {f}
                  </span>
                ))}
              </div>
              <a
                href="https://github.com/Christopher0129/patch-toolbox/tree/main/db"
                target="_blank"
                rel="noopener noreferrer"
                className="mt-4 inline-flex items-center gap-1 text-sm text-accent-cyan transition-colors hover:text-accent-blue"
              >
                {t('formats.sqlite.cta') as string}
              </a>
              {/* Mixed-mode: SQLite download + structured data link */}
              <div className="mt-4 flex flex-wrap gap-3 border-t border-border-subtle pt-4">
                <a
                  href="/patch-toolbox/db/network-security.db"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 rounded-md bg-accent-blue/10 px-3 py-1.5 text-xs font-medium text-accent-blue transition-colors hover:bg-accent-blue/20"
                >
                  <Database className="h-3.5 w-3.5" />
                  Download SQLite .db
                </a>
                <a
                  href="/patch-toolbox/data/entries.json"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 rounded-md bg-accent-cyan/10 px-3 py-1.5 text-xs font-medium text-accent-cyan transition-colors hover:bg-accent-cyan/20"
                >
                  <FileText className="h-3.5 w-3.5" />
                  Browse entries.json
                </a>
              </div>
            </motion.div>

            {/* Markdown Card */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={formatsInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
              className="rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:border-border-active hover:shadow-[0_0_20px_rgba(34,197,94,0.08)]"
            >
              <FileText className="h-10 w-10 text-accent-green" />
              <h3 className="mt-4 font-heading text-xl font-medium text-text-primary">
                {t('formats.markdown.title') as string}
              </h3>
              <p className="mt-2 text-sm text-text-secondary">
                {t('formats.markdown.description') as string}
              </p>
              <div className="mt-4 overflow-hidden rounded-lg border border-[#30363D] bg-[#0D1117] px-4 py-3">
                <pre className="font-mono text-[11px] leading-relaxed text-text-secondary">
                  <span className="text-accent-purple">###</span>{' '}
                  <span className="text-accent-cyan">CVE-2024-XXXX</span>
                  {'\n'}
                  <span className="text-text-muted">**Severity / 严重程度**:</span>{' '}
                  <span className="text-accent-red">CRITICAL</span> | CVSS: 9.8
                  {'\n'}
                  <span className="text-text-muted">**Description / 漏洞描述**:</span> Buffer overflow in ...
                  {'\n'}
                  <span className="text-text-muted">**Mitigation / 缓解方案**:</span> Apply patch ...
                </pre>
              </div>
              <div className="mt-3 flex flex-wrap gap-2">
                {['network-security/index.md', 'system-vulnerabilities/*.md', 'system-troubleshooting/*.md'].map(
                  (f) => (
                    <span key={f} className="text-xs text-text-muted font-mono">
                      {f}
                    </span>
                  ),
                )}
              </div>
              <a
                href="https://github.com/Christopher0129/patch-toolbox/tree/main"
                target="_blank"
                rel="noopener noreferrer"
                className="mt-4 inline-flex items-center gap-1 text-sm text-accent-green transition-colors hover:text-accent-blue"
              >
                {t('formats.markdown.cta') as string}
              </a>
              {/* Mixed-mode: Markdown source + structured data link */}
              <div className="mt-4 flex flex-wrap gap-3 border-t border-border-subtle pt-4">
                <a
                  href="https://github.com/Christopher0129/patch-toolbox/blob/main/network-security/index.md"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 rounded-md bg-accent-green/10 px-3 py-1.5 text-xs font-medium text-accent-green transition-colors hover:bg-accent-green/20"
                >
                  <FileText className="h-3.5 w-3.5" />
                  View Markdown (GitHub)
                </a>
                <a
                  href="/patch-toolbox/data/categories.json"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 rounded-md bg-accent-amber/10 px-3 py-1.5 text-xs font-medium text-accent-amber transition-colors hover:bg-accent-amber/20"
                >
                  <FileText className="h-3.5 w-3.5" />
                  Browse categories.json
                </a>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* ============ CTA BANNER ============ */}
      <section
        ref={ctaRef}
        className="relative border-y border-border-subtle bg-bg-surface py-20"
        style={{
          backgroundImage: 'radial-gradient(ellipse at 50% 50%, rgba(59,130,246,0.08) 0%, transparent 70%)',
        }}
      >
        <div className="mx-auto max-w-[600px] px-6 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={ctaInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5 }}
          >
            <span className="text-xs font-medium uppercase tracking-[0.1em] text-accent-blue">
              {t('cta.label') as string}
            </span>
            <h2 className="mt-3 font-heading text-3xl font-bold text-text-primary md:text-4xl">
              {t('cta.title') as string}
            </h2>
            <p className="mt-4 text-lg text-text-secondary">
              {t('cta.description') as string}
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
              <Link
                to="/contributing"
                className="rounded-lg bg-accent-blue px-6 py-3 text-sm font-medium text-white transition-all hover:scale-[1.02] hover:bg-[#2563EB]"
              >
                {t('cta.contribute') as string}
              </Link>
              <a
                href="https://github.com/Christopher0129/patch-toolbox"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-2 rounded-lg border border-border-active px-6 py-3 text-sm font-medium text-text-secondary transition-all hover:border-text-muted hover:text-text-primary"
              >
                <Star className="h-4 w-4" />
                {t('cta.starOnGithub') as string}
              </a>
            </div>
          </motion.div>
        </div>
      </section>
    </>
  );
}

/* ------------------------------------------------------------------ */
/*  Severity Stat Component                                            */
/* ------------------------------------------------------------------ */
function SeverityStat({
  pct,
  color,
  label,
  desc,
  start,
}: {
  pct: number;
  color: string;
  label: string;
  desc: string;
  start: boolean;
}) {
  const count = useCountUp(pct, 1200, start);
  return (
    <div>
      <span className="font-mono text-4xl font-bold" style={{ color }}>
        {count}%
      </span>
      <h4 className="mt-2 font-heading text-lg font-medium text-text-primary">{label}</h4>
      <p className="mt-1 text-sm text-text-secondary">{desc}</p>
      <div className="mt-4 h-1.5 w-full overflow-hidden rounded-full bg-bg-base">
        <motion.div
          className="h-full rounded-full"
          style={{ backgroundColor: color }}
          initial={{ width: 0 }}
          animate={start ? { width: `${pct}%` } : { width: 0 }}
          transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] as [number, number, number, number], delay: 0.3 }}
        />
      </div>
    </div>
  );
}
