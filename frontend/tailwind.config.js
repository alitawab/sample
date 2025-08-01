/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}', // <- includes all files in src
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}
