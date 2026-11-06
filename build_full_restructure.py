# build_full_restructure.py
# Restructures the landing page so every section is full-width, dedicated and ultra-premium,
# matching the 5 uploaded reference screenshots.

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<section class="focus-strip-section" id="focus-areas">'
end_marker = '<section class="final-cta-section" data-aos="zoom-in">'

pos_start = text.find(start_marker)
pos_end = text.find(end_marker)

if pos_start == -1 or pos_end == -1:
    print("Error: Boundary markers not found!")
    exit(1)

new_sections_html = '''<!-- ======================================================================
       SECTION 3: FOCUS AREAS (FULL WIDTH, MATCHING SCREENSHOT 2)
       ====================================================================== -->
  <section class="dedicated-section sec-focus-areas" id="focus-areas">
    <div class="container">
      <div class="section-center-header" data-aos="fade-up">
        <div class="sec-eyebrow-pill">OUR FOCUS AREAS</div>
        <h2 class="sec-headline">Nationwide Protection. <span class="swoop-keyword">Every Human Rights Initiative.</span></h2>
        <p class="sec-subheadline">Comprehensive grassroots programs designed to protect constitutional rights, foster equality, and provide social support across 28 states.</p>
      </div>

      <div class="focus-grid-modern">
        <!-- Item 1 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="50">
          <div class="focus-modern-icon icon-blue">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a1 1 0 00-1 1v1.07A7.002 7.002 0 005.07 10H4a1 1 0 000 2h1.07A7.002 7.002 0 0011 17.93V21H9a1 1 0 000 2h6a1 1 0 000-2h-2v-3.07A7.002 7.002 0 0018.93 12H20a1 1 0 000-2h-1.07A7.002 7.002 0 0013 4.07V3a1 1 0 00-1-1zm-5 9a5 5 0 1110 0 5 5 0 01-10 0z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Legal Awareness &amp; Guidance</h4>
            <p>Free legal literacy camps, constitutional counseling, and grievance guidance for marginalized citizens.</p>
          </div>
        </a>

        <!-- Item 2 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="100">
          <div class="focus-modern-icon icon-amber">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3zm0 14.5l-7-3.82V17l7 3.82L19 17v-3.32l-7 3.82z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Training &amp; Skill Development</h4>
            <p>Youth leadership workshops, human rights advocate training, and vocational empowerment initiatives.</p>
          </div>
        </a>

        <!-- Item 3 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="150">
          <div class="focus-modern-icon icon-emerald">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Social Welfare Initiatives</h4>
            <p>Healthcare drives, women protection cells, anti-child labor enforcement, and community emergency aid.</p>
          </div>
        </a>

        <!-- Item 4 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="200">
          <div class="focus-modern-icon icon-purple">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V9h14v11z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Events &amp; Awareness Programs</h4>
            <p>National Human Rights Summits, public legal forums, and district-level social impact conventions.</p>
          </div>
        </a>

        <!-- Item 5 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="250">
          <div class="focus-modern-icon icon-cyan">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>National Membership Network</h4>
            <p>Connect with 70,000+ advocates, social workers, doctors, business leaders, and active change-makers.</p>
          </div>
        </a>

        <!-- Item 6 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="300">
          <div class="focus-modern-icon icon-rose">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1c0-2 4-3.1 6-3.1s6 1.1 6 3.1v1z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Official Membership ID Card</h4>
            <p>Instant digital ID card with QR code verification plus physical embossed PVC card delivered to your address.</p>
          </div>
        </a>
      </div>
    </div>
  </section>


  <!-- ======================================================================
       SECTION 4: ABOUT HRCI & WHY JOIN (SPLIT SHOWCASE, MATCHING SCREENSHOT 3)
       ====================================================================== -->
  <section class="dedicated-section sec-about-why" id="about">
    <div class="container">
      <div class="about-why-showcase-grid">
        <!-- Left Column: Leadership & Impact Showcase -->
        <div class="about-showcase-visual" data-aos="fade-right">
          <div class="about-visual-card">
            <div class="about-image-wrapper">
              <img src="assets/images/hands-plant.jpg" alt="Humanity, Dignity & Social Welfare" class="about-main-photo" loading="lazy">
              <div class="about-image-badge">
                <span class="badge-icon">🏛️</span>
                <div class="badge-content">
                  <strong>MCA Section 8 Company</strong>
                  <small>Registered under Govt. of India</small>
                </div>
              </div>
            </div>

            <div class="president-quote-card">
              <div class="president-quote-icon">❝</div>
              <p class="president-quote-text">
                "Our sacred mission is to empower every Indian citizen with legal awareness, constitutional protection, and equal opportunity."
              </p>
              <div class="president-author">
                <strong>Hon. Shri Haji S. Shaikh</strong>
                <span>Founder &amp; National President, HRCI</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Why Join HRCI & Value Checklist -->
        <div class="about-showcase-content" data-aos="fade-left">
          <div class="sec-eyebrow-pill">ABOUT HRCI &amp; WHY JOIN</div>
          <h2 class="sec-headline">A Dedicated National Voice <span class="swoop-keyword">For Every Citizen.</span></h2>
          <p class="sec-subheadline-left">
            <strong>Human Rights Council of India (HRCI) / भारतीय मानवाधिकार परिषद</strong> is a registered, non-political, and secular NGO established on <strong>11 January 2013</strong>. We work nationwide for the protection of constitutional rights, legal education, healthcare, and social welfare.
          </p>

          <div class="benefits-two-col-grid" id="why-join">
            <div class="benefit-item">
              <span class="benefit-check-icon">✓</span>
              <div class="benefit-text">
                <strong>Official Membership ID Card</strong>
                <p>Digital QR-verified card + physical PVC card delivered to you.</p>
              </div>
            </div>

            <div class="benefit-item">
              <span class="benefit-check-icon">✓</span>
              <div class="benefit-text">
                <strong>Pan-India Network</strong>
                <p>Direct connect with 70,000+ professionals across 28 states.</p>
              </div>
            </div>

            <div class="benefit-item">
              <span class="benefit-check-icon">✓</span>
              <div class="benefit-text">
                <strong>Free Legal Aid Taskforce</strong>
                <p>24/7 legal guidance &amp; social grievance assistance desk.</p>
              </div>
            </div>

            <div class="benefit-item">
              <span class="benefit-check-icon">✓</span>
              <div class="benefit-text">
                <strong>National Summits &amp; Events</strong>
                <p>Priority access to HRCI Global Peace Awards &amp; legal seminars.</p>
              </div>
            </div>

            <div class="benefit-item">
              <span class="benefit-check-icon">✓</span>
              <div class="benefit-text">
                <strong>Leadership Opportunities</strong>
                <p>Eligible to lead state, district, and city-level social cells.</p>
              </div>
            </div>

            <div class="benefit-item">
              <span class="benefit-check-icon">✓</span>
              <div class="benefit-text">
                <strong>Govt. Registered Recognition</strong>
                <p>Authentic affiliation with a prestigious MCA Section 8 NGO.</p>
              </div>
            </div>
          </div>

          <div class="about-action-btns">
            <a href="#membership-form" class="btn btn-primary-red btn-lg">
              <span>Join HRCI Membership Now →</span>
            </a>
            <a href="https://wa.me/919594441319?text=Hello%20HRCI,%20I%20want%20to%20know%20more%20about%20membership" target="_blank" rel="noopener" class="btn btn-whatsapp btn-lg">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
              <span>Chat on WhatsApp</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ======================================================================
       SECTION 5: VIDEOS & MEMBER TESTIMONIALS (FULL WIDTH)
       ====================================================================== -->
  <section class="dedicated-section sec-videos-testimonials" id="videos">
    <div class="container">
      <div class="section-center-header" data-aos="fade-up">
        <div class="sec-eyebrow-pill">VERIFIED IMPACT &amp; STORIES</div>
        <h2 class="sec-headline">Watch HRCI in Action. <span class="swoop-keyword">Real Impact, Real Voices.</span></h2>
        <p class="sec-subheadline">Watch our latest national peace summits and hear directly from verified members active across India.</p>
      </div>

      <!-- 4-Video Gallery Grid -->
      <div class="video-cards-grid-full" data-aos="fade-up">
        <div class="video-card-item" data-video-id="dQw4w9WgXcQ" data-video-title="HRCI Global Peace Award 2026">
          <div class="video-thumb-container">
            <img src="assets/images/video_thumb_1.jpg" alt="HRCI Global Peace Award 2026" loading="lazy">
            <div class="video-play-btn"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></div>
            <span class="video-duration-badge">8:24</span>
          </div>
          <div class="video-info-box">
            <div class="video-title">HRCI Global Peace Award 2026</div>
            <div class="video-meta">National Peace Summit &amp; Award Ceremony</div>
          </div>
        </div>

        <div class="video-card-item" data-video-id="dQw4w9WgXcQ" data-video-title="HRCI Global Peace Summit">
          <div class="video-thumb-container">
            <img src="assets/images/video_thumb_2.jpg" alt="HRCI Global Peace Summit" loading="lazy">
            <div class="video-play-btn"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></div>
            <span class="video-duration-badge">6:37</span>
          </div>
          <div class="video-info-box">
            <div class="video-title">HRCI Global Peace Summit</div>
            <div class="video-meta">Convention of Legal Advocates &amp; Leaders</div>
          </div>
        </div>

        <div class="video-card-item" data-video-id="dQw4w9WgXcQ" data-video-title="Human Rights Awareness">
          <div class="video-thumb-container">
            <img src="assets/images/video_thumb_3.jpg" alt="Human Rights Awareness Drive" loading="lazy">
            <div class="video-play-btn"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></div>
            <span class="video-duration-badge">5:18</span>
          </div>
          <div class="video-info-box">
            <div class="video-title">Human Rights Awareness Drive</div>
            <div class="video-meta">Community Legal Literacy &amp; Guidance</div>
          </div>
        </div>

        <div class="video-card-item" data-video-id="dQw4w9WgXcQ" data-video-title="HRCI Social Impact Video">
          <div class="video-thumb-container">
            <img src="assets/images/video_thumb_4.jpg" alt="HRCI Social Impact Video" loading="lazy">
            <div class="video-play-btn"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></div>
            <span class="video-duration-badge">0:59</span>
          </div>
          <div class="video-info-box">
            <div class="video-title">HRCI Social Impact Story</div>
            <div class="video-meta">Grassroots Welfare &amp; Citizen Support</div>
          </div>
        </div>
      </div>

      <!-- Testimonials Row -->
      <div class="testimonials-full-wrapper" id="testimonials" data-aos="fade-up">
        <div class="testimonials-header-center">
          <h3>What Our <strong>Members Say</strong></h3>
          <p>Real Stories • Real Impact • Trusted by 70,000+ Members Nationwide</p>
        </div>

        <div class="testimonials-cards-grid">
          <div class="testimonial-card-premium">
            <div class="testimonial-stars-svg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            </div>
            <p class="testimonial-quote">"HRCI ने मुझे समाज के लिए कुछ करने का अवसर दिया है। आज हमारे जिले में लीगल अवेयरनेस कैम्प्स चल रहे हैं। मुझे गर्व है कि मैं इसका सदस्य हूँ!"</p>
            <div class="testimonial-author-box">
              <img src="assets/images/member-1.jpg" alt="Mohammed A." class="testimonial-avatar" loading="lazy">
              <div>
                <strong class="author-name">Mohammed A.</strong>
                <span class="author-role">HRCI Member, Maharashtra</span>
              </div>
            </div>
          </div>

          <div class="testimonial-card-premium">
            <div class="testimonial-stars-svg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            </div>
            <p class="testimonial-quote">"HRCI के साथ जुड़कर मुझे Legal Awareness और Social Work में सीखने और योगदान देने का मौका मिला। ऑफिशियल आईडी कार्ड से बहुत सम्मान मिलता है।"</p>
            <div class="testimonial-author-box">
              <img src="assets/images/member-2.jpg" alt="Adv. Priya S." class="testimonial-avatar" loading="lazy">
              <div>
                <strong class="author-name">Adv. Priya S.</strong>
                <span class="author-role">HRCI Member, Delhi</span>
              </div>
            </div>
          </div>

          <div class="testimonial-card-premium">
            <div class="testimonial-stars-svg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            </div>
            <p class="testimonial-quote">"HRCI के कार्यक्रम बहुत अच्छे रहते हैं और समाज में सकारात्मक बदलाव आता है। संस्था की ईमानदारी और कार्यशैली वाकई में सराहनीय है!"</p>
            <div class="testimonial-author-box">
              <img src="assets/images/member-3.jpg" alt="Rakesh K." class="testimonial-avatar" loading="lazy">
              <div>
                <strong class="author-name">Rakesh K.</strong>
                <span class="author-role">HRCI Member, Gujarat</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ======================================================================
       SECTION 6: MEMBERSHIP PLANS (DEDICATED FULL-WIDTH BAND, MATCHING SCREENSHOT 4)
       ====================================================================== -->
  <section class="dedicated-section sec-pricing-plans-band" id="plans">
    <div class="container">
      <div class="section-center-header header-dark" data-aos="fade-up">
        <div class="sec-eyebrow-pill pill-light">MEMBERSHIP TIERS</div>
        <h2 class="sec-headline text-white">Transparent Membership Plans. <span class="swoop-keyword-gold">No Hidden Costs.</span></h2>
        <p class="sec-subheadline text-slate-300">Choose the plan that suits your goal and be part of India's premier national human rights movement.</p>
      </div>

      <div class="pricing-cards-grid-spacious">
        <!-- Plan 1: Annual Membership -->
        <div class="pricing-card-luxury" data-aos="fade-up" data-aos-delay="100">
          <div class="plan-header-top">
            <div class="plan-tag-pill tag-blue">ANNUAL MEMBERSHIP</div>
            <h3 class="plan-name">Annual Plan</h3>
            <p class="plan-desc-short">Essential membership for active social contributors &amp; advocates.</p>
          </div>

          <div class="plan-price-block">
            <span class="price-symbol">₹</span>
            <span class="price-number">600</span>
            <span class="price-tenure">/ 1 Year Validity</span>
          </div>

          <div class="plan-divider"></div>

          <ul class="plan-checklist">
            <li><span class="plan-check">✓</span> Official Membership ID Card (Digital)</li>
            <li><span class="plan-check">✓</span> Access to National HRCI Programs</li>
            <li><span class="plan-check">✓</span> Human Rights Event Participation</li>
            <li><span class="plan-check">✓</span> Digital Membership Certificate</li>
            <li><span class="plan-check">✓</span> Pan-India Member Community Access</li>
          </ul>

          <div class="plan-action-bottom">
            <a href="#membership-form" class="btn btn-plan-outline">
              Join Annual Membership →
            </a>
          </div>
        </div>

        <!-- Plan 2: Lifetime Membership (Featured) -->
        <div class="pricing-card-luxury featured-luxury-plan" data-aos="fade-up" data-aos-delay="200">
          <div class="popular-ribbon">★ MOST POPULAR</div>
          <div class="plan-header-top">
            <div class="plan-tag-pill tag-primary">LIFETIME MEMBERSHIP</div>
            <h3 class="plan-name">Lifetime Plan</h3>
            <p class="plan-desc-short">Permanent affiliation, leadership roles &amp; supreme privileges.</p>
          </div>

          <div class="plan-price-block">
            <span class="price-symbol">₹</span>
            <span class="price-number">3,000</span>
            <span class="price-tenure">/ One-Time Investment</span>
          </div>

          <div class="plan-divider"></div>

          <ul class="plan-checklist">
            <li><span class="plan-check">✓</span> <strong>Lifetime Permanent HRCI Membership</strong></li>
            <li><span class="plan-check">✓</span> <strong>Premium Embossed PVC ID Card &amp; Certificate</strong></li>
            <li><span class="plan-check">✓</span> Priority Access to National Peace Summits</li>
            <li><span class="plan-check">✓</span> Leadership Opportunities at District/State Level</li>
            <li><span class="plan-check">✓</span> Direct Free Legal Aid Taskforce Access</li>
            <li><span class="plan-check">✓</span> Official Recognition &amp; Social Honors</li>
          </ul>

          <div class="plan-action-bottom">
            <a href="#membership-form" class="btn btn-plan-solid-primary">
              Join Lifetime Membership Now →
            </a>
          </div>
        </div>

        <!-- Plan 3: Executive / Leadership Membership -->
        <div class="pricing-card-luxury" data-aos="fade-up" data-aos-delay="300">
          <div class="plan-header-top">
            <div class="plan-tag-pill tag-amber">EXECUTIVE / LEADERSHIP</div>
            <h3 class="plan-name">Leadership Role</h3>
            <p class="plan-desc-short">For advocates, doctors, executives &amp; dedicated social leaders.</p>
          </div>

          <div class="plan-price-block">
            <span class="price-designation">As per Designation</span>
            <span class="price-tenure">(National / State / District)</span>
          </div>

          <div class="plan-divider"></div>

          <ul class="plan-checklist">
            <li><span class="plan-check">✓</span> For Leaders, Professionals &amp; Social Workers</li>
            <li><span class="plan-check">✓</span> Special Recognition, Badges &amp; Official Roles</li>
            <li><span class="plan-check">✓</span> Priority Leadership Access to HRCI Initiatives</li>
            <li><span class="plan-check">✓</span> Direct Liaison with National Council Executives</li>
            <li><span class="plan-check">✓</span> By Nomination / Official Committee Approval</li>
          </ul>

          <div class="plan-action-bottom">
            <a href="#membership-form" class="btn btn-plan-outline">
              Apply for Leadership Membership →
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ======================================================================
       SECTION 7: SIMPLE PROCESS & MEMBERSHIP ENROLLMENT (DEDICATED SECTION)
       ====================================================================== -->
  <section class="dedicated-section sec-membership-enrollment" id="membership-form">
    <div class="container">
      <div class="section-center-header" data-aos="fade-up">
        <div class="sec-eyebrow-pill">HOW TO JOIN</div>
        <h2 class="sec-headline">Simple 4-Step Process. <span class="swoop-keyword">Instant Official Enrollment.</span></h2>
        <p class="sec-subheadline">Follow these 4 simple steps to receive your verified HRCI digital membership credentials.</p>
      </div>

      <!-- Process 4-Step Flow -->
      <div class="process-steps-row" data-aos="fade-up">
        <div class="process-step-box">
          <div class="step-badge-num">1</div>
          <div class="step-icon-wrap"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg></div>
          <h4>Fill Form</h4>
          <p>Provide basic personal &amp; contact details.</p>
        </div>
        <div class="process-arrow-divider">➔</div>

        <div class="process-step-box">
          <div class="step-badge-num">2</div>
          <div class="step-icon-wrap"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/></svg></div>
          <h4>Get Details</h4>
          <p>Instant WhatsApp &amp; SMS confirmation.</p>
        </div>
        <div class="process-arrow-divider">➔</div>

        <div class="process-step-box">
          <div class="step-badge-num">3</div>
          <div class="step-icon-wrap"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg></div>
          <h4>Choose Plan</h4>
          <p>Select Annual, Lifetime, or Leadership.</p>
        </div>
        <div class="process-arrow-divider">➔</div>

        <div class="process-step-box step-success">
          <div class="step-badge-num num-green">4</div>
          <div class="step-icon-wrap icon-green"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg></div>
          <h4>Become Member</h4>
          <p>Instant official digital ID card issued.</p>
        </div>
      </div>

      <!-- High-Conversion Centered Lead Form Card -->
      <div class="enrollment-form-container" data-aos="fade-up" data-aos-delay="150">
        <div class="lead-form-card-full">
          <div class="form-card-header-flex">
            <div class="header-badge-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
            </div>
            <div>
              <h3>Join HRCI Today</h3>
              <p>Start your official membership journey with India's trusted human rights council.</p>
            </div>
          </div>

          <form id="membershipForm" class="membership-form-grid" novalidate>
            <div class="form-row-2col">
              <div class="form-group">
                <label for="fullName">Full Name <span class="required-star">*</span></label>
                <div class="form-input-wrap">
                  <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                  <input type="text" id="fullName" name="fullName" class="form-control" placeholder="Enter Full Name" required>
                </div>
              </div>

              <div class="form-group">
                <label for="whatsappNumber">WhatsApp Number <span class="required-star">*</span></label>
                <div class="form-input-wrap">
                  <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                  <input type="tel" id="whatsappNumber" name="whatsappNumber" class="form-control" placeholder="e.g. 9876543210" pattern="[0-9]{10}" required>
                </div>
              </div>
            </div>

            <div class="form-row-2col">
              <div class="form-group">
                <label for="cityState">City / State <span class="required-star">*</span></label>
                <div class="form-input-wrap">
                  <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
                  <input type="text" id="cityState" name="cityState" class="form-control" placeholder="Enter City &amp; State" required>
                </div>
              </div>

              <div class="form-group">
                <label for="membershipType">Membership Type <span class="required-star">*</span></label>
                <div class="form-input-wrap">
                  <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                  <select id="membershipType" name="membershipType" class="form-control" required>
                    <option value="" disabled selected>Select Membership Type</option>
                    <option value="Annual Membership (₹600)">Annual Membership (₹600 / 1 Year)</option>
                    <option value="Lifetime Membership (₹3,000)">Lifetime Membership (₹3,000 / One-Time)</option>
                    <option value="Executive / Leadership Membership">Executive / Leadership Membership (By Designation)</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="form-group">
              <label for="profession">Profession / Occupation <span class="required-star">*</span></label>
              <div class="form-input-wrap">
                <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20 6h-4V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-6 0h-4V4h4v2z"/></svg>
                <input type="text" id="profession" name="profession" class="form-control" placeholder="Doctor, Advocate, Social Worker, Business, Teacher, etc." required>
              </div>
            </div>

            <div class="form-submit-row">
              <button type="submit" class="btn btn-submit-lead-full" id="submitLeadBtn">
                <span>Get Membership Details &amp; Join HRCI →</span>
              </button>
            </div>

            <div class="form-trust-guarantee">
              <span>🔒 Your information is 100% safe &amp; confidential</span>
              <span class="trust-dot">•</span>
              <span>✓ Instant WhatsApp Confirmation</span>
              <span class="trust-dot">•</span>
              <span>✓ Govt. Regd. Section 8 NGO</span>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>


  <!-- ======================================================================
       SECTION 8: FREQUENTLY ASKED QUESTIONS (MATCHING SCREENSHOT 5)
       ====================================================================== -->
  <section class="dedicated-section sec-faq-split" id="faq">
    <div class="container">
      <div class="faq-two-col-layout">
        <!-- Left Column: Headline & WhatsApp Support Card -->
        <div class="faq-left-column" data-aos="fade-right">
          <div class="sec-eyebrow-pill">FAQ</div>
          <h2 class="sec-headline">Questions? <span class="swoop-keyword">Answered.</span></h2>
          <p class="sec-subheadline-left">
            Everything you need to know about HRCI Membership, ID cards, validity, and our nationwide mission.
          </p>

          <!-- WhatsApp Quick Support Card (Matching Screenshot 5) -->
          <div class="faq-support-card">
            <h4>Still have a question?</h4>
            <p>Write to us on WhatsApp. Our national desk replies quickly.</p>
            <a href="https://wa.me/919594441319?text=Hello%20HRCI,%20I%20have%20a%20question%20about%20membership" target="_blank" rel="noopener" class="btn btn-faq-whatsapp">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
              <span>Chat on WhatsApp</span>
            </a>
          </div>
        </div>

        <!-- Right Column: Accordion List (Matching Screenshot 5) -->
        <div class="faq-right-column" data-aos="fade-left">
          <div class="faq-accordion-list">
            <!-- FAQ 1 (Active by default) -->
            <div class="faq-item-modern active">
              <button class="faq-modern-btn" type="button" aria-expanded="true">
                <span class="faq-q-text">HRCI Membership क्या है?</span>
                <span class="faq-toggle-icon">✕</span>
              </button>
              <div class="faq-modern-answer" style="display:block;">
                <p>HRCI (भारतीय मानवाधिकार परिषद) की सदस्यता समाज के सजग नागरिकों, अधिवक्ताओं, डॉक्टरों, शिक्षकों और समाजसेवियों को एक राष्ट्रीय मंच प्रदान करती है। सदस्य बनकर आप मानव अधिकारों की रक्षा, विधिक जागरूकता और सामाजिक कल्याण में सक्रिय योगदान दे सकते हैं।</p>
              </div>
            </div>

            <!-- FAQ 2 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">Membership कितने समय के लिए वैध है?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Annual Membership 1 वर्ष के लिए वैध होती है, जबकि Lifetime Membership जीवनभर के लिए मान्य होती है। Executive / Leadership Membership पद एवं दायित्व के अनुसार निर्धारित की जाती है।</p>
              </div>
            </div>

            <!-- FAQ 3 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">कौन सदस्य बन सकता है?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>भारत का कोई भी 18 वर्ष से अधिक आयु का नागरिक, जिसका कोई आपराधिक रिकॉर्ड न हो और जो समाज कल्याण व मानवाधिकारों के संरक्षण में विश्वास रखता हो, HRCI का सदस्य बन सकता है।</p>
              </div>
            </div>

            <!-- FAQ 4 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">क्या Membership Renew करनी होती है?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Annual Membership को 1 वर्ष पूर्ण होने पर रिन्यू कराना होता है। यदि आपने Lifetime Membership ली है, तो आपको कभी भी रिन्यूअल फीस देने की आवश्यकता नहीं होती।</p>
              </div>
            </div>

            <!-- FAQ 5 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">Membership ID Card कैसे मिलेगा?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>आवेदन और सत्यापन प्रक्रिया पूर्ण होते ही आपका डिजिटल ID Card आपके WhatsApp और Email पर तुरंत भेजा जाता है। इसके अलावा आधिकारिक PVC कार्ड डाक द्वारा आपके पते पर भेजा जाता है।</p>
              </div>
            </div>

            <!-- FAQ 6 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">क्या यह सरकारी संस्था है?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>HRCI भारत सरकार के कॉर्पोरेट कार्य मंत्रालय (Ministry of Corporate Affairs) के अंतर्गत पंजीकृत एक राष्ट्रीय, गैर-राजनीतिक एवं धर्मनिरपेक्ष सेक्शन 8 गैर-सरकारी संगठन (NGO) है।</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ======================================================================
       SECTION 9: CONTACT SECRETARIAT DIRECTORY (CLEAN 4-COL GRID)
       ====================================================================== -->
  <section class="dedicated-section sec-contact-directory" id="contact">
    <div class="container">
      <div class="section-center-header" data-aos="fade-up">
        <div class="sec-eyebrow-pill">NATIONAL DIRECTORY</div>
        <h2 class="sec-headline">Contact Our Secretariat. <span class="swoop-keyword">Here For You 24/7.</span></h2>
        <p class="sec-subheadline">We are dedicated to serving citizens, legal advocates, and members nationwide.</p>
      </div>

      <div class="contact-cards-grid-4col" data-aos="fade-up">
        <div class="contact-card-premium">
          <div class="contact-icon-bubble">📍</div>
          <h4>National Headquarters</h4>
          <p class="contact-meta">Central Administration &amp; Legal Wing</p>
          <p class="contact-detail">Barakhamba Road, Connaught Place, New Delhi – 110001, India</p>
        </div>

        <div class="contact-card-premium">
          <div class="contact-icon-bubble">🏢</div>
          <h4>Western Coordination Office</h4>
          <p class="contact-meta">State Operations &amp; Event Liaison</p>
          <p class="contact-detail">Mumbai Metropolitan Region, Maharashtra – 400001, India</p>
        </div>

        <div class="contact-card-premium">
          <div class="contact-icon-bubble">📞</div>
          <h4>National Citizen Helpline</h4>
          <p class="contact-meta">Direct Inquiries &amp; Member Support</p>
          <p class="contact-detail"><strong>+91 95944 41319</strong><br><strong>+91 95944 41315</strong></p>
        </div>

        <div class="contact-card-premium">
          <div class="contact-icon-bubble">✉️</div>
          <h4>Official Correspondence</h4>
          <p class="contact-meta">Verification &amp; Documentation</p>
          <p class="contact-detail"><strong>info@hrcofindia.org</strong><br><strong>www.hrcofindia.org</strong></p>
        </div>
      </div>
    </div>
  </section>

  '''

# Replace the region in index.html
new_html = text[:pos_start] + new_sections_html + text[pos_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Restructured index.html into dedicated, full-width sections successfully!")

