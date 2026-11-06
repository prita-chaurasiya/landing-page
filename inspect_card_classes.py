import re

with open('index.html', encoding='utf-8') as f:
    text = f.read()

classes = re.findall(r'class=[\'"]([^\'"]+)[\'"]', text)
unique_classes = set()
for c in classes:
    for cls in c.split():
        unique_classes.add(cls)

target_keywords = ['about', 'why', 'video', 'testi', 'lead', 'form', 'pricing', 'process', 'achieve', 'faq', 'contact', 'hero', 'stat', 'focus']
matched = {k: [] for k in target_keywords}
for cls in sorted(unique_classes):
    for k in target_keywords:
        if k in cls.lower():
            matched[k].append(cls)

for k, v in matched.items():
    print(f'=== {k.upper()} ===')
    print(', '.join(v[:12]))

