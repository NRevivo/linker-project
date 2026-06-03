import { useState } from 'react';
import { shortenUrl } from '../api/client.js';
import ResultView from './ResultView.jsx';

function LinkIcon({ className = '' }) {
  return (
    <svg className={className} width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" />
      <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" />
    </svg>
  );
}

function QrIcon({ className = '' }) {
  return (
    <svg className={className} width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="3" width="7" height="7" />
      <rect x="14" y="3" width="7" height="7" />
      <rect x="3" y="14" width="7" height="7" />
      <path d="M14 14h3v3h-3z" />
      <path d="M20 14v3" />
      <path d="M14 20h3" />
      <path d="M20 20v1" />
    </svg>
  );
}

function QrIconLarge() {
  return (
    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="3" width="7" height="7" />
      <rect x="14" y="3" width="7" height="7" />
      <rect x="3" y="14" width="7" height="7" />
      <path d="M14 14h3v3h-3z" />
      <path d="M20 14v3" />
      <path d="M14 20h3" />
      <path d="M20 20v1" />
    </svg>
  );
}

function ArrowRight() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
      <line x1="5" y1="12" x2="19" y2="12" />
      <polyline points="12 5 19 12 12 19" />
    </svg>
  );
}

function Spinner() {
  return (
    <svg className="animate-spin" width="18" height="18" viewBox="0 0 24 24" fill="none">
      <circle cx="12" cy="12" r="10" stroke="currentColor" strokeOpacity="0.25" strokeWidth="4" />
      <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" strokeWidth="4" strokeLinecap="round" />
    </svg>
  );
}

export default function ShortenerCard() {
  const [tab, setTab] = useState('short');
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  async function onSubmit(e) {
    e.preventDefault();
    if (loading) return;

    const trimmed = url.trim();
    if (!trimmed) {
      setError('Please enter a URL starting with http:// or https://');
      return;
    }
    if (!/^https?:\/\//i.test(trimmed)) {
      setError('Please enter a URL starting with http:// or https://');
      return;
    }

    setError(null);
    setLoading(true);
    try {
      const data = await shortenUrl(trimmed);
      setResult(data);
    } catch (err) {
      setError(err.message || 'Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  }

  function onChange(e) {
    setUrl(e.target.value);
    if (error) setError(null);
  }

  function reset() {
    setResult(null);
    setUrl('');
    setError(null);
  }

  const isShort = tab === 'short';

  return (
    <section className="mx-auto w-full max-w-3xl">
      <div className="overflow-hidden rounded-2xl bg-white text-slate-900 shadow-2xl ring-1 ring-black/5">
        <div className="flex border-b border-slate-200 bg-slate-50">
          <button
            type="button"
            onClick={() => setTab('short')}
            className={`flex flex-1 items-center justify-center gap-2 px-4 py-4 text-sm font-semibold transition sm:flex-none sm:px-6 ${
              isShort
                ? 'border-b-2 border-brand-blue bg-white text-slate-900'
                : 'text-slate-500 hover:text-slate-700'
            }`}
          >
            <LinkIcon />
            Short Link
          </button>
          <button
            type="button"
            onClick={() => setTab('qr')}
            className={`flex flex-1 items-center justify-center gap-2 px-4 py-4 text-sm font-semibold transition sm:flex-none sm:px-6 ${
              !isShort
                ? 'border-b-2 border-brand-blue bg-white text-slate-900'
                : 'text-slate-500 hover:text-slate-700'
            }`}
          >
            <QrIcon />
            QR Code
          </button>
        </div>

        <div className="p-6 sm:p-10">
          {!isShort ? (
            <div className="flex flex-col items-center justify-center py-10 text-center">
              <span className="text-brand-blue">
                <QrIconLarge />
              </span>
              <h2 className="mt-4 text-xl font-bold text-slate-900">Coming soon</h2>
              <p className="mt-2 max-w-sm text-sm text-slate-500">
                QR codes aren't ready yet — we're still building this feature.
              </p>
            </div>
          ) : result ? (
            <ResultView result={result} onReset={reset} />
          ) : (
            <form onSubmit={onSubmit} noValidate>
              <h2 className="text-2xl font-bold text-slate-900 sm:text-3xl">
                Shorten a long link
              </h2>
              <p className="mt-1 text-sm text-slate-500">No credit card required.</p>

              <label
                htmlFor="long-url"
                className="mt-6 block text-sm font-semibold text-slate-800"
              >
                Paste your long link here
              </label>
              <input
                id="long-url"
                type="text"
                value={url}
                onChange={onChange}
                placeholder="https://example.com/my-very-long-url"
                disabled={loading}
                className={`mt-2 block w-full rounded-lg border bg-white px-4 py-3 text-base text-slate-900 placeholder-slate-400 outline-none transition focus:ring-2 focus:ring-brand-blue/30 ${
                  error
                    ? 'border-red-400 focus:border-red-500'
                    : 'border-slate-300 focus:border-brand-blue'
                }`}
              />
              {error && <p className="mt-2 text-sm text-red-600">{error}</p>}

              <button
                type="submit"
                disabled={loading}
                className="mt-6 inline-flex w-full items-center justify-center gap-2 rounded-lg bg-brand-blue px-5 py-3.5 text-base font-semibold text-white shadow transition hover:bg-brand-blueDark disabled:cursor-not-allowed disabled:opacity-60 sm:w-auto"
              >
                {loading ? (
                  <>
                    <Spinner />
                    Shortening…
                  </>
                ) : (
                  <>
                    Get your link for free
                    <ArrowRight />
                  </>
                )}
              </button>
            </form>
          )}
        </div>
      </div>
    </section>
  );
}
