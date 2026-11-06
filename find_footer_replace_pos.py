with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos_poster = text.find('class="poster-matching-footer-bar"')
pos_footer_end = text.find('</footer>')

print("pos_poster:", pos_poster)
print("pos_footer_end:", pos_footer_end)

if pos_poster != -1 and pos_footer_end != -1:
    print("Found section to replace. Length:", pos_footer_end + len('</footer>') - pos_poster)
    print("Snippet:")
    print(text[pos_poster-50:pos_poster+100])

