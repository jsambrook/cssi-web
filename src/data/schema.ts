import { siteConfig, footerContact } from './site';

function toTrailingSlashUrl(rawUrl: string): string {
  try {
    const parsed = new URL(rawUrl);
    if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
      return rawUrl;
    }
    if (!parsed.pathname.endsWith('/')) {
      parsed.pathname = `${parsed.pathname}/`;
    }
    return parsed.toString();
  } catch {
    return rawUrl;
  }
}

function toSiteUrl(href: string): string {
  return toTrailingSlashUrl(new URL(href, `${siteConfig.siteUrl}/`).toString());
}

function toAbsoluteUrl(rawUrl: string): string {
  try {
    return new URL(rawUrl, `${siteConfig.siteUrl}/`).toString();
  } catch {
    return rawUrl;
  }
}

function toIdFragment(value: string): string {
  const normalized = value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
  return normalized || 'item';
}

export function parseAddress(raw: string) {
  // "11227 NE 128th St Unit I-102\nKirkland, WA 98034"
  const parts = raw.split('\n');
  if (parts.length !== 2) {
    throw new Error(`parseAddress: expected "street\\ncity, ST ZIP", got ${JSON.stringify(raw)}`);
  }
  const [streetLine, cityLine] = parts;
  const street = streetLine.trim();
  if (!street) {
    throw new Error(`parseAddress: street line is empty in ${JSON.stringify(raw)}`);
  }
  const cityMatch = cityLine.match(/^(.+),\s*([A-Z]{2})\s+(\d{5})/);
  if (!cityMatch) {
    throw new Error(
      `parseAddress: city line must match "City, ST ZIP", got ${JSON.stringify(cityLine)}`
    );
  }
  return {
    streetAddress: street,
    addressLocality: cityMatch[1],
    addressRegion: cityMatch[2],
    postalCode: cityMatch[3],
  };
}

const address = parseAddress(footerContact.address);
const organizationSameAs = [
  'https://www.linkedin.com/company/common-sense-systems',
  siteConfig.xProfileUrl,
  siteConfig.youtubeUrl,
  'https://maps.google.com/?cid=14125900726605051430', // Google Business Profile
];

const founderKnowsAbout = [
  {
    '@type': 'DefinedTerm',
    name: 'Theory of Constraints (TOC)',
    sameAs: [
      'https://en.wikipedia.org/wiki/Theory_of_constraints',
      'https://www.tocico.org/',
      'https://www.wikidata.org/wiki/Q27857',
    ],
  },
  {
    '@type': 'DefinedTerm',
    name: 'TOC Thinking Processes',
    sameAs: [
      'https://en.wikipedia.org/wiki/Thinking_processes_(theory_of_constraints)',
      'https://www.tocico.org/page/TP_Committee',
    ],
  },
  {
    '@type': 'DefinedTerm',
    name: 'IEC 62304 - Medical Device Software',
    sameAs: ['https://en.wikipedia.org/wiki/IEC_62304', 'https://www.iso.org/standard/38421.html'],
  },
  {
    '@type': 'DefinedTerm',
    name: 'IEC 60601 - Medical Electrical Equipment',
    sameAs: ['https://en.wikipedia.org/wiki/IEC_60601', 'https://www.iso.org/standard/65529.html'],
  },
  {
    '@type': 'DefinedTerm',
    name: 'Throughput Accounting',
    sameAs: [
      'https://en.wikipedia.org/wiki/Throughput_accounting',
      'https://www.wikidata.org/wiki/Q1056501',
    ],
  },
  {
    '@type': 'DefinedTerm',
    name: 'Medical Ultrasound',
    sameAs: [
      'https://en.wikipedia.org/wiki/Medical_ultrasound',
      'https://www.wikidata.org/wiki/Q171442',
    ],
  },
  {
    '@type': 'DefinedTerm',
    name: 'Defibrillation',
    sameAs: [
      'https://en.wikipedia.org/wiki/Defibrillation',
      'https://www.wikidata.org/wiki/Q380299',
    ],
  },
];

const founderCredentials = [
  {
    '@type': 'EducationalOccupationalCredential',
    name: 'TOC Jonah (Thinking Processes Implementer)',
    recognizedBy: {
      '@type': 'Organization',
      name: 'TOCICO',
      url: 'https://www.tocico.org/',
    },
    about: {
      '@type': 'DefinedTerm',
      name: 'TOC Thinking Processes',
      url: 'https://www.tocico.org/page/Jonah',
    },
  },
];

const founderAlumni = [
  {
    '@type': 'CollegeOrUniversity',
    name: 'Washington State University',
    url: 'https://wsu.edu/',
  },
];

