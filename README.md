<div align="center">

<p align="center">
  <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" />
  <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" />
  <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" />
  <a href="LICENSE">
    <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" />
  </a>
</p>

<br />

<img src="./readme-images/project-logo.png" alt="JSA Living Logo" width="180" />

<h1 align="center">JSA Living — Furniture Store Landing Page</h1>

<p>
  Responsive landing page for <strong>JSA Living</strong>, a furniture store showcasing modern and classic home collections, built with semantic HTML5, CSS3, and vanilla JavaScript.
</p>

<p>
  🌐 <strong>Language:</strong> English | <a href="./README-ES.md">Español (README-ES.md)</a>
</p>

</div>

---

## Overview

**JSA Living** is a static, mobile-first landing page designed to present furniture collections, highlight product quality, introduce the founding team, and provide navigation and social channels for customers.

> **Note on Demo Screenshots:** The files `readme-images/desktop.png` and `readme-images/mobile.png` belong to the original starter template and were omitted here. You can replace them with updated screenshots of JSA Living when available.

---

## Features

### Page Sections (`index.html`)
- **Header & Navigation:** Brand logo (`./readme-images/project-logo.png`), responsive hamburger menu toggle (`[data-navbar-toggle-btn]`), section links (`Inicio`, `Nuestro Equipo`, `¿Por qué nosotros?`, `Nuestra Colección`, `Contacto`), and a primary CTA button.
- **Hero (`#home`):** Main headline, value proposition, catalog button, hero furniture banner, and decorative background shape (`./assets/images/bg.png`).
- **Collection Gallery (`#gallery`):** Responsive CSS Grid (`repeat(auto-fit, minmax(280px, 1fr))`) displaying 6 furniture showcase cards with `4/3` aspect ratio and hover zoom transitions.
- **Team & About (`#about`):** Founding team cards with circular portraits and roles, paired with an interior design highlight block.
- **Features (`#features`):** Alternating layout showcasing *Salas y Comedores* (Living & Dining Rooms) and *Dormitorios y Espacios de Descanso* (Bedrooms & Rest Spaces).
- **Contact (`#contact`):** Contact callout section with visual banner.
- **Footer:** Brand logo, `@JSA_Living` social links (Instagram, YouTube, Facebook), 4 organized link columns (`Empresa`, `Productos`, `Recursos`, `Relevante`), and copyright notice.
- **Go-to-Top Button:** Floating `[data-go-top]` button for quick return to `#top`.

### Technical Highlights
- **CSS Architecture (`assets/css/style.css`):**
  - Centralized `:root` custom properties for color palette (`--royal-blue-dark`, `--oxford-blue`, `--bittersweet`, `--maximum-yellow-red`, `--french-rose`, etc.), typography scale (`--fs-1` to `--fs-6`), font weights (`--fw-500` to `--fw-700`), and transitions (`--transition: 0.25s ease-in-out`).
  - Smooth scrolling (`scroll-behavior: smooth`) and custom scrollbar styling.
  - Mobile-first responsive media queries at `768px`, `1024px`, and `1200px`.
- **Vanilla JavaScript (`assets/js/script.js`):**
  - Strict mode (`'use strict'`).
  - Mobile navigation drawer toggle (`.active` class on `[data-navbar]`).
  - Scroll listener activating `[data-go-top]` when `window.scrollY >= 800`.
- **External Resources:**
  - [Google Fonts](https://fonts.google.com/) (`Poppins`, weights 300–700).
  - [Ionicons v5.5.2](https://ionic.io/ionicons) for UI and social icons.
  - [Unsplash](https://unsplash.com/) for furniture photography.

---

## Project Structure

```text
.
├── .github/
│   ├── scripts/
│   │   └── validate_site.py   # Static validation for HTML, CSS, assets, and docs links
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI pipeline and preview environment
├── assets/
│   ├── css/
│   │   └── style.css          # Design tokens, base styles, layout, and responsive breakpoints
│   ├── images/                # Local graphics, favicon (logo_small.png), and background shapes
│   └── js/
│       └── script.js          # Navbar toggle and scroll-to-top logic
├── readme-images/             # Brand logo (project-logo.png) and team member portraits
├── index.html                 # Main landing page markup
├── LICENSE                    # MIT License
├── README.md                  # Project documentation (English)
├── README-ES.md               # Project documentation (Spanish)
└── style-guide.md             # Style reference notes
```

---

## Continuous Integration (GitHub Actions)

The workflow in [.github/workflows/ci.yml](./.github/workflows/ci.yml) runs automatically on `push` and `pull_request` for `main`, `master`, and `v2` (and manually via `workflow_dispatch`):

1. **`validate-assets`:** Runs `.github/scripts/validate_site.py` to check required files, unique HTML IDs, local image/script/stylesheet references, CSS `url()` paths, and documentation links.
2. **`lint-code`:** Validates `assets/js/script.js` syntax (`node --check`), structural HTML rules (`htmlhint`), and CSS parsing (`postcss-cli`).
3. **`smoke-test`:** Starts a local Python HTTP server and verifies HTTP `200` responses for `index.html`, CSS, JS, and brand images.
4. **`package-preview`:** Builds the deployable `dist/` bundle inside the `preview` GitHub environment and uploads the `jsa-living-site` artifact.

---

## Getting Started

### Prerequisites
No build tools or package managers are required. You only need a modern web browser (and optionally [Git](https://git-scm.com/downloads) to clone the repository).

### Run Locally
1. Clone or download this repository.
2. Open `index.html` directly in your browser, or serve the folder with any static server (for example, VS Code Live Server or Python):
   ```bash
   python -m http.server 8000
   ```
3. Visit `http://localhost:8000` in your browser.

---

## Team & Contact

- **Ángel Parra** — Director Ejecutivo (CEO)
- **Santiago Medina** — Especialista en Marketing
- **Juan Reyes** — Asesor Comercial
- **Social Media:** `@JSA_Living` (Instagram, YouTube, Facebook)

---

## Acknowledgments & License

- Built on top of the **Funel - Agency landing page** starter template by [Amit Ashok Swain](mailto:business.amitswain@gmail.com).
- Licensed under the [MIT License](LICENSE).
