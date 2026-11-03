#!/data/data/com.termux/files/usr/bin/bash
echo "installing draken-dl.."
echo ""
echo "updating paquetes"
pkg update -y && pkg upgrade -y

echo "installing system packages"
pkg install python ffmpeg git nodejs chafa -y

echo "installing dependencies"
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

termux-setup-storage

ALIAS_CMD="alias draken='cd ~/draken-dl && source venv/bin/activate && python descarga.py'"
FISH_FUNC_DIR="$HOME/.config/fish/functions"

# bash
if [ -f "$HOME/.bashrc" ]; then
    grep -q "alias draken=" "$HOME/.bashrc" || echo "$ALIAS_CMD" >> "$HOME/.bashrc"
    echo "[bash] alias agregado"
fi

# zsh
if [ -f "$HOME/.zshrc" ]; then
    grep -q "alias draken=" "$HOME/.zshrc" || echo "$ALIAS_CMD" >> "$HOME/.zshrc"
    echo "[zsh] alias agregado"
else

    if command -v zsh >/dev/null 2>&1; then
        echo "$ALIAS_CMD" >> "$HOME/.zshrc"
        echo "[zsh] .zshrc creado + alias"
    fi
fi

# fish
if command -v fish >/dev/null 2>&1; then
    mkdir -p "$FISH_FUNC_DIR"
    cat > "$FISH_FUNC_DIR/draken.fish" << 'EOF'
function draken
    cd ~/draken-dl
    source venv/bin/activate.fish
    python descarga.py
end
EOF
    echo "[fish] función draken.fish creada"
fi

echo ""
echo "Once installed, close your terminal and simply type draken to run the program."
echo "if that doesn't work, do: source ~/.bashrc (o source ~/.zshrc)"
