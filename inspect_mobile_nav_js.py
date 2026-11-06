with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initMobileNav()')
print(text[pos:pos+1500])

