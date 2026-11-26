"""Validates static site structure, local asset links, and documentation references."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "index.html",
    "assets/css/style.css",
    "assets/js/script.js",
    "README.md",
    "README-ES.md",
    "LICENSE",
]

REQUIRED_HTML_TOKENS = [
    'id="top"',
    'id="home"',
    'id="gallery"',
    'id="about"',
    'id="features"',
    'id="contact"',
    "data-navbar-toggle-btn",
    "data-navbar",
    "data-go-top",
    "JSA Living",
]

EXTERNAL_PREFIXES = ("http://", "https://", "#", "mailto:", "tel:", "javascript:")


def check_required_files() -> list[str]:
    """Ensure all core project and documentation files exist."""
    errors: list[str] = []
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).is_file():
            errors.append(f"Missing required file: {rel_path}")
    return errors


def check_html() -> list[str]:
    """Validate local asset links, unique IDs, and required hooks in index.html."""
    errors: list[str] = []
    html_path = ROOT / "index.html"
    if not html_path.is_file():
        return ["index.html not found"]

    html = html_path.read_text(encoding="utf-8")

    for token in REQUIRED_HTML_TOKENS:
        if token not in html:
            errors.append(f"Missing expected token in index.html: {token}")

    ids = re.findall(r'\bid=["\']([^"\']+)["\']', html)
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"Duplicate HTML id attributes found: {', '.join(duplicates)}")

    refs = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', html)
    for ref in refs:
        if ref.startswith(EXTERNAL_PREFIXES):
            continue
        target = ROOT / ref.removeprefix("./")
        if not target.exists():
            errors.append(f"Broken local reference in index.html: {ref}")

    return errors


def check_css() -> list[str]:
    """Validate local url(...) references and brace balance in assets/css/style.css."""
    errors: list[str] = []
    css_path = ROOT / "assets/css/style.css"
    if not css_path.is_file():
        return ["assets/css/style.css not found"]

    css = css_path.read_text(encoding="utf-8")

    # Strip comments before checking brace balance
    css_no_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    if css_no_comments.count("{") != css_no_comments.count("}"):
        errors.append("Unbalanced curly braces in assets/css/style.css")

    urls = re.findall(r'url\(["\']?([^"\')]+)["\']?\)', css)
    for raw_url in urls:
        if raw_url.startswith(("http://", "https://", "data:")):
            continue
        resolved = Path(os.path.normpath(css_path.parent / raw_url))
        if not resolved.exists():
            errors.append(f"Broken CSS url() reference: {raw_url} -> {resolved}")

    return errors


def check_docs() -> list[str]:
    """Validate local links and images referenced in README.md and README-ES.md."""
    errors: list[str] = []
    for doc_name in ("README.md", "README-ES.md"):
        doc_path = ROOT / doc_name
        if not doc_path.is_file():
            continue
        content = doc_path.read_text(encoding="utf-8")
        matches = re.findall(
            r'(?:src|href)=["\']([^"\']+)["\']|\[[^\]]*\]\(([^)]+)\)',
            content,
        )
        for attr_target, md_target in matches:
            target = attr_target or md_target
            if not target or target.startswith(EXTERNAL_PREFIXES):
                continue
            resolved = ROOT / target.removeprefix("./")
            if not resolved.exists():
                errors.append(f"Broken local link in {doc_name}: {target}")
    return errors


def main() -> int:
    """Run all static validation checks and report results."""
    all_errors = [
        *check_required_files(),
        *check_html(),
        *check_css(),
        *check_docs(),
    ]

    if all_errors:
        print("Validation failed with the following errors:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("All static structure, asset, CSS, and documentation checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
