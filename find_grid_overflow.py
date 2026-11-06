with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.pricing-cards-grid[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)

matches2 = re.findall(r'(\.card-lifetime-banner[^{]*\{[^}]*\})', css)
for m in matches2:
    print(m)

