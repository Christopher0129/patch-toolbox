import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Monitor,
  Terminal,
  Apple,
  AlertTriangle,
  ChevronRight,
  Clock,
  CheckCircle2,
} from 'lucide-react';
import { useTranslation } from '@/i18n/LanguageContext';
import { loadEntries } from '@/lib/content';

/* ------------------------------------------------------------------ */
/*  Types                                                               */
/* ------------------------------------------------------------------ */

type Severity = 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
type Platform = 'windows' | 'linux' | 'macos';

interface VulnerabilityItem {
  id: string;
  cve?: string;
  name: string;
  severity: Severity;
  affected: string;
  patchStatus: string;
  description: string;
  date: string;
}

/* ------------------------------------------------------------------ */
/*  Mock Data                                                           */
/* ------------------------------------------------------------------ */

const vulnerabilities: Record<Platform, VulnerabilityItem[]> = {
  windows: [
    {
      id: 'KB5034441',
      cve: 'CVE-2024-21305',
      name: 'Windows Hyper-V Privilege Escalation',
      severity: 'CRITICAL',
      affected: 'Windows 10/11, Server 2019, Server 2022',
      patchStatus: 'patched',
      description: 'A vulnerability in Hyper-V allows attackers to escape the guest VM and execute code on the host system with elevated privileges.',
      date: '2026-04-28',
    },
    {
      id: 'KB5036893',
      cve: 'CVE-2024-21412',
      name: 'Windows Defender SmartScreen Bypass',
      severity: 'HIGH',
      affected: 'Windows 10/11, Server 2022',
      patchStatus: 'patched',
      description: 'Attackers can craft malicious files that bypass SmartScreen warnings, leading to remote code execution via social engineering.',
      date: '2026-04-15',
    },
    {
      id: 'KB5036892',
      cve: 'CVE-2024-21413',
      name: 'Microsoft Outlook Remote Code Execution',
      severity: 'CRITICAL',
      affected: 'Office 2019, Office 2021, Microsoft 365',
      patchStatus: 'patched',
      description: 'A critical RCE vulnerability in Outlook that can be triggered without user interaction when processing certain email formats.',
      date: '2026-04-10',
    },
    {
      id: 'KB5034440',
      cve: 'CVE-2024-26198',
      name: 'Windows Kernel Elevation of Privilege',
      severity: 'HIGH',
      affected: 'Windows 10/11, Server 2019+',
      patchStatus: 'patched',
      description: 'Local attackers can exploit a race condition in the Windows kernel to gain SYSTEM-level privileges.',
      date: '2026-03-28',
    },
    {
      id: 'KB5034442',
      cve: 'CVE-2024-30051',
      name: 'Windows DWM Information Disclosure',
      severity: 'MEDIUM',
      affected: 'Windows 11 22H2, 23H2',
      patchStatus: 'patched',
      description: 'The Desktop Window Manager improperly handles objects in memory, allowing information disclosure across process boundaries.',
      date: '2026-03-15',
    },
    {
      id: 'KB5036894',
      cve: 'CVE-2024-30044',
      name: 'Windows SMB Denial of Service',
      severity: 'MEDIUM',
      affected: 'Windows 10/11, Server 2016+',
      patchStatus: 'pending',
      description: 'A specially crafted SMB packet can cause the server service to crash, resulting in a system-wide denial of service.',
      date: '2026-03-05',
    },
    {
      id: 'KB5036895',
      cve: 'CVE-2024-38063',
      name: 'Windows IPv6 Remote Code Execution',
      severity: 'HIGH',
      affected: 'Windows 10/11, Server 2019+',
      patchStatus: 'patched',
      description: 'A heap-based buffer overflow in the Windows TCP/IP stack when processing IPv6 packets enables remote code execution.',
      date: '2026-02-20',
    },
  ],
  linux: [
    {
      id: 'CVE-2024-1086',
      name: 'Linux Kernel Local Privilege Escalation (Nftables)',
      severity: 'CRITICAL',
      affected: 'Linux 5.14 - 6.6',
      patchStatus: 'patched',
      description: 'A use-after-free vulnerability in the nftables subsystem allows unprivileged local users to escalate to root.',
      date: '2026-04-25',
    },
    {
      id: 'CVE-2024-3094',
      name: 'XZ Utils Backdoor (Supply Chain)',
      severity: 'CRITICAL',
      affected: 'XZ Utils 5.6.0 - 5.6.1',
      patchStatus: 'patched',
      description: 'A sophisticated supply chain attack inserted a backdoor into XZ Utils, allowing remote code execution via SSH.',
      date: '2026-04-01',
    },
    {
      id: 'CVE-2024-28085',
      name: 'util-linux wall Escape Sequence Injection',
      severity: 'MEDIUM',
      affected: 'util-linux 2.37 - 2.39',
      patchStatus: 'patched',
      description: 'The wall command does not filter escape sequences, allowing attackers to inject terminal escape codes and manipulate displays.',
      date: '2026-03-20',
    },
    {
      id: 'CVE-2024-27316',
      name: 'Apache HTTP/2 Rapid Reset DDoS',
      severity: 'HIGH',
      affected: 'Apache HTTP Server 2.4.17 - 2.4.58',
      patchStatus: 'patched',
      description: 'HTTP/2 rapid stream resets can be abused to cause a denial of service on affected Apache servers with minimal client bandwidth.',
      date: '2026-03-10',
    },
    {
      id: 'CVE-2024-2961',
      name: 'glibc Iconv Buffer Overflow',
      severity: 'HIGH',
      affected: 'glibc 2.32 - 2.38',
      patchStatus: 'patched',
      description: 'A buffer overflow in glibc iconv conversion functions can lead to code execution when processing specially crafted character sequences.',
      date: '2026-02-28',
    },
    {
      id: 'CVE-2024-22252',
      name: 'Linux KVM vmx VM Escape',
      severity: 'HIGH',
      affected: 'Linux 5.10 - 6.7',
      patchStatus: 'patched',
      description: 'A vulnerability in the KVM vmx implementation allows a malicious guest VM to read memory from the host kernel.',
      date: '2026-02-15',
    },
    {
      id: 'CVE-2024-0646',
      name: 'Linux Netfilter Use-After-Free',
      severity: 'MEDIUM',
      affected: 'Linux 5.4 - 6.5',
      patchStatus: 'patched',
      description: 'A use-after-free in the netfilter subsystem can be triggered by local users to cause kernel panic or privilege escalation.',
      date: '2026-02-05',
    },
  ],
  macos: [
    {
      id: 'CVE-2024-23225',
      name: 'macOS Kernel Privilege Escalation',
      severity: 'HIGH',
      affected: 'macOS Sonoma 14.0 - 14.3, Ventura 13.6',
      patchStatus: 'patched',
      description: 'A memory corruption issue in the macOS kernel allows a malicious application to execute arbitrary code with kernel privileges.',
      date: '2026-04-22',
    },
    {
      id: 'CVE-2024-23204',
      name: 'Shortcuts App Information Disclosure',
      severity: 'MEDIUM',
      affected: 'macOS Sonoma 14.0 - 14.3',
      patchStatus: 'patched',
      description: 'A vulnerability in the Shortcuts app may allow access to sensitive user information without proper authorization checks.',
      date: '2026-04-12',
    },
    {
      id: 'CVE-2024-23296',
      name: 'Safari WebKit Remote Code Execution',
      severity: 'CRITICAL',
      affected: 'Safari 17.0 - 17.3, iOS 17.0 - 17.3',
      patchStatus: 'patched',
      description: 'A type confusion vulnerability in WebKit allows malicious web content to execute arbitrary code when processed by Safari.',
      date: '2026-03-30',
    },
    {
      id: 'CVE-2024-23222',
      name: 'macOS Mail App Privilege Escalation',
      severity: 'HIGH',
      affected: 'macOS Sonoma 14.0 - 14.2',
      patchStatus: 'patched',
      description: 'A path handling issue in Mail allows a maliciously crafted email attachment to gain elevated privileges when opened.',
      date: '2026-03-18',
    },
    {
      id: 'CVE-2024-23212',
      name: 'Time Machine Backup Encryption Bypass',
      severity: 'MEDIUM',
      affected: 'macOS Ventura 13.0 - 13.6, Sonoma 14.0 - 14.1',
      patchStatus: 'patched',
      description: 'An encryption logic flaw may cause Time Machine backups to be stored without proper encryption on certain network destinations.',
      date: '2026-03-08',
    },
    {
      id: 'CVE-2024-23234',
      name: 'macOS System Preferences Sandbox Escape',
      severity: 'HIGH',
      affected: 'macOS Sonoma 14.0 - 14.3',
      patchStatus: 'patched',
      description: 'A sandbox escape vulnerability in System Preferences allows malicious applications to modify system settings without authorization.',
      date: '2026-02-25',
    },
    {
      id: 'CVE-2024-23256',
      name: 'macOS Bluetooth Stack Buffer Overflow',
      severity: 'MEDIUM',
      affected: 'macOS Ventura 13.0 - 13.6',
      patchStatus: 'pending',
      description: 'A buffer overflow in the Bluetooth stack can be triggered by nearby devices, potentially leading to arbitrary code execution.',
      date: '2026-02-10',
    },
  ],
};

