with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<div class="pricing-cards-container".*?</div>\s*</div>\s*</div>)', text, re.DOTALL)
if m:
    print(m.group(1)[:1500])
else:
    print("Not found, searching id=plans...")
    idx = text.find('id="plans"')
    print(text[idx:idx+2000])
