/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#4F359B',
        lightgray: '#D8D9DD',
        dark: '#26303E',
        muted: '#5C6672',
      }
    }
  },
  plugins: [],
}
