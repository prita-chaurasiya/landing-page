with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [(m.start(), m.group(0)) for m in re.finditer(r'\.hero-section[^{]*\{', text)]
for idx, match in matches[:5]:
    print(match)
    print(text[idx:idx+500])
    print('='*40)
