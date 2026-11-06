with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.plan[^{]*\{[^}]*\})', css)
for m in matches[:10]:
    print(m)
    print('-'*40)

matches2 = re.findall(r'(\.pricing-card[^{]*\{[^}]*\})', css)
for m in matches2[:10]:
    print(m)
    print('-'*40)
