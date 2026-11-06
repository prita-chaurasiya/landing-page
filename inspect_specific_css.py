with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
classes_to_check = [
    'about-card-box', 'why-join-box', 'focus-strip-item', 'video-gallery-card',
    'testimonials-box', 'simple-process-banner-card', 'achievements-strip-section',
    'achieve-item', 'contact-card-box', 'pricing-card', 'lead-form-card'
]

for cls in classes_to_check:
    matches = re.findall(rf'(\.{cls}[^{{]*\{{[^}}]*\}})', css)
    print(f'=== {cls} (matches: {len(matches)}) ===')
    for m in matches[:2]:
        print(m[:120].replace('\n', ' '))

