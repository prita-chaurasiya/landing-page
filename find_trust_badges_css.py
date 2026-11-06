with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.finditer(r'hero-trust', css)
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(css), m.end() + 250)
    print(css[start:end])
    print('='*50)

