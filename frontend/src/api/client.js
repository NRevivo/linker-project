const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';
const GENERIC_ERROR = 'Something went wrong. Please try again.';

function extractDetail(detail) {
  if (typeof detail === 'string') return detail;
  if (Array.isArray(detail)) {
    const msgs = detail
      .map((d) => (d && typeof d.msg === 'string' ? d.msg : null))
      .filter(Boolean);
    if (msgs.length) return msgs.join('; ');
  }
  return null;
}

export async function shortenUrl(longUrl) {
  let response;
  try {
    response = await fetch(`${BASE_URL}/shorten`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ original_url: longUrl }),
    });
  } catch {
    throw new Error(GENERIC_ERROR);
  }

  if (response.status === 201) {
    return response.json();
  }

  if (response.status === 400 || response.status === 422) {
    let message = 'Invalid URL.';
    try {
      const body = await response.json();
      const detail = extractDetail(body && body.detail);
      if (detail) message = detail;
    } catch {
      /* ignore parse error, use default */
    }
    throw new Error(message);
  }

  throw new Error(GENERIC_ERROR);
}
