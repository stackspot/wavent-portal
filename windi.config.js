import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  extract: {
    // A common use case is scanning files from the root directory
    include: ['./resources/**/*.{vue,html,jsx,tsx}', './templates/**/*.html'],
    // if you are excluding files, make sure you always include node_modules and .git
    exclude: ['node_modules', '.git', 'dist'],
  },
})