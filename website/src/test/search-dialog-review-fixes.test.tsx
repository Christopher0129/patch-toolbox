/// <reference types="vitest/globals" />
import { render, screen, waitFor, fireEvent } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import SearchDialog from '@/components/SearchDialog'
import zh from '@/i18n/locales/zh.json'
import ja from '@/i18n/locales/ja.json'
import ko from '@/i18n/locales/ko.json'

const mockNavigate = vi.fn()
const mockLoadSearchIndex = vi.fn()

vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual<typeof import('react-router-dom')>('react-router-dom')
  return {
    ...actual,
    useNavigate: () => mockNavigate,
  }
})

vi.mock('@/lib/search', () => ({
  loadSearchIndex: () => mockLoadSearchIndex(),
}))

vi.mock('@/i18n/LanguageContext', () => ({
  useTranslation: () => ({
    t: (key: string) => {
      const map: Record<string, string> = {
        'searchDialog.placeholder': 'Search entries',
        'searchDialog.noResults': 'No results',
        'searchDialog.noResultsHint': 'Try another query',
        'searchDialog.navigate': 'Navigate',
        'searchDialog.open': 'Open',
        'searchDialog.close': 'Close',
      }
      return map[key] ?? key
    },
  }),
}))

describe('SearchDialog review fixes', () => {
  beforeEach(() => {
    mockNavigate.mockReset()
    mockLoadSearchIndex.mockResolvedValue([
      {
        slug: 'network-security-1-cve-2024-9999-sample-entry',
        title: 'CVE-2024-9999 Sample Entry',
        category: 'network-security',
        keywords: 'sample entry network security',
      },
    ])
  })

  it('uses SPA navigation with the hit deep-link when pressing Enter', async () => {
    const onClose = vi.fn()
    render(
      <MemoryRouter>
        <SearchDialog open={true} onClose={onClose} />
      </MemoryRouter>,
    )

    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-9999 Sample Entry/i)).toBeInTheDocument()
    })

    const input = screen.getByPlaceholderText('Search entries')
    fireEvent.keyDown(input, { key: 'Enter' })

    expect(onClose).toHaveBeenCalled()
    expect(mockNavigate).toHaveBeenCalledWith('/network-security#network-security-1-cve-2024-9999-sample-entry')
  })

  it('renders search result links with deep-link targets instead of the category root only', async () => {
    render(
      <MemoryRouter>
        <SearchDialog open={true} onClose={() => {}} />
      </MemoryRouter>,
    )

    await waitFor(() => {
      expect(screen.getByText(/CVE-2024-9999 Sample Entry/i)).toBeInTheDocument()
    })

    const resultLink = screen.getByRole('link', { name: /CVE-2024-9999 Sample Entry/i })
    expect(resultLink).toHaveAttribute('href', '/network-security#network-security-1-cve-2024-9999-sample-entry')
  })
})

describe('Localized daily stat labels', () => {
  it('keeps zh daily label distinct from zh dailyUpdates', () => {
    expect(zh.hero.stats.daily).not.toBe(zh.hero.stats.dailyUpdates)
  })

  it('keeps ja daily label distinct from ja dailyUpdates', () => {
    expect(ja.hero.stats.daily).not.toBe(ja.hero.stats.dailyUpdates)
  })

  it('keeps ko daily label distinct from ko dailyUpdates', () => {
    expect(ko.hero.stats.daily).not.toBe(ko.hero.stats.dailyUpdates)
  })
})
