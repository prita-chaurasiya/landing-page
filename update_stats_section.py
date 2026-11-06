with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s = text.find('class="stats-strip-section"')
section_start = text.rfind('<section', 0, s)
section_end = text.find('</section>', s) + len('</section>')

new_stats_html = '''<section class="stats-strip-section" id="stats" aria-label="Key Statistics">
    <div class="container">
      <div class="stats-grid-luxury">
        <!-- 1. Active Members -->
        <div class="stat-card-luxury" data-aos="fade-up" data-aos-delay="100">
          <div class="stat-top-row">
            <div class="stat-icon-wrap icon-navy">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
            </div>
            <span class="stat-badge-pill">PAN-INDIA</span>
          </div>
          <div class="stat-number-wrap">
            <span class="stat-number" data-target="70000" data-suffix="+">70,000+</span>
          </div>
          <div class="stat-title">Active Members</div>
          <div class="stat-subtitle">Verified Citizen Network</div>
        </div>

        <!-- 2. Active States -->
        <div class="stat-card-luxury" data-aos="fade-up" data-aos-delay="200">
          <div class="stat-top-row">
            <div class="stat-icon-wrap icon-gold">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
            </div>
            <span class="stat-badge-pill">COVERAGE</span>
          </div>
          <div class="stat-number-wrap">
            <span class="stat-number" data-target="28" data-suffix=" States">28 States</span>
          </div>
          <div class="stat-title">State Councils</div>
          <div class="stat-subtitle">Active Across India</div>
        </div>

        <!-- 3. People Assisted -->
        <div class="stat-card-luxury" data-aos="fade-up" data-aos-delay="300">
          <div class="stat-top-row">
            <div class="stat-icon-wrap icon-navy">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
            </div>
            <span class="stat-badge-pill">AID &amp; WELFARE</span>
          </div>
          <div class="stat-number-wrap">
            <span class="stat-number" data-target="20000" data-suffix="+">20,000+</span>
          </div>
          <div class="stat-title">People Assisted</div>
          <div class="stat-subtitle">Free Legal &amp; Social Guidance</div>
        </div>

        <!-- 4. Established Date -->
        <div class="stat-card-luxury" data-aos="fade-up" data-aos-delay="400">
          <div class="stat-top-row">
            <div class="stat-icon-wrap icon-gold">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L2 6v2h20V6L12 1zM4 10v9h3v-9H4zm6 0v9h3v-9h-3zm6 0v9h3v-9h-3zM2 21v2h20v-2H2z"/></svg>
            </div>
            <span class="stat-badge-pill">GOVT. REGD.</span>
          </div>
          <div class="stat-number-wrap">
            <span class="stat-number stat-date">11 Jan 2013</span>
          </div>
          <div class="stat-title">Established Date</div>
          <div class="stat-subtitle">MCA Section 8 Company</div>
        </div>

        <!-- 5. Years of Service -->
        <div class="stat-card-luxury" data-aos="fade-up" data-aos-delay="500">
          <div class="stat-top-row">
            <div class="stat-icon-wrap icon-navy">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19 5h-2V3H7v2H5c-1.1 0-2 .9-2 2v1c0 2.55 1.92 4.63 4.39 4.94A5.01 5.01 0 0011 15.9V19H7v2h10v-2h-4v-3.1c1.83-.43 3.24-1.89 3.61-3.76A5.01 5.01 0 0021 8V7c0-1.1-.9-2-2-2zM5 8V7h2v3.82C5.84 10.4 5 9.3 5 8zm14 0c0 1.3-.84 2.4-2 2.82V7h2v1z"/></svg>
            </div>
            <span class="stat-badge-pill">LEGACY</span>
          </div>
          <div class="stat-number-wrap">
            <span class="stat-number" data-target="13" data-suffix="+ Years">13+ Years</span>
          </div>
          <div class="stat-title">Nationwide Service</div>
          <div class="stat-subtitle">Of Unbroken Leadership</div>
        </div>
      </div>
    </div>
  </section>'''

text = text[:section_start] + new_stats_html + text[section_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated stats section in index.html successfully!")

