with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[575:590], 576):
    print(f'{i}: {line.rstrip()}')

