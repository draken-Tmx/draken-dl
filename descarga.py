import yt_dlp

from rich import print

from rich.align import Align

import os

import time

import subprocess

from rich.console import Console

from guardar import guardar_video, guardar_tiktok, guardar_audio, limpiar,renombrar_archivo,abrir_kew2,instalar_kew,guardar_playlist_video,guardar_playlist_audio,guardar_pin

ruta1="/storage/emulated/0/musica"

ruta2="/storage/emulated/0/videos"

menu=["pinterest 📌","youtube ☘️","tiktok","musica 🎧",
"ver archivos 📁","eliminar vid❌",
"eliminar aud❌","renombrar",
"mi github","instalar kew","abrir kew",
"Plist aud","Plist vid","salir"]

console=Console()

# MENU


def down():
    while True:
        limpiar()
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
                    limpiar()
                    print("[bold cyan]1.[/][bold blue]ingresar link[/]")
                    print("[bold cyan]2.[/][bold blue]salir[/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_pin()
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
                    limpiar()
                    print("[bold cyan]1.[/][bold blue]ingresar link[/]")
                    print("[bold cyan]2.[/bold cyan][bold blue]salir[/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_video()
                        elif ingresar=="2":
                                break
                        else:
                            print("[bold red]ingrese una opcion valida[/]")
                    except Exception as e:
                            print(f"[bold red] error [/]{e}")
            except Exception as e:
                print(f"[bold red]error [/]🥀{e}")
                print("")




        elif op=="3":
            try:
                while True:
                    limpiar()
                    print("[bold cyan]1.[/][bold blue]ingresar link[/]")
                    print("[bold cyan]2.[/][bold blue]salir [/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_tiktok()
                            print("[bold green]descarga completa[/] ✅✅") 
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
                    limpiar()
                    print("[bold cyan]1.[/][bold blue]ingresar link[/]")
                    print("[bold cyan]2.[/][bold blue]salir[/]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_audio()
                            print("[bold green]descarga completa[/] ✅✅") 
                            print("")
                        elif ingresar=="2":
                            break
                    except Exception as e:
                        print(f"[bold red]error[/]{e}")
            except Exception as e:
                print(f"[bold red]fallo[/] ❌❌{e}")
                print("")
        elif op=="5":
            print("")       
            if not os.path.exists(ruta1) and not os.path.exists(ruta2):
                while True:
                    print("[bold red]no hay archivos descargados[/]")
                    print("[bold cyan]00.[/][bold blue] salir[/]")
                    salir=input("> ")
                    if salir =="00":
                        break
            elif not os.path.exists(ruta1):
                while True:
                    print("[bold red]no hay canciones,solo videos[/]")
                    print("[bold cyan]00.[/][bold blue] salir[/]")
                    salir=input("> ")
                    if salir=="00":
                        break
            elif not os.path.exists(ruta2):
                while True:
                    print("[bold red]no hay videos,solo canciones[/]")
                    for archivo in os.listdir(ruta1):
                        print(archivo)
                        print("[bold cyan]00.[/][bold blue] salir[/]")
                        salir=input("> ")
                        if salir=="00":
                            break
            else:
                if not os.listdir(ruta1) and not os.listdir(ruta2):
                    while True:
                        print("[bold red]no hay archivos descargados[/]")
                        print("[bold cyan]00.[/][bold blue]salir[/]")
                        select=input("> ")
                        if select=="00":
                            break
                else:
                    while True:
                        print("")
                        for archivo in os.listdir(ruta1):
                            print("[bold green]canciones descargadas[/]")
                            print(archivo)
                            print("")
                        for archivo in os.listdir(ruta2):
                            print("[bold green]videos de/scargados[/]")
                            print(archivo)
                            print("")
                        print("[bold cyan]00.[/][bold blue] salir[/]")
                        salir=input("> ")
                        if salir=="00":
                            break




            # FLUJO DE VIDEO
        if op == "6":
            if not os.path.exists(ruta2):
                print("[bold red]no hay nada[/]")
                while True:
                    print("00.salir")
                    salir=input("> ")
                    if salir=="00":
                        break
            else:
                archivos = os.listdir(ruta2)
                if not archivos:
                    print("[bold red]no hay archivos[/]")
                    while True:
                        print("00.salir")
                        salir=input("> ")
                        if salir=="00":
                            break
                else:
                    while True:
                        for i, archivo in enumerate(archivos, 1):
                            print(f"{i}-{archivo}")
                        print("[bold cyan]00.[/][bold blue]salir[/b]")
                        opcion = console.input("[bold blue]> [/]").strip()
                        if opcion == "00":
                            print("")
                            break  
                        try:
                            num = int(opcion)
                            if 1 <= num <= len(archivos):
                                archivo_a_borrar = archivos[num - 1]
                                confirmar = console.input(f"[bold yellow]seguro que quieres borrar {archivo_a_borrar}? si/no: [/]")
                                if confirmar.lower() == "si":
                                    os.remove(os.path.join(ruta2, archivo_a_borrar))
                                    print(f"[bold green]{archivo_a_borrar} borrado [/]✅")
                                    archivos = os.listdir(ruta2)
                                    if not archivos:
                                        break
                                elif confirmar.lower() == "no":
                                    print("[bold red]operacion cancelada[/]")
                                else:
                                    print("[bold red]opcion invalida[/]")
                            else:
                                print("[bold red]fuera de rango[/]")
                        except ValueError:
                            print("[yellow]pon un numero valido[/]")

                #FLUJO DE AUDIO
        if op == "7":
            if not os.path.exists(ruta1):
                print("[bold red]no hay nada[/]")
                while True:
                    print("00.salir")
                    salir=input("> ")
                    if salir=="00":
                        break
            else:
                archivos = os.listdir(ruta1)
                if not archivos:
                    print("[bold red]no hay archivos[/]")
                    while True:
                        print("00.salir")
                        salir=input("> ")
                        if salir=="00":
                            break
                else:
                    while True:
                        for i, archivo in enumerate(archivos, 1):
                            print(f"{i}-{archivo}")
                        print("[bold cyan]00.[/][bold blue]salir[/]")
                        opcion = console.input("[bold blue]> [/]").strip()
                        if opcion == "00":
                            print("")
                            break  
                        try:
                            num = int(opcion)
                            if 1 <= num <= len(archivos):
                                archivo_a_borrar = archivos[num - 1]
                                confirmar = console.input(f"[bold yellow]seguro que quieres borrar {archivo_a_borrar}? si/no: [/]")
                                if confirmar.lower() == "si":
                                    os.remove(os.path.join(ruta1, archivo_a_borrar))
                                    print(f"[bold green]{archivo_a_borrar} borrado [/]✅")
                                    archivos = os.listdir(ruta1)
                                    if not archivos:
                                        break
                                elif confirmar.lower() == "no":
                                    print("[bold red]operacion cancelada[/]")
                                else:
                                    print("[bold red]opcion invalida[/]")
                            else:
                                print("[bold red]fuera de rango[/]")
                        except ValueError:
                            print("[yellow]pon un numero valido[/]")

        elif op=="8":
            print("")
            limpiar()
            renombrar_archivo()
        elif op=="9":
            limpiar()
            print("[bold green]viendo codigo fuente...[/]")
            os.system("termux-open-url https://github.com/draken-Tmx/draken-dl")
        elif op =="10":
            instalar_kew()
        elif op == "11":
            abrir_kew2()
        elif op =="12":
            guardar_playlist_audio()
        elif op =="13":
            guardar_playlist_video()
        elif op == "14":
            print("[bold green]saliendo...[/]")
            time.sleep(0.5)
            break
        else:
            print("[bold red]opcion invalida[/]")

if __name__=="__main__":
    down()

