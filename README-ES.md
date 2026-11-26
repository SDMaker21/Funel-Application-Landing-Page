<div align="center">

<p align="center">
  <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" />
  <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" />
  <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" />
  <a href="LICENSE">
    <img alt="Licencia MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" />
  </a>
</p>

<br />

<img src="./readme-images/project-logo.png" alt="Logo de JSA Living" width="180" />

<h1 align="center">JSA Living — Venta de Muebles</h1>

<p>
  Landing page responsiva para <strong>JSA Living</strong>, tienda enfocada en muebles modernos y clásicos para el hogar, desarrollada con HTML5 semántico, CSS3 y JavaScript puro.
</p>

<p>
  🌐 <strong>Idioma:</strong> <a href="./README.md">English (README.md)</a> | Español
</p>

</div>

---

## Descripción General

**JSA Living** es una página de aterrizaje estática con enfoque *mobile-first*, diseñada para presentar colecciones de mobiliario, destacar la calidad de los acabados, presentar al equipo fundador y ofrecer acceso a las secciones y redes sociales de la marca.

> **Nota sobre capturas de pantalla:** Los archivos `readme-images/desktop.png` y `readme-images/mobile.png` pertenecen a la plantilla base original y se han omitido aquí. Puedes reemplazarlos con capturas actualizadas de JSA Living cuando lo desees.

---

## Características del Código

### Secciones de la Página (`index.html`)
- **Encabezado y Navegación (`header`):** Logotipo de la marca (`./readme-images/project-logo.png`), botón de menú hamburguesa para móviles (`[data-navbar-toggle-btn]`), enlaces internos (`Inicio`, `Nuestro Equipo`, `¿Por qué nosotros?`, `Nuestra Colección`, `Contacto`) y botón de acción (`Contáctanos`).
- **Sección Principal (`#home`):** Título principal, descripción de la propuesta de valor, botón `Ver Catálogo`, imagen destacada y forma decorativa de fondo (`./assets/images/bg.png`).
- **Galería de Colección (`#gallery`):** Cuadrícula responsiva con CSS Grid (`repeat(auto-fit, minmax(280px, 1fr))`) que muestra 6 tarjetas de muebles con proporción `4/3` y efecto de zoom suave al pasar el cursor (`scale(1.05)`).
- **Nuestro Equipo y Propuesta (`#about`):** Tarjetas para cada integrante del equipo con retrato circular y rol asignado, acompañadas del bloque *Apasionados por el diseño de interiores*.
- **Características y Espacios (`#features`):** Diseño alternado para presentar las líneas de *Colección de Salas y Comedores* y *Dormitorios y Espacios de Descanso*.
- **Contacto (`#contact`):** Sección de llamado a la acción con banner visual.
- **Pie de Página (`footer`):** Logotipo, enlaces a redes sociales `@JSA_Living` (Instagram, YouTube, Facebook), 4 columnas de enlaces (`Empresa`, `Productos`, `Recursos`, `Relevante`) y aviso de derechos reservados.
- **Botón Ir Arriba:** Botón flotante `[data-go-top]` para regresar suavemente al inicio (`#top`).

### Aspectos Técnicos
- **Arquitectura CSS (`assets/css/style.css`):**
  - Variables CSS centralizadas en `:root` para paleta de colores (`--royal-blue-dark`, `--oxford-blue`, `--bittersweet`, `--maximum-yellow-red`, `--french-rose`, etc.), escala tipográfica (`--fs-1` a `--fs-6`), grosores (`--fw-500` a `--fw-700`) y transiciones (`--transition: 0.25s ease-in-out`).
  - Desplazamiento suave (`scroll-behavior: smooth`) y barra de desplazamiento personalizada.
  - Diseño responsivo *mobile-first* con *media queries* en `768px`, `1024px` y `1200px`.
- **JavaScript Puro (`assets/js/script.js`):**
  - Modo estricto (`'use strict'`).
  - Control del menú móvil alternando la clase `.active` en `[data-navbar]`.
  - Listener de `scroll` que muestra el botón `[data-go-top]` al superar `window.scrollY >= 800`.
- **Recursos Externos:**
  - [Google Fonts](https://fonts.google.com/) (tipografía `Poppins`, pesos 300–700).
  - [Ionicons v5.5.2](https://ionic.io/ionicons) para iconografía de interfaz y redes sociales.
  - [Unsplash](https://unsplash.com/) para las fotografías de mobiliario.

---

## Estructura del Proyecto

```text
.
├── .github/
│   ├── scripts/
│   │   └── validate_site.py   # Validación estática de HTML, CSS, recursos y enlaces de docs
│   └── workflows/
│       └── ci.yml             # Pipeline de CI en GitHub Actions y entorno preview
├── assets/
│   ├── css/
│   │   └── style.css          # Variables de diseño, estilos base, layout y breakpoints responsivos
│   ├── images/                # Gráficos locales, favicon (logo_small.png) y formas de fondo
│   └── js/
│       └── script.js          # Lógica del menú móvil y botón de retorno arriba
├── readme-images/             # Logotipo (project-logo.png) y retratos del equipo
├── index.html                 # Estructura HTML principal de la landing page
├── LICENSE                    # Licencia MIT
├── README.md                  # Documentación del proyecto (Inglés)
├── README-ES.md               # Documentación del proyecto (Español)
└── style-guide.md             # Guía de referencia de estilos
```

---

## Integración Continua (GitHub Actions)

El flujo de trabajo en [.github/workflows/ci.yml](./.github/workflows/ci.yml) se ejecuta automáticamente en eventos `push` y `pull_request` sobre `main`, `master` y `v2` (además de ejecución manual con `workflow_dispatch`):

1. **`validate-assets`:** Ejecuta `.github/scripts/validate_site.py` para verificar archivos requeridos, IDs HTML únicos, rutas locales de imágenes/scripts/estilos, referencias `url()` en CSS y enlaces en la documentación.
2. **`lint-code`:** Valida la sintaxis de `assets/js/script.js` (`node --check`), reglas estructurales de HTML (`htmlhint`) y análisis sintáctico de CSS (`postcss-cli`).
3. **`smoke-test`:** Levanta un servidor HTTP local con Python y verifica respuestas HTTP `200` para `index.html`, CSS, JS e imágenes de la marca.
4. **`package-preview`:** Empaqueta el sitio estático en `dist/` dentro del entorno `preview` de GitHub y sube el artefacto `jsa-living-site`.

---

## Cómo Ejecutarlo Localmente

### Requisitos Previos
No requiere herramientas de compilación ni gestores de paquetes. Solo necesitas un navegador web moderno (y opcionalmente [Git](https://git-scm.com/downloads) para clonar el repositorio).

### Pasos
1. Clona o descarga este repositorio.
2. Abre `index.html` directamente en tu navegador, o sirve la carpeta con un servidor estático (por ejemplo, Live Server de VS Code o Python):
   ```bash
   python -m http.server 8000
   ```
3. Abre `http://localhost:8000` en tu navegador.

---

## Equipo y Contacto

- **Ángel Parra** — Director Ejecutivo
- **Santiago Medina** — Especialista en Marketing
- **Juan Reyes** — Asesor Comercial
- **Redes Sociales:** `@JSA_Living` (Instagram, YouTube, Facebook)

---

## Reconocimientos y Licencia

- Basado en la plantilla inicial **Funel - Agency landing page** creada por [Amit Ashok Swain](mailto:business.amitswain@gmail.com).
- Distribuido bajo la [Licencia MIT](LICENSE).
