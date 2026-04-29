import { useState, useEffect, useMemo, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Search,
  Database,
  FileText,
  Calendar,
  X,
  ArrowRight,
  SearchX,
  Shield,
  Github,
  Flame,
  Landmark,
  ChevronDown,
  ExternalLink,
} from 'lucide-react';
import { useTranslation } from '@/i18n/LanguageContext';
import { loadEntries } from '@/lib/content';
import { cn } from '@/lib/utils';

/* ─── Types ─── */
type Severity = 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW' | 'N/A' | 'EXPLOIT';
type Source = 'NVD' | 'Exploit-DB' | 'GitHub' | 'CISA';

interface Vulnerability {
  id: string;
  severity: Severity;
  cvss?: number;
  description: string;
  source: Source;
  date: string;
  affected: string[];
  mitigation?: string;
  references?: string[];
}

/* ─── Fallback data (will be replaced by generated static data) ─── */
const FALLBACK_DATA: Vulnerability[] = [
  {
    id: 'CVE-2024-1086',
    severity: 'CRITICAL',
    cvss: 9.8,
    description: 'Use-after-free vulnerability in the Linux kernel netfilter subsystem allows local privilege escalation.',
    source: 'NVD',
    date: '2026-04-25',
    affected: ['Linux Kernel 5.15', 'Linux Kernel 6.1'],
    mitigation: 'Upgrade to Linux kernel 5.15.149+ or 6.1.76+. Apply vendor patches immediately.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-1086'],
  },
  {
    id: 'CVE-2024-38063',
    severity: 'CRITICAL',
    cvss: 9.8,
    description: 'Windows TCP/IP remote code execution vulnerability. An unauthenticated attacker can send malicious IPv6 packets.',
    source: 'NVD',
    date: '2026-04-24',
    affected: ['Windows 10', 'Windows 11', 'Windows Server 2022'],
    mitigation: 'Install Microsoft security update KB5043178. Disable IPv6 if not required as temporary workaround.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-38063'],
  },
  {
    id: 'CVE-2024-4358',
    severity: 'CRITICAL',
    cvss: 9.9,
    description: 'Progress Telerik Report Server authentication bypass allows remote code execution.',
    source: 'NVD',
    date: '2026-04-23',
    affected: ['Telerik Report Server 2024'],
    mitigation: 'Upgrade to Telerik Report Server 2024 Q2 or later. Restrict network access to management interface.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-4358'],
  },
  {
    id: 'GHSA-7jm2-g593-4qrc',
    severity: 'HIGH',
    cvss: 8.8,
    description: 'Express.js open redirect vulnerability via malformed URLs in location header.',
    source: 'GitHub',
    date: '2026-04-22',
    affected: ['express < 4.19.2', 'express < 5.0.0-beta.3'],
    mitigation: 'Update express to version 4.19.2 or 5.0.0-beta.3 and later. Validate redirect URLs.',
    references: ['https://github.com/advisories/GHSA-7jm2-g593-4qrc'],
  },
  {
    id: 'CVE-2024-4577',
    severity: 'HIGH',
    cvss: 8.5,
    description: 'PHP CGI argument injection vulnerability allowing remote code execution on Windows servers.',
    source: 'NVD',
    date: '2026-04-21',
    affected: ['PHP 8.1', 'PHP 8.2', 'PHP 8.3'],
    mitigation: 'Upgrade to PHP 8.1.29, 8.2.20, or 8.3.8. Apply mod_rewrite rules as workaround.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-4577'],
  },
  {
    id: 'CVE-2024-6387',
    severity: 'HIGH',
    cvss: 8.1,
    description: 'OpenSSH regreSSHion remote unauthenticated code execution in glibc-based Linux systems.',
    source: 'NVD',
    date: '2026-04-20',
    affected: ['OpenSSH 8.5p1 - 9.7p1'],
    mitigation: 'Upgrade to OpenSSH 9.8p1. Set LoginGraceTime to 0 as temporary mitigation.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-6387'],
  },
  {
    id: 'GHSA-qrp5-gfw2-gxv4',
    severity: 'HIGH',
    cvss: 8.2,
    description: 'Webpack-dev-middleware path traversal vulnerability exposing arbitrary files.',
    source: 'GitHub',
    date: '2026-04-19',
    affected: ['webpack-dev-middleware < 7.4.2'],
    mitigation: 'Update webpack-dev-middleware to 7.4.2 or later.',
    references: ['https://github.com/advisories/GHSA-qrp5-gfw2-gxv4'],
  },
  {
    id: 'CVE-2024-3400',
    severity: 'HIGH',
    cvss: 8.8,
    description: 'Palo Alto PAN-OS command injection in GlobalProtect gateway allowing arbitrary code execution.',
    source: 'NVD',
    date: '2026-04-18',
    affected: ['PAN-OS 10.2', 'PAN-OS 11.0', 'PAN-OS 11.1'],
    mitigation: 'Apply hotfix from Palo Alto. Enable threat prevention signatures.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-3400'],
  },
  {
    id: 'CVE-2024-4956',
    severity: 'MEDIUM',
    cvss: 5.3,
    description: 'Sonatype Nexus Repository Manager path traversal allowing unauthorized file access.',
    source: 'NVD',
    date: '2026-04-17',
    affected: ['Nexus Repository 3.68.0'],
    mitigation: 'Upgrade to Nexus Repository 3.68.1 or later.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-4956'],
  },
  {
    id: 'GHSA-m425-mxf2-mq53',
    severity: 'MEDIUM',
    cvss: 5.5,
    description: 'gRPC-Go denial of service via malformed HTTP/2 frames causing excessive CPU consumption.',
    source: 'GitHub',
    date: '2026-04-16',
    affected: ['google.golang.org/grpc < 1.64.1'],
    mitigation: 'Update gRPC-Go to 1.64.1 or later.',
    references: ['https://github.com/advisories/GHSA-m425-mxf2-mq53'],
  },
  {
    id: 'CVE-2024-22243',
    severity: 'MEDIUM',
    cvss: 5.9,
    description: 'Spring Framework open redirect via UriComponentsBuilder allowing unsafe URL redirection.',
    source: 'NVD',
    date: '2026-04-15',
    affected: ['Spring Framework 6.1.0 - 6.1.3', 'Spring Framework 6.0.15 - 6.0.16'],
    mitigation: 'Upgrade to Spring Framework 6.1.4 or 6.0.17.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-22243'],
  },
  {
    id: 'CVE-2024-27322',
    severity: 'MEDIUM',
    cvss: 6.5,
    description: 'RStudio deserialization vulnerability in RDS files allowing arbitrary code execution.',
    source: 'NVD',
    date: '2026-04-14',
    affected: ['RStudio Desktop 2023.12.0'],
    mitigation: 'Update to RStudio 2023.12.1 or later. Do not open untrusted RDS files.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-27322'],
  },
  {
    id: 'CVE-2024-21762',
    severity: 'MEDIUM',
    cvss: 6.3,
    description: 'Fortinet FortiOS SSL VPN out-of-bounds write allowing remote code execution.',
    source: 'NVD',
    date: '2026-04-13',
    affected: ['FortiOS 7.4.0 - 7.4.2', 'FortiOS 7.2.0 - 7.2.6'],
    mitigation: 'Upgrade to FortiOS 7.4.3 or 7.2.7. Disable SSL-VPN if not required.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-21762'],
  },
  {
    id: 'CVE-2024-10418',
    severity: 'LOW',
    cvss: 3.1,
    description: 'WordPress plugin WPForms Lite reflected cross-site scripting via admin page parameters.',
    source: 'NVD',
    date: '2026-04-12',
    affected: ['WPForms Lite < 1.8.9.6'],
    mitigation: 'Update WPForms Lite to 1.8.9.6 or later.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-10418'],
  },
  {
    id: 'CVE-2024-22369',
    severity: 'LOW',
    cvss: 3.7,
    description: 'Apache Airflow information disclosure in task logs exposing sensitive connection data.',
    source: 'NVD',
    date: '2026-04-11',
    affected: ['Apache Airflow < 2.8.2'],
    mitigation: 'Upgrade to Apache Airflow 2.8.2 or later. Review task log masking policies.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-22369'],
  },
  {
    id: 'CVE-2024-24557',
    severity: 'LOW',
    cvss: 3.9,
    description: 'Docker credential helper potential credential leak via environment variable exposure.',
    source: 'NVD',
    date: '2026-04-10',
    affected: ['docker-credential-helpers < 0.8.1'],
    mitigation: 'Update docker-credential-helpers to 0.8.1 or later.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-24557'],
  },
  {
    id: 'CVE-2024-3721',
    severity: 'N/A',
    cvss: undefined,
    description: 'Kubernetes kubelet potential denial of service via excessive pod creation requests.',
    source: 'NVD',
    date: '2026-04-09',
    affected: ['Kubernetes 1.28', 'Kubernetes 1.29'],
    mitigation: 'Apply resource quotas and limit ranges. Upgrade when patch is available.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-3721'],
  },
  {
    id: 'CVE-2024-1999',
    severity: 'N/A',
    cvss: undefined,
    description: 'Mozilla Firefox memory safety bugs fixed in version 125. Some bugs showed evidence of memory corruption.',
    source: 'NVD',
    date: '2026-04-08',
    affected: ['Firefox < 125.0'],
    mitigation: 'Update Firefox to version 125.0 or later.',
    references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-1999'],
  },
  {
    id: 'EDB-52042',
    severity: 'EXPLOIT',
    cvss: undefined,
    description: 'WordPress Plugin Duplicate Page 4.5.3 - Authenticated SQL Injection exploit.',
    source: 'Exploit-DB',
    date: '2026-04-07',
    affected: ['WordPress Duplicate Page 4.5.3'],
    mitigation: 'Update Duplicate Page plugin to latest version. Restrict admin access.',
    references: ['https://www.exploit-db.com/exploits/52042'],
  },
  {
    id: 'EDB-52038',
    severity: 'EXPLOIT',
    cvss: undefined,
    description: 'Apache Tomcat 9.0.82 - Remote Code Execution via JSP upload bypass.',
    source: 'Exploit-DB',
    date: '2026-04-06',
    affected: ['Apache Tomcat 9.0.82'],
    mitigation: 'Upgrade to Apache Tomcat 9.0.83 or later. Disable JSP uploads if not required.',
    references: ['https://www.exploit-db.com/exploits/52038'],
  },
  {
    id: 'CISA-KEV-2024-001',
    severity: 'CRITICAL',
    cvss: 9.6,
    description: 'CISA Known Exploited Vulnerability: Ivanti Connect Secure command injection actively exploited in the wild.',
    source: 'CISA',
    date: '2026-04-05',
    affected: ['Ivanti Connect Secure 22.6R1'],
    mitigation: 'Apply Ivanti hotfix immediately. Monitor for IOCs. Consider network segmentation.',
    references: ['https://www.cisa.gov/known-exploited-vulnerabilities-catalog'],
  },
  {
    id: 'CISA-KEV-2024-002',
    severity: 'HIGH',
    cvss: 8.4,
    description: 'CISA Known Exploited Vulnerability: JetBrains TeamCity authentication bypass with active exploitation.',
    source: 'CISA',
    date: '2026-04-04',
    affected: ['TeamCity 2023.11.3'],
    mitigation: 'Upgrade to TeamCity 2023.11.4 immediately. Rotate all CI/CD secrets.',
    references: ['https://www.cisa.gov/known-exploited-vulnerabilities-catalog'],
  },
];