const platformMeta: Record<
  Platform,
  { icon: React.ReactNode; color: string; labelKey: string; count: number }
> = {
  windows: {
    icon: <Monitor className="h-5 w-5" />,
    color: '#3B82F6',
    labelKey: 'windows',
    count: vulnerabilities.windows.length,
  },
  linux: {
    icon: <Terminal className="h-5 w-5" />,
    color: '#F59E0B',
    labelKey: 'linux',
    count: vulnerabilities.linux.length,
  },
  macos: {
    icon: <Apple className="h-5 w-5" />,
    color: '#94A3B8',
    labelKey: 'macos',
    count: vulnerabilities.macos.length,
  },
};

/* ------------------------------------------------------------------ */
/*  Severity Config                                                       */
/* ------------------------------------------------------------------ */

const severityConfig: Record<
  Severity,
  { bg: string; text: string; border: string }
> = {
  CRITICAL: {
    bg: 'rgba(239,68,68,0.15)',
    text: '#EF4444',
    border: '#EF4444',
  },
  HIGH: {
    bg: 'rgba(249,115,22,0.15)',
    text: '#F97316',
    border: '#F97316',
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
};

/* ------------------------------------------------------------------ */
/*  Animation Variants                                                  */
/* ------------------------------------------------------------------ */

const containerVariants = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.06 },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] },
  },
};

const tabContentVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { duration: 0.3 },
  },
  exit: { opacity: 0, transition: { duration: 0.15 } },
};

/* ------------------------------------------------------------------ */
/*  Page Component                                                      */
/* ------------------------------------------------------------------ */

export default function SystemVulnerabilities() {
  const { t } = useTranslation();
  const [activeTab, setActiveTab] = useState<Platform>('windows');
  const [data, setData] = useState(vulnerabilities);

  // Wire to generated static data
  useEffect(() => {
    loadEntries().then((entries) => {
      if (Array.isArray(entries) && entries.length > 0) {
        // Map entries into the Platform record shape if they match
        setData(prev => prev); // placeholder — static data will replace mock in future task
      }
    }).catch(() => {});
  }, []);

  // Mixed-mode access URLs
  const markdownUrl = 'https://github.com/Christopher0129/patch-toolbox/blob/main/system-vulnerabilities/index.md';
  const dbUrl = '/patch-toolbox/db/system-vulnerabilities.db';
  const entriesUrl = '/patch-toolbox/data/entries.json';

  const tabs: Platform[] = ['windows', 'linux', 'macos'];
  const currentData = data[activeTab];
  const meta = platformMeta[activeTab];

  return (
    <div className="min-h-[100dvh] bg-bg-base">
      {/* ============ HERO ============ */}
      <section className="relative flex min-h-[40vh] items-center border-b border-border-subtle px-6 pt-16">
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              'radial-gradient(ellipse at 50% 0%, rgba(59,130,246,0.12) 0%, transparent 60%)',
          }}
        />
        <div className="relative mx-auto w-full max-w-[1200px] py-12 md:py-20">
          {/* Breadcrumb */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.4 }}
            className="text-xs uppercase tracking-wider text-text-muted"
          >
            {t('systemVulnerabilities.breadcrumb') as string}
          </motion.p>

          {/* Title */}
          <motion.h1
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number], delay: 0.1 }}
            className="mt-4 font-heading text-3xl font-bold text-text-primary md:text-4xl"
          >
            {t('systemVulnerabilities.title') as string}
          </motion.h1>

          {/* Subtitle */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="mt-3 max-w-[640px] text-lg text-text-secondary"
          >
            {t('systemVulnerabilities.subtitle') as string}
          </motion.p>

          {/* Platform Summary Cards */}
          <motion.div
            initial="hidden"
            animate="visible"
            variants={containerVariants}
            className="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-3"
          >
            {tabs.map((tab) => {
              const m = platformMeta[tab];
              return (
                <motion.div
                  key={tab}
                  variants={itemVariants}
                  className="flex items-center gap-4 rounded-xl border border-border-subtle bg-bg-surface px-5 py-4 transition-all duration-300 hover:border-border-active"
                >
                  <div style={{ color: m.color }}>{m.icon}</div>
                  <div>
                    <p className="text-sm font-medium text-text-primary">
                      {t(`systemVulnerabilities.platform.${m.labelKey}`) as string}
                    </p>
                    <p className="text-xs text-text-muted">
                      {m.count} {t('systemVulnerabilities.entries') as string} ·{' '}
                      {t('systemVulnerabilities.updated') as string} 2026-04
                    </p>
                  </div>
                </motion.div>
              );
            })}
          </motion.div>
        </div>
      </section>

      {/* ============ STICKY TAB BAR ============ */}
      <div className="sticky top-16 z-40 border-b border-border-subtle" style={{ backgroundColor: 'rgba(10,14,23,0.95)', backdropFilter: 'blur(12px)' }}>
        <div className="mx-auto flex max-w-[1200px] items-center justify-center">
          {tabs.map((tab) => {
            const m = platformMeta[tab];
            const isActive = activeTab === tab;
            return (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                className="relative flex items-center gap-2 px-8 py-4 text-sm font-medium transition-colors"
                style={{
                  color: isActive ? '#F8FAFC' : '#64748B',
                  backgroundColor: isActive ? 'rgba(255,255,255,0.03)' : 'transparent',
                }}
                onMouseEnter={(e) => {
                  if (!isActive) e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.02)';
                }}
                onMouseLeave={(e) => {
                  if (!isActive) e.currentTarget.style.backgroundColor = 'transparent';
                }}
              >
                <span style={{ color: isActive ? m.color : undefined }}>{m.icon}</span>
                <span>{t(`systemVulnerabilities.platform.${m.labelKey}`) as string}</span>
                {isActive && (
                  <motion.div
                    layoutId="vuln-active-tab"
                    className="absolute bottom-0 left-0 right-0 h-0.5"
                    style={{ backgroundColor: m.color }}
                    transition={{ type: 'spring', stiffness: 400, damping: 30 }}
                  />
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* ============ CONTENT AREA ============ */}
      <section className="mx-auto max-w-[1200px] px-6 py-10">
        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial="hidden"
            animate="visible"
            exit="exit"
            variants={tabContentVariants}
          >
            {/* Platform Header */}
            <div className="mb-8 flex items-center gap-3">
              <span style={{ color: meta.color }} className="scale-125">
                {meta.icon}
              </span>
              <h2 className="font-heading text-2xl font-medium text-text-primary">
                {t(`systemVulnerabilities.platform.${meta.labelKey}`) as string}{' '}
                {t('systemVulnerabilities.vulnerabilities') as string}
              </h2>
            </div>

            {/* Mixed-mode Access Links */}
            <div className="mb-4 flex flex-wrap items-center gap-3">
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
            </div>

            {/* Stats Row */}
            <div className="mb-6 flex flex-wrap items-center gap-3">
              <span className="rounded bg-bg-surface px-3 py-1 text-xs text-text-muted">
                {currentData.length} {t('systemVulnerabilities.total') as string}
              </span>
              {['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'].map((sev) => {
                const count = currentData.filter((v) => v.severity === sev).length;
                if (count === 0) return null;
                const cfg = severityConfig[sev as Severity];
                return (
                  <span
                    key={sev}
                    className="rounded px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider"
                    style={{ backgroundColor: cfg.bg, color: cfg.text }}
                  >
                    {sev} {count}
                  </span>
                );
              })}
            </div>

            {/* Cards Grid */}
            <motion.div
              variants={containerVariants}
              initial="hidden"
              animate="visible"
              className="grid grid-cols-1 gap-5 md:grid-cols-2"
            >
              {currentData.map((item, idx) => (
                <motion.div
                  key={item.id + item.date}
                  variants={itemVariants}
                  custom={idx}
                  className="group relative overflow-hidden rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:-translate-y-0.5 hover:border-border-active hover:shadow-[0_0_20px_rgba(59,130,246,0.06)]"
                  style={{ borderLeftWidth: '3px', borderLeftColor: meta.color }}
                >
                  {/* Header Row */}
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="font-mono text-sm font-medium text-text-primary">
                        {item.id}
                        {item.cve && (
                          <span className="ml-2 text-xs text-text-muted">({item.cve})</span>
                        )}
                      </p>
                      <h3 className="mt-1 font-heading text-lg font-medium text-text-primary">
                        {item.name}
                      </h3>
                    </div>
                    <span
                      className="shrink-0 rounded px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider"
                      style={{
                        backgroundColor: severityConfig[item.severity].bg,
                        color: severityConfig[item.severity].text,
                      }}
                    >
                      {item.severity}
                    </span>
                  </div>

                  {/* Affected */}
                  <p className="mt-3 text-xs" style={{ color: meta.color }}>
                    {t('systemVulnerabilities.affected') as string}: {item.affected}
                  </p>

                  {/* Description */}
                  <p className="mt-2 line-clamp-2 text-sm leading-relaxed text-text-secondary">
                    {item.description}
                  </p>

                  {/* Patch Status */}
                  <div className="mt-4 flex items-center gap-2">
                    {item.patchStatus === 'patched' ? (
                      <CheckCircle2 className="h-4 w-4 text-accent-green" />
                    ) : (
                      <AlertTriangle className="h-4 w-4 text-accent-amber" />
                    )}
                    <span className="text-xs text-accent-green">
                      {t(`systemVulnerabilities.patchStatus.${item.patchStatus}`) as string}
                    </span>
                  </div>

                  {/* Meta */}
                  <div className="mt-4 flex items-center justify-between border-t border-border-subtle pt-3">
                    <div className="flex items-center gap-1.5 text-xs text-text-muted">
                      <Clock className="h-3.5 w-3.5" />
                      {item.date}
                    </div>
                    <span className="inline-flex items-center gap-1 text-xs text-text-muted transition-colors group-hover:text-accent-blue">
                      {t('systemVulnerabilities.readMore') as string}
                      <ChevronRight className="h-3.5 w-3.5" />
                    </span>
                  </div>
                </motion.div>
              ))}
            </motion.div>
          </motion.div>
        </AnimatePresence>
      </section>
    </div>
  );
}
