import yt_dlp

from log import console,get_progress,get_ydl_opts

from rich import print

import os

from rich.console import Console

from guardar import guardar_video, guardar_tiktok, guardar_audio, limpiar

ruta1="/storage/emulated/0/musica"

ruta2="/storage/emulated/0/videos"

menu=["youtube 🎥","tiktok 📱","musica 🎧","ver archivos descargados 💾","eliminar videos ❌🎥","eliminar audios ❌🎧","salir 🚪","mi github 💻"]

console=Console()

# MENU


def down():
    while True:
        limpiar()
        print("[bold yellow]bienvenido al menu de descargas[/bold yellow] 👾")
        for posicion,opcion in enumerate(menu,start=1):
            print("")
            print(f"[bold cyan]{posicion}-[/bold cyan][bold blue]{opcion}[/bold blue]")
        op=console.input("[blue] > [/blue]")
        print("")



        if op=="1":
            try:
                while True:
                    print("[bold cyan]1.[/bold cyan][bold blue]ingresar link[/bold blue]")
                    print("[bold cyan]2.[/bold cyan][bold blue]salir[/bold blue]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_video()
                            print("[bold green]descarga completa[/bold green] ✅✅") 
                            print("")
                        elif ingresar=="2":
                                break
                        else:
                            print("[bold red]ingrese una opcion valida")
                    except Exception as e:
                            print(f"[bold red] error [/bold red]{e}")
            except Exception as e:
                print(f"[bold red]error [/bold red]🥀{e}")
                print("")




        elif op=="2":
            try:
                while True:
                    limpiar()
                    print("[bold cyan]1.[/bold cyan][bold blue]ingresar link[/bold blue]")
                    print("[bold cyan]2.[/bold cyan][bold blue]salir [/bold blue]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_tiktok()
                            print("[bold green]descarga completa[/bold green] ✅✅") 
                            print("")
                        elif ingresar=="2":
                            break
                    except Exception as e:
                        print(f"[bold red]error[/bold red]{e}")
            except Exception as e:
                print(f"[bold red]error[/bold red]{e}")
                print("")





        elif op=="3":
            try:
                while True:
                    print("[bold cyan]1.[/bold cyan][bold blue]ingresar link[/bold blue]")
                    print("[bold cyan]2.[/bold cyan][bold blue]salir[/bold blue]")
                    ingresar=input("> ")
                    try:
                        if ingresar=="1":
                            guardar_audio()
                            print("[bold green]descarga completa[/bold green] ✅✅") 
                            print("")
                        elif ingresar=="2":
                            break
                    except Exception as e:
                        print(f"[bold red]error[/bold red]{e}")
            except Exception as e:
                print(f"[bold red]fallo[/bold red] ❌❌{e}")
                print("")
        elif op=="4":
            print("")       
            if not os.path.exists(ruta1) and not os.path.exists(ruta2):
                while True:
                    print("[bold red]no hay archivos descargados[/bold red]")
                    print("[bold cyan]00.[/bold cyan][bold blue] salir[/bold blue]")
                    salir=input("> ")
                    if salir =="00":
                        break
            elif not os.path.exists(ruta1):
                while True:
                    print("[bold red]no hay canciones,solo videos[/bold red]")
                    print("[bold cyan]00.[/bold cyan][bold blue] salir[/bold blue]")
                    salir=input("> ")
                    if salir=="00":
                        break
            elif not os.path.exists(ruta2):
                while True:
                    print("[bold red]no hay videos,solo canciones[/bold red]")
                    for archivo in os.listdir(ruta1):
                        print(archivo)
                        print("[bold cyan]00.[/bold cyan][bold blue] salir[/bold blue]")
                        salir=input("> ")
                        if salir=="00":
                            break
            else:
                if not os.listdir(ruta1) and not os.listdir(ruta2):
                    while True:
                        print("[bold red]no hay archivos descargados[/bold red]")
                        print("[bold cyan]00.[/bold cyan][bold blue]salir[/bold blue]")
                        select=input("> ")
                        if select=="00":
                            break
                else:
                    while True:
                        print("")
                        for archivo in os.listdir(ruta1):
                            print("[bold green]canciones descargadas[/bold green]")
                            print(archivo)
                            print("")
                        for archivo in os.listdir(ruta2):
                            print("[bold green]videos descargados[/bold green]")
                            print(archivo)
                            print("")
                        print("[bold cyan]00.[/bold cyan][bold blue] salir[/bold blue]")
                        salir=input("> ")
                        if salir=="00":
                            break




            # FLUJO DE VIDEO
        if op == "5":
            if not os.path.exists(ruta2):
                print("[bold red]no hay nada[/bold red]")
                while True:
                    print("00.salir")
                    salir=input("> ")
                    if salir=="00":
                        break
            else:
                archivos = os.listdir(ruta2)
                if not archivos:
                    print("[bold red]no hay archivos[/bold red]")
                    while True:
                        print("00.salir")
                        salir=input("> ")
                        if salir=="00":
                            break
                else:
                    while True:
                        for i, archivo in enumerate(archivos, 1):
                            print(f"{i}-{archivo}")
                        print("[bold cyan]00.[/bold cyan][bold blue]salir[/bold blue]")
                        opcion = console.input("[bold blue]> [/bold blue]").strip()
                        if opcion == "00":
                            print("")
                            break  
                        try:
                            num = int(opcion)
                            if 1 <= num <= len(archivos):
                                archivo_a_borrar = archivos[num - 1]
                                confirmar = console.input(f"[bold yellow]seguro que quieres borrar {archivo_a_borrar}? si/no: [/bold yellow]")
                                if confirmar.lower() == "si":
                                    os.remove(os.path.join(ruta2, archivo_a_borrar))
                                    print(f"[bold green]{archivo_a_borrar} borrado [/bold green]✅")
                                    archivos = os.listdir(ruta2)
                                    if not archivos:
                                        break
                                elif confirmar.lower() == "no":
                                    print("[bold red]operacion cancelada[/bold red]")
                                else:
                                    print("[bold red]opcion invalida[/bold red]")
                            else:
                                print("[bold red]fuera de rango[/bold red]")
                        except ValueError:
                            print("[yellow]pon un numero valido[/yellow]")

                #FLUJO DE AUDIO
        if op == "6":
            if not os.path.exists(ruta1):
                print("[bold red]no hay nada[/bold red]")
                while True:
                    print("00.salir")
                    salir=input("> ")
                    if salir=="00":
                        break
            else:
                archivos = os.listdir(ruta1)
                if not archivos:
                    print("[bold red]no hay archivos[/bold red]")
                    while True:
                        print("00.salir")
                        salir=input("> ")
                        if salir=="00":
                            break
                else:
                    while True:
                        for i, archivo in enumerate(archivos, 1):
                            print(f"{i}-{archivo}")
                        print("[bold cyan]00.[/bold cyan][bold blue]salir[/bold blue]")
                        opcion = console.input("[bold blue]> [/bold blue]").strip()
                        if opcion == "00":
                            print("")
                            break  
                        try:
                            num = int(opcion)
                            if 1 <= num <= len(archivos):
                                archivo_a_borrar = archivos[num - 1]
                                confirmar = console.input(f"[bold yellow]seguro que quieres borrar {archivo_a_borrar}? si/no: [/bold yellow]")
                                if confirmar.lower() == "si":
                                    os.remove(os.path.join(ruta1, archivo_a_borrar))
                                    print(f"[bold green]{archivo_a_borrar} borrado [/bold green]✅")
                                    archivos = os.listdir(ruta1)
                                    if not archivos:
                                        break
                                elif confirmar.lower() == "no":
                                    print("[bold red]operacion cancelada[/bold red]")
                                else:
                                    print("[bold red]opcion invalida[/bold red]")
                            else:
                                print("[bold red]fuera de rango[/bold red]")
                        except ValueError:
                            print("[yellow]pon un numero valido[/yellow]")

        elif op=="7":
            print("[bold green]saliendo[/bold green]")
            break
        elif op=="8":
            limpiar()
            print("[bold green]viendo codigo fuente...[/bold green]")
            os.system("termux-open-url https://github.com/joakonoqui-cmd/drakentmx")
        else:
            print("[bold red]opcion invalida[/bold red]")

if __name__=="__main__":
    down()

