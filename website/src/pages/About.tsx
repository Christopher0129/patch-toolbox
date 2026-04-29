import { Database, FileText, ExternalLink, Shield } from 'lucide-react';
import { useTranslation } from '@/i18n/LanguageContext';
import { loadStats, loadEntries } from '@/lib/content';
import { motion } from 'framer-motion';
import {
  Shield,
  Radio,
  RefreshCw,
  FileText,
  Github,
  Star,
  GitFork,
  Users,
  GitCommit,
  Database,
  Flame,
  Layers,
  MessageSquare,
  CheckCircle,
  ChevronRight,
  ExternalLink,
} from 'lucide-react';
import { useState, useEffect, type ReactNode } from 'react';

/* ── Reusable animation variants ─────────────────────────────── */
const fadeUp = {
  hidden: { opacity: 0, y: 20 },
  visible: (i: number) => ({
    opacity: 1,
    y: 0,
    transition: {
      delay: i * 0.08,
      duration: 0.5,
      ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
    },
  }),
};

const staggerContainer = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.08 },
  },
};

/* ── Sub-components ────────────────────────────────────────── */
function SectionHeader({
  label,
  title,
  description,
}: {
  label: string;
  title: string;
  description?: string;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-60px' }}
      transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
      className="mb-10 text-center"
    >
      <p className="mb-3 text-xs font-medium uppercase tracking-wider text-accent-blue">
        {label}
      </p>
      <h2 className="font-heading text-3xl font-bold text-text-primary md:text-4xl">
        {title}
      </h2>
      {description && (
        <p className="mx-auto mt-4 max-w-2xl text-lg leading-relaxed text-text-secondary">
          {description}
        </p>
      )}
    </motion.div>
  );
}

function TerminalBlock({
  children,
  header,
  accent = 'blue',
}: {
  children: ReactNode;
  header?: string;
  accent?: 'blue' | 'green';
}) {
  const accentColor = accent === 'green' ? 'border-l-accent-green' : 'border-l-accent-blue';
  return (
    <div
      className={`overflow-hidden rounded-lg border border-[#30363D] bg-gradient-to-b from-[#0D1117] to-[#161B22] ${accentColor} border-l-[3px]`}
    >
      {header && (
        <div className="flex items-center gap-2 border-b border-[#30363D] px-4 py-2">
          <span className="h-2.5 w-2.5 rounded-full bg-[#FF5F56]" />
          <span className="h-2.5 w-2.5 rounded-full bg-[#FFBD2E]" />
          <span className="h-2.5 w-2.5 rounded-full bg-[#27C93F]" />
          <span className="ml-2 text-xs text-text-muted">{header}</span>
        </div>
      )}
      <div className="p-4 font-mono text-sm leading-relaxed text-text-secondary">
        {children}
      </div>
    </div>
  );
}

function DataCard({
  children,
  className = '',
  hover = true,
}: {
  children: ReactNode;
  className?: string;
  hover?: boolean;
}) {
  return (
    <div
      className={`rounded-xl border border-border-subtle bg-gradient-to-br from-bg-surface/90 to-[#1A2332]/60 p-6 ${
        hover
          ? 'transition-all duration-300 hover:-translate-y-0.5 hover:border-border-active hover:shadow-[0_0_20px_rgba(59,130,246,0.08)]'
          : ''
      } ${className}`}
    >
      {children}
    </div>
  );
}

