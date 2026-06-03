import { useState } from 'react';
import Wordmark from './Wordmark.jsx';

const NAV_ITEMS = ['Platform', 'AI', 'Solutions', 'Pricing', 'Resources'];

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <header className="w-full">
      <div className="mx-auto flex w-full max-w-6xl items-center justify-between px-4 py-4 sm:px-6">
        <a href="#" className="flex items-center">
          <Wordmark className="text-2xl" />
        </a>

        <nav className="hidden items-center gap-7 lg:flex">
          {NAV_ITEMS.map((item) => (
            <a
              key={item}
              href="#"
              className="text-sm font-medium text-white/80 transition hover:text-white"
            >
              {item}
            </a>
          ))}
        </nav>

        <div className="hidden items-center gap-3 lg:flex">
          <a href="#" className="text-sm font-medium text-white/90 hover:text-white">
            Log in
          </a>
          <a
            href="#"
            className="rounded-full bg-brand-orange px-4 py-2 text-sm font-semibold text-white shadow-sm transition hover:brightness-110"
          >
            Sign up Free
          </a>
        </div>

        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          className="inline-flex items-center justify-center rounded-md p-2 text-white/90 lg:hidden"
          aria-label="Toggle navigation"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            {open ? (
              <>
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </>
            ) : (
              <>
                <line x1="3" y1="6" x2="21" y2="6" />
                <line x1="3" y1="12" x2="21" y2="12" />
                <line x1="3" y1="18" x2="21" y2="18" />
              </>
            )}
          </svg>
        </button>
      </div>

      {open && (
        <div className="border-t border-white/10 bg-navy-800/95 lg:hidden">
          <div className="mx-auto flex max-w-6xl flex-col gap-2 px-4 py-4 sm:px-6">
            {NAV_ITEMS.map((item) => (
              <a
                key={item}
                href="#"
                className="rounded-md px-2 py-2 text-base font-medium text-white/90 hover:bg-white/5"
              >
                {item}
              </a>
            ))}
            <div className="mt-2 flex items-center gap-3 border-t border-white/10 pt-3">
              <a href="#" className="text-sm font-medium text-white/90">
                Log in
              </a>
              <a
                href="#"
                className="rounded-full bg-brand-orange px-4 py-2 text-sm font-semibold text-white"
              >
                Sign up Free
              </a>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
