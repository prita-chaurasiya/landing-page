css = '''

/* ==========================================================================
   AGENCY-GRADE VECTOR SVG ICONS FOR CONTACT DIRECTORY & HERO BADGES
   ========================================================================== */
.contact-icon-bubble {
  width: 52px !important;
  height: 52px !important;
  border-radius: 16px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin-bottom: 18px !important;
  box-shadow: 0 8px 20px -3px rgba(10, 26, 63, 0.08) !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.contact-card-premium:hover .contact-icon-bubble {
  transform: scale(1.08) translateY(-2px) !important;
}

.contact-icon-bubble.bubble-navy {
  background: linear-gradient(135deg, #0A1A3F 0%, #1E3A8A 100%) !important;
  color: #F59E0B !important;
  box-shadow: 0 8px 22px rgba(10, 26, 63, 0.25) !important;
}

.contact-icon-bubble.bubble-amber {
  background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%) !important;
  color: #B45309 !important;
  border: 1px solid #FCD34D !important;
  box-shadow: 0 8px 20px rgba(245, 158, 11, 0.18) !important;
}

.contact-icon-bubble.bubble-sapphire {
  background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%) !important;
  color: #1D4ED8 !important;
  border: 1px solid #BFDBFE !important;
  box-shadow: 0 8px 20px rgba(29, 78, 216, 0.16) !important;
}

.contact-icon-bubble.bubble-emerald {
  background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%) !important;
  color: #15803D !important;
  border: 1px solid #BBF7D0 !important;
  box-shadow: 0 8px 20px rgba(22, 163, 74, 0.16) !important;
}

.contact-icon-bubble svg {
  width: 24px !important;
  height: 24px !important;
  display: block !important;
}

/* HERO FLOATING BADGE VECTOR ICONS */
.badge-icon-svg {
  width: 34px !important;
  height: 34px !important;
  border-radius: 10px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
}

.badge-icon-svg.icon-svg-blue {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
  border: 1px solid #BFDBFE !important;
}

.badge-icon-svg.icon-svg-amber {
  background: #FEF3C7 !important;
  color: #D97706 !important;
  border: 1px solid #FDE68A !important;
}

.badge-icon-svg.icon-svg-gold {
  background: #FFFBEB !important;
  color: #B45309 !important;
  border: 1px solid #FDE68A !important;
}

.badge-icon-svg.icon-svg-sapphire {
  background: #DBEAFE !important;
  color: #1E40AF !important;
  border: 1px solid #93C5FD !important;
}

.badge-icon-svg svg {
  display: block !important;
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Appended vector icon styles to style.css")

