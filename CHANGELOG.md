# Changelog

Todas las versiones notables de este proyecto se documentan en este archivo.

## [Unreleased]

## [1.1.0] - 2026-09-23

### Added
- Soporte para impersonation de Chrome en TikTok y Youtube.
- Ya no son necesarias las cookies, impersonate hace el trabajo, pero no está mal tenerlas.
- Nodejs para poder pedir solicitudes a Youtube desde su ultima version.
- Aparto para visitar el repositorio
- Agregado VENV/ para no manchar sus paquetes.
- Se agrego un alias para hacer mas rapido y optimizado el comando de inicio, basta con solo escribir `draken`,no importa en que ruta estés, el comando se va ejecutar.
- Mejora de animacion al descargar.
- Se añadio abrir un reproductor de termimal `kew`.
- Opcion de instalar el reproductor.
- Mejor de calidad.
- Portadas de musica incorporadas con `chafa`,`sixcels`.
- Mejora de menu y portada añadida.
- Nueva funcion agregada, permite descargar videos de `pinterest`.

### Changed
- Configuración de `ydl_opts` con `js_runtimes` y `remote_components`, encontrados en `guardar.py`.
- Animacion de `rich` mas fluida y agradable.

### Fixed
- Error de "no impersonate target available" al extraer de TikTok.
- Error de descargas y animaciones.

### Removed
- Opciones basura que hacian lento el progroma.
- Log.py y hooks