/* ── Architecture Tree Diagram ───────────────────────────────── */
function ArchitectureTree() {
  const domains = [
    {
      name: 'network-security',
      files: ['index.md', 'db/'],
      color: 'text-accent-blue',
      border: 'border-accent-blue/30',
    },
    {
      name: 'system-vulnerabilities',
      files: ['index.md', 'windows.md', 'linux.md', 'macos.md', 'db/'],
      color: 'text-accent-orange',
      border: 'border-accent-orange/30',
    },
    {
      name: 'system-troubleshooting',
      files: ['index.md', 'windows.md', 'linux.md', 'macos.md', 'db/'],
      color: 'text-accent-green',
      border: 'border-accent-green/30',
    },
  ];

  return (
    <motion.div
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: '-60px' }}
      variants={staggerContainer}
      className="mx-auto max-w-3xl"
    >
      <DataCard hover={false} className="font-mono text-sm">
        <div className="mb-4 text-accent-cyan">patch-toolbox/</div>
        {domains.map((d, i) => (
          <motion.div key={d.name} variants={fadeUp} custom={i} className="mb-3">
            <div className="flex items-start gap-2">
              <span className="text-text-muted">{i === domains.length - 1 ? '└──' : '├──'}</span>
              <div className={`rounded-md border ${d.border} bg-bg-elevated/40 px-3 py-2 ${d.color}`}>
                <span className="font-medium">{d.name}/</span>
                <span className="mx-2 text-text-muted">→</span>
                <span className="text-text-secondary">
                  {d.files.join(' + ')}
                </span>
              </div>
            </div>
          </motion.div>
        ))}
        <div className="mt-6 flex flex-wrap gap-4">
          <div className="flex items-center gap-2 rounded-md border border-border-subtle bg-bg-elevated/50 px-3 py-1.5 text-xs text-text-secondary">
            <Database className="h-3.5 w-3.5 text-accent-cyan" />
            SQLite for programs
          </div>
          <div className="flex items-center gap-2 rounded-md border border-border-subtle bg-bg-elevated/50 px-3 py-1.5 text-xs text-text-secondary">
            <FileText className="h-3.5 w-3.5 text-accent-green" />
            Markdown for humans
          </div>
        </div>
      </DataCard>
    </motion.div>
  );
}

/* ── Source Card ─────────────────────────────────────────────── */
function SourceCard({
  icon,
  title,
  description,
  link,
  badge,
  accent,
  delay,
}: {
  icon: ReactNode;
  title: string;
  description: string;
  link?: string;
  badge?: string;
  accent: string;
  delay: number;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{
        delay,
        duration: 0.5,
        ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
      }}
    >
      <DataCard className="h-full">
        <div className="mb-3 flex items-center gap-3">
          <div className={`flex h-10 w-10 items-center justify-center rounded-lg ${accent}`}>
            {icon}
          </div>
          <div className="flex-1">
            <h3 className="font-heading text-base font-medium text-text-primary">{title}</h3>
            {link && (
              <a
                href={`https://${link}`}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs text-accent-blue transition-colors hover:text-accent-cyan"
              >
                {link}
              </a>
            )}
          </div>
        </div>
        <p className="mb-3 text-sm leading-relaxed text-text-secondary">{description}</p>
        {badge && (
          <span className="inline-block rounded bg-accent-green/10 px-2 py-0.5 text-xs font-medium text-accent-green">
            {badge}
          </span>
        )}
      </DataCard>
    </motion.div>
  );
}

/* ── Timeline Item ───────────────────────────────────────────── */
function TimelineItem({
  year,
  title,
  description,
  isLast,
  delay,
}: {
  year: string;
  title: string;
  description: string;
  isLast?: boolean;
  delay: number;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      whileInView={{ opacity: 1, x: 0 }}
      viewport={{ once: true }}
      transition={{
        delay,
        duration: 0.5,
        ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
      }}
      className="relative flex gap-4"
    >
      <div className="flex flex-col items-center">
        <div className="flex h-4 w-4 items-center justify-center rounded-full bg-accent-blue ring-4 ring-bg-surface" />
        {!isLast && (
          <div className="mt-2 h-full w-px bg-border-subtle" style={{ minHeight: '48px' }} />
        )}
      </div>
      <div className="pb-6">
        <span className="font-mono text-xs font-medium text-accent-blue">{year}</span>
        <h4 className="mt-0.5 text-base font-medium text-text-primary">{title}</h4>
        <p className="mt-1 text-sm text-text-secondary">{description}</p>
      </div>
    </motion.div>
  );
}

