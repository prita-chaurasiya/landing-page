# update_footer_and_color.py
import re

# 1. UPDATE index.html: Replace heavy footer with minimal landing page footer
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern matching from poster-matching-footer-bar through </footer>
pattern = re.compile(
    r'<!-- =+\s*SECTION 15A: POSTER MATCHING BLUE FOOTER STRIP\s*=+\s*-->.*?</footer>',
    re.DOTALL
)

new_footer_html = '''<!-- ======================================================================
       MINIMAL LANDING PAGE FOOTER (INSPIRED BY REFERENCE SCREENSHOT)
       ====================================================================== -->
  <footer class="simple-landing-footer" id="contact">
    <div class="container simple-footer-container">
      <div class="simple-footer-grid">
        <!-- Col 1: Brand & Overview -->
        <div class="simple-footer-col brand-col">
          <div class="simple-footer-brand-title">
            <img src="assets/images/hrci-navbar-logo.svg" alt="HRCI Seal" class="simple-footer-logo" width="36" height="36">
            <h4>Human Rights Council of India</h4>
          </div>
          <p class="simple-footer-desc">
            A National, Non-Political &amp; Secular NGO registered under Govt. of India MCA – Section 8 Company for human rights, education, healthcare &amp; social welfare across India.
          </p>
          <div class="simple-footer-divider"></div>
          <p class="simple-footer-copy">
            © 2026 Human Rights Council of India (HRCI). All rights reserved.
          </p>
        </div>

        <!-- Col 2: Explore In-Page Links -->
        <div class="simple-footer-col explore-col">
          <h5 class="simple-footer-heading">Explore</h5>
          <ul class="simple-footer-nav">
            <li><a href="#about">About</a></li>
            <li><a href="#focus-areas">Focus Areas</a></li>
            <li><a href="#videos">Videos</a></li>
            <li><a href="#testimonials">Members Say</a></li>
            <li><a href="#plans">Membership Plans</a></li>
            <li><a href="#faq">FAQ</a></li>
          </ul>
        </div>

        <!-- Col 3: Contact Details -->
        <div class="simple-footer-col contact-col">
          <h5 class="simple-footer-heading">Contact</h5>
          <div class="simple-footer-contact-list">
            <p class="contact-addr">Barakhamba Road, Connaught Place, New Delhi 110001</p>
            <p><a href="tel:+919594441315">+91 95944 41315</a></p>
            <p><a href="mailto:info@hrcofindia.org">info@hrcofindia.org</a></p>
            <p><a href="https://www.hrcofindia.org" target="_blank" rel="noopener">www.hrcofindia.org</a></p>
          </div>
        </div>
      </div>
    </div>
  </footer>'''

if pattern.search(html):
    html = pattern.sub(new_footer_html, html)
    print("Successfully replaced footer using regex pattern!")
