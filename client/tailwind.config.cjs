const { fontFamily } = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        lg: '2rem',
      },
    },
    extend: {
      screens: {
        '2xl': '1280px',
      },
      fontFamily: {
        serif: ['var(--font-merriweather)', ...fontFamily.serif],
      },
    },
  },
  future: {
    hoverOnlyWhenSupported: true,
  },
  // eslint-disable-next-line global-require
  plugins: [require('@headlessui/tailwindcss')],
};
