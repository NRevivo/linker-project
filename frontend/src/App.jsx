import Navbar from './components/Navbar.jsx';
import Hero from './components/Hero.jsx';
import ShortenerCard from './components/ShortenerCard.jsx';
import FeatureBullets from './components/FeatureBullets.jsx';
import Sparkles from './components/Sparkles.jsx';

export default function App() {
  return (
    <div className="relative min-h-screen overflow-hidden bg-navy-900">
      <Sparkles />
      <div className="relative z-10">
        <Navbar />
        <main className="mx-auto w-full max-w-5xl px-4 pb-24 pt-10 sm:px-6 sm:pt-16">
          <Hero />
          <ShortenerCard />
          <FeatureBullets />
        </main>
      </div>
    </div>
  );
}