const aboutTermSameAs: Record<string, string[]> = {
  'Theory of Constraints': [
    'https://en.wikipedia.org/wiki/Theory_of_constraints',
    'https://www.tocico.org/',
  ],
  'Five Focusing Steps': [
    'https://en.wikipedia.org/wiki/Theory_of_constraints#The_five_focusing_steps',
  ],
  'Evaporating Cloud': ['https://en.wikipedia.org/wiki/Evaporating_Cloud'],
  'Current Reality Tree': [
    'https://en.wikipedia.org/wiki/Current_reality_tree_(theory_of_constraints)',
  ],
  'Future Reality Tree': ['https://en.wikipedia.org/wiki/Future_reality_tree'],
  'Critical Chain Project Management': [
    'https://en.wikipedia.org/wiki/Critical_chain_project_management',
  ],
  'Lean manufacturing': ['https://en.wikipedia.org/wiki/Lean_manufacturing'],
  'Value stream mapping': ['https://en.wikipedia.org/wiki/Value-stream_mapping'],
  'Healthcare operations': ['https://en.wikipedia.org/wiki/Health_system'],
};

function toAboutThing(term: string): Record<string, unknown> {
  const thing: Record<string, unknown> = {
    '@type': 'Thing',
    name: term,
  };
  const sameAs = aboutTermSameAs[term];
  if (sameAs && sameAs.length > 0) {
    thing.sameAs = sameAs;
  }
  return thing;
}

export function buildOrganizationSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': `${siteConfig.siteUrl}/#organization`,
    name: siteConfig.name,
    description: siteConfig.defaultDescription,
    url: toTrailingSlashUrl(siteConfig.siteUrl),
    telephone: footerContact.phones[0],
    email: footerContact.email,
    foundingDate: '1996',
    address: {
      '@type': 'PostalAddress',
      ...address,
      addressCountry: 'US',
    },
    founder: {
      '@id': `${siteConfig.siteUrl}/#founder`,
    },
    logo: {
      '@type': 'ImageObject',
      url: `${siteConfig.siteUrl}/images/logo.png`,
    },
    image: `${siteConfig.siteUrl}/images/logo.png`,
    sameAs: organizationSameAs,
  };
}

export function buildWebSiteSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    '@id': `${siteConfig.siteUrl}/#website`,
    name: siteConfig.name,
    url: toTrailingSlashUrl(siteConfig.siteUrl),
  };
}

export function buildWebPageSchema(options: {
  name: string;
  description: string;
  url: string;
  inLanguage?: string;
  image?: string;
  datePublished?: string;
  dateModified?: string;
  about?: string[];
  hasBreadcrumb?: boolean;
}): Record<string, unknown> {
  const pageUrl = toTrailingSlashUrl(options.url);
  const imageUrl = toAbsoluteUrl(options.image ?? siteConfig.defaultOgImage);
  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    '@id': pageUrl,
    name: options.name,
    description: options.description,
    url: pageUrl,
    inLanguage: options.inLanguage ?? 'en-US',
    isPartOf: { '@id': `${siteConfig.siteUrl}/#website` },
    publisher: { '@id': `${siteConfig.siteUrl}/#organization` },
    primaryImageOfPage: {
      '@type': 'ImageObject',
      url: imageUrl,
    },
    image: imageUrl,
  };

  if (options.datePublished) {
    schema.datePublished = options.datePublished;
  }
  if (options.dateModified ?? options.datePublished) {
    schema.dateModified = options.dateModified ?? options.datePublished;
  }
  if (options.about && options.about.length > 0) {
    schema.about = options.about.map((term) => toAboutThing(term));
  }
  if (options.hasBreadcrumb) {
    schema.breadcrumb = { '@id': `${pageUrl}#breadcrumb` };
  }

  return schema;
}

export function buildProfessionalServiceSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'ProfessionalService',
    '@id': `${siteConfig.siteUrl}/#professional-service`,
    name: siteConfig.name,
    url: toTrailingSlashUrl(siteConfig.siteUrl),
    telephone: footerContact.phones[0],
    email: footerContact.email,
    address: {
      '@type': 'PostalAddress',
      ...address,
      addressCountry: 'US',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: 47.6769,
      longitude: -122.206,
    },
    logo: {
      '@type': 'ImageObject',
      url: `${siteConfig.siteUrl}/images/logo.png`,
    },
    image: `${siteConfig.siteUrl}/images/logo.png`,
    description: siteConfig.defaultDescription,
    priceRange: '$$',
    foundingDate: '1996',
    knowsAbout: [
      'Theory of Constraints',
      'Throughput Accounting',
      'Constraint Analysis',
      'Offer Strategy',
      'Healthcare Operations',
      'Embedded Systems Engineering',
    ],
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: 'Consulting Services',
      itemListElement: [
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Constraint Analysis',
            description:
              'Identify the single constraint limiting your organization and fix it. Fixed fee, 2-4 weeks, satisfaction guarantee.',
          },
        },
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Offer Analysis',
            description:
              'Diagnose why your market offer is not differentiating and build one your ideal client cannot refuse. Fixed fee, 2-4 weeks, satisfaction guarantee.',
          },
        },
      ],
    },
    founder: {
      '@type': 'Person',
      '@id': `${siteConfig.siteUrl}/#founder`,
      name: 'John Sambrook',
      jobTitle: 'Systems Architect & Constraint Analyst',
      knowsAbout: founderKnowsAbout,
      hasCredential: founderCredentials,
      alumniOf: founderAlumni,
    },
    areaServed: [
      {
        '@type': 'Place',
        name: 'Puget Sound / Seattle Metro Area',
      },
      {
        '@type': 'Place',
        name: 'Washington State',
      },
      {
        '@type': 'Place',
        name: 'Oregon',
      },
      {
        '@type': 'Place',
        name: 'Idaho',
      },
      {
        '@type': 'Place',
        name: 'Montana',
      },
    ],
    serviceType: [
      'Theory of Constraints Consulting',
      'Constraint Analysis',
      'Offer Strategy',
      'Operational Improvement',
      'Business Process Improvement',
      'Healthcare Operations Consulting',
    ],
    sameAs: organizationSameAs,
  };
}

