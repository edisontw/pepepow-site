import { getCollection } from 'astro:content';

export const prerender = true;

type SearchEntry = {
  title: string;
  href: string;
  kind: string;
  date: string;
  categories: string[];
  tags: string[];
  text: string;
};

const cleanBody = (body: string) =>
  body
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/[`*_>#|{}\[\]~-]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 1800);

const slugFor = (entry: any) =>
  (entry.data.slug || entry.id.replace(/\.mdx?$/, '')).replace(/^\/+|\/+$/g, '');

const routeFor = (entry: any) => {
  const slug = slugFor(entry);

  if (entry.collection === 'pages') {
    if (slug === 'home-new') return '/';
    if (slug === 'announcements') return '/announcements/';
    return `/${slug}/`;
  }

  if (entry.collection === 'guides') return `/guides/${slug}/`;
  if (entry.collection === 'learn') return `/learn/${slug}/`;
  if (entry.collection === 'incidents') return `/incidents/${slug}/`;

  if (entry.data.legacy_url) {
    return new URL(entry.data.legacy_url).pathname;
  }

  return `/${slug}/`;
};

const kindFor = (entry: any) => {
  if (entry.collection === 'pages') return 'Current page';
  if (entry.collection === 'announcements') return 'Announcement';
  if (entry.collection === 'articles') return 'Historical article';
  if (entry.collection === 'guides') return 'Guide';
  if (entry.collection === 'learn') return 'Learn';
  if (entry.collection === 'incidents') return 'Incident';
  return 'Content';
};

export async function GET() {
  const groups = await Promise.all([
    getCollection('pages'),
    getCollection('announcements'),
    getCollection('articles'),
    getCollection('guides'),
    getCollection('learn'),
    getCollection('incidents'),
  ]);

  const searchIndex: SearchEntry[] = groups
    .flat()
    .filter((entry) => entry.data.status !== 'archived')
    .map((entry) => ({
      title: entry.data.title,
      href: routeFor(entry),
      kind: kindFor(entry),
      date: entry.data.date.toISOString().slice(0, 10),
      categories: entry.data.categories,
      tags: entry.data.tags,
      text: [
        entry.data.description,
        entry.data.categories.join(' '),
        entry.data.tags.join(' '),
        cleanBody(String((entry as any).body ?? '')),
      ]
        .filter(Boolean)
        .join(' '),
    }))
    .sort((a, b) => b.date.localeCompare(a.date));

  return new Response(JSON.stringify(searchIndex), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=300',
    },
  });
}
