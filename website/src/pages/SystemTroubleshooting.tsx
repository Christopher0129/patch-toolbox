import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Monitor,
  Terminal,
  Apple,
  Wrench,
  CheckCircle2,
  Clock,
  ChevronRight,
  AlertCircle,
  Users,
} from 'lucide-react';
import { useTranslation } from '@/i18n/LanguageContext';
import { loadEntries } from '@/lib/content';

/* ------------------------------------------------------------------ */
/*  Types                                                               */
/* ------------------------------------------------------------------ */

type Difficulty = 'Easy' | 'Medium' | 'Hard';
type Platform = 'windows' | 'linux' | 'macos';

interface TroubleshootingItem {
  id: string;
  title: string;
  symptoms: string[];
  solution: string[];
  difficulty: Difficulty;
  source: string;
  contributor: string;
  date: string;
  verified: boolean;
}

/* ------------------------------------------------------------------ */
/*  Mock Data                                                           */
/* ------------------------------------------------------------------ */

const troubleshooting: Record<Platform, TroubleshootingItem[]> = {
  windows: [
    {
      id: 'win-001',
      title: 'Windows Update stuck at "Downloading - 0%" indefinitely',
      symptoms: [
        'Windows Update shows 0% progress for hours',
        'High CPU usage from svchost.exe processes',
        'System becomes unresponsive during update checks',
      ],
      solution: [
        'Run Windows Update Troubleshooter: Settings > System > Troubleshoot > Other troubleshooters',
        'Reset Windows Update components via CMD (admin): net stop wuauserv && net stop bits',
        'Delete contents of C:\\Windows\\SoftwareDistribution\\Download',
        'Restart wuauserv and bits services, then retry update',
      ],
      difficulty: 'Easy',
      source: 'Microsoft Community Forums',
      contributor: 'WinAdmin_42',
      date: '2026-04-28',
      verified: true,
    },
    {
      id: 'win-002',
      title: 'BSOD with CRITICAL_PROCESS_DIED after driver update',
      symptoms: [
        'Blue screen appears shortly after boot',
        'Stop code: CRITICAL_PROCESS_DIED (0x000000EF)',
        'System enters automatic repair loop',
      ],
      solution: [
        'Boot into Safe Mode by interrupting startup 3 times',
        'Open Device Manager and roll back the recently updated driver',
        'Use DISM /Online /Cleanup-Image /RestoreHealth to repair system image',
        'Run sfc /scannow to fix corrupted system files',
      ],
      difficulty: 'Medium',
      source: 'Super User Stack Exchange',
      contributor: 'SysEngPro',
      date: '2026-04-20',
      verified: true,
    },
    {
      id: 'win-003',
      title: 'Windows Explorer crashes when right-clicking files',
      symptoms: [
        'Explorer.exe restarts automatically after right-click',
        'Context menu takes very long to appear',
        'Event Viewer shows Application Error 1000',
      ],
      solution: [
        'Disable third-party shell extensions using ShellExView utility',
        'Run chkdsk /f to check and repair disk errors',
        'Clear thumbnail cache: del /f /s /q /a %LocalAppData%\\Microsoft\\Windows\\Explorer\\thumbcache_*',
        'Create new user profile if issue persists in current profile',
      ],
      difficulty: 'Medium',
      source: 'TenForums',
      contributor: 'Brink',
      date: '2026-04-15',
      verified: true,
    },
    {
      id: 'win-004',
      title: 'System clock keeps resetting after reboot',
      symptoms: [
        'Date and time revert to incorrect values on every restart',
        'BIOS/UEFI clock also shows wrong time',
        'Time zone changes unexpectedly',
      ],
      solution: [
        'Replace CMOS battery on the motherboard (CR2032)',
        'Enable "Set time automatically" in Date & Time settings',
        'Sync with time server: w32tm /resync in elevated CMD',
        'Check for malware that may be tampering with system time',
      ],
      difficulty: 'Easy',
      source: 'Reddit r/techsupport',
      contributor: 'PCRepairTom',
      date: '2026-04-08',
      verified: true,
    },
    {
      id: 'win-005',
      title: 'Audio crackling and dropouts after Windows 11 24H2 update',
      symptoms: [
        'Audio stutters every few seconds during playback',
        'YouTube videos freeze momentarily with audio pops',
        'Different audio devices show same behavior',
      ],
      solution: [
        'Disable audio enhancements: Speaker properties > Enhancements > Disable all',
        'Update audio driver from manufacturer website (not Windows Update)',
        'Set audio service to restart automatically: services.msc > Windows Audio > Recovery',
        'Try different audio format in Advanced tab (e.g., 24-bit 48000 Hz)',
      ],
      difficulty: 'Medium',
      source: 'Microsoft Answers',
      contributor: 'AudioTech_Mike',
      date: '2026-03-25',
      verified: true,
    },
    {
      id: 'win-006',
      title: 'High memory usage by "System and compressed memory"',
      symptoms: [
        'System process uses 2-4GB RAM consistently',
        'Overall memory usage at 90%+ even with few apps open',
        'Computer slows down significantly after several hours of uptime',
      ],
      solution: [
        'Disable Superfetch/SysMain service: services.msc > SysMain > Disabled',
        'Adjust virtual memory settings to system-managed size on all drives',
        'Run RAM diagnostic: mdsched.exe to check for hardware faults',
        'Check for memory leaks in third-party antivirus software',
      ],
      difficulty: 'Hard',
      source: 'Super User Stack Exchange',
      contributor: 'MemoryExpert',
      date: '2026-03-15',
      verified: true,
    },
    {
      id: 'win-007',
      title: 'Network adapter disappears after sleep/hibernate',
      symptoms: [
        'Wi-Fi or Ethernet adapter missing after waking from sleep',
        'Device Manager shows adapter with yellow warning triangle',
        'Network troubleshooter cannot identify the problem',
      ],
      solution: [
        'Disable power management on adapter: Device Manager > Network adapter > Power Management > Uncheck "Allow computer to turn off"',
        'Update network driver from manufacturer website',
        'Reset network stack: netsh winsock reset && netsh int ip reset',
        'Disable Fast Startup in Power Options to prevent driver unload',
      ],
      difficulty: 'Medium',
      source: 'Reddit r/Windows11',
      contributor: 'NetFixer88',
      date: '2026-03-05',
      verified: true,
    },
  ],
  linux: [
    {
      id: 'lin-001',
      title: 'System boot failure after kernel update (dracut/initramfs issue)',
      symptoms: [
        'Boot hangs at "Loading initial ramdisk" or dracut prompt',
        'Kernel panic with VFS: unable to mount root fs',
        'Previous kernel version boots successfully from GRUB',
      ],
      solution: [
        'Boot from previous kernel in GRUB advanced options',
        'Regenerate initramfs: sudo dracut --force --regenerate-all (Fedora/RHEL) or sudo update-initramfs -u (Debian/Ubuntu)',
        'Check /etc/fstab for incorrect UUIDs after disk changes',
        'Verify kernel modules are available for current kernel version',
      ],
      difficulty: 'Hard',
      source: 'Unix & Linux Stack Exchange',
      contributor: 'KernelHacker',
      date: '2026-04-26',
      verified: true,
    },
    {
      id: 'lin-002',
      title: 'apt/dnf package manager stuck with lock file errors',
      symptoms: [
        'E: Could not get lock /var/lib/dpkg/lock-frontend',
        'Another process is using the package manager message',
        'Package installation or update commands fail immediately',
      ],
      solution: [
        'Identify blocking process: lsof /var/lib/dpkg/lock-frontend',
        'Kill stale process: sudo kill -9 <PID> if the process is truly stuck',
        'Remove lock files manually if no process is running: sudo rm /var/lib/dpkg/lock-frontend',
        'Repair package database: sudo dpkg --configure -a && sudo apt update',
      ],
      difficulty: 'Easy',
      source: 'Ask Ubuntu',
      contributor: 'AptWizard',
      date: '2026-04-18',
      verified: true,
    },
    {
      id: 'lin-003',
      title: 'Desktop environment freezes with 100% CPU on Xorg',
      symptoms: [
        'Mouse cursor moves but clicks do not register',
        'Top shows Xorg or gnome-shell consuming 100% CPU',
        'Cannot switch to TTY with Ctrl+Alt+F3',
      ],
      solution: [
        'Switch to TTY: Ctrl+Alt+F3 (may take several attempts)',
        'Restart display manager: sudo systemctl restart gdm (or sddm/lightdm)',
        'Check ~/.local/share/xorg/Xorg.0.log for driver errors',
        'Disable problematic GNOME extensions and reset GNOME: dconf reset -f /org/gnome/',
      ],
      difficulty: 'Medium',
      source: 'Unix & Linux Stack Exchange',
      contributor: 'X11Expert',
      date: '2026-04-10',
      verified: true,
    },
    {
      id: 'lin-004',
      title: 'SSH connection refused after firewall configuration',
      symptoms: [
        'ssh: connect to host port 22: Connection refused',
        'Cannot connect remotely after enabling ufw/firewalld',
        'Local SSH works but remote connections fail',
      ],
      solution: [
        'Verify SSH service is running: sudo systemctl status sshd',
        'Allow SSH through firewall: sudo ufw allow 22/tcp or sudo firewall-cmd --add-service=ssh --permanent',
        'Check /etc/ssh/sshd_config for ListenAddress restricting to localhost',
        'Test with verbose mode: ssh -vvv user@host to identify exact failure point',
      ],
      difficulty: 'Easy',
      source: 'Server Fault',
      contributor: 'SecOps_Lin',
      date: '2026-04-02',
      verified: true,
    },
    {
      id: 'lin-005',
      title: 'Docker containers fail to start with "permission denied"',
      symptoms: [
        'docker run fails with permission denied on socket',
        'Cannot connect to Docker daemon at unix:///var/run/docker.sock',
        'Works with sudo but not as regular user',
      ],
      solution: [
        'Add user to docker group: sudo usermod -aG docker $USER',
        'Log out and log back in for group changes to take effect',
        'Verify socket permissions: ls -la /var/run/docker.sock',
        'Restart Docker service: sudo systemctl restart docker',
      ],
      difficulty: 'Easy',
      source: 'Stack Overflow',
      contributor: 'DevOps_Dave',
      date: '2026-03-20',
      verified: true,
    },
    {
      id: 'lin-006',
      title: 'Systemd service stuck in "activating" state indefinitely',
      symptoms: [
        'systemctl status shows service as activating (start) for hours',
        'Dependent services fail to start',
        'No useful logs in journalctl for the service',
      ],
      solution: [
        'Check for timeout directives in service unit file',
        'Add TimeoutStartSec=30 to [Service] section if missing',
        'Review ExecStart command for processes that daemonize incorrectly',
        'Use Type=forking or Type=simple appropriately based on service behavior',
      ],
      difficulty: 'Medium',
      source: 'Unix & Linux Stack Exchange',
      contributor: 'SystemdGuru',
      date: '2026-03-12',
      verified: true,
    },
    {
      id: 'lin-007',
      title: 'Home directory encrypted disk full causing login failure',
      symptoms: [
        'Login loop - enters password then returns to login screen',
        'Home directory is ecryptfs/encfs mounted with no free space',
        'Guest session or root login works fine',
      ],
      solution: [
        'Login via TTY or recovery mode to bypass graphical session',
        'Check disk usage: df -h and du -sh ~/* to find large files',
        'Clean package cache: sudo apt clean or sudo dnf clean all',
        'Temporarily mount encrypted home with ecryptfs-recover-private to clear space',
      ],
      difficulty: 'Hard',
      source: 'Ask Ubuntu',
      contributor: 'CryptoRescue',
      date: '2026-03-01',
      verified: true,
    },
  ],
  macos: [
    {
      id: 'mac-001',
      title: 'macOS Sonoma Finder repeatedly crashes on external drive connect',
      symptoms: [
        'Finder quits unexpectedly when USB drive is plugged in',
        'Console shows NSException in com.apple.finder process',
        'Same drive works fine on other Macs and Windows PCs',
      ],
      solution: [
        'Reset Finder preferences: rm ~/Library/Preferences/com.apple.finder.plist && killall Finder',
        'Check and repair drive with Disk Utility First Aid',
        'Delete Finder sidebar favorites that reference missing network locations',
        'Boot in Safe Mode (hold Shift during startup) to clear caches',
      ],
      difficulty: 'Easy',
      source: 'Apple Communities',
      contributor: 'MacHelper_99',
      date: '2026-04-27',
      verified: true,
    },
    {
      id: 'mac-002',
      title: 'MacBook fans at maximum speed with no CPU load',
      symptoms: [
        'Fans run at full speed constantly even on idle desktop',
        'No visible process using significant CPU in Activity Monitor',
        'SMC reset temporarily fixes issue for a few hours',
      ],
      solution: [
        'Reset SMC: Intel - Shift+Ctrl+Option+Power; Apple Silicon - shutdown and wait 30s',
        'Check for runaway kernel_task by reviewing Activity Monitor > CPU tab',
        'Remove all USB devices and test - kernel_task scales with USB power draw',
        'Clean internal fans and vents; replace thermal paste if Mac is >3 years old',
      ],
      difficulty: 'Medium',
      source: 'MacRumors Forums',
      contributor: 'ThermalEngineer',
      date: '2026-04-19',
      verified: true,
    },
    {
      id: 'mac-003',
      title: 'Time Machine backup fails with "The backup disk is not available"',
      symptoms: [
        'Time Machine shows red icon in menu bar',
        'Network-attached backup disk intermittently disappears',
        'Same NAS works fine for file sharing (SMB/AFP)',
      ],
      solution: [
        'Restart Time Machine service: sudo tmutil stopbackup && sudo tmutil startbackup',
        'Delete .inProgress file from backup disk if partially completed backup is stuck',
        'Verify disk with: tmutil verifychecksums /Volumes/TimeMachine',
        'Re-select backup disk in Time Machine preferences and re-enter credentials',
      ],
      difficulty: 'Medium',
      source: 'Apple Communities',
      contributor: 'BackupBuddy',
      date: '2026-04-11',
      verified: true,
    },
    {
      id: 'mac-004',
      title: 'Spotlight search returns no results after macOS update',
      symptoms: [
        'Spotlight shows blank results for all queries',
        'mdfind command returns empty results in Terminal',
        'Rebuilding from System Settings does not complete',
      ],
      solution: [
        'Force rebuild index: sudo mdutil -E /',
        'Check Spotlight privacy list for accidentally added system folders',
        'Restart mds and mdworker processes via Activity Monitor',
        'For external drives: sudo mdutil -i on /Volumes/ExternalDriveName',
      ],
      difficulty: 'Easy',
      source: 'MacRumors Forums',
      contributor: 'SpotlightFixer',
      date: '2026-04-04',
      verified: true,
    },
    {
      id: 'mac-005',
      title: 'Keychain Access repeatedly prompts for password after reset',
      symptoms: [
        'Multiple "Keychain login cannot be found" dialogs appear',
        'Apps request keychain password on every launch',
        'User changed account password recently',
      ],
      solution: [
        'Open Keychain Access and lock then unlock keychain with current password',
        'If passwords differ, reset default keychain: Keychain Access > Preferences > Reset Default',
        'Delete old login.keychain file from ~/Library/Keychains/ after creating new one',
        'Restart affected applications so they store credentials in new keychain',
      ],
      difficulty: 'Easy',
      source: 'Apple Support Communities',
      contributor: 'KeychainKate',
      date: '2026-03-22',
      verified: true,
    },
    {
      id: 'mac-006',
      title: 'Rosetta 2 apps fail to launch on Apple Silicon Mac',
      symptoms: [
        'Intel apps show "You can\'t open the application because it may be damaged"',
        'Rosetta 2 installed but apps crash immediately on launch',
        'Same apps worked before a recent macOS patch update',
      ],
      solution: [
        'Reinstall Rosetta 2: softwareupdate --install-rosetta --agree-to-license',
        'Remove quarantine attribute: xattr -d com.apple.quarantine /Applications/AppName.app',
        'Check app for notarization issues: spctl -a -vv /Applications/AppName.app',
        'Update the Intel app to latest Universal 2 version from developer',
      ],
      difficulty: 'Medium',
      source: 'Apple Developer Forums',
      contributor: 'SiliconDev',
      date: '2026-03-14',
      verified: true,
    },
    {
      id: 'mac-007',
      title: 'Wi-Fi disconnects every 10-15 minutes on macOS Ventura',
      symptoms: [
        'Wi-Fi drops randomly requiring manual reconnect',
        'Other devices on same network remain connected',
        'Console shows nl80211 related errors periodically',
      ],
      solution: [
        'Delete Wi-Fi preferences: sudo rm /Library/Preferences/SystemConfiguration/com.apple.wifi*',
        'Create new network location: System Settings > Network > Locations > Edit > +',
        'Disable Wake for Wi-Fi network access in Energy Saver settings',
        'Renew DHCP lease and set custom DNS (e.g., 1.1.1.1, 8.8.8.8)',
      ],
      difficulty: 'Medium',
      source: 'Reddit r/MacOS',
      contributor: 'WiFiWarrior',
      date: '2026-03-06',
      verified: true,
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
    count: troubleshooting.windows.length,
  },
  linux: {
    icon: <Terminal className="h-5 w-5" />,
    color: '#F59E0B',
    labelKey: 'linux',
    count: troubleshooting.linux.length,
  },
  macos: {
    icon: <Apple className="h-5 w-5" />,
    color: '#94A3B8',
    labelKey: 'macos',
    count: troubleshooting.macos.length,
  },
};

const difficultyConfig: Record<
  Difficulty,
  { bg: string; text: string; labelKey: string }
> = {
  Easy: { bg: 'rgba(34,197,94,0.15)', text: '#22C55E', labelKey: 'easy' },
  Medium: { bg: 'rgba(245,158,11,0.15)', text: '#F59E0B', labelKey: 'medium' },
  Hard: { bg: 'rgba(239,68,68,0.15)', text: '#EF4444', labelKey: 'hard' },
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

export default function SystemTroubleshooting() {
  const { t } = useTranslation();
  const [activeTab, setActiveTab] = useState<Platform>('windows');
  const [data, setData] = useState(troubleshooting);

  // Wire to generated static data
  useEffect(() => {
    loadEntries().then((entries) => {
      if (Array.isArray(entries) && entries.length > 0) {
        setData(prev => prev); // placeholder — static data will replace mock in future task
      }
    }).catch(() => {});
  }, []);

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
              'radial-gradient(ellipse at 50% 0%, rgba(34,197,94,0.08) 0%, transparent 60%)',
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
            {t('systemTroubleshooting.breadcrumb') as string}
          </motion.p>

          {/* Title */}
          <motion.h1
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] as [number, number, number, number], delay: 0.1 }}
            className="mt-4 font-heading text-3xl font-bold text-text-primary md:text-4xl"
          >
            {t('systemTroubleshooting.title') as string}
          </motion.h1>

          {/* Subtitle */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="mt-3 max-w-[640px] text-lg text-text-secondary"
          >
            {t('systemTroubleshooting.subtitle') as string}
          </motion.p>

          {/* Community Badge */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.3 }}
            className="mt-4 inline-flex items-center gap-2 rounded-full border border-accent-green/30 px-4 py-1.5 text-xs font-medium text-accent-green"
          >
            <Users className="h-3.5 w-3.5" />
            {t('systemTroubleshooting.communityBadge') as string}
          </motion.div>

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
                      {t(`systemTroubleshooting.platform.${m.labelKey}`) as string}
                    </p>
                    <p className="text-xs text-text-muted">
                      {m.count} {t('systemTroubleshooting.entries') as string} ·{' '}
                      {t('systemTroubleshooting.updated') as string} 2026-04
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
                <span>{t(`systemTroubleshooting.platform.${m.labelKey}`) as string}</span>
                {isActive && (
                  <motion.div
                    layoutId="trouble-active-tab"
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
                {t(`systemTroubleshooting.platform.${meta.labelKey}`) as string}{' '}
                {t('systemTroubleshooting.solutions') as string}
              </h2>
            </div>

            {/* Cards (single column, full-width) */}
            <motion.div
              variants={containerVariants}
              initial="hidden"
              animate="visible"
              className="flex flex-col gap-4"
            >
              {currentData.map((item) => (
                <motion.div
                  key={item.id}
                  variants={itemVariants}
                  className="group relative overflow-hidden rounded-xl border border-border-subtle bg-bg-surface p-6 transition-all duration-300 hover:-translate-y-0.5 hover:border-border-active hover:shadow-[0_0_20px_rgba(34,197,94,0.06)]"
                  style={{ borderLeftWidth: '3px', borderLeftColor: '#22C55E' }}
                >
                  {/* Header Row */}
                  <div className="flex flex-wrap items-start justify-between gap-3">
                    <div className="flex-1">
                      <h3 className="font-heading text-xl font-medium text-text-primary">
                        {item.title}
                      </h3>
                    </div>
                    <div className="flex shrink-0 items-center gap-2">
                      {/* Platform Badge */}
                      <span
                        className="rounded px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider"
                        style={{
                          backgroundColor: `${meta.color}20`,
                          color: meta.color,
                        }}
                      >
                        {t(`systemTroubleshooting.platform.${meta.labelKey}`) as string}
                      </span>
                      {/* Verification Badge */}
                      {item.verified && (
                        <span className="inline-flex items-center gap-1 rounded bg-accent-green/15 px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider text-accent-green">
                          <CheckCircle2 className="h-3 w-3" />
                          {t('systemTroubleshooting.verified') as string}
                        </span>
                      )}
                      {/* Difficulty Badge */}
                      <span
                        className="rounded px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider"
                        style={{
                          backgroundColor: difficultyConfig[item.difficulty].bg,
                          color: difficultyConfig[item.difficulty].text,
                        }}
                      >
                        {t(`systemTroubleshooting.difficulty.${difficultyConfig[item.difficulty].labelKey}`) as string}
                      </span>
                    </div>
                  </div>

                  {/* Symptoms Section */}
                  <div className="mt-5">
                    <div className="mb-2 flex items-center gap-1.5 text-xs uppercase tracking-wider text-text-muted">
                      <AlertCircle className="h-3.5 w-3.5" />
                      {t('systemTroubleshooting.symptoms') as string}
                    </div>
                    <ul className="ml-4 list-disc space-y-1 text-sm text-text-secondary">
                      {item.symptoms.map((s, i) => (
                        <li key={i}>{s}</li>
                      ))}
                    </ul>
                  </div>

                  {/* Solution Section */}
                  <div className="mt-4">
                    <div className="mb-2 flex items-center gap-1.5 text-xs uppercase tracking-wider text-text-muted">
                      <Wrench className="h-3.5 w-3.5" />
                      {t('systemTroubleshooting.solution') as string}
                    </div>
                    <ol className="ml-4 list-decimal space-y-1.5 text-sm text-text-primary">
                      {item.solution.map((s, i) => (
                        <li key={i} className="pl-1">
                          <span className="rounded bg-bg-elevated px-1.5 py-0.5 font-mono text-xs text-accent-cyan">
                            {i + 1}
                          </span>{' '}
                          {s}
                        </li>
                      ))}
                    </ol>
                  </div>

                  {/* Source */}
                  <div className="mt-4">
                    <span className="text-xs uppercase tracking-wider text-text-muted">
                      {t('systemTroubleshooting.source') as string}:{' '}
                    </span>
                    <span className="text-sm text-accent-blue">{item.source}</span>
                  </div>

                  {/* Meta Row */}
                  <div className="mt-5 flex items-center justify-between border-t border-border-subtle pt-4">
                    <div className="flex items-center gap-4 text-xs text-text-muted">
                      <span className="inline-flex items-center gap-1.5">
                        <Users className="h-3.5 w-3.5" />
                        {t('systemTroubleshooting.contributedBy') as string} {item.contributor}
                      </span>
                      <span className="inline-flex items-center gap-1.5">
                        <Clock className="h-3.5 w-3.5" />
                        {item.date}
                      </span>
                    </div>
                    <span className="inline-flex items-center gap-1 text-xs text-text-muted transition-colors group-hover:text-accent-green">
                      {t('systemTroubleshooting.readFull') as string}
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
