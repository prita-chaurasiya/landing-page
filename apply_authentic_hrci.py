import re

refined_header_hero_html = '''<body id="top">

  <!-- ======================================================================
       TOP UTILITY STRIP (CLEAN, AUTHORITATIVE, SINGLE ROW)
       ====================================================================== -->
  <div class="top-utility-strip">
    <div class="wrap top-utility-inner">
      <div class="top-utility-left">
        <a href="tel:+919594441315" class="utility-link" title="Call Citizen Helpline">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1.02l-2.2 2.2z"/></svg>
          <span>Helpline: <strong>+91 95944 41315</strong></span>
        </a>
        <span class="utility-divider">•</span>
        <a href="mailto:info@hrcofindia.org" class="utility-link" title="Email Secretariat">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          <span>info@hrcofindia.org</span>
        </a>
      </div>
      <div class="top-utility-right">
        <span>Registered under Govt. of India MCA – Section 8 Company • Estd. 11 Jan 2013</span>
      </div>
    </div>
  </div>

  <!-- ======================================================================
       MODERN STICKY NAVBAR (LANDING PAGE ARCHITECTURE)
       ====================================================================== -->
  <nav class="modern-sticky-nav" id="mainNavbar">
    <div class="wrap nav-container">
      <!-- Left: Official Emblem & Bilingual Brand -->
      <a href="#top" class="brand-logo-wrap" title="Human Rights Council of India (HRCI)">
        <img src="assets/images/hrci-navbar-logo.svg" alt="HRCI Emblem" width="46" height="46">
        <div class="brand-logo-text">
          <span class="brand-name-en">HUMAN RIGHTS COUNCIL OF INDIA</span>
          <span class="brand-name-hi">भारतीय मानवाधिकार परिषद</span>
        </div>
      </a>

      <!-- Middle: Clean In-Page Anchor Links -->
      <div class="nav-links-menu" id="navbarList">
        <div class="drawer-header-bar">
          <div class="drawer-title-brand">
            <img src="assets/images/hrci-navbar-logo.svg" alt="HRCI Seal" class="drawer-logo-mini">
            <span>HRCI National Portal</span>
          </div>
          <button class="drawer-close-btn" id="drawerCloseBtn" aria-label="Close Menu">✕</button>
        </div>

        <a href="#top" class="nav-link-item active">Home</a>
        <a href="#about" class="nav-link-item">About</a>
        <a href="#focus-areas" class="nav-link-item">Focus Areas</a>
        <a href="#videos" class="nav-link-item">Videos</a>
        <a href="#testimonials" class="nav-link-item">Members Say</a>
        <a href="#plans" class="nav-link-item">Plans</a>
        <a href="#faq" class="nav-link-item">FAQ</a>
        <a href="#contact" class="nav-link-item">Contact</a>
      </div>

      <!-- Right: Helpline Desk + Glossy Red Pill CTA -->
      <div class="nav-actions-right">
        <div class="nav-helpline-box">
          <small>National Desk</small>
          <b><a href="tel:+919594441319">+91 95944 41319</a></b>
        </div>
        <a href="#membership-form" class="btn btn-primary-red btn-nav-cta">
          <span>Join Membership →</span>
        </a>
        <button class="nav-hamburger-toggle" id="navHamburger" aria-label="Toggle Navigation Menu">
          <span>☰</span>
        </button>
      </div>
    </div>
  </nav>

  <!-- ======================================================================
       HERO SECTION (ROYAL BLUE & GOLD LUXURY LANDING PAGE)
       ====================================================================== -->
  <section class="hero-section" id="home">
    <!-- Dynamic Atmospheric Effects: Particles, Light Rays & Layered Glows -->
    <canvas id="heroParticles" class="hero-particles-canvas"></canvas>
    <div class="hero-bg-overlay"></div>
    <div class="hero-light-rays"></div>
    <div class="hero-glow-circle glow-circle-gold-main" aria-hidden="true"></div>
    <div class="hero-glow-circle glow-circle-blue-ambient" aria-hidden="true"></div>
    <div class="hero-glow-circle glow-circle-trophy" aria-hidden="true"></div>

    <div class="container hero-container">
      <!-- Left Content Column -->
      <div class="hero-content">
        <div class="hero-badge-pill" data-aos="fade-down">
          <svg class="chakra-svg" width="16" height="16" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#FF9933" stroke-width="2.5"/><circle cx="12" cy="12" r="6" stroke="#0B3D91" stroke-width="1.5"/><circle cx="12" cy="12" r="2" fill="#0B3D91"/></svg>
          <span>National Human Rights Organization • Govt. Regd. Section 8</span>
        </div>

        <h1 class="hero-title" data-aos="fade-up">
          <span class="hero-title-white">Be a Voice for</span>
          <span class="gold-gradient-text">Human Rights</span>
        </h1>

        <!-- Yellow/Gold Sub-Banner Matching Brand -->
        <div class="hero-gold-call-banner" data-aos="fade-up" data-aos-delay="100">
          Join HRCI Membership
        </div>

        <p class="hero-tagline" data-aos="fade-up" data-aos-delay="200">
          For Justice, Equality, Social Welfare &amp; Nation Building across 28 States of India.
        </p>

        <!-- 3 Feature Checkpoints -->
        <div class="hero-checklist" data-aos="fade-up" data-aos-delay="300">
          <div class="hero-check-item">
            <span class="check-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg></span>
            <span>Be a Member</span>
          </div>
          <div class="hero-check-item">
            <span class="check-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg></span>
            <span>Support Society</span>
          </div>
          <div class="hero-check-item">
            <span class="check-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg></span>
            <span>Create Impact</span>
          </div>
        </div>

        <!-- High Conversion Action Buttons: Glossy Red, WhatsApp, Glass Video -->
        <div class="hero-cta-group" data-aos="fade-up" data-aos-delay="400">
          <a href="#membership-form" class="btn btn-primary-red">
            <span>Join HRCI Membership Now →</span>
          </a>

          <a href="https://wa.me/919594441319?text=Hello%20HRCI,%20I%20want%20to%20join%20HRCI%20Membership" target="_blank" rel="noopener" class="btn btn-whatsapp">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            <span>Chat on WhatsApp</span>
          </a>

          <a href="#videos" class="btn btn-hero-video" id="heroWatchVideoBtn">
            <span class="video-play-pulse"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
            <span>Watch Video</span>
          </a>
        </div>

        <!-- Trust Badges Strip Under Hero CTA -->
        <div class="hero-trust-badges" data-aos="fade-up" data-aos-delay="450">
          <div class="hero-trust-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
            <span>100% Verified NGO</span>
          </div>
          <span class="hero-trust-separator" aria-hidden="true">•</span>
          <div class="hero-trust-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1c0-2 4-3.1 6-3.1s6 1.1 6 3.1v1z"/></svg>
            <span>Instant Digital ID</span>
          </div>
          <span class="hero-trust-separator" aria-hidden="true">•</span>
          <div class="hero-trust-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
            <span>70,000+ Strong Network</span>
          </div>
        </div>
      </div>

      <!-- Right Visual Composition: Photorealistic 3D Golden Lady Justice, Indian Flag, Crowd & Peace Award -->
      <div class="hero-visual-wrapper" data-aos="zoom-in" data-aos-delay="200">
        <div class="hero-composition-card" title="3D Golden Lady Justice, Indian National Flag &amp; HRCI Global Peace Award">
          <div class="hero-art-backlight" aria-hidden="true"></div>
          <div class="hero-trophy-glow" aria-hidden="true"></div>

          <!-- Subtle Luxury Floating Badges in Royal Palette -->
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
          </div>

          <img src="assets/images/hero_statue_ultra_hd_seamless.png" alt="3D Golden Lady Justice, Indian National Flag, Cheering Crowd and HRCI Global Peace Award" class="hero-real-statue-img" width="1200" height="505" fetchpriority="high">
        </div>
      </div>
    </div>
  </section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_body = html.find('<body id="top">')
idx_stats = html.find('<!-- ======================================================================\n       SECTION 3: TRUST STATISTICS')

if idx_stats == -1:
    idx_stats = html.find('class="stats-strip-section"')
    idx_stats = html.rfind('<!--', 0, idx_stats)

html = html[:idx_body] + refined_header_hero_html + '\n\n  ' + html[idx_stats:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully with authentic HRCI Royal Blue + Gold + Modern Landing Page layout!")
