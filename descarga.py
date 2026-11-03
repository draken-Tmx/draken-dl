import yt_dlp

from rich import print

from rich.align import Align

import os

import time

import subprocess

from rich.console import Console

from guardar import save_video, save_tiktok, save_audio, clear,rename_file,open_kew2,install_kew,save_playlist_video,save_playlist_audio,save_pin,erased

ruta1="/storage/emulated/0/musica"

ruta2="/storage/emulated/0/videos"

menu=["pinterest ","youtube ","tiktok","music ",
"view files ","deleted vid",
"deleted aud","rename",
"my github","install kew","open kew",
"Plist aud","Plist vid","exit"]

console=Console()

# MENU


def down():
    while True:
        clear()
        os.system("chafa --align mid,top --size 40x35 logos/dragon1.png")
        for i in range(0, len(menu), 2):
            izq = f"{i+1}.{menu[i]}"
            if i+1 < len(menu):
                der = f"{i+2}.{menu[i+1]}"
                print("")
                console.print(Align.center(f"{izq: <45} {der}"))
            else:
                console.print(Align.center(izq))
                print("")
        print("")
        op=console.input("[bold blue]> [/]")

        if op=="1":
            try:
                while True:
                    clear()
                    print("[bold cyan]1.[/][bold blue]Enter link: [/]")
                    print("[bold cyan]2.[/][bold blue]exit[/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            save_pin()
                        elif ingresar=="2":
                            break
                        else:
                            print("[bold red]error[/]")
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)



        if op=="2":
            try:
                while True:
                    clear()
                    print("[bold cyan]1.[/][bold blue]Enter link: [/]")
                    print("[bold cyan]2.[/bold cyan][bold blue]exit[/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            save_video()
                        elif ingresar=="2":
                                break
                        else:
                            print("[bold red]Enter a valid option[/]")
                    except Exception as e:
                            print(f"[bold red] error [/]{e}")
            except Exception as e:
                print(f"[bold red]error [/]🥀{e}")
                print("")




        elif op=="3":
            try:
                while True:
                    clear()
                    print("[bold cyan]1.[/][bold blue]Enter link: [/]")
                    print("[bold cyan]2.[/][bold blue]exit [/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            save_tiktok()
                            print("[bold green]complete download [/] ✅✅") 
                            print("")
                        elif ingresar=="2":
                            break
                    except Exception as e:
                        print(f"[bold red]error[/]{e}")
            except Exception as e:
                print(f"[bold red]error[/]{e}")
                print("")





        elif op=="4":
            try:
                while True:
                    clear()
                    print("[bold cyan]1.[/][bold blue]Enter link: [/]")
                    print("[bold cyan]2.[/][bold blue]exit[/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_audio()
                            print("[bold green]complete download[/] ✅✅") 
                            print("")
                        elif ingresar=="2":
                            break
                    except Exception as e:
                        print(f"[bold red]error[/]{e}")
            except Exception as e:
                print(f"[bold red]failed[/] ❌❌{e}")
                print("")
        elif op=="5":
            print("")       
            if not os.path.exists(ruta1) and not os.path.exists(ruta2):
                while True:
                    print("[bold red]No files downloaded[/]")
                    print("[bold cyan]00.[/][bold blue] exit[/]")
                    exit=input("> ")
                    if exit =="00":
                        break
            elif not os.path.exists(ruta1):
                while True:
                    print("[bold red]there are no songs,only videos[/]")
                    print("[bold cyan]00.[/][bold blue] exit[/]")
                    exit=input("> ")
                    if exit=="00":
                        break
            elif not os.path.exists(ruta2):
                while True:
                    print("[bold red]there are no videos,only songs[/]")
                    for archivo in os.listdir(ruta1):
                        print(archivo)
                        print("[bold cyan]00.[/][bold blue] exit[/]")
                    exit=input("> ")
                    if exit=="00":
                        break
            else:
                if not os.listdir(ruta1) and not os.listdir(ruta2):
                    while True:
                        print("[bold red]No files downloaded[/]")
                        print("[bold cyan]00.[/][bold blue]exit[/]")
                        select=input("> ")
                        if select=="00":
                            break
                else:
                    while True:
                        print("")
                        for archivo in os.listdir(ruta1):
                            print("[bold green]downloaded songs[/]")
                            print(archivo)
                            print("")
                        for archivo in os.listdir(ruta2):
                            print("[bold green]downloaded videos[/]")
                            print(archivo)
                            print("")
                        print("[bold cyan]00.[/][bold blue] exit[/]")
                        exit=input("> ")
                        if exit=="00":
                            break




            # FLUJO DE VIDEO
        if op == "6":
            if not os.path.exists(ruta2):
                print("[bold red]there is nothing[/]")
                while True:
                    print("00.exit")
                    exit=input("> ")
                    if exit=="00":
                        break
            else:
                archivos = os.listdir(ruta2)
                if not archivos:
                    print("[bold red]there are no files[/]")
                    while True:
                        print("00.exit")
                        exit=input("> ")
                        if exit=="00":
                            break
                else:
                    while True:
                        for i, archivo in enumerate(archivos, 1):
                            print(f"{i}-{archivo}")
                        print("[bold cyan]00.[/][bold blue]exit[/b]")
                        opcion = console.input("[bold blue]> [/]").strip()
                        if opcion == "00":
                            print("")
                            break  
                        try:
                            num = int(opcion)
                            if 1 <= num <= len(archivos):
                                archivo_a_borrar = archivos[num - 1]
                                confirmar = console.input(f"[bold yellow]surely you want do delete {archivo_a_borrar}? yes/no: [/]")
                                if confirmar.lower() == "yes":
                                    borrado(os.path.join(ruta2, archivo_a_borrar))
                                    print(f"[bold green]{archivo_a_borrar}erased[/]✅")
                                    archivos = os.listdir(ruta2)
                                    if not archivos:
                                        break
                                elif confirmar.lower() == "no":
                                    print("[bold red]canceled operation[/]")
                                else:
                                    print("[bold red]invalid option[/]")
                            else:
                                print("[bold red]out of range[/]")
                        except ValueError:
                            print("[yellow]enter a valid number[/]")

                #FLUJO DE AUDIO
        if op == "7":
            if not os.path.exists(ruta1):
                print("[bold red]there is nothing[/]")
                while True:
                    print("00.exit")
                    exit=input("> ")
                    if exit=="00":
                        break
            else:
                archivos = os.listdir(ruta1)
                if not archivos:
                    print("[bold red]there are no files[/]")
                    while True:
                        print("00.exit")
                        exit=input("> ")
                        if exit=="00":
                            break
                else:
                    while True:
                        for i, archivo in enumerate(archivos, 1):
                            print(f"{i}-{archivo}")
                        print("[bold cyan]00.[/][bold blue]exit[/]")
                        opcion = console.input("[bold blue]> [/]").strip()
                        if opcion == "00":
                            print("")
                            break  
                        try:
                            num = int(opcion)
                            if 1 <= num <= len(archivos):
                                archivo_a_borrar = archivos[num - 1]
                                confirmar = console.input(f"[bold yellow]surely you want do delete {archivo_a_borrar}? si/no: [/]")
                                if confirmar.lower() == "si":
                                    borrado(os.path.join(ruta1, archivo_a_borrar))
                                    print(f"[bold green]{archivo_a_borrar}erased[/]✅")
                                    archivos = os.listdir(ruta1)
                                    if not archivos:
                                        break
                                elif confirmar.lower() == "no":
                                    print("[bold red]canceled operation[/]")
                                else:
                                    print("[bold red]invalid option[/]")
                            else:
                                print("[bold red]out of range[/]")
                        except ValueError:
                            print("[yellow]enter a valid number[/]")

        elif op=="8":
            print("")
            clear()
            rename_file()
        elif op=="9":
            clear()
            print("[bold green]viewing source code...[/]")
            os.system("termux-open-url https://github.com/draken-Tmx/draken-dl")
        elif op =="10":
            install_kew()
        elif op == "11":
            open_kew2()
        elif op =="12":
            save_playlist_audio()
        elif op =="13":
            save_playlist_video()
        elif op == "14":
            print("[bold green]leaving...[/]")
            time.sleep(0.5)
            break
        else:
            print("[bold red]invalid option[/]")

if __name__=="__main__":
    down()

