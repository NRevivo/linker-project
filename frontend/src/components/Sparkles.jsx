const SPARKS = [
  { top: '8%', left: '6%', size: 18, rotate: 0, opacity: 0.35 },
  { top: '14%', left: '88%', size: 12, rotate: 20, opacity: 0.25 },
  { top: '28%', left: '15%', size: 10, rotate: 0, opacity: 0.3 },
  { top: '40%', left: '92%', size: 22, rotate: 15, opacity: 0.2 },
  { top: '58%', left: '4%', size: 16, rotate: 0, opacity: 0.25 },
  { top: '70%', left: '90%', size: 14, rotate: 30, opacity: 0.3 },
  { top: '82%', left: '20%', size: 10, rotate: 0, opacity: 0.2 },
  { top: '20%', left: '50%', size: 8, rotate: 0, opacity: 0.18 },
  { top: '90%', left: '70%', size: 18, rotate: 10, opacity: 0.2 },
];

function Spark({ size = 16, rotate = 0, opacity = 0.3, style }) {
  return (
    <svg
      viewBox="0 0 24 24"
      width={size}
      height={size}
      fill="white"
      style={{ position: 'absolute', opacity, transform: `rotate(${rotate}deg)`, ...style }}
      aria-hidden="true"
    >
      <path d="M12 0 L13.6 9.4 L22 12 L13.6 14.6 L12 24 L10.4 14.6 L2 12 L10.4 9.4 Z" />
    </svg>
  );
}

export default function Sparkles() {
  return (
    <div className="pointer-events-none absolute inset-0 overflow-hidden">
      {SPARKS.map((s, i) => (
        <Spark
          key={i}
          size={s.size}
          rotate={s.rotate}
          opacity={s.opacity}
          style={{ top: s.top, left: s.left }}
        />
      ))}
    </div>
  );
}
