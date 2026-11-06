/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          DEFAULT: '#12275A',
          primary: '#12275A',
          secondary: '#1E3F8C',
          light: '#254EA6',
          dark: '#0C1C40',
        },
        slate: {
          body: '#475569',
          muted: '#64748B',
          light: '#F8FAFC',
        },
        gold: {
          DEFAULT: '#C9971C',
          start: '#C9971C',
          end: '#E8BE55',
          light: '#F5D27A',
          pale: '#FFF6DF',
        },
        ivory: {
          DEFAULT: '#FAF8F3',
          border: '#ECE6D8',
          dark: '#F0ECE1',
        }
      },
      backgroundImage: {
        'navy-gradient': 'linear-gradient(135deg, #12275A 0%, #1E3F8C 100%)',
        'navy-hero': 'linear-gradient(145deg, #10224E 0%, #173273 60%, #1E3F8C 100%)',
        'gold-gradient': 'linear-gradient(135deg, #C9971C 0%, #E8BE55 100%)',
        'gold-hover': 'linear-gradient(135deg, #D4A328 0%, #F0CB6E 100%)',
        'ivory-gradient': 'linear-gradient(180deg, #FFFFFF 0%, #FAF8F3 100%)',
      },
      fontFamily: {
        heading: ['Poppins', 'sans-serif'],
        sans: ['Inter', 'Noto Sans Devanagari', 'sans-serif'],
        devanagari: ['Noto Sans Devanagari', 'sans-serif'],
      },
      borderRadius: {
        '20': '20px',
        'card': '20px',
      },
      boxShadow: {
        'soft-card': '0 10px 30px rgba(18, 39, 90, 0.08)',
        'soft-card-hover': '0 14px 35px rgba(18, 39, 90, 0.12)',
        'gold-glow-subtle': '0 8px 25px rgba(201, 151, 28, 0.2)',
        'hero-form': '0 20px 50px rgba(18, 39, 90, 0.14)',
      }
    },
  },
  plugins: [],
}
