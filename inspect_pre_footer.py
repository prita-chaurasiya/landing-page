with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'(.{0,400}<footer)', text, re.DOTALL)
if match:
    print(match.group(1))

