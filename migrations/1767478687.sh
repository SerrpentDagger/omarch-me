echo "Add opencode with system themeing"

# SD: opencode should be optional. Moved back to install AI menu, but keep configs in case installed later.
# omarchy-pkg-add opencode

# Add config using omarchy theme by default
if [[ ! -f ~/.config/opencode/opencode.json ]]; then
  mkdir -p ~/.config/opencode
  cp $OMARCHY_PATH/config/opencode/opencode.json ~/.config/opencode/opencode.json
fi