/* ─── Severity Config ─── */
const SEVERITY_CONFIG: Record<
  Severity,
  { bg: string; text: string; border: string; pulse?: boolean }
> = {
  CRITICAL: {
    bg: 'rgba(239,68,68,0.15)',
    text: '#EF4444',
    border: '#EF4444',
    pulse: true,
  },
  HIGH: {
    bg: 'rgba(249,115,22,0.15)',
    text: '#F97316',
    border: '#F97316',
    pulse: true,
  },
  MEDIUM: {
    bg: 'rgba(245,158,11,0.15)',
    text: '#F59E0B',
    border: '#F59E0B',
  },
  LOW: {
    bg: 'rgba(59,130,246,0.15)',
    text: '#3B82F6',
    border: '#3B82F6',
  },
  'N/A': {
    bg: 'rgba(100,116,139,0.15)',
    text: '#64748B',
    border: '#64748B',
  },
  EXPLOIT: {
    bg: 'rgba(168,85,247,0.15)',
    text: '#A855F7',
    border: '#A855F7',
  },
};

const SEVERITY_ORDER: Severity[] = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'N/A', 'EXPLOIT'];

/* ─── Helpers ─── */
function severityRank(s: Severity): number {
  return SEVERITY_ORDER.indexOf(s);
}

