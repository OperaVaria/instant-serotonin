# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024.03.27

## Added

- Implemented minification with Flask-Minify.
- Implemented HTTP security headers with Flask-Talisman.
- New sources: Pexels, Pixabay, Unsplash.
- Pylint workflow.
- SEO files (robots.txt, sitemap.xml).
- humans.txt.
- Added more comments.

### Changed

- Revamped scraping entirely with new sources.
- Eliminated inline JavaScript.
- HTML restructured for accessibility and SEO.
- Slow loading "current year" JS swapped out for Jinja/Python variable.
- ChaceLib settings for new Flask-Session version 0.8.0.
- Updated docs.
- Updated requirements.txt.

### Fixed

- Code formatting, typos.

## [1.0.0] - 2024.02.26

### Added

- Initial "release".
