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
    logo: `${siteConfig.siteUrl}/images/logo.png`,
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
    logo: `${siteConfig.siteUrl}/images/logo.png`,
    description: siteConfig.defaultDescription,
    priceRange: '$',
    foundingDate: '1996',
    founder: {
      '@type': 'Person',
      name: 'John Sambrook',
      jobTitle: 'Healthcare Systems Architect',
      knowsAbout: [
        'Theory of Constraints',
        'Healthcare Operations',
        'Systems Engineering',
        'Hospital Discharge Processes',
        'Medical Device Development',
        'AI-Assisted Analysis',
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
    ],
    knowsAbout: [
      'Theory of Constraints',
      'Healthcare Operations',
      'Systems Engineering',
      'Hospital Discharge Processes',
      'Medical Device Development',
      'AI-Assisted Analysis',
    ],
  };
}

export function buildFounderSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'Person',
    name: 'John Sambrook',
    jobTitle: 'Healthcare Systems Architect',
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
      'Medical Device Software',
      'Embedded Systems Engineering',
      'AI-Assisted Policy Analysis',
    ],
    alumniOf: {
      '@type': 'CollegeOrUniversity',
      name: 'Washington State University',
    },
    url: `${siteConfig.siteUrl}/about`,
  };
}

export function buildArticleSchema(options: {
  title: string;
  description: string;
  datePublished: string;
  dateModified?: string;
  author: string;
  url: string;
}): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: options.title,
    description: options.description,
    datePublished: options.datePublished,
    dateModified: options.dateModified ?? options.datePublished,
    url: options.url,
    author: {
      '@type': 'Person',
      name: options.author,
    },
    publisher: {
      '@type': 'Organization',
      name: siteConfig.name,
      url: siteConfig.siteUrl,
    },
  };
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
