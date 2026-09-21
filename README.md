# DrakenTMX

Panel de descargas multimedia para Termux + Python.

DrakenTMX es una herramienta de línea de comandos desarrollada en Python para Termux en Android, diseñada para descargar y administrar contenido multimedia de distintas plataformas.

Permite descargar videos de YouTube y TikTok, extraer audio en formato MP3 y administrar fácilmente los archivos descargados desde un menú interactivo.

---

## Características

- Descarga de videos de YouTube
- Descarga de videos de TikTok
- Descarga de contenido de TikTok sin marca de agua cuando la fuente lo permite
- Descarga de audio en formato MP3
- Conversión automática mediante FFmpeg
- Visualización de archivos descargados
- Eliminación de videos
- Eliminación de archivos de audio
- Soporte para "cookies.txt"
- Compatible con Termux
- Diseñado para funcionar directamente desde Android

## 📸 Capturas

![menu](img/menu.jpg)
![descarga con exito](img/descarga.jpg)

---

Paquetes:

- Android
- Termux
- Python 3
- Git
- FFmpeg
- yt-dlp
- rich color

---

## Instalación

1. instalar git `pkg install git -y`
2. Clonar repositorio `git clone https://github.com/joakonoqui-cmd/drakentmx.git`
2. Ir a la carpeta `cd drakentmx`
3. Permisos `chmod +x install.sh`
4. Ejecutar sh `./install.sh`

Aceptá el permiso de almacenamiento cuando Android lo solicite.

---

## Ejecutar DrakenTMX

Una vez instalado todo, ejecutá `python descarga.py`

Aparecerá el menú principal:

```
1-youtube
2-tiktok
3-musica
4-ver archivos descargados
5-eliminar videos
6-eliminar audios
7-salir
```

Desde este menú podés descargar contenido y administrar los archivos almacenados en el dispositivo.

---

## Cookies de YouTube

En algunas ocasiones, YouTube puede limitar las solicitudes de descarga o mostrar mensajes como:

Sign in to confirm you're not a bot

o solicitar información adicional para verificar la sesión.

Para estos casos, DrakenTMX permite utilizar un archivo "cookies.txt" generado desde tu propia sesión de YouTube.

¿Cómo descargar las cookies?

Una forma sencilla desde Android es utilizar Kiwi Browser, que permite instalar extensiones de Chrome.

1. Instalar Kiwi Browser

Instalá Kiwi Browser en tu dispositivo Android.

2. Instalar la extensión

Abrí Kiwi Browser y dirigite al menú de los tres puntos ubicado en la esquina superior derecha.

Entrá en:

Extensiones

y buscá una extensión compatible con la exportación de cookies en formato Netscape, por ejemplo una extensión de tipo:

Get cookies.txt

Instalala y otorgale los permisos que solicite.

3. Iniciar sesión en YouTube

Abrí:

youtube.com

Iniciá sesión normalmente con tu cuenta.

4. Exportar las cookies

Una vez iniciada la sesión:

1. Abrí nuevamente el menú de los tres puntos
2. Entrá en las extensiones
3. Abrí la extensión para exportar cookies
4. Seleccioná la opción correspondiente al sitio actual ("Current Site") si está disponible
5. Exportá las cookies de YouTube

La extensión generará un archivo `cookies.txt`. Normalmente quedará guardado en la carpeta de descargas del dispositivo.

---

## Instalar las cookies en DrakenTMX

Mové o copiá el archivo `cookies.txt` a `drakentmx/`. La estructura quedaría aproximadamente así:

```
drakentmx/
└── cookies.txt
```

DrakenTMX buscará automáticamente el archivo en la carpeta `Download/`.

Después simplemente ejecutá:

```
python descarga.py
```

Si las cookies son válidas, **yt-dlp** podrá utilizarlas durante las descargas que necesiten autenticación.

---

## Importante

Nunca compartas tu archivo `cookies.txt`.

Las cookies pueden contener información asociada a tu sesión y, dependiendo de la plataforma y de las cookies exportadas, podrían permitir acceder a una sesión autenticada.

**Por seguridad:**

- No envíes `cookies.txt` a otras personas
- No lo publiques en GitHub
- No lo subas a ningún repositorio público
- No lo compartas por Telegram, Discord u otras plataformas
- Utilizá únicamente tus propias cookies

El archivo debe mantenerse fuera del repositorio.

DrakenTMX incluye ".gitignore" para evitar que `cookies.txt` sea agregado accidentalmente a Git.

---

## Estructura del proyecto

```
drakentmx/
├── descarga.py
├── guardar.py
├── README.md
├── cookies.txt
└── .gitignore
```

El archivo `cookies.txt` no forma parte del repositorio.

---

## Uso responsable

DrakenTMX utiliza [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) para realizar las descargas.

Utilizá la herramienta de forma responsable y respetando:

- Los términos de servicio de las plataformas
- Los derechos de autor
- Las leyes aplicables en tu país

El proyecto está pensado para descargar contenido al que tengas derecho de acceso o para usos permitidos por la plataforma correspondiente.

---

## Créditos

Autor [Joako](https://github.com/joakonoqui-cmd)

Si te gusta el proyecto, podés dejar una estrella en el repositorio.

---

DrakenTMX

Un proyecto hecho en Python + Termux, pensado para tener un panel de descargas multimedia simple y funcional directamente desde Android.
