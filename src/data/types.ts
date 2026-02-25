export interface CTA {
  text: string;
  href: string;
}

export interface HeroBullet {
  bold: string;
  text: string;
}

export interface PageHeader {
  label?: string;
  heading: string;
  subheading?: string;
}

export interface GridItem {
  title: string;
  description: string;
}

export interface ContentBlock {
  text: string;
  lead?: boolean;
}

export type ColorVariant = 'default' | 'red' | 'orange' | 'amber' | 'blue' | 'green' | 'purple';

export interface CTAContent {
  headline: string;
  description: string;
  primaryCta: CTA;
  secondaryCta?: CTA;
  footnote?: string;
}

export interface ContactGridItem {
  heading: string;
  description: string;
  linkText?: string;
  href?: string;
}

export type ContactGrid = Record<string, ContactGridItem>;

export type LegalBlock =
  | { type: 'heading'; text: string; level: 2 | 3 }
  | { type: 'text'; html: string }
  | { type: 'list'; items: string[] };

export interface IntakeFormOption {
  id: string;
  icon: string;
  title: string;
  description: string;
}

export interface IntakeFormStep {
  id: string;
  question: string;
  subtitle?: string;
  inputType: 'select' | 'text' | 'email';
  options?: IntakeFormOption[];
  placeholder?: string;
  required?: boolean;
}

export interface IntakeFormConfig {
  steps: IntakeFormStep[];
  footerText?: string;
  submitButtonText: string;
  successMessage: string;
  formspree: {
    endpoint: string;
    fieldNames: Record<string, string>;
  };
}

export interface AmbitionCard {
  label: string;
  text: string;
  scrollTarget: string;
}

export type Industry = 'healthcare' | 'tech';

export interface IndustryVariant {
  title: string;
  description: string;
}

export interface ServiceCardItem {
  id: string;
  color?: ColorVariant;
  variants: Record<Industry, IndustryVariant>;
}

export interface ManualInsight {
  slug: string;
  title: string;
  description: string;
  date: Date;
  author: string;
  tags: string[];
  ogImage?: string;
  imageAlt?: string;
}
