with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[1015:1060], 1016):
    print(f'{i}: {line.rstrip()}')

