Common Sense Systems Website

Welcome to the Common Sense Systems static-site repository. This README covers:

Project overview

Prerequisites & setup

Directory structure

Daily blog workflow

Makefile commands

Maintenance & housekeeping

Deployment steps

Contributing guidelines

🏗️ Project Overview
We use a combination of M4 templates and Python scripts to generate:

Static pages (about.html, services.html, etc.) via M4

Daily blog posts via LLMs + JSON → HTML pipelines

A styled blog index with CTA and full site footer

Everything lives in Git; new posts are generated locally, committed, and then pushed to production.

⚙️ Prerequisites
Git

GNU Make

Python 3.8+

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
(Your requirements.txt should include openai and any other libs you need.)

OpenAI API key in your environment:

bash
Copy
Edit
export OPENAI_API_KEY="sk-..."
📂 Directory Structure
css
Copy
Edit
/                ← repo root
├── Makefile
├── src
│   ├── bin
│   │   ├── generate_blog_json.py
│   │   ├── generate_blog_post.py
│   │   └── generate_blog_index.py
│   ├── blog
│   │   ├── drafts        ← intermediate JSON drafts
│   │   └── blog_index.json
│   ├── includes
│   │   ├── head.m4
│   │   ├── blog_macros.m4
│   │   ├── blog_index_template.html
│   │   ├── blog_cta.html
│   │   └── site_footer.html
│   └── assets
│       └── img/blog/...  ← graphics prompts for each post
└── blog               ← generated blog posts & index.html
📆 Daily Blog Workflow
Use these steps every day you want to publish a new article:

Draft generation

bash
Copy
Edit
make blog-today DESCRIPTION="Short, pithy prompt describing your post"
Calls generate_blog_json.py to create a JSON draft

Calls generate_blog_post.py to turn JSON → HTML (with CTA & footer)

Rebuilds blog/index.html with CTA & full footer

Local verification

bash
Copy
Edit
make clean      # remove old HTML
make            # rebuild static pages
open blog/2025/04/<today’s-slug>.html
open blog/index.html
Confirm the new post appears under /blog/YYYY/MM/slug.html

Confirm index shows your new post, CTA, and footer

Commit & push

bash
Copy
Edit
git add blog/ src/blog/drafts/<today’s-draft>.json
git commit -m "Blog: Add YYYY-MM-DD slug title"
git push origin <your-branch>
Deploy

bash
Copy
Edit
# on your web host, in the website root:
git pull origin <your-branch>
make clean && make
Optionally clear any caches or CDN

🛠️ Makefile Commands

Target	Description
make	Build all static pages & blog posts
make clean	Prune old drafts & remove generated HTML
make rebuild	make clean && make
make pages	Build only non-blog pages
make blog-today	Generate today’s blog post (requires DESCRIPTION="...")
make blog-index	Regenerate blog/index.html from metadata
make prune-drafts	Delete JSON drafts older than 30 days
make help	Show help message
🧹 Maintenance & Housekeeping
Prune old drafts

bash
Copy
Edit
make prune-drafts
Verify blog build
Ensure each make blog-today produces a new /blog/YYYY/MM/slug.html

Update templates or CSS
Edit any fragment in src/includes/ to affect all pages

🚀 Deployment Tips
Keep your OpenAI key out of Git—use environment variables

Run make clean on the server to avoid stale files

If you use a CDN, invalidate /blog/* after each push

🤝 Contributing
Fork & clone this repo

Create a feature branch

Make changes & local-test (make && make blog-today …)

Commit & open a PR against master or add-blog

Review & merge when green

Thank you for using Common Sense Systems’ automated blog pipeline!
If you have questions or ideas, just reach out. 🚀




