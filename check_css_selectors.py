with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
selectors = [
    '.top-utility-strip',
    '.modern-sticky-nav',
    '.hero-section',
    '.hero-content',
    '.hero-title',
    '.hero-tagline',
    '.hero-gold-call-banner',
    '.hero-badge-pill',
    '.hero-check-item',
    '.hero-trust-badges',
    '.hero-composition-card',
    '.stats-strip-section',
    '.stat-card',
    '.focus-strip-section',
    '.focus-card',
    '.main-two-col-section',
    '.lead-form-card',
    '.about-card',
    '.why-card',
    '.video-card',
    '.testimonial-card',
    '.pricing-card',
    '.faq-section',
    '.contact-directory-section',
    '.main-footer'
]

print("Found selectors in style.css:")
for s in selectors:
    cnt = len(re.findall(re.escape(s), css))
    print(f"{s}: {cnt} occurrences")

