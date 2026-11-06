with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s = text.find('class="stats-strip-section"')
if s != -1:
    section_start = text.rfind('<section', 0, s)
    section_end = text.find('</section>', s) + len('</section>')
    print("Found section bounds:", section_start, section_end)
    print("Current snippet:\n", text[section_start:section_start+400])
else:
    print("Not found stats-strip-section")

