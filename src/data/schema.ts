import { siteConfig, footerContact } from './site';

export function parseAddress(raw: string) {
  // "11227 NE 128 ST, Unit I-102\nKirkland, WA 98034"
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
      'Healthcare Patient Flow',
      'Medical Device Commercialization',
      'Embedded Systems Engineering',
      'Mafia Offers (Strategy)',
    ],
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: 'Operational Interventions',
      itemListElement: [
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Flow Dynamics & Throughput',
            description:
              'Rapid intervention for gridlocked systems (Patient Flow or R&D Pipelines).',
          },
        },
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Market Offer Architecture',
            description: "Designing 'Mafia Offers' that competitors cannot replicate.",
          },
        },
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Cross-Functional Synchronization',
            description: 'Aligning Sales, Ops, and Engineering to a single constraint.',
          },
        },
      ],
    },
    founder: {
      '@type': 'Person',
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
    knowsAbout: founderKnowsAbout,
    hasCredential: founderCredentials,
    alumniOf: founderAlumni,
    url: `${siteConfig.siteUrl}/about`,
    sameAs: ['https://www.linkedin.com/in/johnsambrook'],
  };
}

export function buildOfferCatalogSchema(): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'OfferCatalog',
    name: `${siteConfig.name} Services`,
    description: 'Constraint-based consulting for healthcare and technology leaders.',
    itemListElement: [
      {
        '@type': 'OfferCatalog',
        name: 'Healthcare Leadership Services',
        itemListElement: [
          {
            '@type': 'Offer',
            itemOffered: {
              '@type': 'Service',
              name: 'Flow Dynamics & Throughput',
              description:
                'Accelerate patient flow, slash length of stay, and eliminate ED boarding without adding staff.',
            },
          },
          {
            '@type': 'Offer',
            itemOffered: {
              '@type': 'Service',
              name: 'Market Offer Architecture',
              description:
                'Direct-to-employer contracting and network integrity strategies that bypass insurance friction.',
            },
          },
          {
            '@type': 'Offer',
            itemOffered: {
              '@type': 'Service',
              name: 'Synchronization & Alignment',
              description:
                'Unify ED, inpatient, and discharge teams so the entire hospital moves as one synchronized system.',
            },
          },
        ],
      },
      {
        '@type': 'OfferCatalog',
        name: 'Tech & Product Leadership Services',
        itemListElement: [
          {
            '@type': 'Offer',
            itemOffered: {
              '@type': 'Service',
              name: 'Flow Dynamics & Throughput',
              description:
                'Accelerate R&D and slash time-to-market by identifying the bottleneck in your dev cycle.',
            },
          },
          {
            '@type': 'Offer',
            itemOffered: {
              '@type': 'Service',
              name: 'Market Offer Architecture',
              description:
                'Risk-shared licensing and recurring revenue models that align with customer utility.',
            },
          },
          {
            '@type': 'Offer',
            itemOffered: {
              '@type': 'Service',
              name: 'Synchronization & Alignment',
              description:
                'Align product roadmaps with sales promises through operational handshakes.',
            },
          },
        ],
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
  items: { name: string; href: string }[]
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
