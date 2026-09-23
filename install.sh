#!/bin/bash
echo "Instalando drakenTMX.."
echo ""
echo "Actualizando paquetes"
pkg update -y && pkg upgrade -y

echo "instalando paquetes"
pkg install python ffmpeg git nodejs -y

echo "instalando dependencias" 

pip install -r requirements.txt

termux-setup-storage

echo "Todo listo, ejecute: python descarga.py "

echo "para cualquier error, hacerselo saber al dueño del repositorio"