function sourceIcon(source: Source) {
  switch (source) {
    case 'NVD':
      return <Shield className="h-3.5 w-3.5 text-accent-blue" />;
    case 'GitHub':
      return <Github className="h-3.5 w-3.5 text-accent-purple" />;
    case 'Exploit-DB':
      return <Flame className="h-3.5 w-3.5 text-accent-orange" />;
    case 'CISA':
      return <Landmark className="h-3.5 w-3.5 text-accent-red" />;
  }
}

function sourceLabel(source: Source): string {
  switch (source) {
    case 'NVD':
      return 'NVD/CVE';
    case 'GitHub':
      return 'GitHub Advisory';
    case 'Exploit-DB':
      return 'Exploit-DB';
    case 'CISA':
      return 'CISA KEV';
  }
}

/* ─── Severity Badge ─── */
function SeverityBadge({ severity }: { severity: Severity }) {
  const cfg = SEVERITY_CONFIG[severity];
  return (
    <span
      className={cn(
        'inline-flex items-center rounded px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider',
        cfg.pulse && 'animate-severity-pulse',
      )}
      style={{
        backgroundColor: cfg.bg,
        color: cfg.text,
        borderLeft: `3px solid ${cfg.border}`,
      }}
    >
      {severity}
    </span>
  );
}

