# apply_final_polish.py

css_refinements = """
/* ==========================================================================
   FINAL POLISH & CONTRAST REFINEMENTS
   ========================================================================== */

/* 1. Pre-footer poster bar text contrast */
.poster-matching-footer-bar {
  background: #091326 !important;
  border-top: 1px solid #1E293B !important;
}
.poster-matching-footer-bar .poster-footer-text h4 {
  color: #FFFFFF !important;
  font-weight: 800 !important;
}
.poster-matching-footer-bar .poster-footer-text h5 {
  color: var(--ng-coral) !important;
  font-weight: 700 !important;
}
.poster-matching-footer-bar .poster-footer-text p {
  color: #94A3B8 !important;
}

/* 2. Final CTA Section Contrast & Spacing */
.final-cta-section {
  padding: 56px 24px !important;
  margin: 50px auto !important;
}
.final-cta-section .final-cta-badge {
  background: var(--ng-lavender-bg) !important;
  color: var(--ng-lavender-text) !important;
  border: 1px solid var(--ng-lavender-border) !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  border-radius: 9999px !important;
  padding: 6px 18px !important;
  display: inline-flex !important;
  align-items: center !important;
  margin-bottom: 14px !important;
}
.final-cta-section p, .final-cta-subtitle {
  color: #475569 !important;
  font-size: 1.05rem !important;
  line-height: 1.65 !important;
  max-width: 680px !important;
  margin: 12px auto 24px auto !important;
}

/* 3. Pricing Lifetime Card Most Popular Badge */
.card-lifetime-banner {
  padding-top: 36px !important;
  margin-top: 10px !important;
}
.card-lifetime-banner::before {
  top: -14px !important;
  z-index: 10 !important;
}

/* 4. Floating Action Buttons */
.floating-action-desk {
  position: fixed !important;
  bottom: 24px !important;
  right: 24px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  z-index: 9999 !important;
}
.float-btn {
  width: 50px !important;
  height: 50px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.16) !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  position: relative !important;
}
.float-btn:hover {
  transform: scale(1.1) !important;
}
.float-call {
  background: #6366F1 !important;
  color: #FFFFFF !important;
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.45) !important;
}
.float-call:hover {
  background: #4F46E5 !important;
}
.float-whatsapp {
  background: #25D366 !important;
  color: #FFFFFF !important;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.45) !important;
}
.float-scroll-top {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1.5px solid #E2E8F0 !important;
  font-weight: 800 !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_refinements)

# Add float-call button to index.html if not already present
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'class="float-btn float-call"' not in html:
    target = '<aside class="floating-action-desk" aria-label="Quick Actions">'
    replacement = '''<aside class="floating-action-desk" aria-label="Quick Actions">
    <a href="tel:+919594441315" class="float-btn float-call" title="Call National Helpline">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1.02l-2.2 2.2z"/></svg>
      <span class="float-tooltip">Call Helpline</span>
    </a>'''
    html = html.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added float-call button to index.html")
else:
    print("float-call button already in index.html")

print("Applied final polish successfully!")

