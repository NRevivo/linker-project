/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        navy: {
          900: '#0B1736',
          800: '#101F47',
          700: '#1A2A5E',
        },
        brand: {
          orange: '#FF5C28',
          blue: '#1E6BFF',
          blueDark: '#1556CC',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
