sudo mkdir -p /etc/sddm.conf.d

if niri --version &> /dev/null; then
  compositor='niri-uwsm'
  omarch-me-niri-add-session
else
  compositor='hyprland-uwsm'
fi

if [ ! -f /etc/sddm.conf.d/autologin.conf ]; then
  cat <<EOF | sudo tee /etc/sddm.conf.d/autologin.conf
[Autologin]
User=$USER
Session=$compositor

[Theme]
Current=breeze
EOF
fi

# Don't use chrootable here as --now will cause issues for manual installs
sudo systemctl enable sddm.service
