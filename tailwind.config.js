/* Modified tailwind.config.js content */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: '#0a4d0a',
        secundary: '#f9a8d4'
      },
      fontFamily: {
        source: ['Source Sans 3', 'serif'],
        playfair: ['Playfair Display', 'serif'],
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
  ],
};
