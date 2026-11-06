with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Final CTA snippet:")
match = re.search(r'(<section[^>]*final-cta-section.*?<\/section>)', text, re.DOTALL)
if match:
    print(match.group(1)[:400])

print("\nFooter top bar snippet:")
match = re.search(r'(<footer.*?<\/footer>)', text, re.DOTALL)
if match:
    print(match.group(1)[:600])

