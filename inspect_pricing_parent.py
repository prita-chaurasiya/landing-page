with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[545:565], 546):
    print(f'{i}: {line.rstrip()}')

