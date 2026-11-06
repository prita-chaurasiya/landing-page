with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_stats = text.find('<!-- ======================================================================\n       SECTION 3: TRUST STATISTICS')
print(text[:idx_stats])
