with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

needle_start = 'class="focus-grid-modern"'
s = text.find(needle_start)
if s != -1:
    section_end = text.find('</section>', s)
    # find the </div>\n    </div> before </section>
    div_end = text.rfind('</div>\n    </div>', s, section_end)
    print("Found s:", s, "div_end:", div_end)
    
    new_focus_grid = '''class="focus-grid-modern">
        <!-- Item 1 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="50">
          <div class="focus-modern-icon icon-blue">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a1 1 0 00-1 1v1.07A7.002 7.002 0 005.07 10H4a1 1 0 000 2h1.07A7.002 7.002 0 0011 17.93V21H9a1 1 0 000 2h6a1 1 0 000-2h-2v-3.07A7.002 7.002 0 0018.93 12H20a1 1 0 000-2h-1.07A7.002 7.002 0 0013 4.07V3a1 1 0 00-1-1zm-5 9a5 5 0 1110 0 5 5 0 01-10 0z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Legal Awareness &amp; Guidance</h4>
            <p>Free legal literacy camps, constitutional counseling, and grievance guidance for marginalized citizens.</p>
            <div class="focus-card-action"><span>Explore Initiative</span> <span class="action-arrow">→</span></div>
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
            <div class="focus-card-action"><span>Explore Workshops</span> <span class="action-arrow">→</span></div>
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
            <div class="focus-card-action"><span>Explore Drives</span> <span class="action-arrow">→</span></div>
          </div>
        </a>

        <!-- Item 4 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="200">
          <div class="focus-modern-icon icon-purple">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V9h14v11zM7 11h5v5H7z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Events &amp; Awareness Programs</h4>
            <p>National Human Rights Summits, public legal forums, and district-level social impact conventions.</p>
            <div class="focus-card-action"><span>Explore Summits</span> <span class="action-arrow">→</span></div>
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
            <div class="focus-card-action"><span>View Network</span> <span class="action-arrow">→</span></div>
          </div>
        </a>

        <!-- Item 6 -->
        <a href="#membership-form" class="focus-modern-card" data-aos="fade-up" data-aos-delay="300">
          <div class="focus-modern-icon icon-rose">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1c0-2 4-3.1 6-3.1s6 1.1 6 3.1v1z"/></svg>
          </div>
          <div class="focus-modern-content">
            <h4>Official Membership ID Card</h4>
            <p>Instant digital ID card with QR code verification plus physical embossed PVC card delivered to your address.</p>
            <div class="focus-card-action"><span>Get Your Card</span> <span class="action-arrow">→</span></div>
          </div>
        </a>\n      '''

    text = text[:s] + new_focus_grid + text[div_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced focus-grid-modern successfully!")

