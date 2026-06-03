const FEATURES = [
  '5 short links/month',
  '3 custom back-halves/month',
  'Unlimited link clicks',
];

function Check() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="20 6 9 17 4 12" />
    </svg>
  );
}

export default function FeatureBullets() {
  return (
    <ul className="mx-auto mt-8 flex max-w-3xl flex-col items-start gap-3 px-2 text-white/85 sm:flex-row sm:items-center sm:justify-center sm:gap-8">
      {FEATURES.map((label) => (
        <li key={label} className="flex items-center gap-2 text-sm">
          <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-white/10 text-brand-orange">
            <Check />
          </span>
          {label}
        </li>
      ))}
    </ul>
  );
}
