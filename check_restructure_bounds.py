with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<section class="focus-strip-section" id="focus-areas">'
end_marker = '<section class="final-cta-section" data-aos="zoom-in">'

pos_start = text.find(start_marker)
pos_end = text.find(end_marker)

print("pos_start:", pos_start)
print("pos_end:", pos_end)

if pos_start != -1 and pos_end != -1:
    print("Found region to restructure! Length:", pos_end - pos_start)
    print("Starts with:", text[pos_start:pos_start+80])
    print("Ends before:", text[pos_end:pos_end+80])

