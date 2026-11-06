# fix_plans_badge_and_focus.py

css_fixes = """
/* ==========================================================================
   PLANS BADGE & FOCUS TITLE BLOCK REFINEMENTS
   ========================================================================== */
.membership-plans-box {
  padding-top: 38px !important;
  overflow: visible !important;
}

.pricing-cards-grid {
  overflow: visible !important;
  padding-top: 10px !important;
}

.card-lifetime-banner {
  overflow: visible !important;
  position: relative !important;
}

.card-lifetime-banner::before {
  content: '★ MOST POPULAR' !important;
  position: absolute !important;
  top: -14px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  background: linear-gradient(135deg, #F4683A 0%, #FF8A50 100%) !important;
  color: #FFFFFF !important;
  font-size: 0.72rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.06em !important;
  padding: 5px 16px !important;
  border-radius: 9999px !important;
  box-shadow: 0 6px 16px rgba(244, 104, 58, 0.4) !important;
  white-space: nowrap !important;
  width: max-content !important;
  z-index: 20 !important;
}

.focus-title-block {
  background: linear-gradient(135deg, #F4683A 0%, #FF8A50 100%) !important;
  color: #FFFFFF !important;
  border-radius: 18px !important;
  box-shadow: 0 8px 22px rgba(244, 104, 58, 0.25) !important;
}

.focus-title-block h3, 
.focus-title-block h4, 
.focus-title-block p, 
.focus-title-block span,
.focus-sub {
  color: #FFFFFF !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_fixes)

print("Appended plans badge & focus block fixes successfully!")

