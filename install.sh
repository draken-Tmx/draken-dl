#!/data/data/com.termux/files/usr/bin/bash
echo "Instalando draken-dl.."
echo ""
echo "Actualizando paquetes"
pkg update -y && pkg upgrade -y

echo "Instalando paquetes del sistema"
pkg install python ffmpeg git nodejs -y

echo "Instalando dependencias"
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

termux-setup-storage

echo "alias draken='cd ~/draken-dl && source venv/bin/activate && python descarga.py'" >> ~/.bashrc
source ~/.bashrc 2>/dev/null
source ~/.bashrc 
echo ""

echo "Instalado! Ahora solo escribe draken para correr"

