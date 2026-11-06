with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.membership-plans-box[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)

