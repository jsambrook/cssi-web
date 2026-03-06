import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import { siteConfig } from './src/data/site.ts';
import { sitemapSerialize } from './src/utils/sitemap.ts';

export default defineConfig({
  integrations: [
    tailwind(),
    sitemap({
      serialize: sitemapSerialize,
    }),
  ],
  site: siteConfig.siteUrl,
  trailingSlash: 'always',
});
