# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Updated changelog.
- Updated requirements.txt.

### Removed

- Redundant Minify parameters.

## [2.0.2] - 2026.01.17

### Added

- Internal file path security.

### Fixed

- Typos.

### Changed

- Updated screenshots.
- Updated requirements.txt.
- Updated changelog.

### Removed

- Temporary CSP exceptions.

## [2.0.1] - 2024.03.28

### Changed

- Updated requirements.txt.

### Fixed

- Page loading imperfections.
- Typos.

## [2.0.0] - 2024.03.28

### Added

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

[Unreleased]: https://github.com/OperaVaria/instant-serotonin/compare/2.0.2...HEAD
[2.0.2]: https://github.com/OperaVaria/instant-serotonin/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/OperaVaria/instant-serotonin/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/OperaVaria/instant-serotonin/compare/1.0.0...2.0.0
[1.0.0]: https://github.com/OperaVaria/instant-serotonin/releases/tag/1.0.0
