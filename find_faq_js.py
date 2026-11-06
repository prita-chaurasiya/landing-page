with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'(\bfsq\b|\bfaq\b[^\n]*\n[^\n]*)', js, re.IGNORECASE)
print("Matches found in script.js:")
for m in matches[:5]:
    print(m)

# Find FAQ function in script.js
pos = js.find('faq')
if pos != -1:
    print("\nFAQ context in script.js:")
    print(js[pos-50:pos+400])

