import os
import shutil
import subprocess
import sys
import yt_dlp
from rich import print
from yt_dlp.networking.impersonate import ImpersonateTarget
from rich.console import Console

console = Console()

video_path = "/storage/emulated/0/videos"
audio_path = "/storage/emulated/0/musica"

def animacion(funcion, *args, mensaje=""):
    with console.status(f"[bold green]{mensaje}[/bold green]", spinner="dots"):
        return funcion(*args)

def limpiar():
    console.clear()

def obtener_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"
    return None

def abrir_kew2():
    while True:
        limpiar()
        print("")
        print("[bold cyan]1.[/bold cyan][bold blue]abrir reproductor[/bold blue]")
        print("[bold cyan]2.[/bold cyan][bold blue]salir[/bold blue]")

        select = input("> ")

        if select == "1":
            if shutil.which("kew"):
                subprocess.run(["kew", "path", audio_path])
                subprocess.run(["kew"])
                os.system("stty sane")
                sys.stdin = open("/dev/tty", "r")
            else:
                print("no tienes el reproductor, quieres instalarlo? y/n")
                inst = input("> ").lower()
                if inst == "y":
                    instalar_kew()
                elif inst == "n":
                    break
                else:
                    print("opción inválida")
        elif select == "2":
            break
        else:
            print("opción inválida")

def instalar_kew():
    if shutil.which("kew"):
        console.print("[bold green]✓ Kew ya está instalado[/bold green]")
        console.input("[bold cyan]Enter para salir[/bold cyan]")
        return

    with console.status("[bold cyan]Instalando Kew...[/bold cyan]", spinner="dots"):
        resultado = subprocess.run(["pkg", "install", "kew", "chafa", "libsixel", "-y"])

    if resultado.returncode == 0:
        console.print("[bold green]✓ Instalación completa[/bold green]")
    else:
        console.print("[bold red]✗ La instalación falló[/bold red]")

    console.input("[bold green]Enter para salir...[/bold green]")

def renombrar_archivo():
    limpiar()
    try:
        t = console.input("[green]¿(v)ideos o (m)usica?: [/green]").lower()
        path = video_path if t == "v" else audio_path
        files = os.listdir(path)

        for i, n in enumerate(files):
            console.print(f"{i} > {n}")

        idx = int(console.input("Numero: "))
        viejo = os.path.join(path, files[idx])

        nuevo = console.input("Nuevo nombre sin extension: ").strip()
        ext = os.path.splitext(viejo)[1]

        os.rename(viejo, os.path.join(path, nuevo + ext))
        console.print(f"[green]Listo: {nuevo + ext}[/green]")
    except Exception as e:
        console.print(f"[red]{e}[/red]")

    console.input("[bold cyan]Enter para salir...[/bold cyan]")

def guardar_video():
    limpiar()
    try:
        os.makedirs(video_path, exist_ok=True)
        url = console.input("[bold green]ingresar link: [/bold green]")
        yt_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{video_path}/%(title)s.%(id)s.%(ext)s",
            "impersonate": ImpersonateTarget.from_str("chrome"),
            "js_runtimes": {"node": {}},
            "remote_components": ["ejs:github"],
            "quiet": True,
            "no_warnings": True,
        }
        cookies = obtener_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animacion(ydl.download, [url], mensaje="descargando...")
        print("[bold green]descarga completa[/bold green]")
        console.input('[bold cyan]Enter para salir[/bold cyan]')
    except Exception as e:
        print(e)

def guardar_audio():
    limpiar()
    try:
        os.makedirs(audio_path, exist_ok=True)
        url = console.input("[bold green]ingresar link: [/bold green]")
        yt_opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "outtmpl": f"{audio_path}/%(title)s.%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "writethumbnail": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "0",
                },
                {
                    "key": "FFmpegThumbnailsConvertor",
                    "format": "jpg",
                },
                {
                    "key": "EmbedThumbnail",
                },
                {
                    "key": "FFmpegMetadata",
                }
            ],
            "js_runtimes": {"node": {"path": "/data/data/com.termux/files/usr/bin/node"}},
            "remote_components": ["ejs:github"],
        }
        cookies = obtener_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animacion(ydl.download, [url], mensaje="descargando...")
        print("[bold green]descarga completa[/bold green]")
        console.input('[bold cyan]Enter para salir[/bold cyan]')
    except Exception as e:
        print(e)

def guardar_tiktok():
    limpiar()
    try:
        os.makedirs(video_path, exist_ok=True)
        url = console.input("[bold green]link de tiktok: [/bold green]")

        yt_opts = {
            "format": "best",
            "outtmpl": f"{video_path}/%(title)s.%(id)s.%(ext)s",
            "impersonate": ImpersonateTarget.from_str("chrome"),
            "quiet": True,
            "no_warnings": True,
            "extractor_args": {
                "tiktok": {"api_hostname": ["api22-normal-c-useast2a.tiktokv.com"]}
            },
        }
        cookies = obtener_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animacion(ydl.download, [url], mensaje="descargando...")

        print("[bold green]descarga exitosa[/bold green]")
        console.input("[bold cyan]Enter para salir[/bold cyan]")
    except Exception as e:
        print(e)


def guardar_playlist_audio():
    limpiar()
    try:
        os.makedirs(audio_path, exist_ok=True)
        url = console.input("[bold green]link de la PLAYLIST: [/bold green]")

        yt_opts = {
            "format": "bestaudio/best",
            "noplaylist": False, 
            "yes_playlist": True,
            "outtmpl": f"{audio_path}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "writethumbnail": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "0",
                },
                {
                    "key": "FFmpegThumbnailsConvertor",
                    "format": "jpg",
                },
                {
                    "key": "EmbedThumbnail",
                },
                {
                    "key": "FFmpegMetadata",
                }
            ],
            "js_runtimes": {"node": {"path": "/data/data/com.termux/files/usr/bin/node"}},
            "remote_components": ["ejs:github"],
        }
        cookies = obtener_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animacion(ydl.download, [url], mensaje="Descargando playlist...")

        console.print(f"[bold green]✓ Playlist completa[/bold green]")
        console.input('[bold cyan]Enter para salir[/bold cyan]')
    except Exception as e:
        print(e)

def guardar_playlist_video():
    limpiar()
    try:
        os.makedirs(video_path, exist_ok=True)
        url = console.input("[bold green]link de la PLAYLIST: [/bold green]")
        yt_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "noplaylist": False,
            "yes_playlist": True,
            "outtmpl": f"{video_path}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "impersonate": ImpersonateTarget.from_str("chrome"),
            "js_runtimes": {"node": {}},
            "remote_components": ["ejs:github"],
        }
        cookies = obtener_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animacion(ydl.download, [url], mensaje="Descargando playlist...")

        console.print(f"[bold green]✓ Playlist completa[/bold green]")
    except Exception as e:
        print(e)
