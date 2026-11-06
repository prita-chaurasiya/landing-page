with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. NEW TESTIMONIALS HTML
old_testimonials_start = text.find('<div class="testimonials-cards-grid">')
old_testimonials_end = text.find('</div>\n      </div>\n    </div>\n  </section>\n\n  <!-- ======================================================================\n       SECTION 5: DEDICATED DARK ROYAL NAVY MEMBERSHIP PLANS BAND')

new_testimonials_html = '''<div class="testimonials-cards-grid">
          <!-- Member 1 -->
          <div class="testimonial-card-premium" data-aos="fade-up" data-aos-delay="100">
            <div class="testimonial-card-top">
              <div class="testimonial-stars-row">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <span class="testimonial-verified-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="#16A34A"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                Verified Member
              </span>
            </div>
            
            <div class="testimonial-quote-mark">“</div>
            <p class="testimonial-quote">
              "HRCI provided me with an official national platform to lead grassroots legal awareness camps and social grievance resolution across Maharashtra. The official PVC ID card and direct council backing command immense respect from local authorities."
            </p>

            <div class="testimonial-author-box">
              <img src="assets/images/member-1.jpg" alt="Mohammed A." class="testimonial-avatar" loading="lazy">
              <div class="author-details">
                <strong class="author-name">Mohammed A.</strong>
                <span class="author-role">District Coordinator • Maharashtra</span>
                <span class="author-badge-pill">Lifetime Member</span>
              </div>
            </div>
          </div>

          <!-- Member 2 -->
          <div class="testimonial-card-premium" data-aos="fade-up" data-aos-delay="200">
            <div class="testimonial-card-top">
              <div class="testimonial-stars-row">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <span class="testimonial-verified-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="#16A34A"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                Verified Member
              </span>
            </div>
            
            <div class="testimonial-quote-mark">“</div>
            <p class="testimonial-quote">
              "As a legal advocate, partnering with HRCI has allowed me to contribute meaningfully to free constitutional legal aid drives. The council's transparency, government-grade governance, and pan-India reach are truly unmatched."
            </p>

            <div class="testimonial-author-box">
              <img src="assets/images/member-2.jpg" alt="Adv. Priya S." class="testimonial-avatar" loading="lazy">
              <div class="author-details">
                <strong class="author-name">Adv. Priya S.</strong>
                <span class="author-role">Legal Counsel &amp; Member • New Delhi</span>
                <span class="author-badge-pill">Executive Member</span>
              </div>
            </div>
          </div>

          <!-- Member 3 -->
          <div class="testimonial-card-premium" data-aos="fade-up" data-aos-delay="300">
            <div class="testimonial-card-top">
              <div class="testimonial-stars-row">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <span class="testimonial-verified-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="#16A34A"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                Verified Member
              </span>
            </div>
            
            <div class="testimonial-quote-mark">“</div>
            <p class="testimonial-quote">
              "Being an active member has connected me with dedicated professionals, civil leaders, and social workers across 28 states. From national peace summits to community assistance, the impact is real and visible on the ground."
            </p>

            <div class="testimonial-author-box">
              <img src="assets/images/member-3.jpg" alt="Rakesh K." class="testimonial-avatar" loading="lazy">
              <div class="author-details">
                <strong class="author-name">Rakesh K.</strong>
                <span class="author-role">State Executive Member • Gujarat</span>
                <span class="author-badge-pill">Annual Member</span>
              </div>
            </div>
          </div>
        </div>'''

if old_testimonials_start != -1 and old_testimonials_end != -1:
    text = text[:old_testimonials_start] + new_testimonials_html + text[old_testimonials_end:]
    print("Testimonials replaced successfully!")
else:
    print("Could not find exact testimonial bounds")

# 2. NEW ENGLISH FAQS
old_faq_start = text.find('<div class="faq-accordion-list">')
old_faq_end = text.find('</div>\n        </div>\n      </div>\n    </div>\n  </section>\n\n  <!-- ======================================================================\n       SECTION 8: CONTACT SECRETARIAT & HELPLINE DIRECTORY')

new_faq_html = '''<div class="faq-accordion-list">
            <!-- FAQ 1 (Active by default) -->
            <div class="faq-item-modern active">
              <button class="faq-modern-btn" type="button" aria-expanded="true">
                <span class="faq-q-text">What is HRCI Membership?</span>
                <span class="faq-toggle-icon">✕</span>
              </button>
              <div class="faq-modern-answer" style="display:block;">
                <p>HRCI (Human Rights Council of India) membership offers conscious citizens, advocates, doctors, educators, and social contributors an official national platform. As an active member, you participate directly in defending constitutional rights, organizing legal awareness camps, and delivering grassroots community welfare across 28 states of India.</p>
              </div>
            </div>

            <!-- FAQ 2 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">What is the validity period of the membership?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Annual Membership is valid for 1 full year from the date of official issuance. Lifetime Membership grants permanent, lifelong affiliation with supreme organizational privileges and zero renewal requirement. Executive &amp; Leadership Memberships are assigned based on institutional role and committee tenure.</p>
              </div>
            </div>

            <!-- FAQ 3 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">Who is eligible to become an HRCI Member?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Any Indian citizen aged 18 years or above with a clean track record, who is committed to constitutional values, justice, equality, and social service, is eligible to apply for HRCI membership through our official verification process.</p>
              </div>
            </div>

            <!-- FAQ 4 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">Is membership renewal required after one year?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Annual Membership requires a yearly renewal to maintain active digital credentials. Lifetime Members enjoy permanent status with zero recurring renewal fees and lifetime access to national summits, conventions, and welfare programs.</p>
              </div>
            </div>

            <!-- FAQ 5 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">How and when will I receive my Membership ID Card?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Upon successful verification and approval of your enrollment, an instant QR-verified Digital Membership ID Card and Certificate are issued immediately to your WhatsApp and registered email. A physical embossed PVC Smart Card is subsequently dispatched to your postal address.</p>
              </div>
            </div>

            <!-- FAQ 6 -->
            <div class="faq-item-modern">
              <button class="faq-modern-btn" type="button" aria-expanded="false">
                <span class="faq-q-text">Is HRCI a Government-recognized Organization?</span>
                <span class="faq-toggle-icon">+</span>
              </button>
              <div class="faq-modern-answer">
                <p>Yes. Human Rights Council of India (HRCI) is an authentic, non-political, and secular national organization incorporated under the Ministry of Corporate Affairs (MCA), Government of India as an approved Section 8 Company (Established 11 January 2013).</p>
              </div>
            </div>
          </div>'''

if old_faq_start != -1 and old_faq_end != -1:
    text = text[:old_faq_start] + new_faq_html + text[old_faq_end:]
    print("FAQs replaced successfully!")
else:
    print("Could not find exact FAQ bounds")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated index.html")

