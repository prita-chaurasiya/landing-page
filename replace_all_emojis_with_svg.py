with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. REPLACE CONTACT ICONS
old_contact_grid_start = text.find('<div class="contact-cards-grid-4col"')
old_contact_grid_end = text.find('</div>\n    </div>\n  </section>\n\n  <section class="final-cta-section"')

new_contact_grid = '''<div class="contact-cards-grid-4col" data-aos="fade-up">
        <!-- 1. National Headquarters -->
        <div class="contact-card-premium">
          <div class="contact-icon-bubble bubble-navy">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
          </div>
          <h4>National Headquarters</h4>
          <p class="contact-meta">Central Administration &amp; Legal Wing</p>
          <p class="contact-detail">Barakhamba Road, Connaught Place, New Delhi – 110001, India</p>
        </div>

        <!-- 2. Western Coordination Office -->
        <div class="contact-card-premium">
          <div class="contact-icon-bubble bubble-amber">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 2h2v2h-2V5zm0 4h2v2h-2V9zm0 4h2v2h-2v-2zm-4-8h2v2H8V5zm0 4h2v2H8V9zm0 4h2v2H8v-2zm-4-8h2v2H4V5zm0 4h2v2H4V9zm0 4h2v2H4v-2zm14 8H4v-2h16v2zm0-4h-2v-2h2v2zm0-4h-2V9h2v2zm0-4h-2V5h2v2z"/></svg>
          </div>
          <h4>Western Coordination Office</h4>
          <p class="contact-meta">State Operations &amp; Event Liaison</p>
          <p class="contact-detail">Mumbai Metropolitan Region, Maharashtra – 400001, India</p>
        </div>

        <!-- 3. National Citizen Helpline -->
        <div class="contact-card-premium">
          <div class="contact-icon-bubble bubble-sapphire">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-2.2 2.2a15.053 15.053 0 01-6.59-6.59l2.2-2.21a.96.96 0 00.25-1A11.36 11.36 0 018.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1zM19 12h2a9 9 0 00-9-9v2c3.87 0 7 3.13 7 7zm-4 0h2c0-2.76-2.24-5-5-5v2c1.66 0 3 1.34 3 3z"/></svg>
          </div>
          <h4>National Citizen Helpline</h4>
          <p class="contact-meta">Direct Inquiries &amp; Member Support</p>
          <p class="contact-detail"><strong>+91 95944 41319</strong><br><strong>+91 95944 41315</strong></p>
        </div>

        <!-- 4. Official Correspondence -->
        <div class="contact-card-premium">
          <div class="contact-icon-bubble bubble-emerald">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </div>
          <h4>Official Correspondence</h4>
          <p class="contact-meta">Verification &amp; Documentation</p>
          <p class="contact-detail"><strong>info@hrcofindia.org</strong><br><strong>www.hrcofindia.org</strong></p>
        </div>
      </div>'''

if old_contact_grid_start != -1 and old_contact_grid_end != -1:
    text = text[:old_contact_grid_start] + new_contact_grid + text[old_contact_grid_end:]
    print("Replaced Contact Icons successfully!")
else:
    print("Could not find contact grid bounds, let's check")

# 2. REPLACE HERO BADGE EMOJIS
text = text.replace(
    '<span class="badge-icon-shield">🛡️</span>',
    '<span class="badge-icon-svg icon-svg-blue"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg></span>'
)

text = text.replace(
    '<span class="badge-icon-star">⚖️</span>',
    '<span class="badge-icon-svg icon-svg-amber"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a1 1 0 00-1 1v1.07A7.002 7.002 0 005.07 10H4a1 1 0 000 2h1.07A7.002 7.002 0 0011 17.93V21H9a1 1 0 000 2h6a1 1 0 000-2h-2v-3.07A7.002 7.002 0 0018.93 12H20a1 1 0 000-2h-1.07A7.002 7.002 0 0013 4.07V3a1 1 0 00-1-1zm-5 9a5 5 0 1110 0 5 5 0 01-10 0z"/></svg></span>'
)

text = text.replace(
    '<span class="badge-icon-trophy">🎖️</span>',
    '<span class="badge-icon-svg icon-svg-gold"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19 5h-2V3H7v2H5c-1.1 0-2 .9-2 2v1c0 2.55 1.92 4.63 4.39 4.94A5.01 5.01 0 0011 15.9V19H7v2h10v-2h-4v-3.1c1.83-.43 3.24-1.89 3.61-3.76A5.01 5.01 0 0021 8V7c0-1.1-.9-2-2-2zM5 8V7h2v3.82C5.84 10.4 5 9.3 5 8zm14 0c0 1.3-.84 2.4-2 2.82V7h2v1z"/></svg></span>'
)

text = text.replace(
    '<span class="badge-icon-card">🪪</span>',
    '<span class="badge-icon-svg icon-svg-sapphire"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg></span>'
)

# 3. REPLACE ABOUT STAMP EMOJI
text = text.replace(
    '<span class="badge-icon">🏛️</span>',
    '<span class="badge-icon-svg icon-svg-blue"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L2 6v2h20V6L12 1zM4 10v9h3v-9H4zm6 0v9h3v-9h-3zm6 0v9h3v-9h-3zM2 21v2h20v-2H2z"/></svg></span>'
)

# 4. REPLACE LEAD FORM LOCK EMOJI
text = text.replace(
    '<span>🔒 Your information is 100% safe &amp; confidential</span>',
    '<span class="form-lock-line"><svg width="14" height="14" viewBox="0 0 24 24" fill="#16A34A" style="vertical-align:-2px;margin-right:6px;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>Your information is 100% safe &amp; confidential</span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated index.html without any AI emojis!")

