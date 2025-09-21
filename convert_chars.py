#!/usr/bin/env python3
import opencc
import re

# Initialize OpenCC converter for Traditional to Simplified Chinese
converter = opencc.OpenCC('t2s')

# Read the original file
with open('cglyphlist.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all Chinese characters in the "c" field and convert them
def convert_chinese_chars(match):
    full_match = match.group(0)
    chinese_char = match.group(1)
    simplified_char = converter.convert(chinese_char)
    return full_match.replace(chinese_char, simplified_char)

# Use regex to find and convert Chinese characters in the "c" field
# Pattern matches: "c":"[Chinese character]"
pattern = r'("c":")([一-龯])(")'
content = re.sub(pattern, lambda m: m.group(1) + converter.convert(m.group(2)) + m.group(3), content)

# Write the converted content back to the file
with open('cglyphlist.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Conversion completed! All traditional Chinese characters have been converted to simplified Chinese.")
