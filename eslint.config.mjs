import eslintPluginAstro from 'eslint-plugin-astro';
import tsParser from '@typescript-eslint/parser';

export default [
  // Ignore generated files
  {
    ignores: ['.astro/**', 'dist/**', 'node_modules/**'],
  },
  // TypeScript files
  {
    files: ['**/*.ts'],
    languageOptions: {
      parser: tsParser,
    },
  },
  ...eslintPluginAstro.configs.recommended,
  {
    rules: {
      'astro/no-unused-css-selector': 'off',
    },
  },
];
