with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("index.html length:", len(html))
print("Sections found:")
for m in re.finditer(r'<section[^>]*id="([^"]+)"', html):
    print("-", m.group(1))
