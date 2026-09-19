import { defineConfig } from 'astro/config';
import removeMigrationBanner from './scripts/markdown/remove-migration-banner.mjs';

export default defineConfig({
  site: 'https://pepepow.net',
  output: 'static',
  trailingSlash: 'always',
  markdown: {
    remarkPlugins: [removeMigrationBanner],
  },
});
