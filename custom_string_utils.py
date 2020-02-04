import html
import re

def decode_improper_html_chars(str):
	return html.unescape(re.sub(r'(?<![&])#38;', '&', str))