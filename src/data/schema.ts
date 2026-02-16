import { siteConfig, footerContact } from './site';

function parseAddress(raw: string) {
  // "11227 NE 128 ST, Unit I-102\nKirkland, WA 98034"
  const [streetLine, cityLine] = raw.split('\n');
  const cityMatch = cityLine?.match(/^(.+),\s*([A-Z]{2})\s+(\d{5})/);
  return {
    streetAddress: streetLine?.trim() ?? '',
    addressLocality: cityMatch?.[1] ?? '',
    addressRegion: cityMatch?.[2] ?? '',
    postalCode: cityMatch?.[3] ?? '',
  };
}

const address = parseAddress(footerContact.address);
const organizationSameAs = [
  'https://www.linkedin.com/company/common-sense-systems',
  siteConfig.xProfileUrl,
];

export function buildOrganizationSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: siteConfig.name,
    url: siteConfig.siteUrl,
    telephone: footerContact.phones[0],
    email: footerContact.email,
    address: {
      '@type': 'PostalAddress',
      ...address,
      addressCountry: 'US',
    },
    founder: {
      '@type': 'Person',
      name: 'John Sambrook',
    },
    logo: {
      '@type': 'ImageObject',
      url: `${siteConfig.siteUrl}/images/logo.png`,
    },
    image: `${siteConfig.siteUrl}/images/logo.png`,
    sameAs: [...organizationSameAs, 'https://www.linkedin.com/in/johnsambrook'],
  };
}

export function buildWebSiteSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: siteConfig.name,
    url: siteConfig.siteUrl,
  };
}

export function buildWebPageSchema(options: {
  name: string;
  description: string;
  url: string;
}): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    name: options.name,
    description: options.description,
    url: options.url,
    isPartOf: { '@type': 'WebSite', name: siteConfig.name, url: siteConfig.siteUrl },
  };
}

export function buildProfessionalServiceSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'ProfessionalService',
    name: siteConfig.name,
    url: siteConfig.siteUrl,
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
      longitude: -122.2060,
    },
    logo: {
      '@type': 'ImageObject',
      url: `${siteConfig.siteUrl}/images/logo.png`,
    },
    image: `${siteConfig.siteUrl}/images/logo.png`,
    description: siteConfig.defaultDescription,
    priceRange: '$$',
    foundingDate: '1996',
    founder: {
      '@type': 'Person',
      name: 'John Sambrook',
      jobTitle: 'Systems Architect & Constraint Analyst',
      knowsAbout: [
        'Theory of Constraints',
        'Systems Engineering',
        'Healthcare Operations',
        'Eli Goldratt Thinking Processes',
        'Sales Process Engineering',
        'Business Process Improvement',
        'Operational Constraint Analysis',
        'Medical Device Software',
        'Embedded Systems Engineering',
        'AI-Assisted Policy Analysis',
      ],
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
      'Healthcare Systems Consulting',
      'Hospital Operations Consulting',
      'Theory of Constraints Consulting',
      'Healthcare AI Consulting',
      'Complex Discharge Analysis',
      'Operational Constraint Analysis',
      'Sales Process Engineering',
      'Business Process Improvement',
      'Organizational Constraint Analysis',
    ],
    sameAs: organizationSameAs,
  };
}

export function buildFounderSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'Person',
    name: 'John Sambrook',
    jobTitle: 'Systems Architect & Constraint Analyst',
    worksFor: {
      '@type': 'Organization',
      name: siteConfig.name,
      url: siteConfig.siteUrl,
    },
    address: {
      '@type': 'PostalAddress',
      ...address,
      addressCountry: 'US',
    },
    knowsAbout: [
      'Theory of Constraints',
      'Systems Engineering',
      'Healthcare Operations',
      'Eli Goldratt Thinking Processes',
      'Sales Process Engineering',
      'Business Process Improvement',
      'Operational Constraint Analysis',
      'Medical Device Software',
      'Embedded Systems Engineering',
      'AI-Assisted Policy Analysis',
    ],
    alumniOf: {
      '@type': 'CollegeOrUniversity',
      name: 'Washington State University',
    },
    url: `${siteConfig.siteUrl}/about`,
    sameAs: ['https://www.linkedin.com/in/johnsambrook'],
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
}): Record<string, unknown> {
  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    headline: options.title,
    description: options.description,
    inLanguage: 'en-US',
    isAccessibleForFree: true,
    datePublished: options.datePublished,
    dateModified: options.dateModified ?? options.datePublished,
    url: options.url,
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': options.url,
    },
    author: {
      '@type': 'Person',
      name: options.author,
      jobTitle: 'Founder & President',
      url: `${siteConfig.siteUrl}/about`,
    },
    publisher: {
      '@type': 'Organization',
      name: siteConfig.name,
      url: siteConfig.siteUrl,
      logo: {
        '@type': 'ImageObject',
        url: `${siteConfig.siteUrl}/images/logo.png`,
      },
    },
    isPartOf: {
      '@type': 'Blog',
      name: `${siteConfig.name} Insights`,
      url: `${siteConfig.siteUrl}/insights`,
    },
  };
  if (options.tags && options.tags.length > 0) {
    schema.keywords = options.tags;
    schema.articleSection = options.tags[0];
  }
  if (options.image) {
    schema.image = options.image;
  }
  return schema;
}

export function buildBreadcrumbSchema(
  items: { name: string; href: string }[],
): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      item: `${siteConfig.siteUrl}${item.href}`,
    })),
  };
}

export function buildContactPageSchema(description: string): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'ContactPage',
    name: `Contact ${siteConfig.name}`,
    description,
    url: `${siteConfig.siteUrl}/contact`,
    mainEntity: {
      '@type': 'Organization',
      name: siteConfig.name,
      telephone: footerContact.phones[0],
      email: footerContact.email,
    },
  };
}
