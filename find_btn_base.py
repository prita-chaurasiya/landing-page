with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:300]):
    if '.btn ' in l or '.btn{' in l or l.startswith('.btn'):
        print(f"{i+1}: {l.strip()}")
