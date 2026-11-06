with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'(<nav.*?</nav>)', text, re.DOTALL)
if match:
    print(match.group(1))

match_badges = re.search(r'(<div class="hero-trust-badges".*?</div>\s*</div>)', text, re.DOTALL)
if match_badges:
    print("\n--- HERO TRUST BADGES ---")
    print(match_badges.group(1))