/* ─── Source Filter Dropdown ─── */
const SOURCE_OPTIONS: (Source | 'All')[] = ['All', 'NVD', 'GitHub', 'Exploit-DB', 'CISA'];
const SORT_OPTIONS = ['newest', 'severity', 'cvss', 'id'] as const;
type SortOption = (typeof SORT_OPTIONS)[number];

/* ─── Main Component ─── */
export default function NetworkSecurity() {
  const { t, lang } = useTranslation();

  const [search, setSearch] = useState('');
  const [data, setData] = useState<Vulnerability[]>(FALLBACK_DATA);

  useEffect(() => {
    loadEntries().then((entries) => {
      if (Array.isArray(entries) && entries.length > 0) {
        setData(entries as Vulnerability[]);
      }
    }).catch(() => {});
  }, []);
  const [severityFilter, setSeverityFilter] = useState<Severity | 'All'>('All');
  const [sourceFilter, setSourceFilter] = useState<Source | 'All'>('All');
  const [sortBy, setSortBy] = useState<SortOption>('newest');
  const [sourceDropdownOpen, setSourceDropdownOpen] = useState(false);
  const [sortDropdownOpen, setSortDropdownOpen] = useState(false);
  const [selectedVuln, setSelectedVuln] = useState<Vulnerability | null>(null);

  /* Derived counts for stats */
  const severityCounts = useMemo(() => {
    const counts: Record<Severity, number> = {
      CRITICAL: 0,
      HIGH: 0,
      MEDIUM: 0,
      LOW: 0,
      'N/A': 0,
      EXPLOIT: 0,
    };
    data.forEach((v) => {
      counts[v.severity]++;
    });
    return counts;
  }, [data]);

  /* Filter & sort */
  const filtered = useMemo(() => {
    let items = [...data];

    if (search.trim()) {
      const q = search.toLowerCase();
      items = items.filter(
        (v) =>
          v.id.toLowerCase().includes(q) ||
          v.description.toLowerCase().includes(q) ||
          v.affected.some((a) => a.toLowerCase().includes(q)),
      );
    }

    if (severityFilter !== 'All') {
      items = items.filter((v) => v.severity === severityFilter);
    }

    if (sourceFilter !== 'All') {
      items = items.filter((v) => v.source === sourceFilter);
    }

    switch (sortBy) {
      case 'newest':
        items.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
        break;
      case 'severity':
        items.sort((a, b) => severityRank(a.severity) - severityRank(b.severity));
        break;
      case 'cvss':
        items.sort((a, b) => (b.cvss ?? 0) - (a.cvss ?? 0));
        break;
      case 'id':
        items.sort((a, b) => a.id.localeCompare(b.id));
        break;
    }

    return items;
  }, [search, severityFilter, sourceFilter, sortBy, data]);

  const clearFilters = useCallback(() => {
    setSearch('');
    setSeverityFilter('All');
    setSourceFilter('All');
    setSortBy('newest');
  }, []);

  /* Translation helpers */
  const tx = useCallback(
    (key: string) => (t(`networkSecurity.${key}`) as string) ?? key,
    [t],
  );

  const statsTotal = data.length;
  const statsUpdated = '2026-04-27';

  // Mixed-mode access URLs
  const markdownUrl = 'https://github.com/Christopher0129/patch-toolbox/blob/main/network-security/index.md';
  const dbUrl = '/patch-toolbox/db/network-security.db';
  const entriesUrl = '/patch-toolbox/data/entries.json';

  return (
    <div className="min-h-[100dvh] bg-bg-base">
      {/* ── Hero ── */}
      <section
        className="relative border-b border-border-subtle"
        style={{
          minHeight: 'max(40vh, 320px)',
          background: 'linear-gradient(180deg, #0A0E17 0%, #0F172A 50%, #111827 100%)',
        }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              'radial-gradient(ellipse at 50% 0%, rgba(59,130,246,0.15) 0%, transparent 60%)',
            animation: 'hero-glow-pulse 6s ease-in-out infinite',
          }}
        />
        <div className="relative mx-auto flex max-w-[1200px] flex-col justify-center px-6 pb-16 pt-24">
          {/* Breadcrumb */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.4 }}
            className="mb-4 flex items-center gap-2 text-xs font-medium tracking-wider text-text-muted"
          >
            <Link to="/" className="hover:text-text-primary transition-colors">
              {lang === 'zh' ? '首页' : lang === 'fr' ? 'Accueil' : lang === 'ja' ? 'ホーム' : lang === 'ko' ? '홈' : 'Home'}
            </Link>
            <span>/</span>
            <span>
              {lang === 'zh'
                ? '分类'
                : lang === 'fr'
                  ? 'Catégories'
                  : lang === 'ja'
                    ? 'カテゴリー'
                    : lang === 'ko'
                      ? '카테고리'
                      : 'Categories'}
            </span>
            <span>/</span>
            <span className="text-text-primary">{tx('pageTitle')}</span>
          </motion.div>

          {/* Title */}
          <motion.h1
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.1, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            className="font-heading text-4xl font-bold tracking-tight text-text-primary md:text-5xl"
          >
            {tx('pageTitle')}
          </motion.h1>

          {/* Subtitle */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.25 }}
            className="mt-3 max-w-2xl text-lg leading-relaxed text-text-secondary"
          >
            {tx('subtitle')}
          </motion.p>

          {/* Mixed-mode Access Links */}
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.35 }}
            className="mt-6 flex flex-wrap items-center gap-3"
          >
            <a
              href={markdownUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 rounded-md bg-accent-green/10 px-3 py-1.5 text-xs font-medium text-accent-green transition-colors hover:bg-accent-green/20"
            >
              <FileText className="h-3.5 w-3.5" />
              Markdown 原文
            </a>
            <a
              href={dbUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 rounded-md bg-accent-blue/10 px-3 py-1.5 text-xs font-medium text-accent-blue transition-colors hover:bg-accent-blue/20"
            >
              <Database className="h-3.5 w-3.5" />
              SQLite 下载
            </a>
            <a
              href={entriesUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 rounded-md bg-accent-cyan/10 px-3 py-1.5 text-xs font-medium text-accent-cyan transition-colors hover:bg-accent-cyan/20"
            >
              <ExternalLink className="h-3.5 w-3.5" />
              前端数据
            </a>
          </motion.div>

          {/* Stats Row */}
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="mt-2 flex flex-wrap items-center gap-6 md:gap-8"
          >
            <div className="flex items-center gap-2">
              <Database className="h-5 w-5 text-text-muted" />
              <div>
                <span className="font-mono text-xl font-medium text-text-primary">{statsTotal}</span>
                <span className="ml-2 text-xs font-medium uppercase tracking-wider text-text-muted">
                  {tx('totalEntries')}
                </span>
              </div>
            </div>

            <div className="flex items-center gap-3">
              {(['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'N/A'] as Severity[]).map((sev) => (
                <div key={sev} className="flex items-center gap-1.5">
                  <span
                    className="font-mono text-sm font-medium"
                    style={{ color: SEVERITY_CONFIG[sev].text }}
                  >
                    {severityCounts[sev]}
                  </span>
                  <SeverityBadge severity={sev} />
                </div>
              ))}
            </div>

            <div className="flex items-center gap-2">
              <Calendar className="h-5 w-5 text-text-muted" />
              <div>
                <span className="text-xs font-medium uppercase tracking-wider text-text-muted">
                  {tx('updated')}
                </span>
                <span className="ml-2 font-mono text-sm text-text-primary">{statsUpdated}</span>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* ── Filter Bar ── */}
      <motion.section
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, delay: 0.5 }}
        className="sticky top-16 z-40 border-b border-border-subtle px-6 py-4"
        style={{ backgroundColor: 'rgba(10,14,23,0.95)', backdropFilter: 'blur(12px)' }}
      >
        <div className="mx-auto flex max-w-[1200px] flex-wrap items-center gap-4">
          {/* Search */}
          <div className="relative flex-shrink-0">
            <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-text-muted" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder={tx('searchPlaceholder')}
              className="h-10 w-64 rounded-lg border border-border-subtle bg-bg-surface pl-9 pr-4 text-sm text-text-primary outline-none transition-all placeholder:text-text-muted focus:border-accent-blue focus:ring-1 focus:ring-accent-blue md:w-80"
            />
            {search && (
              <button
                onClick={() => setSearch('')}
                className="absolute right-2 top-1/2 -translate-y-1/2 text-text-muted hover:text-text-primary"
              >
                <X className="h-4 w-4" />
              </button>
            )}
          </div>

          {/* Severity Chips */}
          <div className="flex flex-wrap items-center gap-2">
            {(['All', ...SEVERITY_ORDER] as (Severity | 'All')[]).map((sev) => {
              const active = severityFilter === sev;
              const cfg = sev === 'All' ? null : SEVERITY_CONFIG[sev];
              return (
                <button
                  key={sev}
                  onClick={() => setSeverityFilter(sev)}
                  className={cn(
                    'rounded-full border px-3 py-1 text-xs font-medium uppercase tracking-wider transition-all',
                    active
                      ? 'border-transparent'
                      : 'border-border-subtle text-text-muted hover:border-border-active hover:text-text-primary',
                  )}
                  style={
                    active && cfg
                      ? {
                          backgroundColor: cfg.bg,
                          color: cfg.text,
                          borderColor: cfg.border,
                        }
                      : active && sev === 'All'
                        ? {
                            backgroundColor: 'rgba(59,130,246,0.15)',
                            color: '#3B82F6',
                            borderColor: '#3B82F6',
                          }
                        : {}
                  }
                >
                  {sev === 'All' ? tx('all') : sev}
                </button>
              );
            })}
          </div>

          {/* Source Dropdown */}
          <div className="relative ml-auto">
            <button
              onClick={() => {
                setSourceDropdownOpen(!sourceDropdownOpen);
                setSortDropdownOpen(false);
              }}
              className="flex h-9 items-center gap-1.5 rounded-md border border-border-active px-3 text-xs font-medium text-text-secondary transition-colors hover:border-text-muted hover:text-text-primary"
            >
              {tx('source')}: {sourceFilter === 'All' ? tx('all') : sourceLabel(sourceFilter as Source)}
              <ChevronDown className={`h-3.5 w-3.5 transition-transform ${sourceDropdownOpen ? 'rotate-180' : ''}`} />
            </button>
            <AnimatePresence>
              {sourceDropdownOpen && (
                <motion.div
                  initial={{ opacity: 0, y: -4 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -4 }}
                  transition={{ duration: 0.15 }}
                  className="absolute right-0 top-full mt-2 w-48 overflow-hidden rounded-lg border border-border-subtle bg-bg-elevated shadow-xl"
                >
                  {SOURCE_OPTIONS.map((s) => (
                    <button
                      key={s}
                      onClick={() => {
                        setSourceFilter(s as Source | 'All');
                        setSourceDropdownOpen(false);
                      }}
                      className={cn(
                        'flex w-full items-center gap-2 px-3 py-2 text-left text-sm transition-colors',
                        sourceFilter === s
                          ? 'bg-bg-surface text-accent-blue'
                          : 'text-text-secondary hover:bg-bg-surface hover:text-text-primary',
                      )}
                    >
                      {s !== 'All' && sourceIcon(s as Source)}
                      <span>{s === 'All' ? tx('all') : sourceLabel(s as Source)}</span>
                    </button>
                  ))}
                </motion.div>
              )}
            </AnimatePresence>
          </div>

          {/* Sort Dropdown */}
          <div className="relative">
            <button
              onClick={() => {
                setSortDropdownOpen(!sortDropdownOpen);
                setSourceDropdownOpen(false);
              }}
              className="flex h-9 items-center gap-1.5 rounded-md border border-border-active px-3 text-xs font-medium text-text-secondary transition-colors hover:border-text-muted hover:text-text-primary"
            >
              {tx('sort')}: {tx(`sort_${sortBy}`)}
              <ChevronDown className={`h-3.5 w-3.5 transition-transform ${sortDropdownOpen ? 'rotate-180' : ''}`} />
            </button>
            <AnimatePresence>
              {sortDropdownOpen && (
                <motion.div
                  initial={{ opacity: 0, y: -4 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -4 }}
                  transition={{ duration: 0.15 }}
                  className="absolute right-0 top-full mt-2 w-44 overflow-hidden rounded-lg border border-border-subtle bg-bg-elevated shadow-xl"
                >
                  {SORT_OPTIONS.map((s) => (
                    <button
                      key={s}
                      onClick={() => {
                        setSortBy(s);
                        setSortDropdownOpen(false);
                      }}
                      className={cn(
                        'flex w-full px-3 py-2 text-left text-sm transition-colors',
                        sortBy === s
                          ? 'bg-bg-surface text-accent-blue'
                          : 'text-text-secondary hover:bg-bg-surface hover:text-text-primary',
                      )}
                    >
                      {tx(`sort_${s}`)}
                    </button>
                  ))}
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </motion.section>

      {/* ── Vulnerability Grid ── */}
      <section className="mx-auto max-w-[1200px] px-6 py-10">
        {filtered.length === 0 ? (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="flex flex-col items-center justify-center py-32"
          >
            <SearchX className="h-16 w-16 text-text-muted" />
            <h2 className="mt-6 font-heading text-2xl font-medium text-text-primary">{tx('noResults')}</h2>
            <p className="mt-2 text-text-secondary">{tx('noResultsDesc')}</p>
            <button
              onClick={clearFilters}
              className="mt-6 rounded-md border border-border-active px-4 py-2 text-sm font-medium text-text-secondary transition-all hover:border-text-muted hover:text-text-primary"
            >
              {tx('clearFilters')}
            </button>
          </motion.div>
        ) : (
          <motion.div
            layout
            className="grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3"
          >
            <AnimatePresence mode="popLayout">
              {filtered.map((vuln, i) => (
                <motion.article
                  key={vuln.id}
                  layout
                  initial={{ opacity: 0, y: 30 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{
                    duration: 0.4,
                    delay: i * 0.06,
                    ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
                  }}
                  className="group cursor-pointer"
                  onClick={() => setSelectedVuln(vuln)}
                >
                  <div
                    className="relative flex h-full flex-col rounded-xl border border-border-subtle p-5 transition-all duration-300 hover:-translate-y-0.5 hover:border-border-active"
                    style={{
                      background:
                        'linear-gradient(145deg, rgba(17,24,39,0.9) 0%, rgba(26,35,50,0.6) 100%)',
                      borderLeft: `3px solid ${SEVERITY_CONFIG[vuln.severity].border}`,
                      boxShadow: '0 0 0 rgba(0,0,0,0)',
                    }}
                    onMouseEnter={(e) => {
                      (e.currentTarget as HTMLDivElement).style.boxShadow =
                        '0 4px 20px rgba(0,0,0,0.3), 0 0 20px rgba(59,130,246,0.08)';
                    }}
                    onMouseLeave={(e) => {
                      (e.currentTarget as HTMLDivElement).style.boxShadow = '0 0 0 rgba(0,0,0,0)';
                    }}
                  >
                    {/* Header */}
                    <div className="flex items-start justify-between gap-3">
                      <div className="flex items-center gap-2">
                        {sourceIcon(vuln.source)}
                        <h3 className="font-mono text-base font-medium text-text-primary">
                          {vuln.id}
                        </h3>
                      </div>
                      <SeverityBadge severity={vuln.severity} />
                    </div>

                    {/* Description */}
                    <p className="mt-3 line-clamp-2 text-sm leading-relaxed text-text-secondary">
                      {vuln.description}
                    </p>

                    {/* Meta */}
                    <div className="mt-auto flex items-center justify-between pt-4">
                      <div className="flex items-center gap-3">
                        {vuln.cvss !== undefined ? (
                          <span
                            className="font-mono text-sm font-medium"
                            style={{ color: SEVERITY_CONFIG[vuln.severity].text }}
                          >
                            CVSS: {vuln.cvss}
                          </span>
                        ) : vuln.severity === 'EXPLOIT' ? (
                          <span className="font-mono text-xs text-accent-purple">
                            {tx('exploitConfirmed')}
                          </span>
                        ) : (
                          <span className="font-mono text-xs text-text-muted">
                            {tx('pendingAssessment')}
                          </span>
                        )}
                        <span className="text-xs text-text-muted">{vuln.date}</span>
                      </div>
                      <span className="flex items-center gap-1 text-xs font-medium text-accent-blue transition-colors group-hover:underline">
                        {tx('readMore')} <ArrowRight className="h-3.5 w-3.5" />
                      </span>
                    </div>
                  </div>
                </motion.article>
              ))}
            </AnimatePresence>
          </motion.div>
        )}
      </section>

      {/* ── Detail Modal ── */}
      <AnimatePresence>
        {selectedVuln && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="fixed inset-0 z-[70] flex items-center justify-center p-4"
            style={{ backgroundColor: 'rgba(0,0,0,0.7)', backdropFilter: 'blur(4px)' }}
            onClick={() => setSelectedVuln(null)}
          >
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              transition={{
                duration: 0.3,
                ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
              }}
              onClick={(e) => e.stopPropagation()}
              className="relative w-full max-w-[720px] overflow-hidden rounded-2xl border border-border-subtle bg-bg-surface"
            >
              {/* Modal Header */}
              <div className="flex items-start justify-between border-b border-border-subtle p-6 md:p-8">
                <div>
                  <div className="flex items-center gap-2">
                    {sourceIcon(selectedVuln.source)}
                    <h2 className="font-mono text-2xl font-bold text-text-primary">
                      {selectedVuln.id}
                    </h2>
                  </div>
                  <div className="mt-2 flex items-center gap-3">
                    <SeverityBadge severity={selectedVuln.severity} />
                    <a
                      href={selectedVuln.references?.[0] ?? '#'}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-1 text-xs font-medium text-accent-blue hover:underline"
                    >
                      {tx('viewOnSource')} <ExternalLink className="h-3 w-3" />
                    </a>
                  </div>
                </div>
                <button
                  onClick={() => setSelectedVuln(null)}
                  className="rounded-md p-1 text-text-muted transition-colors hover:bg-bg-elevated hover:text-text-primary"
                >
                  <X className="h-5 w-5" />
                </button>
              </div>

              {/* Modal Body */}
              <div className="space-y-6 p-6 md:p-8">
                {/* Severity Block */}
                <div>
                  <p className="mb-1 text-xs font-medium uppercase tracking-wider text-text-muted">
                    {tx('severityLabel')}
                  </p>
                  <div className="flex items-center gap-3">
                    <span
                      className="font-mono text-xl font-bold"
                      style={{ color: SEVERITY_CONFIG[selectedVuln.severity].text }}
                    >
                      {selectedVuln.severity}
                      {selectedVuln.cvss !== undefined && ` | CVSS: ${selectedVuln.cvss}`}
                    </span>
                  </div>
                  {selectedVuln.cvss !== undefined && (
                    <div className="mt-2 h-2 w-full overflow-hidden rounded-full bg-bg-elevated">
                      <div
                        className="h-full rounded-full transition-all duration-500"
                        style={{
                          width: `${Math.min((selectedVuln.cvss / 10) * 100, 100)}%`,
                          backgroundColor: SEVERITY_CONFIG[selectedVuln.severity].text,
                        }}
                      />
                    </div>
                  )}
                </div>

                {/* Description Block */}
                <div>
                  <p className="mb-2 text-xs font-medium uppercase tracking-wider text-text-muted">
                    {tx('descriptionLabel')}
                  </p>
                  <div
                    className="rounded-lg border-l-[3px] border-l-accent-blue p-4 text-sm leading-relaxed text-text-primary"
                    style={{
                      background: 'linear-gradient(180deg, #0D1117 0%, #161B22 100%)',
                      border: '1px solid #30363D',
                      borderLeft: '3px solid #3B82F6',
                    }}
                  >
                    {selectedVuln.description}
                  </div>
                </div>

                {/* Affected Block */}
                <div>
                  <p className="mb-2 text-xs font-medium uppercase tracking-wider text-text-muted">
                    {tx('affectedLabel')}
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {selectedVuln.affected.map((item) => (
                      <span
                        key={item}
                        className="rounded-md border border-border-subtle px-2.5 py-1 text-xs text-text-secondary"
                        style={{ backgroundColor: 'rgba(26,35,50,0.6)' }}
                      >
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Mitigation Block */}
                {selectedVuln.mitigation && (
                  <div>
                    <p className="mb-2 text-xs font-medium uppercase tracking-wider text-text-muted">
                      {tx('mitigationLabel')}
                    </p>
                    <div
                      className="rounded-lg border-l-[3px] border-l-accent-blue p-4 text-sm leading-relaxed text-text-primary"
                      style={{
                        background: 'linear-gradient(180deg, #0D1117 0%, #161B22 100%)',
                        border: '1px solid #30363D',
                        borderLeft: '3px solid #22C55E',
                      }}
                    >
                      {selectedVuln.mitigation}
                    </div>
                  </div>
                )}

                {/* References Block */}
                {selectedVuln.references && selectedVuln.references.length > 0 && (
                  <div>
                    <p className="mb-2 text-xs font-medium uppercase tracking-wider text-text-muted">
                      {tx('referencesLabel')}
                    </p>
                    <ul className="space-y-1.5">
                      {selectedVuln.references.map((ref) => (
                        <li key={ref}>
                          <a
                            href={ref}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex items-center gap-1 text-sm text-accent-blue underline underline-offset-2 transition-colors hover:text-accent-cyan"
                          >
                            {ref}
                            <ExternalLink className="h-3 w-3" />
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>

              {/* Modal Footer */}
              <div className="flex items-center justify-between border-t border-border-subtle px-6 py-4 text-xs text-text-muted md:px-8">
                <span>
                  {tx('added')}: {selectedVuln.date}
                </span>
                <span>{tx('databaseInfo')}</span>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
