with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[900:1150], 901):
    if any(k in line for k in ['<section', '</section>', '<footer', '</footer>', 'contact-directory', 'final-cta', 'poster-matching']):
        print(f'{i}: {line.strip()[:90]}')

