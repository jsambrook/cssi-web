import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import { siteConfig } from './src/data/site.ts';

export default defineConfig({
  integrations: [tailwind(), sitemap()],
  site: siteConfig.siteUrl,
});
