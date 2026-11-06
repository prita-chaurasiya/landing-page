theme_css = '''
/* ==========================================================================
   NGO-SOFTWARE THEME: WARM LUMINOUS & HIGH-CONVERSION SAAS LANDING PAGE STYLE
   Inspiration: https://ngowebsite.in/ngo-software
   Palette: Luminous Ivory (#FFFBF7) + Deep Charcoal Slate (#0F172A) +
            Sunset Coral (#F4683A) + Soft Lavender (#EDE9FE) + Pure White (#FFFFFF)
   ========================================================================== */

:root {
  --ng-peach-bg: #FFF9F5;
  --ng-ivory: #FFFBF7;
  --ng-white: #FFFFFF;
  --ng-slate-dark: #0F172A;
  --ng-slate-body: #475569;
  --ng-slate-muted: #64748B;
  --ng-border: #F1E9DE;
  --ng-border-light: rgba(226, 232, 240, 0.8);
  
  /* Coral / Sunset Orange Accent */
  --ng-coral: #F4683A;
  --ng-coral-light: #FF8A50;
  --ng-coral-glow: 0 10px 25px -4px rgba(244, 104, 58, 0.4);
  --ng-coral-gradient: linear-gradient(135deg, #F4683A 0%, #FF8A50 100%);
  
  /* Soft Lavender Accent */
  --ng-lavender-bg: #EDE9FE;
  --ng-lavender-text: #6D28D9;
  --ng-lavender-border: #DDD6FE;
  
  /* Card Shadows */
  --ng-card-shadow: 0 12px 35px rgba(15, 23, 42, 0.05);
  --ng-card-hover-shadow: 0 18px 45px rgba(244, 104, 58, 0.1);
}

/* 1. Global Page Background & Text */
body {
  background-color: var(--ng-ivory) !important;
  color: var(--ng-slate-body) !important;
  font-family: 'Poppins', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}

/* 2. Top Utility Strip */
.top-utility-strip {
  background: #FAF5FF !important;
  border-bottom: 1px solid #F3E8FF !important;
  color: #64748B !important;
}
.top-utility-strip a {
  color: #6D28D9 !important;
}
.top-utility-strip a:hover {
  color: var(--ng-coral) !important;
}
.top-utility-right span {
  color: #64748B !important;
  font-weight: 500 !important;
}

/* 3. Modern Sticky Navbar */
.modern-sticky-nav {
  background: rgba(255, 255, 255, 0.94) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border-bottom: 1px solid var(--ng-border) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03) !important;
}
.brand-name-en {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.brand-name-hi {
  color: var(--ng-coral) !important;
  font-weight: 700 !important;
}
.nav-link-item {
  color: #334155 !important;
  font-weight: 600 !important;
  font-size: 0.9rem !important;
}
.nav-link-item:hover, .nav-link-item.active {
  color: var(--ng-coral) !important;
}
.nav-link-item::after {
  background: var(--ng-coral) !important;
}
.nav-helpline-box small {
  color: var(--ng-slate-muted) !important;
}
.nav-helpline-box b a {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.btn-nav-cta, .btn-primary-red {
  background: var(--ng-coral-gradient) !important;
  color: #FFFFFF !important;
  border-radius: 9999px !important;
  box-shadow: 0 4px 16px rgba(244, 104, 58, 0.35) !important;
  border: none !important;
  font-weight: 700 !important;
  letter-spacing: 0.2px !important;
}
.btn-nav-cta:hover, .btn-primary-red:hover {
  background: linear-gradient(135deg, #E05325 0%, #F4683A 100%) !important;
  box-shadow: 0 6px 22px rgba(244, 104, 58, 0.5) !important;
  transform: translateY(-2px) !important;
}

/* 4. HERO SECTION - Luminous Warm SaaS Atmosphere */
.hero-section {
  background: 
    radial-gradient(circle at 14% 22%, rgba(254, 243, 199, 0.55) 0%, transparent 40%),
    radial-gradient(circle at 86% 16%, rgba(237, 233, 254, 0.7) 0%, transparent 45%),
    radial-gradient(ellipse at 50% 100%, rgba(255, 237, 213, 0.35) 0%, transparent 55%),
    linear-gradient(180deg, #FFF9F5 0%, #FFFFFF 100%) !important;
  color: var(--ng-slate-dark) !important;
  border-bottom: 1px solid var(--ng-border) !important;
  padding: 48px 0 64px 0 !important;
}
.hero-particles-canvas {
  opacity: 0.35 !important;
}
.hero-bg-overlay, .hero-light-rays, .glow-circle-gold-main, .glow-circle-blue-ambient, .glow-circle-trophy {
  display: none !important;
}

/* Hero Badge Pill */
.hero-badge-pill {
  background: var(--ng-lavender-bg) !important;
  border: 1px solid var(--ng-lavender-border) !important;
  color: var(--ng-lavender-text) !important;
  font-size: 0.76rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  border-radius: 9999px !important;
  padding: 6px 16px !important;
  box-shadow: 0 2px 8px rgba(109, 40, 217, 0.08) !important;
}

/* Hero Title */
.hero-title {
  color: var(--ng-slate-dark) !important;
  font-weight: 900 !important;
  font-size: clamp(38px, 5.2vw, 62px) !important;
  line-height: 1.12 !important;
  letter-spacing: -0.8px !important;
}
.hero-title-white {
  color: var(--ng-slate-dark) !important;
}
.gold-gradient-text {
  background: linear-gradient(135deg, #F4683A 0%, #F59E0B 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  position: relative !important;
  display: inline-block !important;
}
/* Curved orange swoop underline under Human Rights */
.gold-gradient-text::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 0;
  width: 100%;
  height: 10px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 14' fill='none'%3E%3Cpath d='M2 10C58 3 142 3 198 10' stroke='%23F4683A' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center bottom;
  background-size: 100% 100%;
  pointer-events: none;
}

/* Sub-banner callout */
.hero-gold-call-banner {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border: 1px solid #FFD8CC !important;
  font-weight: 800 !important;
  border-radius: 12px !important;
  padding: 8px 18px !important;
  display: inline-block !important;
  box-shadow: 0 2px 8px rgba(244, 104, 58, 0.08) !important;
}

/* Tagline */
.hero-tagline {
  color: var(--ng-slate-body) !important;
  font-size: 1.1rem !important;
  line-height: 1.65 !important;
  max-width: 580px !important;
}

/* Checklist Pills */
.hero-checklist {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 10px !important;
}
.hero-check-item {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  color: #1E293B !important;
  font-weight: 600 !important;
  font-size: 0.82rem !important;
  padding: 6px 14px !important;
  border-radius: 9999px !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03) !important;
}
.hero-check-item .check-icon {
  color: var(--ng-coral) !important;
}

/* Hero CTA Group */
.hero-cta-group {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 14px !important;
  margin-top: 6px !important;
}
.hero-cta-group .btn-primary-red {
  padding: 14px 30px !important;
  font-size: 0.96rem !important;
  border-radius: 9999px !important;
  box-shadow: var(--ng-coral-glow) !important;
}
.hero-cta-group .btn-whatsapp {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
  border-radius: 9999px !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
  font-weight: 700 !important;
  padding: 13px 24px !important;
  font-size: 0.92rem !important;
}
.hero-cta-group .btn-whatsapp:hover {
  border-color: #25D366 !important;
  color: #16A34A !important;
  transform: translateY(-2px) !important;
}
.hero-cta-group .btn-hero-video {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
  border-radius: 9999px !important;
  font-weight: 700 !important;
  padding: 13px 22px !important;
  font-size: 0.92rem !important;
}
.hero-cta-group .btn-hero-video:hover {
  border-color: var(--ng-coral) !important;
  color: var(--ng-coral) !important;
  transform: translateY(-2px) !important;
}

/* Trust Badges Strip */
.hero-trust-badges {
  background: #FFF7ED !important;
  border: 1px solid #FFEDD5 !important;
  color: #334155 !important;
  border-radius: 9999px !important;
  padding: 8px 18px !important;
  font-size: 0.82rem !important;
  font-weight: 600 !important;
  box-shadow: 0 2px 6px rgba(244, 104, 58, 0.05) !important;
}
.hero-trust-item svg {
  color: var(--ng-coral) !important;
}

/* Hero Artwork Composition (Right Side) */
.hero-composition-card {
  background: 
    radial-gradient(circle at 60% 40%, rgba(254, 215, 170, 0.5) 0%, transparent 60%),
    linear-gradient(135deg, #FFFDFB 0%, #FFF5EC 100%) !important;
  border: 1.5px solid #FED7AA !important;
  border-radius: 24px !important;
  padding: 14px !important;
  box-shadow: 0 25px 60px -12px rgba(244, 104, 58, 0.15) !important;
}
.hero-real-statue-img {
  border-radius: 18px !important;
}
.hero-float-badge {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08) !important;
  color: var(--ng-slate-dark) !important;
  border-radius: 14px !important;
}
.float-badge-left {
  top: 14px !important;
  left: 14px !important;
}
.float-badge-right {
  bottom: 14px !important;
  right: 14px !important;
}

/* 5. STATS STRIP SECTION */
.stats-strip-section {
  background: #FFFFFF !important;
  padding: 32px 0 !important;
  border-bottom: 1px solid var(--ng-border) !important;
}
.stat-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.03) !important;
  padding: 20px 16px !important;
  transition: all 0.25s ease !important;
}
.stat-card:hover {
  transform: translateY(-4px) !important;
  border-color: #FED7AA !important;
  box-shadow: 0 14px 30px rgba(244, 104, 58, 0.08) !important;
}
.stat-card:nth-child(1) .stat-icon-box {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border-radius: 14px !important;
  padding: 8px !important;
}
.stat-card:nth-child(2) .stat-icon-box {
  background: #FEF3C7 !important;
  color: #D97706 !important;
  border-radius: 14px !important;
  padding: 8px !important;
}
.stat-card:nth-child(3) .stat-icon-box {
  background: #E0F2FE !important;
  color: #0284C7 !important;
  border-radius: 14px !important;
  padding: 8px !important;
}
.stat-card:nth-child(4) .stat-icon-box {
  background: #EDE9FE !important;
  color: #7C3AED !important;
  border-radius: 14px !important;
  padding: 8px !important;
}
.stat-card:nth-child(5) .stat-icon-box {
  background: #FFE4E6 !important;
  color: #E11D48 !important;
  border-radius: 14px !important;
  padding: 8px !important;
}
.stat-number {
  color: var(--ng-slate-dark) !important;
  font-weight: 900 !important;
  font-size: 1.8rem !important;
}
.stat-label {
  color: var(--ng-slate-body) !important;
  font-weight: 600 !important;
  font-size: 0.84rem !important;
}

/* 6. FOCUS AREAS SECTION */
.focus-strip-section {
  background: var(--ng-ivory) !important;
  padding: 64px 0 !important;
}
.focus-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 24px 20px !important;
  transition: all 0.25s ease !important;
}
.focus-card:hover {
  transform: translateY(-6px) !important;
  border-color: #FED7AA !important;
  box-shadow: var(--ng-card-hover-shadow) !important;
}
.focus-card-icon {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border-radius: 14px !important;
  width: 52px !important;
  height: 52px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin-bottom: 16px !important;
}
.focus-card-title {
  color: var(--ng-slate-dark) !important;
  font-weight: 700 !important;
}

/* 7. MAIN TWO-COLUMN SECTION & CARDS */
.main-two-col-section {
  background: #FFFFFF !important;
  padding: 64px 0 !important;
}
.about-card, .why-card, .video-card, .testimonial-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 28px !important;
}
.why-check-icon {
  color: #16A34A !important;
}

/* 8. STICKY LEAD FORM CARD */
.lead-form-card {
  background: #FFFFFF !important;
  border: 2px solid #FED7AA !important;
  border-radius: 20px !important;
  box-shadow: 0 20px 50px rgba(244, 104, 58, 0.12) !important;
  padding: 30px 26px !important;
}
.lead-form-header h3 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.form-group label {
  color: #1E293B !important;
  font-weight: 700 !important;
  font-size: 0.84rem !important;
}
.form-input-wrap input, .form-input-wrap select {
  background: #F8FAFC !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 12px !important;
  color: #0F172A !important;
  font-size: 0.88rem !important;
  padding: 10px 14px 10px 40px !important;
}
.form-input-wrap input:focus, .form-input-wrap select:focus {
  border-color: var(--ng-coral) !important;
  background: #FFFFFF !important;
  box-shadow: 0 0 0 3px rgba(244, 104, 58, 0.15) !important;
}
.btn-submit-lead {
  background: var(--ng-coral-gradient) !important;
  color: #FFFFFF !important;
  border-radius: 9999px !important;
  box-shadow: var(--ng-coral-glow) !important;
  font-weight: 800 !important;
  font-size: 0.98rem !important;
  padding: 14px 20px !important;
}
.btn-submit-lead:hover {
  background: linear-gradient(135deg, #E05325 0%, #F4683A 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 28px rgba(244, 104, 58, 0.5) !important;
}

/* 9. SIMPLE MEMBERSHIP PROCESS CARD */
.simple-process-banner-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
}
.process-step-circle {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border: 1.5px solid #FED7AA !important;
}

/* 10. PRICING SECTION CARDS */
.pricing-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 24px 18px !important;
  transition: all 0.25s ease !important;
}
.pricing-card:hover {
  transform: translateY(-6px) !important;
  box-shadow: var(--ng-card-hover-shadow) !important;
}
/* Lifetime Featured Card */
.card-lifetime-banner, .featured-plan {
  border: 2px solid var(--ng-coral) !important;
  box-shadow: 0 15px 40px rgba(244, 104, 58, 0.16) !important;
  position: relative !important;
}
.price-val {
  color: var(--ng-slate-dark) !important;
  font-weight: 900 !important;
}
.price-red {
  color: var(--ng-coral) !important;
}
.price-purple {
  color: var(--ng-slate-dark) !important;
}
.btn-plan-solid-red {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04) !important;
}
.btn-plan-solid-red:hover {
  border-color: var(--ng-coral) !important;
  color: var(--ng-coral) !important;
  background: #FFF7ED !important;
}
.btn-plan-solid-purple {
  background: var(--ng-coral-gradient) !important;
  color: #FFFFFF !important;
  box-shadow: var(--ng-coral-glow) !important;
  border: none !important;
}
.btn-plan-solid-purple:hover {
  background: linear-gradient(135deg, #E05325 0%, #F4683A 100%) !important;
  box-shadow: 0 10px 25px rgba(244, 104, 58, 0.5) !important;
}
.btn-plan-solid-gold {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
}
.btn-plan-solid-gold:hover {
  border-color: #D97706 !important;
  color: #D97706 !important;
  background: #FEF3C7 !important;
}

/* 11. FAQ SECTION */
.faq-section {
  background: var(--ng-ivory) !important;
  padding: 72px 0 !important;
}
.faq-item {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03) !important;
}
.faq-item.active {
  border-color: #FED7AA !important;
  box-shadow: 0 8px 24px rgba(244, 104, 58, 0.08) !important;
}
.faq-icon-toggle {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border-radius: 50% !important;
}

/* 12. DEDICATED CONTACT DIRECTORY */
.contact-directory-section {
  background: #FFFFFF !important;
  padding: 72px 0 !important;
}
.contact-card-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 24px !important;
}
.contact-card-box:hover {
  transform: translateY(-4px) !important;
  box-shadow: var(--ng-card-hover-shadow) !important;
  border-color: #FED7AA !important;
}
.contact-card-icon-circle {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border-radius: 16px !important;
}

/* 13. FOOTER */
.main-footer {
  background: #0F172A !important;
  color: #E2E8F0 !important;
  border-top: 1px solid #1E293B !important;
  padding: 64px 0 32px 0 !important;
}
.footer-logo-text strong {
  color: #FFFFFF !important;
}
.footer-links-col a:hover {
  color: var(--ng-coral) !important;
}

/* 14. FLOATING PHONE & WHATSAPP BUTTONS */
.floating-call-btn {
  position: fixed;
  bottom: 84px;
  right: 22px;
  width: 52px;
  height: 52px;
  background: #6366F1;
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.45);
  z-index: 99;
  transition: all 0.25s ease;
}
.floating-call-btn:hover {
  transform: scale(1.1);
  background: #4F46E5;
}
.floating-wa-btn {
  position: fixed;
  bottom: 22px;
  right: 22px;
  width: 52px;
  height: 52px;
  background: #25D366;
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.45);
  z-index: 99;
  transition: all 0.25s ease;
}
.floating-wa-btn:hover {
  transform: scale(1.1);
  background: #1EBE5D;
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + theme_css)

print('Appended ngowebsite style to style.css successfully!')

