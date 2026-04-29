export async function loadCategories() {
  const response = await fetch('/data/categories.json')
  return response.json()
}

export async function loadEntries() {
  const response = await fetch('/data/entries.json')
  return response.json()
}

export async function loadStats() {
  const response = await fetch('/data/stats.json')
  return response.json()
}

export async function loadSearchIndex() {
  const response = await fetch('/data/search-index.json')
  return response.json()
}
