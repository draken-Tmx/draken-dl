import os
from yt_dlp.networking.impersonate import ImpersonateTarget
import yt_dlp
from rich import print
from log import console,get_progress,get_ydl_opts
from rich.console import Console
video_path="/storage/emulated/0/videos"
audio_path="/storage/emulated/0/musica"
console=Console()
    
def limpiar():
    console.clear()


def obtener_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"

    return None

def guardar_video():
    limpiar()
    try:
        os.makedirs(video_path,exist_ok=True)
        url = console.input("[bold green]ingresar link: [/bold green]")
        progress, hook =get_progress()
        opts = get_ydl_opts(video_path,hook)
        yt_opts ={
            "format": "bestvideo+bestaudio/best",
            "merge_output_format":"mp4",
            "outtmpl": f"{video_path}/%(title)s.%(id)s.%(ext)s",
            "impersonate": ImpersonateTarget.from_str("chrome"),
            "js_runtimes":{"node": {}},
            "remote_components":["ejs:github"],

        }
        cookies= obtener_cookies()
        if cookies:
            yt_opts["cookiefile"]=cookies

        final_opts={**opts,**yt_opts}
        final_opts["progress_hooks"]=[hook]

        with progress:
            with yt_dlp.YoutubeDL(final_opts) as ydl:
                ydl.download([url])
                print("descarga completa")
    except Exception as e:
        print(e)




def guardar_audio():
    limpiar()
    try:
        os.makedirs(audio_path,exist_ok=True)
        url = console.input("[bold green]ingresar link: [/bold green]")
        progress,hook=get_progress()
        opts=get_ydl_opts(audio_path,hook)
        yt_opts ={
            "format":"bestaudio/best",
            "noplaylist":True,
            "outtmpl": f"{audio_path}/%(title)s.%(id)s.%(ext)s",
            "postprocessors":[{
                "key":"FFmpegExtractAudio",
                "preferredcodec":"mp3",
                "preferredquality":"10",
            }],
            "js_runtimes": {"node": {"path": "/data/data/com.termux/files/usr/bin/node"}},
            "remote_components": ["ejs:github"],
        }
        cookies=obtener_cookies()

        if cookies:
            yt_opts["cookiefile"]=cookies
        final_opts={**opts,**yt_opts}
        final_opts["progress_hooks"]=[hook]

        with progress:
            with yt_dlp.YoutubeDL(final_opts) as ydl:
                ydl.download([url])
    except Exception as e:
        print(e)



def guardar_tiktok():
    limpiar()
    try:
        os.makedirs(video_path,exist_ok=True)
        url = console.input("[bold green]link de tiktok: [/bold green]")
        progress,hook= get_progress()
        opts=get_ydl_opts(video_path,hook)

        yt_opts={
            "format":"best",
            "outtmpl":f"{video_path}/%(title)s.%(id)s.%(ext)s",
            "impersonate" : ImpersonateTarget.from_str("chrome"),
            "extractor_args":{
                "tiktok":{"api_hostname": ["api22-normal-c-useast2a.tiktokv.com"]}

            }
        }
        cookies=obtener_cookies()

        if cookies:
            yt_opts["cookiefile"]= cookies
        final_opts={**opts,**yt_opts}
        final_opts["progress_hooks"]=[hook]
        with progress:
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                ydl.download([url])
                print("descarga exitosa")
    except Exception as e:
        print(e)

