export async function loadSearchIndex() {
  const response = await fetch('/data/search-index.json')
  return response.json()
}
