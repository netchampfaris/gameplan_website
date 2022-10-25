/** @type {import('tailwindcss').Config} */
module.exports = {
  presets: [require('frappe-ui/src/utils/tailwind.config')],
  content: ["./gameplan_website/**/*.{html,js}"],
  theme: {
    extend: {
      container: {
        center: true,
        padding: {
          xl: '0rem',
        }
      }
    },
  },
  plugins: [],
}