else:
    # Alternative fallback find
    start_tag = '<div class="poster-matching-footer-bar">'
    end_tag = '</footer>'
    idx_start = html.find(start_tag)
    idx_end = html.find(end_tag)
    if idx_start != -1 and idx_end != -1:
        html = html[:idx_start] + new_footer_html + html[idx_end + len(end_tag):]
        print("Successfully replaced footer using fallback find!")
    else:
        print("Warning: Could not locate footer boundary!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. APPEND THE ROYAL SAPPHIRE & WARM GOLD COLOR SYSTEM TO style.css
css_theme = '''
/* ==========================================================================
   HRCI DISTINCT COLOR IDENTITY: ROYAL SAPPHIRE & WARM GOLD
   - Removes NGO Coral Orange entirely for a unique, prestigious identity
   - Royal Sapphire Blue (#1D4ED8 -> #2563EB) for Authority, Justice & Supreme Trust
   - Warm Saffron Gold (#F59E0B) for Peace Awards, Underline & Accents
   - Sleek Minimal Landing Page Footer matching reference screenshot
   ========================================================================== */

:root {
  --hrci-blue-dark: #1E3A8A;
  --hrci-blue: #1D4ED8;
  --hrci-blue-vibrant: #2563EB;
  --hrci-blue-light: #3B82F6;
  --hrci-blue-tint: #EFF6FF;
  --hrci-blue-border: #BFDBFE;
  --hrci-blue-glow: 0 10px 25px -4px rgba(29, 78, 216, 0.45);
  --hrci-blue-gradient: linear-gradient(135deg, #1E40AF 0%, #2563EB 60%, #3B82F6 100%);
  --hrci-blue-hover: linear-gradient(135deg, #172554 0%, #1D4ED8 100%);
  
  --hrci-gold: #F59E0B;
  --hrci-gold-dark: #D97706;
  --hrci-gold-tint: #FEF3C7;
  --hrci-gold-border: #FDE68A;
}

/* 1. Navbar Buttons & Links */
.brand-name-hi {
  color: var(--hrci-blue) !important;
}
.nav-link-item:hover, .nav-link-item.active {
  color: var(--hrci-blue) !important;
}
.nav-link-item::after {
  background: var(--hrci-blue) !important;
}
.btn-nav-cta, .btn-primary-red {
  background: var(--hrci-blue-gradient) !important;
  color: #FFFFFF !important;
  border-radius: 9999px !important;
  box-shadow: var(--hrci-blue-glow) !important;
  border: none !important;
}
.btn-nav-cta:hover, .btn-primary-red:hover {
  background: var(--hrci-blue-hover) !important;
  box-shadow: 0 12px 28px rgba(29, 78, 216, 0.55) !important;
  transform: translateY(-2px) !important;
}

/* 2. Hero Headline, Underline & Badges */
.hero-badge-pill {
  background: #EFF6FF !important;
  border: 1px solid #BFDBFE !important;
  color: #1D4ED8 !important;
  box-shadow: 0 2px 8px rgba(29, 78, 216, 0.08) !important;
}
.gold-gradient-text {
  background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 55%, #1D4ED8 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  position: relative !important;
  display: inline-block !important;
}
/* Warm Gold Swoop Underline under Human Rights (NOT orange) */
.gold-gradient-text::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 0;
  width: 100%;
  height: 12px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 16' fill='none'%3E%3Cpath d='M3 11C60 3 140 3 197 11' stroke='%23F59E0B' stroke-width='4.5' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center bottom !important;
  background-size: 100% 100% !important;
  pointer-events: none;
}
.hero-gold-call-banner {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
  border: 1px solid #BFDBFE !important;
  box-shadow: 0 2px 8px rgba(29, 78, 216, 0.08) !important;
}
.hero-check-item .check-icon {
  color: var(--hrci-blue) !important;
}
.hero-trust-badges {
  background: #EFF6FF !important;
  border: 1px solid #DBEAFE !important;
  color: #1E3A8A !important;
}
.hero-trust-item svg {
  color: #2563EB !important;
}
.hero-composition-card {
  border: 1.5px solid #BFDBFE !important;
  box-shadow: 0 25px 60px -12px rgba(29, 78, 216, 0.14), 0 0 0 1px rgba(191, 219, 254, 0.5) !important;
}

/* 3. Stats Strip & Focus Areas */
.stat-card:nth-child(1) .stat-icon-box {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
}
.focus-title-block {
  background: var(--hrci-blue-gradient) !important;
  color: #FFFFFF !important;
  border-radius: 18px !important;
  box-shadow: 0 8px 22px rgba(29, 78, 216, 0.25) !important;
}
.focus-icon-circle {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
}
.focus-strip-item:hover {
  border-color: #BFDBFE !important;
  box-shadow: 0 12px 28px rgba(29, 78, 216, 0.1) !important;
}

/* 4. Lead Capture Form */
.lead-form-card {
  border: 2px solid #BFDBFE !important;
  box-shadow: 0 20px 50px rgba(29, 78, 216, 0.12) !important;
}
.lead-form-card::before {
  background: var(--hrci-blue-gradient) !important;
}
.form-card-header {
  background: #EFF6FF !important;
  border: 1px solid #DBEAFE !important;
}
.form-input-wrap input:focus, .form-input-wrap select:focus, .form-control:focus {
  border-color: var(--hrci-blue) !important;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
}
.btn-submit-lead {
  background: var(--hrci-blue-gradient) !important;
  box-shadow: var(--hrci-blue-glow) !important;
}
.btn-submit-lead:hover {
  background: var(--hrci-blue-hover) !important;
  box-shadow: 0 14px 30px rgba(29, 78, 216, 0.5) !important;
}

/* 5. Pricing Cards */
.card-lifetime-banner, .featured-plan {
  border: 2px solid var(--hrci-blue) !important;
  box-shadow: 0 16px 45px rgba(29, 78, 216, 0.16) !important;
}
.card-lifetime-banner::before {
  background: var(--hrci-blue-gradient) !important;
  box-shadow: 0 6px 16px rgba(29, 78, 216, 0.4) !important;
}
.price-red {
  color: var(--hrci-blue) !important;
}
.btn-plan-solid-red:hover {
  border-color: var(--hrci-blue) !important;
  color: var(--hrci-blue) !important;
  background: #EFF6FF !important;
}
.btn-plan-solid-purple {
  background: var(--hrci-blue-gradient) !important;
  box-shadow: var(--hrci-blue-glow) !important;
}
.btn-plan-solid-purple:hover {
  background: var(--hrci-blue-hover) !important;
  box-shadow: 0 10px 25px rgba(29, 78, 216, 0.5) !important;
}

/* 6. Simple Process Steps */
.step-card-bubble {
  background: #EFF6FF !important;
  color: var(--hrci-blue) !important;
  border: 1.5px solid #BFDBFE !important;
}
.banner-step-arrow {
  color: var(--hrci-blue) !important;
}

/* 7. FAQ Toggle & Icons */
.faq-icon-indicator {
  background: #EFF6FF !important;
  color: var(--hrci-blue) !important;
}
.faq-item.active {
  border-color: #BFDBFE !important;
  box-shadow: 0 8px 24px rgba(29, 78, 216, 0.08) !important;
}
.view-all-faq-link, .faq-header-right a {
  color: var(--hrci-blue) !important;
}

/* 8. Contact Secretariat Cards */
.contact-card-box:hover {
  border-color: #BFDBFE !important;
  box-shadow: 0 12px 28px rgba(29, 78, 216, 0.1) !important;
}
.contact-card-icon-circle {
  background: #EFF6FF !important;
  color: var(--hrci-blue) !important;
}

/* 9. Final CTA Band */
.final-cta-section {
  background: linear-gradient(135deg, #EFF6FF 0%, #F0FDF4 100%) !important;
  border: 1px solid #BFDBFE !important;
  box-shadow: 0 20px 45px rgba(29, 78, 216, 0.08) !important;
}
.cta-big-btn {
  background: var(--hrci-blue-gradient) !important;
  box-shadow: var(--hrci-blue-glow) !important;
}

/* 10. SIMPLE LANDING PAGE FOOTER (Matching user reference image) */
.simple-landing-footer {
  background: #0D0B1E !important;
  color: #94A3B8 !important;
  padding: 56px 0 40px 0 !important;
  border-top: 1px solid #1E1A38 !important;
}
.simple-footer-container {
  max-width: 1200px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
}
.simple-footer-grid {
  display: grid !important;
  grid-template-columns: 2.2fr 1fr 1.4fr !important;
  gap: 56px !important;
  align-items: start !important;
}
.simple-footer-brand-title {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  margin-bottom: 14px !important;
}
.simple-footer-logo {
  border-radius: 8px !important;
}
.simple-footer-brand-title h4 {
  color: #FFFFFF !important;
  font-size: 1.15rem !important;
  font-weight: 800 !important;
  margin: 0 !important;
  letter-spacing: -0.2px !important;
}
.simple-footer-desc {
  color: #94A3B8 !important;
  font-size: 0.86rem !important;
  line-height: 1.6 !important;
  max-width: 440px !important;
  margin-bottom: 20px !important;
}
.simple-footer-divider {
  height: 1px !important;
  background: rgba(255, 255, 255, 0.08) !important;
  margin-bottom: 18px !important;
  max-width: 440px !important;
}
.simple-footer-copy {
  color: #64748B !important;
  font-size: 0.8rem !important;
  margin: 0 !important;
}

.simple-footer-heading {
  color: #FFFFFF !important;
  font-size: 1rem !important;
  font-weight: 700 !important;
  margin-bottom: 18px !important;
}
.simple-footer-nav {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}
.simple-footer-nav a {
  color: #94A3B8 !important;
  font-size: 0.88rem !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}
.simple-footer-nav a:hover {
  color: #60A5FA !important;
  transform: translateX(3px) !important;
}

.simple-footer-contact-list {
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
  font-size: 0.88rem !important;
  line-height: 1.5 !important;
}
.simple-footer-contact-list p {
  margin: 0 !important;
  color: #94A3B8 !important;
}
.simple-footer-contact-list a {
  color: #94A3B8 !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}
.simple-footer-contact-list a:hover {
  color: #60A5FA !important;
}
.simple-footer-contact-list .contact-addr {
  color: #CBD5E1 !important;
}

@media (max-width: 900px) {
  .simple-footer-grid {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_theme)

print("Applied Royal Sapphire & Gold theme and minimal footer successfully!")

