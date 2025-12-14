import re
import argparse
import os

__autotheme_marker = "THEME"
__btop_translate = {
	# Also good: main_bg, main_fg, title, hi_fg, selected_bg, selected_fg, inactive_fg.
	'proc_misc': 'detail',
	'cpu_box': 'outline',
	'cpu_start': 'grad_start',
	'cpu_mid': 'grad_mid',
	'cpu_end': 'grad_end'
}
good_keys = [ 'title', 'main_bg', 'main_fg', 'hi_fg', 'selected_bg', 'selected_fg', 'inactive_fg' ] + list(__btop_translate.values())

def deduce_comment(file):
	_, ext = os.path.splitext(file)
	
	comment_chars = {
		'.css': '/*',
		'.sh': '#',
		'.theme': '#',
		'.conf': '#',
		'.toml': '#',
		'.ini': ';',
		'.html': '<!--',
		'.json': '//',
		'.yaml': '#',
		'.yml': '#',
		'.cfg': '#',
		'.properties': '#',
		'.kdl': '//'
	}
	return comment_chars.get(ext, '#')

def btop_translate(btop_key):
	if btop_key in __btop_translate.keys():
		return __btop_translate[btop_key]
	return btop_key

# Read color scheme from btop config file.
def read_omarchy_colors(btop_file):
	colors = {}
	with open(btop_file, 'r') as file:
		for line in file:
			# btop file is in format: theme[<name>]="#<color>"
			match = re.match(r'theme\[(\w+)\]="(#\w+)"', line)
			if match:
				color_name, hex_code = match.groups()
				colors[btop_translate(color_name)] = hex_code
	return colors

# Update a given theme using btop colors
def update_theme_file(theme_file, colors, comment_char):
	comment_char = deduce_comment(theme_file) if comment_char is None else comment_char

	updated_lines = []
	pattern = f"({re.escape(comment_char)}\\s*{__autotheme_marker}:\\s*(\\w+))"
	
	with open(theme_file, 'r') as file:
		for line in file:
			# Check for AUTOTHEME comments
			autotheme_match = re.search(pattern, line)
			if autotheme_match:
				color_name = autotheme_match.group(2)
				hex_code = colors.get(color_name)

				if hex_code:
					# Replace the line with the hex code and add comment
					new_line = re.sub(r'#[0-9A-Fa-f]{6}', hex_code, line)
					updated_lines.append(new_line)
				else:
					updated_lines.append(line)
			else:
				updated_lines.append(line)

	with open(theme_file, 'w') as file:
		file.writelines(updated_lines)

def main():
	parser = argparse.ArgumentParser(description=f'Update theme file with Autotheme colors. Mark config lines which contain hex codes you would like to autotheme with comments of the form # THEME:main_bg.\nRecommended keys: {good_keys}.')
	parser.add_argument('btop_file', help='Path to the btop theme file.')
	parser.add_argument('theme_file', help='Path to the theme file to update.')
	parser.add_argument('--comment_char', default=None, help='Comment character for the theme file.')
	
	args = parser.parse_args()

	colors = read_omarchy_colors(args.btop_file)
	update_theme_file(args.theme_file, colors, args.comment_char)

if __name__ == "__main__":
	main()

