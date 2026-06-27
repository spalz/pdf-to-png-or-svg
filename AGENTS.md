# PDF Extraction Agents

Owner repo: `pdf-to-png-or-svg/`.

## Stack

Python scripts for extracting PDF pages/graphics to PNG or SVG-like outputs. The repo contains source PDFs and generated output directories.

## Commands

Use local Python/venv if needed. Main scripts:

- `python3 pdf_extractor_to_png.py <pdf-path> <output-dir>`
- `python3 pdf_extractor_to_svg.py <pdf-path> <output-dir>`

Run scripts only on a small explicit sample unless the user asks for full regeneration.

## Sensitive Zones

Do not mass-regenerate output images, delete generated assets, or rewrite source PDFs without explicit request. If adding dependencies, document the environment first; this repo currently has no committed `requirements.txt`.

## PR Acceptance

For script changes, run a tiny sample extraction when practical and report output file count/path. For docs/config changes, do not run heavy extraction.
