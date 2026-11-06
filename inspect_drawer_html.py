with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_nav = text.find('id="navbarList"')
print(text[pos_nav-50:pos_nav+1000])

