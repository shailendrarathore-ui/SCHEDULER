const API = import.meta.env.VITE_API || 'http://localhost:8000'

export async function get(path) {
  const res = await fetch(`${API}${path}`)
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}

export async function post(path, body) {
  const res = await fetch(`${API}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body ?? {}),
  })
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}
