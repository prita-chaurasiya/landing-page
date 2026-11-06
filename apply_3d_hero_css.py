css = '''

/* ==========================================================================
   MASTER 3D ANIMATED HERO & 2-COLOR LUXURY DESIGN SYSTEM
   ========================================================================== */

/* 1. HERO ATMOSPHERE & BACKGROUND */
.hero-section {
  background: 
    radial-gradient(circle at 14% 18%, rgba(245, 158, 11, 0.14) 0%, transparent 42%),
    radial-gradient(circle at 86% 22%, rgba(29, 78, 216, 0.11) 0%, transparent 48%),
    radial-gradient(ellipse at 50% 100%, rgba(245, 158, 11, 0.08) 0%, transparent 60%),
    linear-gradient(180deg, #FBF9F5 0%, #FFFFFF 100%) !important;
  color: #0A1A3F !important;
  border-bottom: 1px solid #ECE7DE !important;
  padding: 56px 0 72px 0 !important;
  position: relative !important;
  overflow: hidden !important;
  perspective: 1200px !important;
}

.hero-particles-canvas {
  opacity: 0.65 !important;
  pointer-events: none !important;
}

/* 2. 3D FLOATING DECORATIVE GEOMETRIC SHAPES */
.hero-3d-floating-shape {
  position: absolute !important;
  pointer-events: none !important;
  z-index: 2 !important;
}

.shape-squircle-blue {
  top: 12% !important;
  left: 46% !important;
  width: 52px !important;
  height: 52px !important;
  border-radius: 18px !important;
  background: linear-gradient(135deg, rgba(29, 78, 216, 0.22) 0%, rgba(37, 99, 235, 0.08) 100%) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  border: 1.5px solid rgba(191, 219, 254, 0.6) !important;
  box-shadow: 0 12px 28px rgba(29, 78, 216, 0.14), inset 0 1px 1px #FFFFFF !important;
  transform: rotate(25deg) !important;
  animation: floatShape1 7s ease-in-out infinite alternate !important;
}

.shape-sphere-gold {
  top: 70% !important;
  left: 2.5% !important;
  width: 44px !important;
  height: 44px !important;
  border-radius: 50% !important;
  background: radial-gradient(circle at 35% 35%, #FDE68A 0%, #F59E0B 60%, #B45309 100%) !important;
  box-shadow: 0 14px 30px rgba(245, 158, 11, 0.32), inset -2px -2px 6px rgba(0, 0, 0, 0.2) !important;
  animation: floatShape2 6s ease-in-out infinite alternate !important;
}

.shape-ring-sapphire {
  top: 8% !important;
  right: 5% !important;
  width: 64px !important;
  height: 64px !important;
  border-radius: 50% !important;
  border: 4px solid rgba(29, 78, 216, 0.20) !important;
  box-shadow: 0 8px 25px rgba(29, 78, 216, 0.12) !important;
  animation: floatShape3 8s ease-in-out infinite alternate !important;
}

@keyframes floatShape1 {
  0% { transform: translateY(0px) rotate(25deg); }
  100% { transform: translateY(-16px) rotate(35deg); }
}

@keyframes floatShape2 {
  0% { transform: translateY(0px) scale(1); }
  100% { transform: translateY(-14px) scale(1.08); }
}

@keyframes floatShape3 {
  0% { transform: translateY(0px) scale(1); }
  100% { transform: translateY(18px) scale(0.95); }
}

/* 3. 3D ANIMATED TYPOGRAPHY FOR HEADLINE */
.hero-badge-pill {
  background: #EFF6FF !important;
  border: 1.5px solid #BFDBFE !important;
  color: #1D4ED8 !important;
  font-size: 0.78rem !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  border-radius: 9999px !important;
  padding: 6px 18px !important;
  box-shadow: 0 4px 14px rgba(29, 78, 216, 0.08) !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.hero-title {
  color: #0A1A3F !important;
  font-weight: 900 !important;
  font-size: clamp(42px, 5.5vw, 66px) !important;
  line-height: 1.1 !important;
  letter-spacing: -0.03em !important;
  margin: 16px 0 14px 0 !important;
}

.hero-title-white {
  color: #0A1A3F !important;
  display: block !important;
  /* Multi-layered 3D text physical extrusion */
  text-shadow: 
    0 1px 0 #CBD5E1,
    0 2px 0 #94A3B8,
    0 3px 1px rgba(10, 26, 63, 0.14),
    0 6px 14px rgba(10, 26, 63, 0.18),
    0 14px 30px rgba(10, 26, 63, 0.10) !important;
  position: relative !important;
}

.gold-gradient-text {
  display: inline-block !important;
  position: relative !important;
  /* 3D Metallic Imperial Gold Shimmer */
  background: linear-gradient(110deg, #92400E 0%, #D97706 18%, #F59E0B 35%, #FEF08A 50%, #F59E0B 65%, #D97706 82%, #92400E 100%) !important;
  background-size: 250% auto !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  animation: goldTextShimmerSweep 5s linear infinite !important;
  /* 3D Gold Drop Elevation */
  filter: drop-shadow(0 2px 3px rgba(180, 83, 9, 0.35)) drop-shadow(0 6px 18px rgba(245, 158, 11, 0.25)) !important;
}

@keyframes goldTextShimmerSweep {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}

.gold-gradient-text::after {
  content: '' !important;
  position: absolute !important;
  bottom: -8px !important;
  left: 0 !important;
  width: 100% !important;
  height: 14px !important;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 16' fill='none'%3E%3Cpath d='M3 11C60 3 140 3 197 11' stroke='%23F59E0B' stroke-width='5' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center bottom !important;
  background-size: 100% 100% !important;
  filter: drop-shadow(0 2px 6px rgba(245, 158, 11, 0.45)) !important;
  animation: swoopGlowPulse 3s ease-in-out infinite alternate !important;
}

@keyframes swoopGlowPulse {
  0% { transform: scaleY(0.95); opacity: 0.85; filter: drop-shadow(0 2px 4px rgba(245, 158, 11, 0.35)); }
  100% { transform: scaleY(1.05); opacity: 1; filter: drop-shadow(0 4px 10px rgba(245, 158, 11, 0.65)); }
}

/* Sub-banner Callout: Royal Navy & Gold Accent Ribbon */
.hero-gold-call-banner {
  background: linear-gradient(135deg, #FEF3C7 0%, #EFF6FF 100%) !important;
  color: #0A1A3F !important;
  border: 1.5px solid #FDE68A !important;
  font-weight: 800 !important;
  font-size: 0.92rem !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  border-radius: 12px !important;
  padding: 8px 18px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.15), inset 0 1px 0 #FFFFFF !important;
  margin-bottom: 14px !important;
  transition: transform 0.3s ease !important;
}

.hero-gold-call-banner:hover {
  transform: translateY(-2px) !important;
}

/* Tagline */
.hero-tagline {
  color: #475569 !important;
  font-size: 1.15rem !important;
  line-height: 1.65 !important;
  max-width: 580px !important;
}

/* 4. HERO BUTTONS: STRICTLY 2 COLORS (ROYAL SAPPHIRE & PURE GOLD) */
.hero-cta-group {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  flex-wrap: wrap !important;
  margin: 22px 0 !important;
}

/* Primary Button: 3D Royal Sapphire with Gold Light Sweep */
.hero-cta-group .btn-primary-red {
  background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 55%, #1E40AF 100%) !important;
  color: #FFFFFF !important;
  border: 1px solid rgba(255, 255, 255, 0.35) !important;
  box-shadow: 
    0 10px 25px -4px rgba(29, 78, 216, 0.45),
    0 4px 10px -2px rgba(29, 78, 216, 0.25),
    inset 0 1px 1px rgba(255, 255, 255, 0.45) !important;
  border-radius: 9999px !important;
  font-weight: 700 !important;
  padding: 14px 28px !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  position: relative !important;
  overflow: hidden !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.hero-cta-group .btn-primary-red::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: -100% !important;
  width: 60% !important;
  height: 100% !important;
  background: linear-gradient(90deg, transparent, rgba(254, 240, 138, 0.4), transparent) !important;
  transform: skewX(-25deg) !important;
  animation: btnGoldShineSweep 4s ease-in-out infinite !important;
}

@keyframes btnGoldShineSweep {
  0% { left: -100%; }
  35% { left: 140%; }
  100% { left: 140%; }
}

.hero-cta-group .btn-primary-red:hover {
  transform: translateY(-3px) scale(1.02) !important;
  box-shadow: 
    0 18px 35px -6px rgba(29, 78, 216, 0.5),
    0 6px 15px -2px rgba(245, 158, 11, 0.3) !important;
}

/* Secondary Button: Clean WhatsApp White Pill */
.hero-cta-group .btn-whatsapp {
  background: #FFFFFF !important;
  color: #0A1A3F !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 9999px !important;
  padding: 14px 26px !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(10, 26, 63, 0.08) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.hero-cta-group .btn-whatsapp:hover {
  transform: translateY(-3px) !important;
  border-color: #25D366 !important;
  box-shadow: 0 10px 25px -4px rgba(37, 211, 102, 0.25) !important;
}

/* Watch Video Button */
.hero-cta-group .btn-hero-video {
  background: #FFFFFF !important;
  color: #0A1A3F !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 9999px !important;
  padding: 14px 22px !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(10, 26, 63, 0.08) !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  transition: all 0.3s ease !important;
}

.hero-cta-group .btn-hero-video:hover {
  transform: translateY(-3px) !important;
  border-color: #F59E0B !important;
  box-shadow: 0 10px 25px -4px rgba(245, 158, 11, 0.25) !important;
}

/* 5. RIGHT 3D PERSPECTIVE SHOWCASE CARD */
.hero-visual-wrapper {
  perspective: 1200px !important;
  position: relative !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.hero-composition-card {
  position: relative !important;
  background: #FFFFFF !important;
  border-radius: 28px !important;
  border: 2px solid rgba(255, 255, 255, 0.95) !important;
  box-shadow: 
    0 30px 70px -15px rgba(10, 26, 63, 0.20),
    0 10px 30px -5px rgba(245, 158, 11, 0.12),
    inset 0 0 0 1px rgba(245, 158, 11, 0.25) !important;
  padding: 10px !important;
  transform-style: preserve-3d !important;
  animation: heroCardFloat3D 6s ease-in-out infinite alternate !important;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease !important;
  will-change: transform !important;
}

@keyframes heroCardFloat3D {
  0% {
    transform: translateY(0px) rotateY(-3deg) rotateX(2deg);
  }
  50% {
    transform: translateY(-10px) rotateY(-1deg) rotateX(1deg);
  }
  100% {
    transform: translateY(0px) rotateY(-3deg) rotateX(2deg);
  }
}

.hero-composition-card:hover {
  box-shadow: 
    0 35px 85px -15px rgba(10, 26, 63, 0.24),
    0 12px 35px -4px rgba(245, 158, 11, 0.18),
    inset 0 0 0 1.5px rgba(245, 158, 11, 0.4) !important;
}

.hero-real-statue-img {
  width: 100% !important;
  height: auto !important;
  display: block !important;
  border-radius: 20px !important;
}

/* 6. 4 3D FLOATING NOTIFICATION BADGES IN ROYAL PALETTE */
.hero-float-badge {
  position: absolute !important;
  background: rgba(255, 255, 255, 0.95) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(217, 119, 6, 0.25) !important;
  border-radius: 16px !important;
  padding: 10px 16px !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  box-shadow: 0 14px 30px -5px rgba(10, 26, 63, 0.16), 0 4px 10px rgba(0, 0, 0, 0.05) !important;
  z-index: 10 !important;
  pointer-events: auto !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.hero-float-badge strong {
  display: block !important;
  color: #0A1A3F !important;
  font-size: 0.86rem !important;
  font-weight: 800 !important;
  line-height: 1.2 !important;
}

.hero-float-badge small {
  display: block !important;
  color: #64748B !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
}

.hero-float-badge:hover {
  transform: scale(1.06) translateY(-4px) !important;
  box-shadow: 0 20px 40px -6px rgba(10, 26, 63, 0.22) !important;
}

.float-badge-tl {
  top: -18px !important;
  left: -20px !important;
  animation: floatBadgeSlow1 5s ease-in-out infinite alternate !important;
}

.float-badge-tr {
  top: 15% !important;
  right: -24px !important;
  animation: floatBadgeSlow2 5.5s ease-in-out infinite alternate !important;
}

.float-badge-bl {
  bottom: 12% !important;
  left: -24px !important;
  animation: floatBadgeSlow3 4.8s ease-in-out infinite alternate !important;
}

.float-badge-br {
  bottom: -18px !important;
  right: -16px !important;
  animation: floatBadgeSlow4 5.2s ease-in-out infinite alternate !important;
}

@keyframes floatBadgeSlow1 {
  0% { transform: translateY(0px) rotate(0deg); }
  100% { transform: translateY(-10px) rotate(-1deg); }
}

@keyframes floatBadgeSlow2 {
  0% { transform: translateY(0px) rotate(0deg); }
  100% { transform: translateY(-12px) rotate(1deg); }
}

@keyframes floatBadgeSlow3 {
  0% { transform: translateY(0px) rotate(0deg); }
  100% { transform: translateY(8px) rotate(-1deg); }
}

@keyframes floatBadgeSlow4 {
  0% { transform: translateY(0px) rotate(0deg); }
  100% { transform: translateY(10px) rotate(1deg); }
}

/* 7. 3D TEXT ELEVATION FOR ALL SECTION TITLES */
.sec-title-centered {
  color: #0A1A3F !important;
  font-weight: 900 !important;
  font-size: clamp(32px, 3.8vw, 48px) !important;
  letter-spacing: -0.025em !important;
  line-height: 1.18 !important;
  margin: 16px 0 12px 0 !important;
  text-shadow: 0 1px 0 #CBD5E1, 0 2px 0 #94A3B8, 0 4px 12px rgba(10, 26, 63, 0.12) !important;
}

.plans-title-white {
  color: #FFFFFF !important;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5), 0 8px 24px rgba(0, 0, 0, 0.35) !important;
}

.plans-gold-shimmer {
  background: linear-gradient(110deg, #D97706 0%, #F59E0B 25%, #FEF08A 50%, #F59E0B 75%, #D97706 100%) !important;
  background-size: 200% auto !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  animation: goldTextShimmerSweep 5s linear infinite !important;
  filter: drop-shadow(0 2px 6px rgba(245, 158, 11, 0.45)) !important;
}

/* 8. GLOBAL 3D CARD HOVER & ELEVATION */
.focus-card-horizontal,
.pricing-card-luxury,
.testimonial-card-white,
.contact-card-premium,
.lead-form-card-full,
.step-item-card {
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease !important;
}

.focus-card-horizontal:hover,
.testimonial-card-white:hover,
.step-item-card:hover {
  transform: translateY(-8px) scale(1.015) !important;
  box-shadow: 0 20px 40px -10px rgba(10, 26, 63, 0.12), 0 0 0 1px rgba(245, 158, 11, 0.25) !important;
}

.pricing-card-luxury:hover {
  transform: translateY(-10px) scale(1.02) !important;
  box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.25), 0 0 0 2px rgba(245, 158, 11, 0.4) !important;
}

@media (max-width: 992px) {
  .hero-3d-floating-shape { display: none !important; }
  .hero-float-badge { padding: 6px 10px !important; }
  .hero-float-badge strong { font-size: 0.72rem !important; }
  .hero-float-badge small { font-size: 0.62rem !important; }
  .float-badge-tl { top: -10px !important; left: -8px !important; }
  .float-badge-tr { top: 10% !important; right: -8px !important; }
  .float-badge-bl { bottom: 8% !important; left: -8px !important; }
  .float-badge-br { bottom: -10px !important; right: -8px !important; }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Master 3D Hero CSS appended successfully")

