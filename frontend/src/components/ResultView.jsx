import { useEffect, useState } from 'react';

function CheckCircle({ className = '' }) {
  return (
    <svg
      className={className}
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
      <polyline points="9 12 11.5 14.5 16 10" />
    </svg>
  );
}

function CheckIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="20 6 9 17 4 12" />
    </svg>
  );
}

function ExternalIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
      <polyline points="15 3 21 3 21 9" />
      <line x1="10" y1="14" x2="21" y2="3" />
    </svg>
  );
}

function fallbackSelect(text) {
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.setAttribute('readonly', '');
  ta.style.position = 'absolute';
  ta.style.left = '-9999px';
  document.body.appendChild(ta);
  ta.select();
  // Note: not calling execCommand — let the user copy with Ctrl+C as instructed.
  setTimeout(() => document.body.removeChild(ta), 50);
}

export default function ResultView({ result, onReset }) {
  const [copied, setCopied] = useState(false);
  const [toast, setToast] = useState(null);

  useEffect(() => {
    if (!copied) return;
    const t = setTimeout(() => setCopied(false), 2000);
    return () => clearTimeout(t);
  }, [copied]);

  useEffect(() => {
    if (!toast) return;
    const t = setTimeout(() => setToast(null), 2500);
    return () => clearTimeout(t);
  }, [toast]);

  async function copy() {
    const text = result.short_url;
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) {
        throw new Error('no-clipboard');
      }
      await navigator.clipboard.writeText(text);
      setCopied(true);
    } catch {
      fallbackSelect(text);
      setToast('Press Ctrl+C to copy');
    }
  }

  return (
    <div>
      <div className="flex items-center gap-2 text-emerald-600">
        <CheckCircle />
        <h2 className="text-2xl font-bold text-slate-900 sm:text-3xl">
          Your short link is ready
        </h2>
      </div>

      <div className="mt-6 rounded-lg border border-slate-200 bg-slate-100 px-4 py-4">
        <div
          className="break-all font-mono text-lg font-semibold text-slate-900 sm:text-xl"
          aria-label="Short URL"
        >
          {result.short_url}
        </div>
      </div>

      <div className="mt-4 flex flex-col gap-3 sm:flex-row">
        <button
          type="button"
          onClick={copy}
          className="inline-flex items-center justify-center gap-2 rounded-lg bg-brand-blue px-5 py-3 text-sm font-semibold text-white shadow transition hover:bg-brand-blueDark"
        >
          {copied ? (
            <>
              <CheckIcon />
              Copied!
            </>
          ) : (
            'Copy'
          )}
        </button>
        <a
          href={result.short_url}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center justify-center gap-2 rounded-lg border border-slate-300 bg-white px-5 py-3 text-sm font-semibold text-slate-800 shadow-sm transition hover:bg-slate-50"
        >
          <ExternalIcon />
          Open
        </a>
      </div>

      {toast && (
        <div
          role="status"
          className="mt-3 inline-block rounded-md bg-slate-800 px-3 py-1.5 text-xs font-medium text-white"
        >
          {toast}
        </div>
      )}

      {result.original_url && (
        <p
          className="mt-4 truncate text-xs text-slate-500"
          title={result.original_url}
        >
          Original: {result.original_url}
        </p>
      )}

      <div className="mt-6">
        <button
          type="button"
          onClick={onReset}
          className="text-sm font-semibold text-brand-blue hover:underline"
        >
          Shorten another link
        </button>
      </div>
    </div>
  );
}
