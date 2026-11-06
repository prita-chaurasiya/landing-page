# apply_premium_cards_and_navbar.py

css_premium = """
/* ==========================================================================
   1. NAVBAR REFINEMENT: SINGLE HORIZONTAL LINE (NO WRAPPING)
   Fixes "Focus Areas" and "Members Say" wrapping to 2 lines
   ========================================================================== */
.modern-sticky-nav {
  padding: 10px 0 !important;
  background: rgba(255, 255, 255, 0.96) !important;
  backdrop-filter: blur(18px) !important;
  -webkit-backdrop-filter: blur(18px) !important;
  border-bottom: 1px solid rgba(226, 232, 240, 0.8) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03) !important;
  z-index: 1000 !important;
}

.nav-container {
  max-width: 1400px !important;
  width: 100% !important;
  padding: 0 24px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  flex-wrap: nowrap !important;
  gap: 16px !important;
}

.brand-logo-wrap {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  flex-shrink: 0 !important;
  white-space: nowrap !important;
  text-decoration: none !important;
}

.brand-name-en {
  font-size: 0.88rem !important;
  font-weight: 800 !important;
  letter-spacing: -0.2px !important;
  white-space: nowrap !important;
  color: #0F172A !important;
  line-height: 1.2 !important;
}

.brand-name-hi {
  font-size: 0.76rem !important;
  font-weight: 700 !important;
  white-space: nowrap !important;
  color: #1D4ED8 !important;
  line-height: 1.2 !important;
}

.nav-links-menu {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  flex-wrap: nowrap !important;
  white-space: nowrap !important;
  margin: 0 !important;
  padding: 0 !important;
}

.nav-link-item {
  color: #334155 !important;
  font-size: 0.86rem !important;
  font-weight: 600 !important;
  padding: 6px 8px !important;
  white-space: nowrap !important; /* CRITICAL: Never wrap into 2 lines */
  text-decoration: none !important;
  transition: all 0.2s ease !important;
  display: inline-block !important;
  line-height: 1.4 !important;
}

.nav-link-item:hover, .nav-link-item.active {
  color: #1D4ED8 !important;
}

.nav-actions-right {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  flex-shrink: 0 !important;
  white-space: nowrap !important;
}

.nav-helpline-box {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-end !important;
  white-space: nowrap !important;
  line-height: 1.2 !important;
}

.nav-helpline-box small {
  font-size: 0.72rem !important;
  color: #64748B !important;
  font-weight: 600 !important;
}

.nav-helpline-box b a {
  font-size: 0.86rem !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  text-decoration: none !important;
}

.btn-nav-cta {
  padding: 9px 20px !important;
  font-size: 0.84rem !important;
  font-weight: 700 !important;
  white-space: nowrap !important;
  border-radius: 9999px !important;
}


/* ==========================================================================
   2. HERO TRUST BADGES & TEXT VISIBILITY REFINEMENT
   Fixes "ye niche nhi dikh rha likha hua"
   ========================================================================== */
.hero-trust-badges {
  background: #FFFFFF !important;
  border: 1px solid #CBD5E1 !important;
  border-radius: 9999px !important;
  padding: 9px 20px !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08) !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 16px !important;
  margin-top: 22px !important;
}

.hero-trust-item {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  white-space: nowrap !important;
  color: #0F172A !important; /* CRITICAL: High-contrast crisp dark slate */
  font-weight: 700 !important;
  font-size: 0.86rem !important;
}

.hero-trust-item span {
  color: #0F172A !important; /* CRITICAL: Overrides any old faded rule */
  font-weight: 700 !important;
  font-size: 0.86rem !important;
}

.hero-trust-item svg {
  color: #1D4ED8 !important;
  width: 16px !important;
  height: 16px !important;
  flex-shrink: 0 !important;
}

.hero-trust-separator {
  background: #CBD5E1 !important;
  color: #94A3B8 !important;
  width: 1px !important;
  height: 14px !important;
  display: inline-block !important;
}

/* Also ensure hero-check-item, badge-pill, and sub-banner are crisp & clear */
.hero-badge-pill {
  background: #EFF6FF !important;
  border: 1px solid #BFDBFE !important;
  color: #1D4ED8 !important;
  font-weight: 700 !important;
  font-size: 0.78rem !important;
}
.hero-badge-pill span {
  color: #1D4ED8 !important;
  font-weight: 700 !important;
}
.hero-gold-call-banner {
  background: #EFF6FF !important;
  color: #1E3A8A !important;
  border: 1px solid #BFDBFE !important;
  font-weight: 800 !important;
}
.hero-tagline {
  color: #334155 !important;
  font-weight: 500 !important;
}
.hero-check-item {
  background: #FFFFFF !important;
  border: 1px solid #CBD5E1 !important;
  color: #0F172A !important;
  font-weight: 700 !important;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04) !important;
}
.hero-check-item span {
  color: #0F172A !important;
  font-weight: 700 !important;
}


/* ==========================================================================
   3. ULTRA-PREMIUM CARDS ACROSS THE ENTIRE PAGE
   "cards sbko premium"
   ========================================================================== */

/* Universal Premium Card Elevation */
.stat-card,
.focus-strip-item,
.about-card-box,
.why-join-box,
.video-gallery-card,
.testimonials-box,
.testimonial-card,
.lead-form-card,
.pricing-card,
.simple-process-banner-card,
.faq-item,
.contact-card-box,
.hero-composition-card {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

/* 3A. Key Stats Cards */
.stat-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.05), 0 2px 6px -1px rgba(15, 23, 42, 0.02) !important;
  padding: 24px 20px !important;
}
.stat-card:hover {
  transform: translateY(-6px) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 20px 40px -8px rgba(29, 78, 216, 0.12), 0 4px 12px rgba(15, 23, 42, 0.04) !important;
}
.stat-number {
  color: #0F172A !important;
  font-size: 2.1rem !important;
  font-weight: 900 !important;
  letter-spacing: -0.5px !important;
}
.stat-label {
  color: #334155 !important;
  font-weight: 600 !important;
  font-size: 0.88rem !important;
  margin-top: 4px !important;
}

/* 3B. Focus Areas Cards */
.focus-strip-item {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.04) !important;
  padding: 22px 16px !important;
}
.focus-strip-item:hover {
  transform: translateY(-5px) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 18px 36px -6px rgba(29, 78, 216, 0.1) !important;
}
.focus-item-name {
  color: #0F172A !important;
  font-weight: 700 !important;
  font-size: 0.94rem !important;
}

/* 3C. About & Why Join Cards */
.about-card-box, .why-join-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  box-shadow: 0 12px 35px -5px rgba(15, 23, 42, 0.05) !important;
  padding: 32px 28px !important;
}
.about-card-box:hover, .why-join-box:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 20px 45px -8px rgba(15, 23, 42, 0.09) !important;
  border-color: #CBD5E1 !important;
}
.about-card-box h3, .why-join-box h3 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1.35rem !important;
}
.about-card-desc p {
  color: #334155 !important;
  font-size: 0.95rem !important;
  line-height: 1.7 !important;
}
.why-check-item {
  color: #1E293B !important;
  font-weight: 600 !important;
  font-size: 0.92rem !important;
}

/* 3D. Watch Videos & Testimonials Cards */
.video-gallery-card, .testimonials-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  box-shadow: 0 12px 35px -5px rgba(15, 23, 42, 0.05) !important;
  padding: 28px !important;
}
.video-gallery-card:hover, .testimonials-box:hover {
  box-shadow: 0 20px 45px -8px rgba(15, 23, 42, 0.08) !important;
}
.video-card-item {
  border-radius: 18px !important;
  border: 1px solid #E2E8F0 !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04) !important;
}
.video-card-item:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 28px rgba(29, 78, 216, 0.12) !important;
  border-color: #BFDBFE !important;
}
.testimonial-card {
  background: #F8FAFC !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 18px !important;
  padding: 22px !important;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03) !important;
}
.testimonial-card:hover {
  background: #FFFFFF !important;
  border-color: #CBD5E1 !important;
  box-shadow: 0 10px 25px rgba(15, 23, 42, 0.06) !important;
}
.testimonial-quote {
  color: #334155 !important;
  font-size: 0.92rem !important;
  line-height: 1.6 !important;
}
.author-name {
  color: #0F172A !important;
  font-weight: 800 !important;
}

/* 3E. Lead Form Card */
.lead-form-card {
  background: #FFFFFF !important;
  border: 2px solid #BFDBFE !important;
  border-radius: 24px !important;
  box-shadow: 0 25px 60px -12px rgba(29, 78, 216, 0.16), 0 4px 16px rgba(15, 23, 42, 0.04) !important;
  padding: 30px 26px !important;
}
.lead-form-card:hover {
  box-shadow: 0 30px 70px -12px rgba(29, 78, 216, 0.22) !important;
}
.form-card-header {
  border-radius: 16px !important;
}
.form-input-wrap input, .form-input-wrap select, .form-control {
  border-radius: 14px !important;
  font-weight: 500 !important;
  color: #0F172A !important;
}

/* 3F. Membership Pricing Cards */
.pricing-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.06) !important;
  padding: 28px 22px !important;
}
.pricing-card:hover {
  transform: translateY(-6px) !important;
  box-shadow: 0 20px 45px -8px rgba(15, 23, 42, 0.1) !important;
}
.card-lifetime-banner, .featured-plan {
  border: 2.5px solid #2563EB !important;
  box-shadow: 0 20px 50px -10px rgba(29, 78, 216, 0.22) !important;
}
.card-lifetime-banner:hover {
  transform: scale(1.03) translateY(-4px) !important;
  box-shadow: 0 25px 60px -10px rgba(29, 78, 216, 0.3) !important;
}
.plan-features-list li {
  color: #334155 !important;
  font-weight: 500 !important;
  font-size: 0.9rem !important;
}

/* 3G. FAQ Cards */
.faq-item {
  background: #FFFFFF !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 18px !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03) !important;
}
.faq-item:hover {
  border-color: #BFDBFE !important;
  box-shadow: 0 8px 24px rgba(29, 78, 216, 0.08) !important;
}
.faq-question-btn {
  color: #0F172A !important;
  font-weight: 700 !important;
}
.faq-answer-content {
  color: #334155 !important;
  font-size: 0.94rem !important;
}

/* 3H. Contact Secretariat Cards */
.contact-card-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.05) !important;
  padding: 26px !important;
}
.contact-card-box:hover {
  transform: translateY(-5px) !important;
  box-shadow: 0 18px 40px -6px rgba(29, 78, 216, 0.12) !important;
  border-color: #BFDBFE !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_premium)

print("Applied navbar single line and premium cards styles successfully!")

