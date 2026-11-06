with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[990:1018], 991):
    print(f'{i}: {line.rstrip()}')

