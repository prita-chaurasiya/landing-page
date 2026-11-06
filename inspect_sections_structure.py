with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith('<section') or line.strip().startswith('</section>') or 'id=' in line and ('about' in line or 'videos' in line or 'plans' in line or 'faq' in line or 'process' in line):
        print(f'{i+1}: {line.strip()[:90]}')