export function buildFounderSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'Person',
    '@id': `${siteConfig.siteUrl}/#founder`,
    name: 'John Sambrook',
    jobTitle: 'Systems Architect & Constraint Analyst',
    description:
      'TOC Jonah Certified systems architect and constraint analyst with deep expertise in healthcare operations, medical device software, and throughput-based improvement.',
    image: `${siteConfig.siteUrl}/images/headshots/john-sambrook-headshot-1200.jpg`,
    worksFor: {
      '@id': `${siteConfig.siteUrl}/#organization`,
    },
    address: {
      '@type': 'PostalAddress',
      ...address,
      addressCountry: 'US',
    },
    knowsAbout: founderKnowsAbout,
    hasCredential: founderCredentials,
    alumniOf: founderAlumni,
    url: toSiteUrl('/about'),
    sameAs: [
      'https://www.linkedin.com/in/johnsambrook',
      siteConfig.xProfileUrl,
      siteConfig.youtubeUrl,
    ],
  };
}

export function buildOfferCatalogSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'OfferCatalog',
    name: `${siteConfig.name} Services`,
    description:
      'Constraint analysis and offer strategy for organizations. Fixed fee, fixed timeline, satisfaction guarantee.',
    itemListElement: [
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Constraint Analysis',
          description:
            'Identify the single constraint limiting your organization and fix it. Two to four weeks, $15,000 fixed fee, satisfaction guarantee.',
          url: `${siteConfig.siteUrl}/#service-constraint-analysis`,
        },
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Offer Analysis',
          description:
            'Diagnose why your market offer is not differentiating and build one your ideal client cannot refuse. Two to four weeks, $15,000 fixed fee, satisfaction guarantee.',
          url: `${siteConfig.siteUrl}/#service-offer-analysis`,
        },
      },
    ],
  };
}

export function buildArticleSchema(options: {
  title: string;
  description: string;
  datePublished: string;
  dateModified?: string;
  author: string;
  url: string;
  image?: string;
  tags?: string[];
  wordCount?: number;
}): Record<string, unknown> {
  const articleUrl = toTrailingSlashUrl(options.url);
  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    '@id': articleUrl,
    headline: options.title,
    description: options.description,
    inLanguage: 'en-US',
    isAccessibleForFree: true,
    datePublished: options.datePublished,
    dateModified: options.dateModified ?? options.datePublished,
    url: articleUrl,
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': articleUrl,
    },
    author: {
      '@id': `${siteConfig.siteUrl}/#founder`,
    },
    publisher: {
      '@id': `${siteConfig.siteUrl}/#organization`,
    },
    isPartOf: {
      '@type': 'Blog',
      name: `${siteConfig.name} Insights`,
      url: toSiteUrl('/insights'),
    },
    speakable: {
      '@type': 'SpeakableSpecification',
      cssSelector: ['article h1', 'article > header > p'],
    },
  };
  if (options.tags && options.tags.length > 0) {
    schema.keywords = options.tags;
    schema.articleSection = options.tags[0];
  }
  if (options.image) {
    schema.image = options.image;
  }
  if (options.wordCount) {
    schema.wordCount = options.wordCount;
  }
  return schema;
}

export function buildServiceSchema(options: {
  name: string;
  description: string;
  url: string;
  serviceType: string;
}): Record<string, unknown> {
  const serviceUrl = toTrailingSlashUrl(options.url);
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    '@id': `${serviceUrl}#service-${toIdFragment(options.name)}`,
    name: options.name,
    description: options.description,
    url: serviceUrl,
    serviceType: options.serviceType,
    provider: {
      '@id': `${siteConfig.siteUrl}/#organization`,
    },
  };
}

export function buildBreadcrumbSchema(
  items: { name: string; href: string }[]
): Record<string, unknown> {
  const lastItemHref = items.length > 0 ? items[items.length - 1].href : '/';
  const breadcrumbId = `${toSiteUrl(lastItemHref)}#breadcrumb`;

  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': breadcrumbId,
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      item: toSiteUrl(item.href),
    })),
  };
}

export function buildContactPageSchema(description: string): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'ContactPage',
    name: `Contact ${siteConfig.name}`,
    description,
    url: toSiteUrl('/contact'),
    mainEntity: {
      '@id': `${siteConfig.siteUrl}/#organization`,
    },
  };
}
