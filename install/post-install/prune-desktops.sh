echo 'Removing orphaned .desktop files...'

local applications_path="$HOME/.local/share/applications"

mpv --version &>/dev/null || rm -f "$applications_path/mpv.desktop"
pacman -Q typora &>/dev/null || rm -f "$applications_path/typora.desktop"
