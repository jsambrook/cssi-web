import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { siteConfig } from '../data/site';
import { manualInsights } from '../data/manualInsights';

export async function GET(context: { site: URL }) {
  const blogPosts = await getCollection('blog', ({ data }) => !data.draft);
  const manualPosts = manualInsights.map((insight) => ({
    id: insight.slug,
    data: {
      title: insight.title,
      description: insight.description,
      date: insight.date,
    },
  }));

  const posts = [...blogPosts, ...manualPosts].sort(
    (a, b) => b.data.date.getTime() - a.data.date.getTime()
  );

  return rss({
    title: siteConfig.name,
    description: siteConfig.defaultDescription,
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.date,
      link: `/insights/${post.id}/`,
    })),
  });
}
