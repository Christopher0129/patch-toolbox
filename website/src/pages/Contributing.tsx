import { useTranslation } from '@/i18n/LanguageContext';
import { motion } from 'framer-motion';
import {
  Bug,
  Database,
  Code,
  ChevronRight,
  ExternalLink,
  Users,
  GitCommit,
  MessageCircle,
  FileCheck,
  Languages,
  CheckCircle,
  Github,
  Copy,
  Check,
  Play,
} from 'lucide-react';
import { useState, type ReactNode } from 'react';

/* ── Animation variants ────────────────────────────────────── */
/* const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  visible: (i: number) => ({
    opacity: 1,
    y: 0,
    transition: {
      delay: i * 0.1,
      duration: 0.5,
      ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
    },
  }),
}; */

/* const staggerContainer = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.08 },
  },
}; */

/* ── Reusable components ─────────────────────────────────── */
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

/* ── Contribute Card ───────────────────────────────────────── */
function ContributeCard({
  icon,
  title,
  description,
  buttonText,
  buttonHref,
  buttonVariant = 'primary',
  hoverAccent,
  delay,
}: {
  icon: ReactNode;
  title: string;
  description: string;
  buttonText: string;
  buttonHref: string;
  buttonVariant?: 'primary' | 'secondary';
  hoverAccent: string;
  delay: number;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{
        delay,
        duration: 0.6,
        ease: [0.16, 1, 0.3, 1] as [number, number, number, number],
      }}
    >
      <DataCard
        className={`group h-full transition-all duration-300 hover:border-${hoverAccent} hover:shadow-[0_0_20px_rgba(59,130,246,0.12)]`}
      >
        <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-bg-elevated">
          {icon}
        </div>
        <h3 className="mb-2 font-heading text-xl font-medium text-text-primary">{title}</h3>
        <p className="mb-6 text-sm leading-relaxed text-text-secondary">{description}</p>
        <a
          href={buttonHref}
          target="_blank"
          rel="noopener noreferrer"
          className={`inline-flex items-center gap-1.5 rounded-md px-4 py-2 text-sm font-medium transition-all ${
            buttonVariant === 'primary'
              ? 'bg-accent-blue text-white hover:bg-blue-600 hover:scale-[1.02]'
              : 'border border-border-active text-text-secondary hover:border-text-muted hover:text-text-primary'
          }`}
        >
          {buttonText}
          <ChevronRight className="h-4 w-4" />
        </a>
      </DataCard>
    </motion.div>
  );
}

/* ── Timeline Step ─────────────────────────────────────────── */
function TimelineStep({
  number,
  title,
  description,
  code,
  isLast,
  delay,
}: {
  number: string;
  title: string;
  description: string;
  code?: string;
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
      className="relative flex gap-6"
    >
      {/* Number circle */}
      <div className="flex flex-col items-center">
        <div className="flex h-10 w-10 items-center justify-center rounded-full border border-accent-blue/50 bg-bg-elevated font-mono text-sm font-bold text-accent-blue">
          {number}
        </div>
        {!isLast && (
          <div className="mt-3 w-px flex-1 bg-border-subtle" />
        )}
      </div>

      {/* Content */}
      <div className="pb-10">
        <h4 className="font-heading text-lg font-medium text-text-primary">{title}</h4>
        <p className="mt-1 text-sm leading-relaxed text-text-secondary">{description}</p>
        {code && (
          <div className="mt-3">
            <TerminalBlock>
              <code className="text-accent-green">$ {code}</code>
            </TerminalBlock>
          </div>
        )}
      </div>
    </motion.div>
  );
}

/* ── Format Rule Card ────────────────────────────────────── */
function RuleCard({
  number,
  title,
  description,
  delay,
}: {
  number: string;
  title: string;
  description: string;
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
      <DataCard className="border-l-[2px] border-l-accent-blue">
        <div className="flex items-start gap-3">
          <span className="flex h-6 w-6 items-center justify-center rounded-full bg-accent-blue/10 text-xs font-bold text-accent-blue">
            {number}
          </span>
          <div>
            <h4 className="font-medium text-text-primary">{title}</h4>
            <p className="mt-1 text-sm text-text-secondary">{description}</p>
          </div>
        </div>
      </DataCard>
    </motion.div>
  );
}