/* ── Metric Card ───────────────────────────────────────────── */
function MetricCard({
  icon,
  value,
  label,
  delay,
}: {
  icon: ReactNode;
  value: string;
  label: string;
  delay: number;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{
        delay,
        duration: 0.5,
        ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
      }}
    >
      <DataCard className="flex items-center gap-4">
        <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-accent-blue/10 text-accent-blue">
          {icon}
        </div>
        <div>
          <div className="font-mono text-xl font-bold text-text-primary">{value}</div>
          <div className="text-xs text-text-muted">{label}</div>
        </div>
      </DataCard>
    </motion.div>
  );
}

/* ── Main About Page ─────────────────────────────────────────── */
export default function About() {
  const { t } = useTranslation();

  // Wire to generated static data stats
  const [stats, setStats] = useState({ stars: 21, forks: 1, contributors: 3, commits: 63, entries: 3154 });
  useEffect(() => {
    loadStats().then((s) => {
      if (s?.githubStars) setStats(prev => ({ ...prev, stars: s.githubStars }));
      if (s?.githubForks) setStats(prev => ({ ...prev, forks: s.githubForks }));
      if (s?.totalEntries) setStats(prev => ({ ...prev, entries: s.totalEntries }));
    }).catch(() => {});
  }, []);

  const sources = [
    {
      icon: <Shield className="h-5 w-5 text-accent-blue" />,
      title: 'NVD — National Vulnerability Database',
      description: t('about.sourceNvdDesc') as string,
      link: 'nvd.nist.gov',
      badge: t('about.sourceNvdBadge') as string,
      accent: 'bg-accent-blue/10',
      delay: 0,
    },
    {
      icon: <Flame className="h-5 w-5 text-accent-purple" />,
      title: 'Exploit-DB',
      description: t('about.sourceExploitDbDesc') as string,
      link: 'exploit-db.com',
      badge: t('about.sourceExploitDbBadge') as string,
      accent: 'bg-accent-purple/10',
      delay: 0.1,
    },
    {
      icon: <Github className="h-5 w-5 text-text-primary" />,
      title: 'GitHub Security Advisories',
      description: t('about.sourceGhsaDesc') as string,
      link: 'github.com/advisories',
      accent: 'bg-text-primary/10',
      delay: 0.2,
    },
    {
      icon: <Shield className="h-5 w-5 text-accent-orange" />,
      title: 'CISA KEV',
      description: t('about.sourceCisaDesc') as string,
      link: 'cisa.gov/known-exploited-vulnerabilities-catalog',
      accent: 'bg-accent-orange/10',
      delay: 0.3,
    },
    {
      icon: <Layers className="h-5 w-5 text-accent-cyan" />,
      title: 'Stack Exchange Network',
      description: t('about.sourceStackDesc') as string,
      accent: 'bg-accent-cyan/10',
      delay: 0.4,
    },
    {
      icon: <MessageSquare className="h-5 w-5 text-accent-green" />,
      title: 'Reddit & V2EX',
      description: t('about.sourceCommunityDesc') as string,
      accent: 'bg-accent-green/10',
      delay: 0.5,
    },
  ];

  const timeline = [
    {
      year: '2025',
      title: t('about.timeline2025Title') as string,
      description: t('about.timeline2025Desc') as string,
    },
    {
      year: '2026',
      title: t('about.timeline2026Title') as string,
      description: t('about.timeline2026Desc') as string,
    },
    {
      year: t('about.timelineDailyYear') as string,
      title: t('about.timelineDailyTitle') as string,
      description: t('about.timelineDailyDesc') as string,
    },
    {
      year: t('about.timelineFutureYear') as string,
      title: t('about.timelineFutureTitle') as string,
      description: t('about.timelineFutureDesc') as string,
    },
  ];

  return (
    <div className="min-h-[100dvh]">
      {/* ── Hero ────────────────────────────────────────────── */}
      <section
        className="relative flex min-h-[35vh] flex-col items-center justify-center border-b border-border-subtle px-6"
        style={{
          background: 'linear-gradient(180deg, #0A0E17 0%, #0F172A 50%, #111827 100%)',
        }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              'radial-gradient(ellipse at 50% 0%, rgba(59,130,246,0.12) 0%, transparent 60%)',
          }}
        />
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="relative z-10 text-center"
        >
          <p className="mb-3 text-xs font-medium uppercase tracking-wider text-text-muted">
            {String(t('about.breadcrumb'))}
          </p>
          <h1 className="font-heading text-3xl font-bold text-text-primary md:text-4xl">
            {String(t('about.title'))}
          </h1>
          <p className="mx-auto mt-4 max-w-xl text-lg leading-relaxed text-text-secondary">
            {String(t('about.subtitle'))}
          </p>
        </motion.div>
      </section>

      {/* ── Mission + Stats ─────────────────────────────────── */}
      <section className="px-6 py-20">
        <div className="mx-auto grid max-w-[1200px] gap-12 md:grid-cols-2 md:gap-16">
          {/* Left: Mission text */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: '-60px' }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
          >
            <h2 className="mb-6 font-heading text-2xl font-medium text-text-primary md:text-3xl">
              {String(t('about.missionTitle'))}
            </h2>
            <p className="mb-6 text-lg leading-relaxed text-text-secondary">
              {String(t('about.missionText'))}
            </p>
            <div className="space-y-4">
              {[
                {
                  icon: <Radio className="h-5 w-5 text-accent-blue" />,
                  title: t('about.valueOpenData') as string,
                  desc: t('about.valueOpenDataDesc') as string,
                },
                {
                  icon: <RefreshCw className="h-5 w-5 text-accent-cyan" />,
                  title: t('about.valueDailyUpdates') as string,
                  desc: t('about.valueDailyUpdatesDesc') as string,
                },
                {
                  icon: <FileText className="h-5 w-5 text-accent-green" />,
                  title: t('about.valueDualFormat') as string,
                  desc: t('about.valueDualFormatDesc') as string,
                },
              ].map((item, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 12 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{
                    delay: i * 0.1,
                    duration: 0.4,
                    ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
                  }}
                  className="flex items-start gap-3"
                >
                  <div className="mt-0.5">{item.icon}</div>
                  <div>
                    <p className="font-medium text-text-primary">{item.title}</p>
                    <p className="text-sm text-text-secondary">{item.desc}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>

          {/* Right: Terminal stats */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: '-60px' }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
          >
            <TerminalBlock header="repo_info.json">
              <div className="space-y-1">
                <p>
                  <span className="text-accent-cyan">Stars:</span>{' '}
                  <span className="text-accent-green">21</span>
                </p>
                <p>
                  <span className="text-accent-cyan">Forks:</span>{' '}
                  <span className="text-accent-green">1</span>
                </p>
                <p>
                  <span className="text-accent-cyan">Contributors:</span>{' '}
                  <span className="text-accent-green">3</span>
                </p>
                <p>
                  <span className="text-accent-cyan">Commits:</span>{' '}
                  <span className="text-accent-green">63</span>
                </p>
                <p>
                  <span className="text-accent-cyan">License:</span>{' '}
                  <span className="text-accent-green">MIT</span>
                </p>
                <p>
                  <span className="text-accent-cyan">Languages:</span>{' '}
                  <span className="text-accent-green">Python 100%</span>
                </p>
                <p>
                  <span className="text-accent-cyan">Last Update:</span>{' '}
                  <span className="text-accent-green">2026-04-27</span>
                </p>
              </div>
            </TerminalBlock>
            <a
              href="https://github.com/Christopher0129/patch-toolbox"
              target="_blank"
              rel="noopener noreferrer"
              className="mt-4 inline-flex items-center gap-1.5 rounded-md border border-border-active px-4 py-2 text-sm text-text-secondary transition-all hover:border-text-muted hover:text-text-primary"
            >
              {String(t('about.viewOnGithub'))}
              <ChevronRight className="h-4 w-4" />
            </a>
          </motion.div>
        </div>
      </section>

      {/* ── Architecture ──────────────────────────────────────── */}
      <section className="border-l-[3px] border-l-accent-blue bg-bg-surface px-6 py-20">
        <SectionHeader
          label={t('about.architectureLabel') as string}
          title={t('about.architectureTitle') as string}
          description={t('about.architectureDesc') as string}
        />
        <ArchitectureTree />
      </section>

      {/* ── Data Sources ──────────────────────────────────────── */}
      <section className="px-6 py-20">
        <SectionHeader
          label={t('about.sourcesLabel') as string}
          title={t('about.sourcesTitle') as string}
        />
        <div className="mx-auto grid max-w-[1200px] gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {sources.map((s) => (
            <SourceCard key={s.title} {...s} />
          ))}
        </div>
      </section>

      {/* ── Maintenance ───────────────────────────────────────── */}
      <section className="bg-bg-surface px-6 py-20">
        <div className="mx-auto max-w-[800px]">
          <SectionHeader
            label={t('about.maintenanceLabel') as string}
            title={t('about.maintenanceTitle') as string}
          />

          {/* Stats grid */}
          <div className="mb-12 grid grid-cols-2 gap-4 sm:grid-cols-4">
            <MetricCard icon={<RefreshCw className="h-5 w-5" />} value="Daily" label={t('about.statSync') as string} delay={0} />
            <MetricCard icon={<Database className="h-5 w-5" />} value={stats.entries > 0 ? `${stats.entries.toLocaleString()}+` : '3,154+'} label={t('about.statEntries') as string} delay={0.1} />
            <MetricCard icon={<GitCommit className="h-5 w-5" />} value={String(stats.commits)} label={t('about.statCommits') as string} delay={0.2} />
            <MetricCard icon={<CheckCircle className="h-5 w-5" />} value="MIT" label={t('about.statLicense') as string} delay={0.3} />
          </div>

          {/* Timeline */}
          <div className="mb-10">
            {timeline.map((item, i) => (
              <TimelineItem
                key={item.year}
                {...item}
                isLast={i === timeline.length - 1}
                delay={i * 0.12}
              />
            ))}
          </div>

          {/* CI Badge */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
          >
            <DataCard className="flex items-center gap-4">
              <div className="flex h-10 w-10 items-center justify-center rounded-full bg-accent-green/10 text-accent-green">
                <CheckCircle className="h-5 w-5" />
              </div>
              <div>
                <h4 className="font-medium text-text-primary">{String(t('about.ciBadgeTitle'))}</h4>
                <p className="text-sm text-text-secondary">{String(t('about.ciBadgeDesc'))}</p>
              </div>
            </DataCard>
          </motion.div>
        </div>
      </section>

      {/* ── GitHub Activity Graph ─────────────────────────────── */}
      <section className="px-6 py-16">
        <SectionHeader
          label={t('about.activityLabel') as string}
          title={t('about.activityTitle') as string}
        />
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
          className="mx-auto max-w-[800px]"
        >
          <DataCard hover={false} className="overflow-hidden p-0">
            <img
              src="/github-activity-graph.png"
              alt="GitHub Activity Graph"
              className="w-full object-cover"
              onError={(e) => {
                (e.target as HTMLImageElement).style.display = 'none';
              }}
            />
          </DataCard>
        </motion.div>
      </section>

      {/* ── Maintainer Card ──────────────────────────────────── */}
      <section className="px-6 py-16">
        <div className="mx-auto max-w-[400px]">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
          >
            <DataCard className="text-center">
              <div className="mx-auto mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-bg-elevated">
                <Github className="h-10 w-10 text-text-muted" />
              </div>
              <h3 className="font-heading text-xl font-medium text-text-primary">
                Christopher0129
              </h3>
              <p className="mt-1 font-mono text-sm text-text-muted">
                "{t('about.maintainerTagline') as string}"
              </p>
              <p className="mt-2 text-xs font-medium uppercase tracking-wider text-accent-blue">
                {t('about.maintainerRole') as string}
              </p>
              <a
                href="https://github.com/Christopher0129"
                target="_blank"
                rel="noopener noreferrer"
                className="mt-4 inline-flex items-center gap-1.5 text-sm text-accent-blue transition-colors hover:text-accent-cyan"
              >
                <ExternalLink className="h-3.5 w-3.5" />
                {t('about.viewProfile') as string}
              </a>
            </DataCard>
          </motion.div>
        </div>
      </section>

      {/* ── Mixed-Mode Access Section ──────────────────────── */}
      <section className="border-t border-border-subtle bg-bg-surface px-6 py-16">
        <div className="mx-auto max-w-[800px]">
          <SectionHeader
            label={t('formats.label') as string}
            title={t('formats.title') as string}
            description="patch-toolbox 采用混合模式 (mixed-mode) 发布内容：前端阅读 / Markdown 原文 / SQLite 下载，三种方式均可获取全部数据。"
          />
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-3">
            <a
              href="/patch-toolbox/data/entries.json"
              target="_blank"
              rel="noopener noreferrer"
              className="flex flex-col items-center gap-3 rounded-xl border border-border-subtle bg-bg-elevated p-6 transition-all hover:-translate-y-0.5 hover:border-accent-blue"
            >
              <Database className="h-8 w-8 text-accent-cyan" />
              <span className="font-heading text-lg font-medium text-text-primary">前端阅读</span>
              <span className="text-center text-xs text-text-muted">Front-end reading via entries.json</span>
            </a>
            <a
              href="https://github.com/Christopher0129/patch-toolbox/blob/main/network-security/index.md"
              target="_blank"
              rel="noopener noreferrer"
              className="flex flex-col items-center gap-3 rounded-xl border border-border-subtle bg-bg-elevated p-6 transition-all hover:-translate-y-0.5 hover:border-accent-green"
            >
              <FileText className="h-8 w-8 text-accent-green" />
              <span className="font-heading text-lg font-medium text-text-primary">Markdown 原文</span>
              <span className="text-center text-xs text-text-muted">markdown_path · 原文链接</span>
            </a>
            <a
              href="/patch-toolbox/db/network-security.db"
              target="_blank"
              rel="noopener noreferrer"
              className="flex flex-col items-center gap-3 rounded-xl border border-border-subtle bg-bg-elevated p-6 transition-all hover:-translate-y-0.5 hover:border-accent-amber"
            >
              <Shield className="h-8 w-8 text-accent-amber" />
              <span className="font-heading text-lg font-medium text-text-primary">SQLite 下载</span>
              <span className="text-center text-xs text-text-muted">SQLite .db · 结构可查</span>
            </a>
          </div>
        </div>
      </section>

      {/* ── GitHub Stats Cards ──────────────────────────────── */}
      <section className="border-t border-border-subtle px-6 py-16">
        <div className="mx-auto max-w-[1200px]">
          <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
            <MetricCard icon={<Star className="h-5 w-5" />} value={String(stats.stars)} label={t('about.metricStars') as string} delay={0} />
            <MetricCard icon={<GitFork className="h-5 w-5" />} value={String(stats.forks)} label={t('about.metricForks') as string} delay={0.1} />
            <MetricCard icon={<Users className="h-5 w-5" />} value={String(stats.contributors)} label={t('about.metricContributors') as string} delay={0.2} />
            <MetricCard icon={<GitCommit className="h-5 w-5" />} value={String(stats.commits)} label={t('about.metricCommits') as string} delay={0.3} />
          </div>
        </div>
      </section>
    </div>
  );
}
