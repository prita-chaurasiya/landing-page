with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

def print_section(tag_id):
    pattern = rf'(id=[\'"]{tag_id}[\'"].*?)(?=(id=[\'"][a-zA-Z0-9_\-]+[\'"]|<\/section>|$))'
    m = re.search(pattern, text, re.DOTALL)
    if m:
        print(f"=== FOUND {tag_id} ===")
        print(m.group(1)[:500])
        print("...\nLength:", len(m.group(1)))
    else:
        print(f"=== NOT FOUND {tag_id} ===")

for sid in ['focus-areas', 'about', 'videos', 'testimonials', 'plans', 'process', 'membership-form', 'faq']:
    print_section(sid)

