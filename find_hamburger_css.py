with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 0
while True:
    pos = text.find('.nav-hamburger-toggle', pos)
    if pos == -1:
        break
    print(f"Found .nav-hamburger-toggle at {pos}:")
    print(text[pos:pos+300])
    print('='*50)
    pos += 20

