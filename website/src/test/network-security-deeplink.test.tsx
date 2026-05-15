/// <reference types="vitest/globals" />
import { render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import NetworkSecurity from '@/pages/NetworkSecurity'
import { type Language } from '@/i18n/LanguageContext'

vi.mock('@/lib/content', () => ({
  loadEntries: vi.fn().mockResolvedValue([
    {
      id: 'CVE-2024-38063',
      slug: 'network-security-1-cve-2024-38063',
      severity: 'CRITICAL' as const,
      cvss: 9.8,
      description: 'Windows TCP/IP remote code execution vulnerability.',
      source: 'NVD' as const,
      date: '2026-04-24',
      affected: ['Windows 10', 'Windows 11'],
      mitigation: 'Install security update.',
      references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-38063'],
      platform: 'windows',
    },
    {
      id: 'CVE-2024-6387',
      slug: 'network-security-2-cve-2024-6387',
      severity: 'HIGH' as const,
      cvss: 8.1,
      description: 'OpenSSH regreSSHion remote code execution in Linux systems.',
      source: 'NVD' as const,
      date: '2026-04-20',
      affected: ['OpenSSH 8.5p1 - 9.7p1'],
      mitigation: 'Upgrade OpenSSH.',
      references: ['https://nvd.nist.gov/vuln/detail/CVE-2024-6387'],
      platform: 'linux',
    },
  ]),
}))

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

describe('NetworkSecurity deep-link behavior', () => {
  beforeEach(() => {
    mockT.mockClear()
    Element.prototype.scrollIntoView = vi.fn()
  })

  it('opens the matching vulnerability modal when loading with a hash slug', async () => {
    render(
      <MemoryRouter initialEntries={['/network-security#network-security-1-cve-2024-38063']}>
        <NetworkSecurity />
      </MemoryRouter>,
    )

    await waitFor(() => {
      expect(screen.getAllByText(/CVE-2024-38063/i).length).toBeGreaterThan(0)
    })

    await waitFor(() => {
      expect(screen.getByText('View on source')).toBeInTheDocument()
    })
  })

  it('renders each vulnerability card with a deep-linkable id based on slug', async () => {
    const { container } = render(
      <MemoryRouter initialEntries={['/network-security']}>
        <NetworkSecurity />
      </MemoryRouter>,
    )

    await waitFor(() => {
      expect(screen.getAllByText(/CVE-2024-38063/i).length).toBeGreaterThan(0)
    })

    const deepLinkTarget = container.querySelector('#network-security-1-cve-2024-38063')
    expect(deepLinkTarget).toBeTruthy()
  })
})
