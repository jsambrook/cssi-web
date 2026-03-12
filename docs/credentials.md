# Credentials System

TOCICO professional credentials are represented in two places that must be kept in sync.

## Data Locations

| Purpose                              | File                                          | Format                                          |
| ------------------------------------ | --------------------------------------------- | ----------------------------------------------- |
| Visible credential cards on `/about` | `src/data/pages/about.ts` → `credentials[]`   | `Credential` interface from `src/data/types.ts` |
| JSON-LD structured data (SEO/AI)     | `src/data/schema.ts` → `founderCredentials[]` | Schema.org `EducationalOccupationalCredential`  |

## Adding a New Credential

1. **`src/data/pages/about.ts`** — Append to the `credentials` array with `name`, `description`, `dateEarned`, and `verifyUrl`.
2. **`src/data/schema.ts`** — Append to `founderCredentials` with `@type`, `name`, `credentialCategory`, `dateIssued` (ISO 8601), `url` (verification link), and `recognizedBy`.
3. **PDF archive** — Save the certificate PDF to `~/git/cssi-assets/tocico-credentials/` using the credential hash as the filename (e.g., `af19a4409f7c4932a4a001d1e502da74.pdf`).
4. **Build** — Run `npm run build` to verify structured data renders correctly.

## Schema.org Notes

- The `about` property on the Jonah credential links to the WSU course context (instructor, university). Other credentials don't have this — it's specific to the Jonah provenance.
- `credentialCategory` values used: `Fundamentals`, `Practitioner`, `Jonah`.
- All credentials reference TOCICO as `recognizedBy`.
- The `founderCredentials` array is attached to both the Organization founder and the standalone Person entity in `buildOrganizationSchema()`.
