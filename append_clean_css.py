css_additions = '''
/* ==========================================================================
   AUTHENTIC HRCI MODERN LANDING PAGE DESIGN SYSTEM
   ========================================================================== */

/* ---------- Top Utility Strip ---------- */
.top-utility-strip {
  background: #F8FAFC;
  border-bottom: 1px solid #E2E8F0;
  font-size: 13px;
  color: #475569;
}

.top-utility-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 42px;
}

.top-utility-left {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.utility-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #475569;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.utility-link:hover {
  color: #0B3D91;
}

.utility-link svg {
  color: #0F5BD8;
}

.utility-divider {
  color: #CBD5E1;
}

.top-utility-right {
  font-size: 12.5px;
  font-weight: 600;
  color: #0B3D91;
}

@media (max-width: 820px) {
  .top-utility-strip { display: none; }
}

/* ---------- Modern Sticky Navbar ---------- */
.modern-sticky-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid #E2E8F0;
  transition: all 0.25s ease;
}

.modern-sticky-nav.scrolled {
  box-shadow: 0 10px 30px rgba(11, 61, 145, 0.08);
  background: rgba(255, 255, 255, 0.98);
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 74px;
  gap: 20px;
}

.brand-logo-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.brand-logo-wrap img {
  width: 46px;
  height: 46px;
  object-fit: contain;
  flex-shrink: 0;
}

.brand-logo-text {
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}

.brand-name-en {
  font-size: 1.05rem;
  font-weight: 900;
  color: #991B1B;
  letter-spacing: -0.2px;
}

.brand-name-hi {
  font-size: 0.82rem;
  font-weight: 700;
  color: #0B3D91;
}

.nav-links-menu {
  display: flex;
  gap: 24px;
  font-size: 14.5px;
  font-weight: 600;
  color: #1F2937;
}

.nav-link-item {
  position: relative;
  padding: 6px 0;
  color: #1F2937;
  text-decoration: none;
  transition: color 0.2s ease;
}

.nav-link-item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 100%;
  bottom: 0;
  height: 2.5px;
  background: #F6B000;
  border-radius: 2px;
  transition: right 0.22s ease;
}

.nav-link-item:hover,
.nav-link-item.active {
  color: #0B3D91;
}

.nav-link-item:hover::after,
.nav-link-item.active::after {
  right: 0;
}

.nav-actions-right {
  display: flex;
  align-items: center;
  gap: 18px;
}

.nav-helpline-box {
  display: flex;
  flex-direction: column;
  line-height: 1.25;
  padding-left: 18px;
  border-left: 1px solid #E2E8F0;
}

.nav-helpline-box small {
  font-size: 11.5px;
  color: #64748B;
  font-weight: 500;
}

.nav-helpline-box b a {
  font-size: 14.5px;
  color: #0B3D91;
  text-decoration: none;
  font-weight: 800;
  transition: color 0.2s ease;
}

.nav-helpline-box b a:hover {
  color: #D32F2F;
}

.btn-nav-cta {
  min-height: 44px;
  padding: 0 22px;
  font-size: 14px;
  font-weight: 700;
  border-radius: 999px;
  white-space: nowrap;
}

.nav-hamburger-toggle {
  display: none;
  width: 42px;
  height: 42px;
  border: 0;
  border-radius: 10px;
  background: #EEF2F6;
  color: #0B3D91;
  cursor: pointer;
  font-size: 20px;
  align-items: center;
  justify-content: center;
}

/* Mobile Nav Drawer */
@media (max-width: 991px) {
  .nav-links-menu {
    position: fixed;
    top: 0;
    right: -320px;
    width: 300px;
    height: 100vh;
    background: #FFFFFF;
    flex-direction: column;
    padding: 24px;
    gap: 16px;
    box-shadow: -10px 0 30px rgba(0, 0, 0, 0.15);
    transition: right 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    z-index: 2000;
  }

  .nav-links-menu.open {
    right: 0;
  }

  .nav-helpline-box {
    display: none;
  }

  .nav-hamburger-toggle {
    display: flex;
  }
}

/* ---------- Hero Section Styles ---------- */
.hero-section {
  position: relative;
  background: #040E20;
  background: 
    radial-gradient(circle at 82% 38%, rgba(246, 176, 0, 0.2) 0%, transparent 52%),
    radial-gradient(circle at 18% 68%, rgba(15, 91, 216, 0.32) 0%, transparent 58%),
    radial-gradient(ellipse at 50% 0%, rgba(0, 168, 255, 0.16) 0%, transparent 68%),
    linear-gradient(180deg, #030C1C 0%, #06152F 45%, #051A3E 100%);
  color: #FFFFFF;
  padding: 44px 0 54px 0;
  min-height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  perspective: 1200px;
}

.hero-badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.22);
  padding: 6px 16px;
  border-radius: 999px;
  font-size: 0.76rem;
  font-weight: 700;
  color: #FFE066;
  width: fit-content;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.hero-title {
  font-size: clamp(48px, 5.2vw, 76px);
  font-weight: 900;
  line-height: 1.04;
  letter-spacing: -1.2px;
  margin: 8px 0;
}

.hero-title-white {
  display: block;
  color: #FFFFFF;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
}

.hero-title .gold-gradient-text {
  display: block;
  background: linear-gradient(135deg, #FFFFFF 0%, #FFF3B0 20%, #F6B000 60%, #E69500 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  text-shadow: none !important;
  filter: drop-shadow(0 4px 18px rgba(246, 176, 0, 0.5));
}

.hero-gold-call-banner {
  background: linear-gradient(135deg, #FFE066 0%, #F6B000 50%, #D97706 100%);
  color: #061A3A;
  font-size: clamp(1.15rem, 1.6vw, 1.35rem);
  font-weight: 800;
  padding: 7px 20px;
  border-radius: 8px;
  display: inline-block;
  box-shadow: 0 6px 20px rgba(246, 176, 0, 0.35);
  margin-top: 2px;
  margin-bottom: 4px;
}

.hero-tagline {
  font-size: 1rem;
  color: #E2E8F0;
  max-width: 580px;
  line-height: 1.55;
  margin: 0;
}

.hero-checklist {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 4px;
}

.hero-check-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  color: #FFFFFF;
}

.hero-check-item .check-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(246, 176, 0, 0.2);
  border: 1px solid rgba(246, 176, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFE066;
  font-size: 12px;
}

.hero-cta-group {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px;
  margin-top: 8px;
}

.btn-primary-red {
  background: linear-gradient(135deg, #FF1744 0%, #D50000 60%, #B71C1C 100%);
  color: #FFFFFF !important;
  font-weight: 700;
  font-size: 0.95rem;
  padding: 13px 26px;
  border-radius: 999px;
  box-shadow: 0 10px 25px rgba(213, 0, 0, 0.4);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.25s ease;
  border: 0;
  cursor: pointer;
}

.btn-primary-red:hover {
  transform: translateY(-2.5px);
  box-shadow: 0 16px 32px rgba(213, 0, 0, 0.5);
}

.btn-whatsapp {
  background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
  color: #FFFFFF !important;
  font-weight: 700;
  font-size: 0.95rem;
  padding: 13px 24px;
  border-radius: 999px;
  box-shadow: 0 10px 25px rgba(37, 211, 102, 0.35);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.25s ease;
  border: 0;
  cursor: pointer;
}

.btn-whatsapp:hover {
  transform: translateY(-2.5px);
  box-shadow: 0 16px 32px rgba(37, 211, 102, 0.45);
}

.btn-hero-video {
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid rgba(246, 176, 0, 0.6);
  color: #FFE066 !important;
  font-weight: 700;
  font-size: 0.92rem;
  padding: 12px 22px;
  border-radius: 999px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: all 0.25s ease;
  cursor: pointer;
}

.btn-hero-video:hover {
  background: rgba(246, 176, 0, 0.2);
  color: #FFFFFF !important;
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(246, 176, 0, 0.3);
}

.hero-trust-badges {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.78rem;
  color: #CBD5E1;
  background: rgba(255, 255, 255, 0.06);
  padding: 6px 16px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  width: fit-content;
  margin-top: 4px;
}

.hero-trust-item {
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.hero-trust-item svg {
  color: #FFE066;
}

.hero-trust-separator {
  color: rgba(255, 255, 255, 0.3);
}

/* Floating Luxury Glass Badges */
.hero-float-badge {
  position: absolute;
  z-index: 5;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 16px;
  padding: 10px 16px;
  box-shadow: 0 18px 40px rgba(4, 14, 36, 0.3);
  display: flex;
  align-items: center;
  gap: 12px;
  border: 1px solid rgba(246, 176, 0, 0.45);
  pointer-events: none;
}

.float-badge-left {
  top: 14%;
  left: 2%;
  animation: float-bob-1 5s ease-in-out infinite;
}

.float-badge-right {
  bottom: 12%;
  right: 4%;
  animation: float-bob-2 5.5s ease-in-out infinite;
}

@keyframes float-bob-1 {
  0%, 100% { transform: translateY(0px) rotate(-1deg); }
  50% { transform: translateY(-10px) rotate(1deg); }
}

@keyframes float-bob-2 {
  0%, 100% { transform: translateY(0px) rotate(1deg); }
  50% { transform: translateY(10px) rotate(-1deg); }
}

.badge-text-col strong {
  display: block;
  font-size: 0.82rem;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.2;
}

.badge-text-col small {
  display: block;
  font-size: 0.72rem;
  color: #64748B;
  font-weight: 600;
}
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += '\n' + css_additions

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Appended clean authentic HRCI design CSS!")
