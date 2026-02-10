import {
  siteConfig,
  navItems,
  footerColumns,
  footerContact,
  legalLinks,
  copyright,
} from "./site";

export function getPageTitle(pageTitle?: string): string {
  return pageTitle ? `${pageTitle} | ${siteConfig.name}` : siteConfig.name;
}

export const headerDefaults = {
  navItems,
  ctaText: siteConfig.headerCta.text,
  ctaHref: siteConfig.headerCta.href,
};

export const footerDefaults = {
  columns: footerColumns,
  contact: footerContact,
  contactHeading: siteConfig.footerContactHeading,
  tagline: siteConfig.footerTagline,
  copyright,
  legalLinks,
};
