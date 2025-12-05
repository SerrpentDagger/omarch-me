# --- GPU Detection ---
if [ -n "$(lspci | grep -i 'nvidia')" ]; then
  echo 'IMPORTANT: Nvidia card detected. Recommended automatic configuration will install some proprietary Nvidia software (nvidia-utils, lib32-nvidia-utils), even if your card IS supported by the recent nvidia-open-dkms driver.'
  echo 'If you skip this step, you'"'"'ll be missing some optimisations and configurations for your card for Hyperland, and your card probably won'"'"'t be doing much until you manually install a driver yourself. :('
  echo 'If you know more about Nvidia on Linux than I do, and would like to add options for Nouveau, please contribute to this script on GitHub!: https://github.com/SerrpentDagger/omarch-me/blob/master/install/config/hardware/nvidia.sh'
  pause_log
  if ! gum confirm 'Proceed with Nvidia driver installation and configuration?'; then
    unpause_log 'Installing more configs...'
  else
    unpause_log 'Installing Nvidia drivers and more configs...'
    run_logged $OMARCHY_INSTALL/config/hardware/nvidia.sh
  fi
fi
