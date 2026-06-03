export default function Wordmark({ className = '' }) {
  return (
    <span
      className={`font-extrabold tracking-tight text-brand-orange ${className}`}
      style={{ letterSpacing: '-0.02em' }}
    >
      Linker
    </span>
  );
}
