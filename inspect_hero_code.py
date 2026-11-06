with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[180:245], 181):
    print(f'{i}: {line.rstrip()}')

