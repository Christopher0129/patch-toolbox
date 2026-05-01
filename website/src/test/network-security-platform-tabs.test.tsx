/// <reference types="vitest/globals" />
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import NetworkSecurity from '@/pages/NetworkSecurity'
import { type Language } from '@/i18n/LanguageContext'

/* ─── Mocks ─── */

// Mock loadEntries to return platform-aware entries
vi.mock('@/lib/content', () => ({
  loadEntries: vi.fn().mockResolvedValue([
    {
      id: 'CVE-2024-38063',
      severity: 'CRITICAL' as const,
      cvss: 9.8,
      description: 'Windows TCP/IP remote code execution vulnerability.',
      source: 'NVD' as const,
      date: '2026-04-24',
      affected: ['Windows 10', 'Windows 11'],
      mitigation: 'Install security update.',
      platform: 'windows',
    },
    {
      id: 'CVE-2024-6387',
      severity: 'HIGH' as const,
      cvss: 8.1,
      description: 'OpenSSH regreSSHion remote code execution in Linux systems.',
      source: 'NVD' as const,
      date: '2026-04-20',
      affected: ['OpenSSH 8.5p1 - 9.7p1'],
      mitigation: 'Upgrade OpenSSH.',
      platform: 'linux',
    },
    {
      id: 'CVE-2024-27818',
      severity: 'HIGH' as const,
      cvss: 7.5,
      description: 'macOS Safari WebKit memory corruption.',
      source: 'NVD' as const,
      date: '2026-04-18',
      affected: ['macOS Sonoma 14.5'],
      mitigation: 'Update macOS.',
      platform: 'macos',
    },
  ]),
}))

// Mock useTranslation / LanguageContext
const mockT = vi.fn((key: string) => {
  const map: Record<string, string> = {
    'networkSecurity.pageTitle': 'Network Security',
    'networkSecurity.subtitle': 'CVE database',
    'networkSecurity.totalEntries': 'Total entries',
    'networkSecurity.updated': 'Updated',
    'networkSecurity.searchPlaceholder': 'Search...',
    'networkSecurity.all': 'All',
    'networkSecurity.source': 'Source',
    'networkSecurity.sort': 'Sort',
    'networkSecurity.sort_newest': 'Newest',
    'networkSecurity.sort_severity': 'Severity',
    'networkSecurity.sort_cvss': 'CVSS Score',
    'networkSecurity.sort_id': 'ID',
    'networkSecurity.exploitConfirmed': 'Exploit confirmed',
    'networkSecurity.pendingAssessment': 'Pending assessment',
    'networkSecurity.readMore': 'Read more',
    'networkSecurity.noResults': 'No matching entries',
    'networkSecurity.noResultsDesc': 'Try adjusting your filters.',
    'networkSecurity.clearFilters': 'Clear all filters',
    'networkSecurity.viewOnSource': 'View on source',
    'networkSecurity.severityLabel': 'Severity',
    'networkSecurity.descriptionLabel': 'Description',
    'networkSecurity.affectedLabel': 'Affected',
    'networkSecurity.mitigationLabel': 'Mitigation',
    'networkSecurity.referencesLabel': 'References',
    'networkSecurity.added': 'Added',
    'networkSecurity.databaseInfo': 'Also available in DB',
    'networkSecurity.platforms.windows': 'Windows',
    'networkSecurity.platforms.linux': 'Linux',
    'networkSecurity.platforms.macos': 'macOS',
    'networkSecurity.emptyForPlatform': 'No entries for this platform.',
  }
  return map[key] ?? key
})

vi.mock('@/i18n/LanguageContext', () => ({
  useTranslation: () => ({
    t: mockT,
    lang: 'en' as Language,
  }),
  useLanguage: () => ({
    t: mockT,
    lang: 'en' as Language,
    setLang: vi.fn(),
  }),
}))

/* ─── Tests ─── */

describe('NetworkSecurity platform tabs — pure 3-platform', () => {
  beforeEach(() => {
    mockT.mockClear()
  })

  it('renders three platform tab buttons (Windows, Linux, macOS)', async () => {
    render(
      <MemoryRouter>
        <NetworkSecurity />
      </MemoryRouter>,
    )

    // Wait for async loadEntries to resolve
    await waitFor(() => {
      // Default tab is 'windows', so Windows entry should show
      expect(screen.getByText(/CVE-2024-38063/i)).toBeInTheDocument()
    })

    expect(screen.getByRole('button', { name: /windows/i })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /linux/i })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /macOS|mac os/i })).toBeInTheDocument()
  })

  it('shows only the active platform entries with pure 3-tab design', async () => {
    render(
      <MemoryRouter>
        <NetworkSecurity />
      </MemoryRouter>,
    )

    // Wait for data to load
    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-38063/i)).toBeInTheDocument()
    })

    // Default tab is 'windows' — only Windows entry visible
    expect(screen.getByText(/CVE-2024-38063/i)).toBeInTheDocument()
    expect(screen.queryByText(/CVE-2024-6387/i)).not.toBeInTheDocument()
    expect(screen.queryByText(/CVE-2024-27818/i)).not.toBeInTheDocument()

    // Click Linux tab
    const linuxTab = screen.getByRole('button', { name: /linux/i })
    fireEvent.click(linuxTab)

    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-6387/i)).toBeInTheDocument()
    })
    expect(screen.queryByText(/CVE-2024-38063/i)).not.toBeInTheDocument()
    expect(screen.queryByText(/CVE-2024-27818/i)).not.toBeInTheDocument()

    // Search should still work within the selected platform
    const searchInput = screen.getByPlaceholderText('Search...')
    fireEvent.change(searchInput, { target: { value: 'OpenSSH' } })

    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-6387/i)).toBeInTheDocument()
    })

    // Clear search, Linux entries should still be shown
    fireEvent.change(searchInput, { target: { value: '' } })

    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-6387/i)).toBeInTheDocument()
    })
  })

  it('has no "All" tab button — exactly 3 platform tab buttons', async () => {
    render(
      <MemoryRouter>
        <NetworkSecurity />
      </MemoryRouter>,
    )

    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-38063/i)).toBeInTheDocument()
    })

    // Collect platform tab buttons
    const allButtons = screen.getAllByRole('button')
    const platformTabButtons = allButtons.filter((btn) =>
      ['windows', 'linux', 'macos'].some((p) =>
        btn.textContent?.toLowerCase().includes(p),
      ),
    )

    // Exactly 3 platform tab buttons — no "All" or "general" tab
    expect(platformTabButtons).toHaveLength(3)
  })
})
