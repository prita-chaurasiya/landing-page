with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[1000:1125], 1001):
    print(f'{i}: {line.rstrip()[:100]}')

