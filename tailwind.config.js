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
        sourceRegular: ['Source Sans Pro Regular', 'sans-serif'],
        sourceBold: ['Source Sans Pro Bold', 'sans-serif'],
        sourceSemiBold: ['Source Sans Pro SemiBold', 'sans-serif'],
        sourceLight: ['Source Sans Pro Light', 'sans-serif'],
        sourceExtraLight: ['Source Sans Pro ExtraLight', 'sans-serif'],
        sourceBlack: ['Source Sans Pro Black', 'sans-serif'],
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
  ],
};
