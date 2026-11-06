with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'(<section class="hero-section".*?</section>)', html, re.DOTALL)
if m:
    print(m.group(1)[:2500])

