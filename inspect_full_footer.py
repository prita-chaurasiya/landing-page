with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[1004:1125], 1005):
    print(f'{i}: {line.rstrip()}')

