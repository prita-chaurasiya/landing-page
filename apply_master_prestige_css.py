css = '''

/* ==========================================================================
   MASTER PRESTIGE ELEVATION (SURPASSING NGOWEBSITE.IN IN LUXURY & CRAFT)
   ========================================================================== */

/* 1. JOST GEOMETRIC TYPOGRAPHY */
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  color: #475569 !important;
  -webkit-font-smoothing: antialiased !important;
}

h1, h2, h3, h4, h5, h6,
.hero-title,
.sec-headline,
.sec-title-centered,
.stat-number,
.pricing-amount,
.btn,
.brand-title {
  font-family: 'Jost', 'Poppins', -apple-system, sans-serif !important;
  letter-spacing: -0.028em !important;
}

/* 2. ORGANIC CONVEX CURVED BOTTOM HERO SECTION */
.hero-section {
  border-radius: 0 0 50% 50% / 0 0 70px 70px !important;
  background: 
    radial-gradient(ellipse 70% 65% at 5% 15%, rgba(245, 158, 11, 0.15) 0%, transparent 60%),
    radial-gradient(ellipse 65% 60% at 95% 10%, rgba(29, 78, 216, 0.11) 0%, transparent 55%),
    linear-gradient(180deg, #FBF9F5 0%, #FFFFFF 100%) !important;
  box-shadow: 0 20px 50px -15px rgba(10, 26, 63, 0.07) !important;
  position: relative !important;
  z-index: 5 !important;
  padding: 56px 0 84px 0 !important;
}

/* 3. FOCUS AREAS ACTION LINKS (MATCHING/BEATING NGOWEBSITE) */
.focus-modern-card {
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  padding: 30px 26px !important;
  box-shadow: 0 12px 35px -5px rgba(10, 26, 63, 0.05) !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  text-decoration: none !important;
}

.focus-modern-card:hover {
  transform: translateY(-8px) scale(1.015) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 25px 50px -10px rgba(29, 78, 216, 0.14), 0 0 0 1px rgba(245, 158, 11, 0.25) !important;
}

.focus-card-action {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  font-size: 0.9rem !important;
  font-weight: 700 !important;
  color: #1D4ED8 !important;
  margin-top: 18px !important;
  padding-top: 14px !important;
  border-top: 1px solid #F1F5F9 !important;
  transition: all 0.25s ease !important;
}

.focus-modern-card:hover .focus-card-action {
  color: #D97706 !important;
}

.action-arrow {
  display: inline-block !important;
  transition: transform 0.25s ease !important;
}

.focus-modern-card:hover .action-arrow {
  transform: translateX(5px) !important;
}

/* 4. PILL BUTTON AMBIENT SHADOWS */
.hero-cta-group .btn-primary-red,
.btn-primary-lg {
  min-height: 52px !important;
  padding: 0 32px !important;
  font-size: 1.02rem !important;
  box-shadow: 0 14px 30px rgba(29, 78, 216, 0.38) !important;
}

.hero-cta-group .btn-whatsapp,
.hero-cta-group .btn-hero-video {
  min-height: 52px !important;
  box-shadow: 0 8px 20px rgba(10, 26, 63, 0.06) !important;
}

/* 5. STATS SECTION REFINED SPACING */
.stats-strip-section {
  padding: 56px 0 68px 0 !important;
}

.stat-card-luxury {
  border-radius: 22px !important;
  box-shadow: 0 14px 35px -6px rgba(10, 26, 63, 0.06), 0 2px 6px rgba(0, 0, 0, 0.02) !important;
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Master Prestige CSS appended successfully!")

