import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const status = z.enum(['published', 'draft', 'archived']).default('published');

const commonSchema = z.object({
  title: z.string(),
  description: z.string().default(''),
  date: z.coerce.date(),
  updated: z.coerce.date().optional(),
  slug: z.string().optional(),
  categories: z.array(z.string()).default([]),
  tags: z.array(z.string()).default([]),
  legacy_url: z.string().optional(),
  source_url: z.string().optional(),
  status,
  featured: z.boolean().default(false),
});

const localCollection = (base: string) =>
  defineCollection({
    loader: glob({ base, pattern: '**/[^_]*.{md,mdx}' }),
    schema: commonSchema,
  });

const announcements = localCollection('./src/content/announcements');
const articles = localCollection('./src/content/articles');
const guides = localCollection('./src/content/guides');
const learn = localCollection('./src/content/learn');
const incidents = localCollection('./src/content/incidents');

export const collections = { announcements, articles, guides, learn, incidents };
