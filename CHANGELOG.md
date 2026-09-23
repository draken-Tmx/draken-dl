# Changelog

Todas las versiones notables de este proyecto se documentan en este archivo.

## [Unreleased]

## [1.1.0] - 2026-09-23

### Added
- Soporte para impersonation de Chrome en TikTok y Youtube.
- Ya no son necesarias las cookies, impersonate hace el trabajo, pero no está mal tenerlas.
- Nodejs para poder pedir solicitudes a Youtube desde su ultima version.
- Aparto para visitar el repositorio

### Changed
- Configuración de `ydl_opts` con `js_runtimes` y `remote_components`, encontrados en `guardar.py`.

### Fixed
- Error de "no impersonate target available" al extraer de TikTok.

### Removed
- Opciones basura que hacian lento el progroma.