/* ── Validation Card ───────────────────────────────────────── */
function ValidationCard({
  icon,
  title,
  description,
  script,
  delay,
}: {
  icon: ReactNode;
  title: string;
  description: string;
  script: string;
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
      <DataCard>
        <div className="mb-3 flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-bg-elevated text-accent-green">
            {icon}
          </div>
          <h4 className="font-heading text-base font-medium text-text-primary">{title}</h4>
        </div>
        <p className="mb-3 text-sm text-text-secondary">{description}</p>
        <code className="rounded bg-bg-elevated px-2 py-1 font-mono text-xs text-accent-cyan">
          {script}
        </code>
      </DataCard>
    </motion.div>
  );
}

/* ── CI Badge Pill ─────────────────────────────────────────── */
function BadgePill({ icon, label }: { icon: ReactNode; label: string }) {
  return (
    <div className="inline-flex items-center gap-1.5 rounded-full border border-border-subtle bg-bg-elevated px-3 py-1.5 text-xs text-text-secondary">
      {icon}
      {label}
    </div>
  );
}

/* ── Main Contributing Page ────────────────────────────────── */
export default function Contributing() {
  const { t } = useTranslation();
  const [copied, setCopied] = useState(false);

  const exampleContent = `#### 1. CVE-2024-XXXX

**严重程度 / Severity**: HIGH | CVSS: 8.8

**漏洞描述 / Description**:
Buffer overflow in ExampleSoftware allows remote code execution.

**缓解方案 / Mitigation**:
Apply vendor patch v2.1.0 or disable affected module.

**参考链接 / References**:
- https://nvd.nist.gov/vuln/detail/CVE-2024-XXXX
- https://example.com/security/advisory-2024-001`;

  const handleCopy = () => {
    navigator.clipboard.writeText(exampleContent);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="min-h-[100dvh]">
      {/* ── Hero ──────────────────────────────────────────────── */}
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
            {t('contributing.breadcrumb') as string}
          </p>
          <h1 className="font-heading text-3xl font-bold text-text-primary md:text-4xl">
            {t('contributing.title') as string}
          </h1>
          <p className="mx-auto mt-4 max-w-xl text-lg leading-relaxed text-text-secondary">
            {t('contributing.subtitle') as string}
          </p>

          {/* Quick stats */}
          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.5 }}
            className="mt-8 flex flex-wrap items-center justify-center gap-8"
          >
            {[
              { icon: <Users className="h-5 w-5" />, value: '3', label: t('contributing.statContributors') as string },
              { icon: <GitCommit className="h-5 w-5" />, value: '63', label: t('contributing.statCommits') as string },
              { icon: <MessageCircle className="h-5 w-5" />, value: t('contributing.statIssuesValue') as string, label: t('contributing.statIssues') as string },
            ].map((stat) => (
              <div key={stat.label} className="flex items-center gap-3">
                <div className="text-accent-blue">{stat.icon}</div>
                <div className="text-left">
                  <div className="font-mono text-lg font-bold text-text-primary">{stat.value}</div>
                  <div className="text-xs text-text-muted">{stat.label}</div>
                </div>
              </div>
            ))}
          </motion.div>
        </motion.div>
      </section>

      {/* ── Ways to Contribute ────────────────────────────────── */}
      <section className="px-6 py-20">
        <SectionHeader
          label={t('contributing.getInvolvedLabel') as string}
          title={t('contributing.getInvolvedTitle') as string}
        />
        <div className="mx-auto grid max-w-[1200px] gap-6 md:grid-cols-3">
          <ContributeCard
            icon={<Bug className="h-6 w-6 text-accent-red" />}
            title={t('contributing.reportIssuesTitle') as string}
            description={t('contributing.reportIssuesDesc') as string}
            buttonText={t('contributing.reportIssuesBtn') as string}
            buttonHref="https://github.com/Christopher0129/patch-toolbox/issues"
            buttonVariant="primary"
            hoverAccent="accent-red"
            delay={0}
          />
          <ContributeCard
            icon={<Database className="h-6 w-6 text-accent-cyan" />}
            title={t('contributing.submitDataTitle') as string}
            description={t('contributing.submitDataDesc') as string}
            buttonText={t('contributing.submitDataBtn') as string}
            buttonHref="#format"
            buttonVariant="secondary"
            hoverAccent="accent-cyan"
            delay={0.12}
          />
          <ContributeCard
            icon={<Code className="h-6 w-6 text-accent-green" />}
            title={t('contributing.improveCodeTitle') as string}
            description={t('contributing.improveCodeDesc') as string}
            buttonText={t('contributing.improveCodeBtn') as string}
            buttonHref="https://github.com/Christopher0129/patch-toolbox/tree/main/scripts"
            buttonVariant="secondary"
            hoverAccent="accent-green"
            delay={0.24}
          />
        </div>
      </section>

      {/* ── Workflow Timeline ─────────────────────────────────── */}
      <section className="border-l-[3px] border-l-accent-blue bg-bg-surface px-6 py-20">
        <div className="mx-auto max-w-[800px]">
          <SectionHeader
            label={t('contributing.workflowLabel') as string}
            title={t('contributing.workflowTitle') as string}
          />
          <div className="mt-8">
            <TimelineStep
              number="01"
              title={t('contributing.step1Title') as string}
              description={t('contributing.step1Desc') as string}
              code="git clone https://github.com/YOUR_NAME/patch-toolbox.git"
              delay={0}
            />
            <TimelineStep
              number="02"
              title={t('contributing.step2Title') as string}
              description={t('contributing.step2Desc') as string}
              code="git checkout -b feature/add-cve-2024-xxxx"
              delay={0.1}
            />
            <TimelineStep
              number="03"
              title={t('contributing.step3Title') as string}
              description={t('contributing.step3Desc') as string}
              delay={0.2}
            />
            <TimelineStep
              number="04"
              title={t('contributing.step4Title') as string}
              description={t('contributing.step4Desc') as string}
              code="python scripts/validate_structure.py"
              delay={0.3}
            />
            <TimelineStep
              number="05"
              title={t('contributing.step5Title') as string}
              description={t('contributing.step5Desc') as string}
              isLast
              delay={0.4}
            />
          </div>
        </div>
      </section>

      {/* ── Format Guidelines ─────────────────────────────────── */}
      <section id="format" className="px-6 py-20">
        <div className="mx-auto max-w-[1200px]">
          <SectionHeader
            label={t('contributing.formatLabel') as string}
            title={t('contributing.formatTitle') as string}
          />

          <div className="grid gap-8 lg:grid-cols-2">
            {/* Left: Rules */}
            <div className="space-y-4">
              {[
                {
                  number: '1',
                  title: t('contributing.rule1Title') as string,
                  description: t('contributing.rule1Desc') as string,
                },
                {
                  number: '2',
                  title: t('contributing.rule2Title') as string,
                  description: t('contributing.rule2Desc') as string,
                },
                {
                  number: '3',
                  title: t('contributing.rule3Title') as string,
                  description: t('contributing.rule3Desc') as string,
                },
                {
                  number: '4',
                  title: t('contributing.rule4Title') as string,
                  description: t('contributing.rule4Desc') as string,
                },
                {
                  number: '5',
                  title: t('contributing.rule5Title') as string,
                  description: t('contributing.rule5Desc') as string,
                },
              ].map((rule, i) => (
                <RuleCard key={rule.number} {...rule} delay={i * 0.08} />
              ))}
            </div>

            {/* Right: Example */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
            >
              <div className="sticky top-24">
                <div className="mb-2 flex items-center justify-between">
                  <p className="text-xs font-medium uppercase tracking-wider text-text-muted">
                    {t('contributing.exampleLabel') as string}
                  </p>
                  <button
                    onClick={handleCopy}
                    className="inline-flex items-center gap-1 rounded-md px-2 py-1 text-xs text-text-muted transition-colors hover:text-text-primary"
                  >
                    {copied ? (
                      <>
                        <Check className="h-3.5 w-3.5 text-accent-green" />
                        Copied
                      </>
                    ) : (
                      <>
                        <Copy className="h-3.5 w-3.5" />
                        Copy
                      </>
                    )}
                  </button>
                </div>
                <TerminalBlock accent="green">
                  <pre className="whitespace-pre-wrap text-accent-green">{exampleContent}</pre>
                </TerminalBlock>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* ── CI & Validation ───────────────────────────────────── */}
      <section className="bg-bg-surface px-6 py-20">
        <div className="mx-auto max-w-[1200px]">
          <SectionHeader
            label={t('contributing.validationLabel') as string}
            title={t('contributing.validationTitle') as string}
          />

          <div className="grid gap-6 md:grid-cols-3">
            <ValidationCard
              icon={<FileCheck className="h-5 w-5" />}
              title={t('contributing.checkStructureTitle') as string}
              description={t('contributing.checkStructureDesc') as string}
              script="validate_structure.py"
              delay={0}
            />
            <ValidationCard
              icon={<Languages className="h-5 w-5" />}
              title={t('contributing.checkBilingualTitle') as string}
              description={t('contributing.checkBilingualDesc') as string}
              script="validate_bilingual.py"
              delay={0.1}
            />
            <ValidationCard
              icon={<Database className="h-5 w-5" />}
              title={t('contributing.checkDbTitle') as string}
              description={t('contributing.checkDbDesc') as string}
              script="verify_db_sync.py"
              delay={0.2}
            />
          </div>

          {/* CI Badge Row */}
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ delay: 0.3, duration: 0.5 }}
            className="mt-8 flex flex-wrap justify-center gap-3"
          >
            <BadgePill icon={<Play className="h-3.5 w-3.5" />} label="GitHub Actions" />
            <BadgePill icon={<Code className="h-3.5 w-3.5" />} label="Python 3.12" />
            <BadgePill icon={<CheckCircle className="h-3.5 w-3.5" />} label="MIT Licensed" />
          </motion.div>
        </div>
      </section>

      {/* ── CTA Banner ────────────────────────────────────────── */}
      <section className="border-y border-border-subtle px-6 py-20">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] as [number, number, number, number] }}
          className="mx-auto max-w-[800px] text-center"
        >
          <h2 className="font-heading text-3xl font-bold text-text-primary md:text-4xl">
            {t('contributing.ctaTitle') as string}
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-lg text-text-secondary">
            {t('contributing.ctaDesc') as string}
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
            <a
              href="https://github.com/Christopher0129/patch-toolbox/blob/main/CONTRIBUTING.md"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-md bg-accent-blue px-6 py-3 text-sm font-medium text-white transition-all hover:scale-[1.02] hover:bg-blue-600"
            >
              {t('contributing.ctaPrimaryBtn') as string}
              <ExternalLink className="h-4 w-4" />
            </a>
            <a
              href="https://github.com/Christopher0129/patch-toolbox/issues?q=is%3Aissue+label%3A%22good+first+issue%22"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-md border border-border-active px-6 py-3 text-sm font-medium text-text-secondary transition-all hover:border-text-muted hover:text-text-primary"
            >
              {t('contributing.ctaSecondaryBtn') as string}
              <Github className="h-4 w-4" />
            </a>
          </div>

          {/* Links to docs */}
          <div className="mt-6 flex flex-wrap items-center justify-center gap-4 text-sm text-text-muted">
            <a
              href="https://github.com/Christopher0129/patch-toolbox/blob/main/CONTRIBUTING.md"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 transition-colors hover:text-accent-blue"
            >
              <ExternalLink className="h-3.5 w-3.5" />
              CONTRIBUTING.md
            </a>
            <span className="text-border-active">|</span>
            <a
              href="https://github.com/Christopher0129/patch-toolbox/blob/main/ARCHITECTURE.md"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 transition-colors hover:text-accent-blue"
            >
              <ExternalLink className="h-3.5 w-3.5" />
              ARCHITECTURE.md
            </a>
          </div>
        </motion.div>
      </section>
    </div>
  );
}
