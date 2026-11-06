with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add 3D shapes after hero-glow-circle glow-circle-trophy
old_glows = '<div class="hero-glow-circle glow-circle-trophy" aria-hidden="true"></div>'
new_glows = '''<div class="hero-glow-circle glow-circle-trophy" aria-hidden="true"></div>
    <!-- 3D Decorative Floating Elements (Royal Sapphire & Pure Gold) -->
    <div class="hero-3d-floating-shape shape-squircle-blue" aria-hidden="true"></div>
    <div class="hero-3d-floating-shape shape-sphere-gold" aria-hidden="true"></div>
    <div class="hero-3d-floating-shape shape-ring-sapphire" aria-hidden="true"></div>'''

if old_glows in text:
    text = text.replace(old_glows, new_glows)
    print("Replaced glows")

# Update sub-banner text
old_call = 'Join HRCI Membership'
new_call = '★ Join HRCI Membership • Be The Change'
if '<div class="hero-gold-call-banner"' in text:
    text = text.replace(
        '<div class="hero-gold-call-banner" data-aos="fade-up" data-aos-delay="100">\n          Join HRCI Membership\n        </div>',
        '<div class="hero-gold-call-banner" data-aos="fade-up" data-aos-delay="100">\n          <span>★</span> Join HRCI Membership • Be The Change\n        </div>'
    )
    print("Replaced call banner")

# Update badges in hero-composition-card
old_badges = '''          <!-- Subtle Luxury Floating Badges in Royal Palette -->
          <div class="hero-float-badge float-badge-left">
            <span class="badge-icon-shield">🛡️</span>
            <div class="badge-text-col">
              <strong>Govt. Regd. NGO</strong>
              <small>MCA Section 8 Approved</small>
            </div>
          </div>

          <div class="hero-float-badge float-badge-right">
            <span class="badge-icon-star">⭐</span>
            <div class="badge-text-col">
              <strong>70,000+ Members</strong>
              <small>28 States Pan-India</small>
            </div>
          </div>'''

new_badges = '''          <!-- 4 3D Floating Notification Badges in Royal Palette -->
          <div class="hero-float-badge float-badge-tl" data-aos="fade-down" data-aos-delay="250">
            <span class="badge-icon-shield">🛡️</span>
            <div class="badge-text-col">
              <strong>Govt. Regd. NGO</strong>
              <small>MCA Section 8 Approved</small>
            </div>
          </div>

          <div class="hero-float-badge float-badge-tr" data-aos="fade-down" data-aos-delay="350">
            <span class="badge-icon-star">⚖️</span>
            <div class="badge-text-col">
              <strong>70,000+ Members</strong>
              <small>28 States Pan-India</small>
            </div>
          </div>

          <div class="hero-float-badge float-badge-bl" data-aos="fade-up" data-aos-delay="450">
            <span class="badge-icon-trophy">🎖️</span>
            <div class="badge-text-col">
              <strong>Global Peace Award</strong>
              <small>National Council 2026</small>
            </div>
          </div>

          <div class="hero-float-badge float-badge-br" data-aos="fade-up" data-aos-delay="550">
            <span class="badge-icon-card">🪪</span>
            <div class="badge-text-col">
              <strong>Instant Digital ID</strong>
              <small>QR Verified Member</small>
            </div>
          </div>'''

if old_badges in text:
    text = text.replace(old_badges, new_badges)
    print("Replaced badges")
else:
    print("old_badges not found exactly, let's check")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Finished update_hero_html.py")

