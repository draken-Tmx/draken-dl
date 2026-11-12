import os
import shutil
import subprocess
import sys
import yt_dlp
from rich import print
from yt_dlp.networking.impersonate import ImpersonateTarget
from rich.console import Console

console = Console()

def erased(route):
    if os.path.isdir(route):
        shutil.rmtree(route)
    else:
        os.remove(route)


video_path = "/storage/emulated/0/videos"
audio_path = "/storage/emulated/0/musica"

def animation(funcion, *args, message=""):
    with console.status(f"[bold green]{message}[/bold green]", spinner="dots"):
        return funcion(*args)

def clear():
    console.clear()

def get_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"
    return None

def open_kew2():
    while True:
        clear()
        print("")
        print("[bold cyan]1.[/bold cyan][bold blue]open player[/bold blue]")
        print("[bold cyan]2.[/bold cyan][bold blue]exit[/bold blue]")

        select = input("> ")

        if select == "1":
            if shutil.which("kew"):
                subprocess.run(["kew", "path", audio_path])
                subprocess.run(["kew"])
                os.system("stty sane")
                sys.stdin = open("/dev/tty", "r")
            else:
                print("You don't have the player, do you want to install it? y/n")
                inst = input("> ").lower()
                if inst == "y":
                    install_kew()
                elif inst == "n":
                    break
                else:
                    print("invalid option")
        elif select == "2":
            break
        else:
            print("invalid option")

def install_kew():
    if shutil.which("kew"):
        console.print("[bold green]✓ kew is already installed[/bold green]")
        console.input("[bold cyan]Enter to exit[/bold cyan]")
        return

    with console.status("[bold cyan]Installing Kew...[/bold cyan]", spinner="dots"):
        resulted = subprocess.run(["pkg", "install", "kew", "chafa", "libsixel", "-y"])

    if resulted.returncode == 0:
        console.print("[bold green]✓ complete installation[/bold green]")
    else:
        console.print("[bold red]✗ the installation failed[/bold red]")

    console.input("[bold green]Enter to exit...[/bold green]")

def rename_file():
    clear()
    try:
        t = console.input("[green]¿(v)ideos or (m)usic?: [/green]").lower()
        path = video_path if t == "v" else audio_path
        files = os.listdir(path)

        for i, n in enumerate(files):
            console.print(f"{i} > {n}")

        idx = int(console.input("Number: "))
        old = os.path.join(path, files[idx])

        new = console.input("New name without extension: ").strip()
        ext = os.path.splitext(old)[1]

        os.rename(old, os.path.join(path, new + ext))
        console.print(f"[green]ready: {new + ext}[/green]")
    except Exception as e:
        console.print(f"[red]{e}[/red]")

    console.input("[bold cyan]Enter to exit...[/bold cyan]")

def save_video():
    clear()
    try:
        os.makedirs(video_path, exist_ok=True)
        url = console.input("[bold green]link: [/bold green]")
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
        cookies = get_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url], message="downloading...")
        print("[bold green]download completed[/bold green]")
        console.input('[bold cyan]Enter to exit[/bold cyan]')
    except Exception as e:
        print(e)

def save_audio():
    clear()
    try:
        os.makedirs(audio_path, exist_ok=True)
        url = console.input("[bold green]link: [/bold green]")
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
        cookies = get_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url], message="downloading...")
        print("[bold green]download completed[/bold green]")
        console.input('[bold cyan]Enter to exit[/bold cyan]')
    except Exception as e:
        print(e)

def save_tiktok():
    clear()
    try:
        os.makedirs(video_path, exist_ok=True)
        url = console.input("[bold green]link tiktok: [/bold green]")

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
        cookies = get_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url], message="downloading...")

        print("[bold green]download completed[/bold green]")
        console.input("[bold cyan]Enter to exit[/bold cyan]")
    except Exception as e:
        print(e)


def save_playlist_audio():
    clear()
    try:
        os.makedirs(audio_path, exist_ok=True)
        url = console.input("[bold green]link PLAYLIST: [/bold green]")

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
        cookies = get_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url], message="downloading playlist...")

        console.print(f"[bold green]✓ Playlist completa[/bold green]")
        console.input('[bold cyan]Enter para exit[/bold cyan]')
    except Exception as e:
        print(e)

def save_playlist_video():
    clear()
    try:
        os.makedirs(video_path, exist_ok=True)
        url = console.input("[bold green]link PLAYLIST: [/bold green]")
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
        cookies = get_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url], message="downloading playlist...")

        console.print(f"[bold green]✓ Playlist completed[/bold green]")
    except Exception as e:
        print(e)

def save_pin():
    clear()
    try:
        url=console.input("[bold green]link: [/bold green]")
        yt_opts={
            "format":"bestvideo+bestaudio/best",
            "outtmpl":f"{video_path}%s(ext)",
            "noplaylist":True,
            "outtmpl":f"{video_path}/%(title).50s-%(id)s.%(ext)s",
            "quiet":True,
            "no_warnings":True,
            "noprogress":True
        }

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url],
            message="[bold green]downloading video...[/bold green]")
        console.print("[bold green]download completed[/bold green]")
        console.input("[bold blue]Enter to exit[/bold blue]")
    except Exception as e:
        print(e)

