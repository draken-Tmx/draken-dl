#!/data/data/com.termux/files/usr/bin/bash
echo "Instalando drakenTMX.."
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

echo ""
echo "Todo listo, ahora ejecuta:"
echo "source venv/bin/activate"
echo "python descarga.py"
