with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in style.css:', len(lines))
print(''.join(lines[-40:]))
