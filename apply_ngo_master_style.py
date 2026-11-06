# apply_ngo_master_style.py
# Applies the clean, modern SaaS landing page style inspired by https://ngowebsite.in/ngo-software

css_addon = """
/* ==========================================================================
   NGO-SOFTWARE THEME: HIGH-CONVERSION SAAS LANDING PAGE ARCHITECTURE
   Inspiration: https://ngowebsite.in/ngo-software
   Strict color discipline:
   - Base: Warm Luminous Ivory (#FFFBF7) + Crisp Pure White (#FFFFFF)
   - Typography: Deep Charcoal Slate (#0F172A) + Slate Body (#475569)
   - Primary Accent & CTAs: Radiant Sunset Coral (#F4683A -> #FF8A50)
   - Secondary Accents: Warm Amber (#F59E0B) + Emerald (#10B981) + Soft Lavender (#EDE9FE)
   - Borders: Subtle #F1E9DE & #E2E8F0
   - Modern Squircles: 14px-18px for icons, 20px-24px for cards
   ========================================================================== */

:root {
  --ng-peach-bg: #FFF9F5;
  --ng-ivory: #FFFBF7;
  --ng-white: #FFFFFF;
  --ng-slate-dark: #0F172A;
  --ng-slate-body: #475569;
  --ng-slate-muted: #64748B;
  --ng-border: #F1E9DE;
  --ng-border-card: #E2E8F0;
  
  /* Sunset Coral Accent (from ngowebsite.in) */
  --ng-coral: #F4683A;
  --ng-coral-light: #FF8A50;
  --ng-coral-glow: 0 10px 25px -4px rgba(244, 104, 58, 0.4);
  --ng-coral-gradient: linear-gradient(135deg, #F4683A 0%, #FF8A50 100%);
  
  /* Soft Lavender Accent */
  --ng-lavender-bg: #EDE9FE;
  --ng-lavender-text: #6D28D9;
  --ng-lavender-border: #DDD6FE;
  
  /* Card Shadows */
  --ng-card-shadow: 0 10px 30px rgba(15, 23, 42, 0.05), 0 1px 3px rgba(15, 23, 42, 0.02);
  --ng-card-hover-shadow: 0 20px 45px rgba(244, 104, 58, 0.12), 0 4px 10px rgba(15, 23, 42, 0.04);
}

/* 1. Global Page Background & Body Typography */
body {
  background-color: var(--ng-ivory) !important;
  color: var(--ng-slate-body) !important;
  font-family: 'Poppins', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  overflow-x: hidden !important;
}

h1, h2, h3, h4, h5, h6 {
  color: var(--ng-slate-dark) !important;
  font-family: 'Poppins', sans-serif !important;
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

/* 3. Sticky Modern Navbar */
.modern-sticky-nav {
  background: rgba(255, 255, 255, 0.95) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
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
  font-size: 0.92rem !important;
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
  box-shadow: 0 6px 18px rgba(244, 104, 58, 0.35) !important;
  border: none !important;
  font-weight: 700 !important;
  letter-spacing: 0.2px !important;
}
.btn-nav-cta:hover, .btn-primary-red:hover {
  background: linear-gradient(135deg, #E05325 0%, #F4683A 100%) !important;
  box-shadow: 0 8px 24px rgba(244, 104, 58, 0.5) !important;
  transform: translateY(-2px) !important;
}

/* 4. HERO SECTION - Luminous SaaS Atmosphere */
.hero-section {
  background: 
    radial-gradient(circle at 12% 18%, rgba(254, 243, 199, 0.6) 0%, transparent 45%),
    radial-gradient(circle at 88% 15%, rgba(237, 233, 254, 0.75) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 100%, rgba(255, 237, 213, 0.35) 0%, transparent 55%),
    linear-gradient(180deg, #FFF9F5 0%, #FFFFFF 100%) !important;
  color: var(--ng-slate-dark) !important;
  border-bottom: 1px solid var(--ng-border) !important;
  padding: 48px 0 64px 0 !important;
  position: relative !important;
}
.hero-particles-canvas {
  opacity: 0.25 !important;
}
.hero-bg-overlay, .hero-light-rays, .glow-circle-gold-main, .glow-circle-blue-ambient, .glow-circle-trophy {
  display: none !important;
}

/* Hero Badge Pill */
.hero-badge-pill {
  background: var(--ng-lavender-bg) !important;
  border: 1px solid var(--ng-lavender-border) !important;
  color: var(--ng-lavender-text) !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  border-radius: 9999px !important;
  padding: 6px 16px !important;
  box-shadow: 0 2px 8px rgba(109, 40, 217, 0.08) !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
}

/* Hero Title & Curved Underline (Exactly like ngowebsite.in) */
.hero-title {
  color: var(--ng-slate-dark) !important;
  font-weight: 900 !important;
  font-size: clamp(38px, 5.2vw, 62px) !important;
  line-height: 1.12 !important;
  letter-spacing: -0.8px !important;
  margin: 16px 0 12px 0 !important;
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
.gold-gradient-text::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 0;
  width: 100%;
  height: 12px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 16' fill='none'%3E%3Cpath d='M3 11C60 3 140 3 197 11' stroke='%23F4683A' stroke-width='4.5' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center bottom;
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
  margin-bottom: 12px !important;
}

/* Tagline */
.hero-tagline {
  color: var(--ng-slate-body) !important;
  font-size: 1.12rem !important;
  line-height: 1.65 !important;
  max-width: 580px !important;
}

/* Checklist Pills */
.hero-checklist {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 10px !important;
  margin: 18px 0 !important;
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
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
}
.hero-check-item .check-icon {
  color: var(--ng-coral) !important;
}

/* Hero CTA Group */
.hero-cta-group {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 14px !important;
  margin-top: 8px !important;
  align-items: center !important;
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
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
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
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
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
  display: inline-flex !important;
  align-items: center !important;
  gap: 12px !important;
  margin-top: 18px !important;
}
.hero-trust-item svg {
  color: var(--ng-coral) !important;
}

/* Hero Artwork Composition (Right Side) */
.hero-composition-card {
  background: 
    radial-gradient(circle at 60% 40%, rgba(254, 215, 170, 0.55) 0%, transparent 65%),
    linear-gradient(135deg, #FFFDFB 0%, #FFF5EC 100%) !important;
  border: 1.5px solid #FED7AA !important;
  border-radius: 26px !important;
  padding: 14px !important;
  box-shadow: 0 25px 60px -12px rgba(244, 104, 58, 0.16), 0 0 0 1px rgba(254, 215, 170, 0.4) !important;
  position: relative !important;
}
.hero-real-statue-img {
  border-radius: 20px !important;
  display: block !important;
  width: 100% !important;
  height: auto !important;
}
.hero-float-badge {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.1) !important;
  color: var(--ng-slate-dark) !important;
  border-radius: 16px !important;
  padding: 10px 14px !important;
  position: absolute !important;
  z-index: 5 !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
}
.float-badge-left {
  top: 14px !important;
  left: 14px !important;
}
.float-badge-right {
  bottom: 14px !important;
  right: 14px !important;
}
.hero-float-badge strong {
  display: block !important;
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
  font-size: 0.84rem !important;
}
.hero-float-badge small {
  display: block !important;
  color: var(--ng-slate-muted) !important;
  font-weight: 600 !important;
  font-size: 0.72rem !important;
}

/* 5. STATS STRIP SECTION */
.stats-strip-section {
  background: #FFFFFF !important;
  padding: 34px 0 !important;
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
  padding: 10px !important;
}
.stat-card:nth-child(2) .stat-icon-box {
  background: #FEF3C7 !important;
  color: #D97706 !important;
  border-radius: 14px !important;
  padding: 10px !important;
}
.stat-card:nth-child(3) .stat-icon-box {
  background: #E0F2FE !important;
  color: #0284C7 !important;
  border-radius: 14px !important;
  padding: 10px !important;
}
.stat-card:nth-child(4) .stat-icon-box {
  background: #EDE9FE !important;
  color: #7C3AED !important;
  border-radius: 14px !important;
  padding: 10px !important;
}
.stat-card:nth-child(5) .stat-icon-box {
  background: #FFE4E6 !important;
  color: #E11D48 !important;
  border-radius: 14px !important;
  padding: 10px !important;
}
.stat-number {
  color: var(--ng-slate-dark) !important;
  font-weight: 900 !important;
  font-size: 1.85rem !important;
}
.stat-label {
  color: var(--ng-slate-body) !important;
  font-weight: 600 !important;
  font-size: 0.84rem !important;
}

/* 6. FOCUS AREAS SECTION */
.focus-strip-section {
  background: var(--ng-ivory) !important;
  padding: 60px 0 !important;
}
.focus-strip-item {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 22px 16px !important;
  transition: all 0.25s ease !important;
}
.focus-strip-item:hover {
  transform: translateY(-5px) !important;
  border-color: #FED7AA !important;
  box-shadow: var(--ng-card-hover-shadow) !important;
}
.focus-icon-circle {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border-radius: 16px !important;
  width: 52px !important;
  height: 52px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 12px auto !important;
}
.focus-item-name {
  color: var(--ng-slate-dark) !important;
  font-weight: 700 !important;
  font-size: 0.92rem !important;
}

/* 7. MAIN TWO-COLUMN SECTION & CARDS */
.main-two-col-section {
  background: #FFFFFF !important;
  padding: 60px 0 !important;
}
.about-card-box, .why-join-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 28px !important;
}
.about-card-box h3, .why-join-box h3 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
  font-size: 1.3rem !important;
}
.why-check-item .why-check-icon {
  color: #16A34A !important;
}

/* 8. VIDEO GALLERY CARD - Modern SaaS presentation */
.video-gallery-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 26px !important;
  color: var(--ng-slate-dark) !important;
}
.video-title-wrap h3 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.video-header-sub {
  color: var(--ng-slate-muted) !important;
}
.video-card-item {
  background: #F8FAFC !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
}
.video-card-item:hover {
  transform: translateY(-3px) !important;
  border-color: #FED7AA !important;
  box-shadow: 0 10px 25px rgba(244, 104, 58, 0.1) !important;
}
.video-title {
  color: var(--ng-slate-dark) !important;
  font-weight: 700 !important;
}

/* 9. TESTIMONIALS BOX */
.testimonials-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 26px !important;
}
.testimonials-title-group h3 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.testimonial-card {
  background: #FFFBF7 !important;
  border: 1px solid #F1E9DE !important;
  border-radius: 18px !important;
  padding: 20px !important;
}
.testimonial-stars-svg svg {
  color: #F59E0B !important;
}
.testimonial-quote {
  color: var(--ng-slate-body) !important;
  font-style: italic !important;
}
.author-name {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}

/* 10. STICKY LEAD FORM CARD */
.lead-form-card {
  background: #FFFFFF !important;
  border: 2px solid #FED7AA !important;
  border-radius: 22px !important;
  box-shadow: 0 20px 50px rgba(244, 104, 58, 0.12) !important;
  padding: 28px 24px !important;
  position: relative !important;
}
.lead-form-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: var(--ng-coral-gradient);
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
}
.form-card-header {
  background: #FFF7ED !important;
  border: 1px solid #FED7AA !important;
  border-radius: 14px !important;
  padding: 12px 16px !important;
  margin-bottom: 18px !important;
}
.form-card-header h3 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.form-group label {
  color: #1E293B !important;
  font-weight: 700 !important;
  font-size: 0.84rem !important;
}
.form-input-wrap input, .form-input-wrap select, .form-control {
  background: #F8FAFC !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 12px !important;
  color: #0F172A !important;
  font-size: 0.88rem !important;
  padding: 11px 14px 11px 40px !important;
}
.form-input-wrap input:focus, .form-input-wrap select:focus, .form-control:focus {
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
  border: none !important;
  width: 100% !important;
  display: block !important;
  text-align: center !important;
}
.btn-submit-lead:hover {
  background: linear-gradient(135deg, #E05325 0%, #F4683A 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 28px rgba(244, 104, 58, 0.5) !important;
}

/* 11. SIMPLE MEMBERSHIP PROCESS CARD */
.simple-process-banner-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 22px !important;
}
.process-banner-header h4 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}
.step-card-bubble {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border: 1.5px solid #FED7AA !important;
  border-radius: 14px !important;
}
.step-card-bubble.green-bubble {
  background: #DCFCE7 !important;
  color: #16A34A !important;
  border-color: #86EFAC !important;
}
.banner-step-arrow {
  color: var(--ng-coral) !important;
  font-weight: 800 !important;
}

/* 12. PRICING SECTION CARDS */
.pricing-cards-grid {
  gap: 16px !important;
}
.pricing-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  box-shadow: var(--ng-card-shadow) !important;
  padding: 24px 18px !important;
  transition: all 0.25s ease !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
}
.pricing-card:hover {
  transform: translateY(-5px) !important;
  box-shadow: var(--ng-card-hover-shadow) !important;
}
/* Middle Featured Card (Lifetime Membership) */
.card-lifetime-banner, .featured-plan {
  border: 2px solid var(--ng-coral) !important;
  box-shadow: 0 16px 45px rgba(244, 104, 58, 0.16) !important;
  position: relative !important;
  transform: scale(1.02) !important;
}
.card-lifetime-banner::before {
  content: 'MOST POPULAR';
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--ng-coral-gradient);
  color: #FFFFFF;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 4px 14px;
  border-radius: 9999px;
  box-shadow: 0 4px 12px rgba(244, 104, 58, 0.35);
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
.pricing-card .btn,
.btn-plan-solid-red,
.btn-plan-solid-purple,
.btn-plan-solid-gold {
  white-space: normal !important;
  word-break: normal !important;
  text-align: center !important;
  font-size: 0.82rem !important;
  padding: 11px 12px !important;
  line-height: 1.25 !important;
  width: 100% !important;
  box-sizing: border-box !important;
  border-radius: 9999px !important;
}
.btn-plan-solid-red {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04) !important;
  font-weight: 700 !important;
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
  font-weight: 800 !important;
}
.btn-plan-solid-purple:hover {
  background: linear-gradient(135deg, #E05325 0%, #F4683A 100%) !important;
  box-shadow: 0 10px 25px rgba(244, 104, 58, 0.5) !important;
}
.btn-plan-solid-gold {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
  font-weight: 700 !important;
}
.btn-plan-solid-gold:hover {
  border-color: #D97706 !important;
  color: #D97706 !important;
  background: #FEF3C7 !important;
}

/* 13. ACHIEVEMENTS STRIP */
.achievements-strip-section {
  background: var(--ng-ivory) !important;
  padding: 24px 0 !important;
}
.achieve-item {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03) !important;
  padding: 12px 18px !important;
}
.achieve-text {
  color: var(--ng-slate-dark) !important;
  font-weight: 700 !important;
}

/* 14. FAQ SECTION */
.faq-section {
  background: var(--ng-ivory) !important;
  padding: 64px 0 !important;
}
.faq-item {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03) !important;
  margin-bottom: 12px !important;
  overflow: hidden !important;
}
.faq-item.active {
  border-color: #FED7AA !important;
  box-shadow: 0 8px 24px rgba(244, 104, 58, 0.08) !important;
}
.faq-question-btn {
  color: var(--ng-slate-dark) !important;
  font-weight: 700 !important;
}
.faq-icon-indicator {
  background: #FFF1EC !important;
  color: var(--ng-coral) !important;
  border-radius: 50% !important;
}
.faq-answer-content {
  color: var(--ng-slate-body) !important;
}

/* 15. DEDICATED CONTACT DIRECTORY */
.contact-directory-section {
  background: #FFFFFF !important;
  padding: 68px 0 !important;
  border-top: 1px solid var(--ng-border) !important;
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
.contact-card-box h4 {
  color: var(--ng-slate-dark) !important;
  font-weight: 800 !important;
}

/* 16. FINAL CTA BAND */
.final-cta-section {
  background: linear-gradient(135deg, #FFF1EC 0%, #FEF3C7 100%) !important;
  border: 1px solid #FED7AA !important;
  border-radius: 24px !important;
  box-shadow: 0 20px 45px rgba(244, 104, 58, 0.1) !important;
  color: var(--ng-slate-dark) !important;
}
.final-cta-section h2 {
  color: var(--ng-slate-dark) !important;
  font-weight: 900 !important;
}
.cta-big-btn {
  background: var(--ng-coral-gradient) !important;
  color: #FFFFFF !important;
  border-radius: 9999px !important;
  box-shadow: var(--ng-coral-glow) !important;
  font-weight: 800 !important;
}

/* 17. FOOTER */
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

/* 18. FLOATING CALL & WHATSAPP BUTTONS (Matches ngowebsite.in) */
.floating-action-desk {
  position: fixed !important;
  bottom: 24px !important;
  right: 24px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  z-index: 999 !important;
}
.float-btn {
  width: 52px !important;
  height: 52px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18) !important;
  transition: all 0.25s ease !important;
}
.float-btn:hover {
  transform: scale(1.1) !important;
}
.float-call {
  background: #6366F1 !important;
  color: #FFFFFF !important;
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.45) !important;
}
.float-whatsapp {
  background: #25D366 !important;
  color: #FFFFFF !important;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.45) !important;
}
.float-scroll-top {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1px solid #E2E8F0 !important;
  font-weight: 800 !important;
  font-size: 1.1rem !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
}

/* 19. RESPONSIVE REFINEMENTS */
@media (max-width: 992px) {
  .pricing-cards-grid {
    grid-template-columns: 1fr !important;
  }
  .card-lifetime-banner, .featured-plan {
    transform: none !important;
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding: 32px 0 48px 0 !important;
  }
  .hero-title {
    font-size: 32px !important;
  }
  .hero-float-badge {
    padding: 6px 10px !important;
  }
  .hero-float-badge strong {
    font-size: 0.72rem !important;
  }
  .hero-float-badge small {
    font-size: 0.62rem !important;
  }
  .float-badge-left {
    top: 8px !important;
    left: 8px !important;
  }
  .float-badge-right {
    bottom: 8px !important;
    right: 8px !important;
  }
  .hero-cta-group {
    flex-direction: column !important;
    width: 100% !important;
  }
  .hero-cta-group .btn {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
  }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_addon)

print("Applied NGO-Software master style successfully to style.css!")

