# apply_restructure_css.py

css_restructure = """
/* ==========================================================================
   DEDICATED FULL-WIDTH SECTIONS ARCHITECTURE (MATCHING 5 USER SCREENSHOTS)
   - Every section is an independent, full-width, beautifully spaced section
   - Centered section headings with curved golden swoop underlines
   - 3D squircle icons and ultra-premium card elevations
   - Dedicated dark royal navy band for pricing plans (Screenshot 4)
   - Split 2-column FAQ layout with WhatsApp card on left (Screenshot 5)
   ========================================================================== */

/* Universal Section Headings */
.dedicated-section {
  padding: 88px 0 !important;
  position: relative !important;
}

.section-center-header {
  text-align: center !important;
  max-width: 820px !important;
  margin: 0 auto 52px auto !important;
}

.sec-eyebrow-pill {
  background: #EFF6FF !important;
  border: 1px solid #BFDBFE !important;
  color: #1D4ED8 !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
  padding: 6px 16px !important;
  border-radius: 9999px !important;
  display: inline-block !important;
  margin-bottom: 14px !important;
  box-shadow: 0 2px 8px rgba(29, 78, 216, 0.08) !important;
}

.sec-eyebrow-pill.pill-light {
  background: rgba(255, 255, 255, 0.12) !important;
  border-color: rgba(255, 255, 255, 0.25) !important;
  color: #93C5FD !important;
}

.sec-headline {
  color: #0F172A !important;
  font-weight: 900 !important;
  font-size: clamp(30px, 3.8vw, 46px) !important;
  line-height: 1.18 !important;
  letter-spacing: -0.6px !important;
  margin: 0 0 14px 0 !important;
}

.sec-headline.text-white {
  color: #FFFFFF !important;
}

.swoop-keyword {
  position: relative !important;
  display: inline-block !important;
}

.swoop-keyword::after {
  content: '' !important;
  position: absolute !important;
  bottom: -6px !important;
  left: 0 !important;
  width: 100% !important;
  height: 12px !important;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 16' fill='none'%3E%3Cpath d='M3 11C60 3 140 3 197 11' stroke='%23F59E0B' stroke-width='4.5' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center bottom !important;
  background-size: 100% 100% !important;
  pointer-events: none !important;
}

.swoop-keyword-gold {
  position: relative !important;
  display: inline-block !important;
  color: #F59E0B !important;
}

.swoop-keyword-gold::after {
  content: '' !important;
  position: absolute !important;
  bottom: -6px !important;
  left: 0 !important;
  width: 100% !important;
  height: 12px !important;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 16' fill='none'%3E%3Cpath d='M3 11C60 3 140 3 197 11' stroke='%23F59E0B' stroke-width='4.5' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center bottom !important;
  background-size: 100% 100% !important;
  pointer-events: none !important;
}

.sec-subheadline {
  color: #475569 !important;
  font-size: 1.05rem !important;
  line-height: 1.65 !important;
  max-width: 680px !important;
  margin: 0 auto !important;
}

.sec-subheadline.text-slate-300 {
  color: #CBD5E1 !important;
}

.sec-subheadline-left {
  color: #475569 !important;
  font-size: 1.02rem !important;
  line-height: 1.7 !important;
  margin-bottom: 24px !important;
}

/* 1. FOCUS AREAS SECTION (SCREENSHOT 2 STYLE) */
.sec-focus-areas {
  background: var(--ng-ivory) !important;
}

.focus-grid-modern {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 24px !important;
}

.focus-modern-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  padding: 26px 22px !important;
  display: flex !important;
  align-items: flex-start !important;
  gap: 18px !important;
  box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.05) !important;
  text-decoration: none !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.focus-modern-card:hover {
  transform: translateY(-5px) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 20px 45px -8px rgba(29, 78, 216, 0.12) !important;
}

.focus-modern-icon {
  width: 54px !important;
  height: 54px !important;
  border-radius: 16px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
}

.icon-blue { background: #EFF6FF !important; color: #1D4ED8 !important; }
.icon-amber { background: #FEF3C7 !important; color: #D97706 !important; }
.icon-emerald { background: #DCFCE7 !important; color: #16A34A !important; }
.icon-purple { background: #EDE9FE !important; color: #7C3AED !important; }
.icon-cyan { background: #E0F2FE !important; color: #0284C7 !important; }
.icon-rose { background: #FFE4E6 !important; color: #E11D48 !important; }

.focus-modern-content h4 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1.05rem !important;
  margin: 0 0 6px 0 !important;
}

.focus-modern-content p {
  color: #475569 !important;
  font-size: 0.88rem !important;
  line-height: 1.6 !important;
  margin: 0 !important;
}

/* 2. ABOUT & WHY JOIN SHOWCASE (SCREENSHOT 3 STYLE) */
.sec-about-why {
  background: #FFFFFF !important;
}

.about-why-showcase-grid {
  display: grid !important;
  grid-template-columns: 1fr 1.15fr !important;
  gap: 56px !important;
  align-items: center !important;
}

.about-visual-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 26px !important;
  padding: 20px !important;
  box-shadow: 0 15px 40px -5px rgba(15, 23, 42, 0.08) !important;
}

.about-image-wrapper {
  position: relative !important;
  border-radius: 20px !important;
  overflow: hidden !important;
}

.about-main-photo {
  width: 100% !important;
  height: 320px !important;
  object-fit: cover !important;
  display: block !important;
}

.about-image-badge {
  position: absolute !important;
  bottom: 16px !important;
  left: 16px !important;
  background: rgba(255, 255, 255, 0.95) !important;
  backdrop-filter: blur(14px) !important;
  padding: 10px 16px !important;
  border-radius: 14px !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12) !important;
}

.about-image-badge strong {
  display: block !important;
  color: #0F172A !important;
  font-size: 0.84rem !important;
  font-weight: 800 !important;
}

.about-image-badge small {
  display: block !important;
  color: #64748B !important;
  font-size: 0.72rem !important;
}

.president-quote-card {
  background: #F8FAFC !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 18px !important;
  padding: 22px 24px !important;
  margin-top: 18px !important;
}

.president-quote-icon {
  font-size: 2rem !important;
  color: #1D4ED8 !important;
  line-height: 1 !important;
  margin-bottom: 6px !important;
}

.president-quote-text {
  color: #334155 !important;
  font-size: 0.94rem !important;
  font-style: italic !important;
  line-height: 1.65 !important;
  margin-bottom: 12px !important;
}

.president-author strong {
  display: block !important;
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 0.9rem !important;
}

.president-author span {
  display: block !important;
  color: #64748B !important;
  font-size: 0.78rem !important;
}

.benefits-two-col-grid {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 18px 24px !important;
  margin: 28px 0 32px 0 !important;
}

.benefit-item {
  display: flex !important;
  align-items: flex-start !important;
  gap: 12px !important;
}

.benefit-check-icon {
  background: #DCFCE7 !important;
  color: #16A34A !important;
  width: 24px !important;
  height: 24px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-weight: 800 !important;
  font-size: 0.8rem !important;
  flex-shrink: 0 !important;
  margin-top: 2px !important;
}

.benefit-text strong {
  display: block !important;
  color: #0F172A !important;
  font-weight: 700 !important;
  font-size: 0.92rem !important;
  margin-bottom: 2px !important;
}

.benefit-text p {
  color: #475569 !important;
  font-size: 0.82rem !important;
  line-height: 1.5 !important;
  margin: 0 !important;
}

.about-action-btns {
  display: flex !important;
  gap: 16px !important;
  flex-wrap: wrap !important;
}

/* 3. VIDEOS & TESTIMONIALS SECTION */
.sec-videos-testimonials {
  background: var(--ng-ivory) !important;
}

.video-cards-grid-full {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 20px !important;
}

.testimonials-full-wrapper {
  margin-top: 64px !important;
}

.testimonials-header-center {
  text-align: center !important;
  margin-bottom: 32px !important;
}

.testimonials-header-center h3 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1.6rem !important;
}

.testimonials-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 24px !important;
}

.testimonial-card-premium {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  padding: 28px !important;
  box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.05) !important;
  transition: all 0.3s ease !important;
}

.testimonial-card-premium:hover {
  transform: translateY(-5px) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 20px 45px -8px rgba(29, 78, 216, 0.1) !important;
}

/* 4. DEDICATED DARK BAND FOR PRICING (SCREENSHOT 4 STYLE) */
.sec-pricing-plans-band {
  background: linear-gradient(180deg, #09132B 0%, #0D1C44 100%) !important;
  color: #FFFFFF !important;
  padding: 96px 0 !important;
}

.pricing-cards-grid-spacious {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 28px !important;
  max-width: 1200px !important;
  margin: 0 auto !important;
  align-items: stretch !important;
}

.pricing-card-luxury {
  background: #FFFFFF !important;
  border: 1px solid rgba(226, 232, 240, 0.9) !important;
  border-radius: 26px !important;
  padding: 38px 28px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.28) !important;
  color: #0F172A !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  position: relative !important;
}

.pricing-card-luxury:hover {
  transform: translateY(-6px) !important;
  box-shadow: 0 28px 65px rgba(0, 0, 0, 0.35) !important;
}

.featured-luxury-plan {
  border: 2.5px solid #2563EB !important;
  transform: scale(1.03) !important;
  z-index: 5 !important;
  box-shadow: 0 25px 65px rgba(29, 78, 216, 0.35) !important;
}

.featured-luxury-plan:hover {
  transform: scale(1.04) translateY(-4px) !important;
}

.popular-ribbon {
  position: absolute !important;
  top: -14px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%) !important;
  color: #FFFFFF !important;
  font-size: 0.74rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.06em !important;
  padding: 5px 18px !important;
  border-radius: 9999px !important;
  box-shadow: 0 6px 18px rgba(29, 78, 216, 0.45) !important;
  white-space: nowrap !important;
}

.plan-tag-pill {
  font-size: 0.76rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.06em !important;
  padding: 5px 14px !important;
  border-radius: 9999px !important;
  display: inline-block !important;
  margin-bottom: 12px !important;
}

.tag-blue { background: #EFF6FF !important; color: #1D4ED8 !important; }
.tag-primary { background: #EFF6FF !important; color: #1D4ED8 !important; }
.tag-amber { background: #FEF3C7 !important; color: #D97706 !important; }

.plan-name {
  color: #0F172A !important;
  font-size: 1.4rem !important;
  font-weight: 800 !important;
  margin: 0 0 6px 0 !important;
}

.plan-desc-short {
  color: #64748B !important;
  font-size: 0.84rem !important;
  line-height: 1.5 !important;
  margin: 0 0 18px 0 !important;
}

.plan-price-block {
  margin-bottom: 20px !important;
}

.price-symbol {
  font-size: 1.6rem !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  vertical-align: top !important;
}

.price-number {
  font-size: 2.8rem !important;
  font-weight: 900 !important;
  color: #0F172A !important;
  letter-spacing: -1px !important;
  line-height: 1 !important;
}

.price-designation {
  font-size: 1.55rem !important;
  font-weight: 900 !important;
  color: #0F172A !important;
  display: block !important;
  margin-bottom: 4px !important;
}

.price-tenure {
  display: block !important;
  font-size: 0.82rem !important;
  color: #64748B !important;
  font-weight: 600 !important;
  margin-top: 4px !important;
}

.plan-divider {
  height: 1px !important;
  background: #E2E8F0 !important;
  margin-bottom: 20px !important;
}

.plan-checklist {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 0 28px 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
}

.plan-checklist li {
  color: #334155 !important;
  font-size: 0.88rem !important;
  line-height: 1.45 !important;
  display: flex !important;
  align-items: flex-start !important;
  gap: 8px !important;
}

.plan-check {
  color: #16A34A !important;
  font-weight: 800 !important;
  font-size: 1rem !important;
  flex-shrink: 0 !important;
}

.btn-plan-outline {
  display: block !important;
  width: 100% !important;
  text-align: center !important;
  padding: 13px 18px !important;
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #CBD5E1 !important;
  border-radius: 9999px !important;
  font-weight: 700 !important;
  font-size: 0.88rem !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}

.btn-plan-outline:hover {
  border-color: #1D4ED8 !important;
  color: #1D4ED8 !important;
  background: #EFF6FF !important;
}

.btn-plan-solid-primary {
  display: block !important;
  width: 100% !important;
  text-align: center !important;
  padding: 14px 18px !important;
  background: var(--hrci-blue-gradient) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 9999px !important;
  font-weight: 800 !important;
  font-size: 0.92rem !important;
  text-decoration: none !important;
  box-shadow: 0 8px 24px rgba(29, 78, 216, 0.4) !important;
  transition: all 0.2s ease !important;
}

.btn-plan-solid-primary:hover {
  background: var(--hrci-blue-hover) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 28px rgba(29, 78, 216, 0.55) !important;
}

/* 5. PROCESS & MEMBERSHIP ENROLLMENT FORM */
.sec-membership-enrollment {
  background: #FFFFFF !important;
}

.process-steps-row {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 16px !important;
  flex-wrap: wrap !important;
  margin-bottom: 56px !important;
}

.process-step-box {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  padding: 24px 20px !important;
  width: 220px !important;
  text-align: center !important;
  box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.05) !important;
  position: relative !important;
}

.step-badge-num {
  position: absolute !important;
  top: -12px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  background: #1D4ED8 !important;
  color: #FFFFFF !important;
  width: 26px !important;
  height: 26px !important;
  border-radius: 50% !important;
  font-weight: 800 !important;
  font-size: 0.78rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.step-badge-num.num-green {
  background: #16A34A !important;
}

.step-icon-wrap {
  color: #1D4ED8 !important;
  margin: 6px 0 10px 0 !important;
}

.step-icon-wrap.icon-green {
  color: #16A34A !important;
}

.process-step-box h4 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1rem !important;
  margin: 0 0 4px 0 !important;
}

.process-step-box p {
  color: #64748B !important;
  font-size: 0.8rem !important;
  margin: 0 !important;
}

.process-arrow-divider {
  color: #94A3B8 !important;
  font-size: 1.2rem !important;
  font-weight: 800 !important;
}

.lead-form-card-full {
  background: #FFFFFF !important;
  border: 2px solid #BFDBFE !important;
  border-radius: 26px !important;
  padding: 40px 36px !important;
  max-width: 820px !important;
  margin: 0 auto !important;
  box-shadow: 0 25px 60px -10px rgba(29, 78, 216, 0.16) !important;
}

.form-card-header-flex {
  display: flex !important;
  align-items: center !important;
  gap: 16px !important;
  padding-bottom: 24px !important;
  border-bottom: 1px solid #E2E8F0 !important;
  margin-bottom: 28px !important;
}

.header-badge-icon {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
  width: 52px !important;
  height: 52px !important;
  border-radius: 16px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
}

.form-card-header-flex h3 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1.45rem !important;
  margin: 0 0 4px 0 !important;
}

.form-card-header-flex p {
  color: #64748B !important;
  font-size: 0.9rem !important;
  margin: 0 !important;
}

.form-row-2col {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 20px !important;
}

.btn-submit-lead-full {
  width: 100% !important;
  padding: 16px 24px !important;
  background: var(--hrci-blue-gradient) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 9999px !important;
  font-size: 1.05rem !important;
  font-weight: 800 !important;
  box-shadow: var(--hrci-blue-glow) !important;
  cursor: pointer !important;
  transition: all 0.25s ease !important;
}

.btn-submit-lead-full:hover {
  background: var(--hrci-blue-hover) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 14px 30px rgba(29, 78, 216, 0.5) !important;
}

.form-trust-guarantee {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  flex-wrap: wrap !important;
  font-size: 0.82rem !important;
  color: #64748B !important;
  font-weight: 600 !important;
  margin-top: 18px !important;
}

.trust-dot {
  color: #CBD5E1 !important;
}

/* 6. FAQ TWO-COLUMN LAYOUT (SCREENSHOT 5 STYLE) */
.sec-faq-split {
  background: var(--ng-ivory) !important;
}

.faq-two-col-layout {
  display: grid !important;
  grid-template-columns: 1fr 1.6fr !important;
  gap: 56px !important;
  align-items: start !important;
}

.faq-support-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  padding: 28px !important;
  box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.05) !important;
  margin-top: 28px !important;
}

.faq-support-card h4 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1.15rem !important;
  margin: 0 0 8px 0 !important;
}

.faq-support-card p {
  color: #64748B !important;
  font-size: 0.9rem !important;
  line-height: 1.5 !important;
  margin-bottom: 20px !important;
}

.btn-faq-whatsapp {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  background: #25D366 !important;
  color: #FFFFFF !important;
  border-radius: 9999px !important;
  padding: 12px 22px !important;
  font-weight: 700 !important;
  font-size: 0.9rem !important;
  text-decoration: none !important;
  box-shadow: 0 6px 18px rgba(37, 211, 102, 0.35) !important;
}

.btn-faq-whatsapp:hover {
  background: #1EBE5D !important;
  transform: translateY(-2px) !important;
}

.faq-item-modern {
  background: #FFFFFF !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 18px !important;
  margin-bottom: 14px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03) !important;
  transition: all 0.25s ease !important;
}

.faq-item-modern.active {
  border-color: #BFDBFE !important;
  box-shadow: 0 8px 24px rgba(29, 78, 216, 0.08) !important;
}

.faq-modern-btn {
  width: 100% !important;
  padding: 20px 24px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: none !important;
  border: none !important;
  cursor: pointer !important;
  text-align: left !important;
}

.faq-q-text {
  color: #0F172A !important;
  font-weight: 700 !important;
  font-size: 1.02rem !important;
}

.faq-toggle-icon {
  width: 32px !important;
  height: 32px !important;
  border-radius: 50% !important;
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-weight: 800 !important;
  font-size: 1.1rem !important;
  flex-shrink: 0 !important;
}

.faq-item-modern.active .faq-toggle-icon {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
}

.faq-modern-answer {
  display: none;
  padding: 0 24px 22px 24px !important;
}

.faq-modern-answer p {
  color: #475569 !important;
  font-size: 0.94rem !important;
  line-height: 1.7 !important;
  margin: 0 !important;
}

/* 7. CONTACT SECRETARIAT 4-COL GRID */
.sec-contact-directory {
  background: #FFFFFF !important;
}

.contact-cards-grid-4col {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
}

.contact-card-premium {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 22px !important;
  padding: 26px 20px !important;
  box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.05) !important;
  transition: all 0.3s ease !important;
}

.contact-card-premium:hover {
  transform: translateY(-5px) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 18px 40px -6px rgba(29, 78, 216, 0.12) !important;
}

.contact-icon-bubble {
  font-size: 2rem !important;
  margin-bottom: 12px !important;
}

.contact-card-premium h4 {
  color: #0F172A !important;
  font-weight: 800 !important;
  font-size: 1.1rem !important;
  margin: 0 0 4px 0 !important;
}

.contact-meta {
  color: #64748B !important;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  margin-bottom: 12px !important;
}

.contact-detail {
  color: #334155 !important;
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  margin: 0 !important;
}

/* RESPONSIVE REFINEMENTS */
@media (max-width: 1024px) {
  .focus-grid-modern { grid-template-columns: repeat(2, 1fr) !important; }
  .video-cards-grid-full { grid-template-columns: repeat(2, 1fr) !important; }
  .testimonials-cards-grid { grid-template-columns: 1fr !important; }
  .pricing-cards-grid-spacious { grid-template-columns: 1fr !important; }
  .featured-luxury-plan { transform: none !important; }
  .contact-cards-grid-4col { grid-template-columns: repeat(2, 1fr) !important; }
  .faq-two-col-layout { grid-template-columns: 1fr !important; }
  .about-why-showcase-grid { grid-template-columns: 1fr !important; }
}

@media (max-width: 768px) {
  .focus-grid-modern { grid-template-columns: 1fr !important; }
  .video-cards-grid-full { grid-template-columns: 1fr !important; }
  .benefits-two-col-grid { grid-template-columns: 1fr !important; }
  .form-row-2col { grid-template-columns: 1fr !important; }
  .process-steps-row { flex-direction: column !important; }
  .process-arrow-divider { transform: rotate(90deg); margin: 6px 0; }
  .contact-cards-grid-4col { grid-template-columns: 1fr !important; }
  .lead-form-card-full { padding: 26px 20px !important; }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_restructure)

print("Appended dedicated sections styling to style.css successfully!")

