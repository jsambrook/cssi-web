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

export interface FeatureItem {
  title: string;
  description: string;
  color?: "default" | "red" | "orange" | "amber" | "blue" | "green" | "purple";
  href?: string;
}

export interface TestimonialItem {
  quote: string;
  author: string;
  company?: string;
  initials?: string;
}

export interface CTAContent {
  headline: string;
  description: string;
  primaryCta: CTA;
  secondaryCta?: CTA;
  footnote?: string;
}

export type LegalBlock =
  | { type: "heading"; text: string; level: 2 | 3 }
  | { type: "text"; html: string }
  | { type: "list"; items: string[] };

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
  inputType: "select" | "text" | "email";
  options?: IntakeFormOption[];
  placeholder?: string;
  required?: boolean;
}

export interface IntakeFormConfig {
  steps: IntakeFormStep[];
  footerText?: string;
  submitButtonText: string;
  successMessage: string;
  googleForms: {
    actionUrl: string;
    fieldMappings: Record<string, string>;
  };
}
