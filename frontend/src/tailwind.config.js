/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}"
  ],  
  theme: {
    extend: {
      colors: {
        primary: "#007F5F",
        secondary: "#2B9348",
        accent: "#55A630",
        highlight: "#FFFF3F",
      },
      fontFamily: {
        kanit: ["Kanit", "sans-serif"],
      },
    },
  },
  plugins: [],
};
