css = '''

/* ==========================================================================
   ENHANCED ULTRA-PREMIUM TESTIMONIAL CARDS (SAAS / GOVERNMENT-GRADE NGO)
   ========================================================================== */
.testimonials-full-wrapper {
  margin-top: 64px !important;
  padding-top: 48px !important;
  border-top: 1px solid #E2E8F0 !important;
}

.testimonials-header-center {
  text-align: center !important;
  margin-bottom: 36px !important;
}

.testimonials-header-center h3 {
  font-size: clamp(28px, 3.2vw, 38px) !important;
  font-weight: 800 !important;
  color: #0A1A3F !important;
  letter-spacing: -0.02em !important;
  margin: 0 0 10px 0 !important;
}

.testimonials-header-center h3 strong {
  color: #F59E0B !important;
  font-weight: 900 !important;
}

.testimonials-header-center p {
  color: #64748B !important;
  font-size: 1.05rem !important;
  font-weight: 500 !important;
  margin: 0 !important;
}

.testimonials-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 28px !important;
}

.testimonial-card-premium {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  padding: 32px 28px !important;
  box-shadow: 0 12px 35px -5px rgba(10, 26, 63, 0.06), 0 4px 12px rgba(0, 0, 0, 0.02) !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  position: relative !important;
}

.testimonial-card-premium:hover {
  transform: translateY(-8px) scale(1.015) !important;
  border-color: #F59E0B !important;
  box-shadow: 0 25px 55px -10px rgba(10, 26, 63, 0.14), 0 0 0 1px rgba(245, 158, 11, 0.25) !important;
}

.testimonial-card-top {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 8px !important;
}

.testimonial-stars-row {
  display: inline-flex !important;
  flex-direction: row !important;
  align-items: center !important;
  gap: 4px !important;
}

.testimonial-stars-row svg {
  width: 18px !important;
  height: 18px !important;
  fill: #F59E0B !important;
  color: #F59E0B !important;
  display: inline-block !important;
  flex-shrink: 0 !important;
}

.testimonial-verified-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 5px !important;
  background: #F0FDF4 !important;
  border: 1px solid #BBF7D0 !important;
  color: #15803D !important;
  font-size: 0.74rem !important;
  font-weight: 700 !important;
  padding: 4px 10px !important;
  border-radius: 9999px !important;
  letter-spacing: 0.02em !important;
}

.testimonial-quote-mark {
  font-family: Georgia, serif !important;
  font-size: 44px !important;
  line-height: 1 !important;
  color: #F59E0B !important;
  opacity: 0.45 !important;
  margin: 6px 0 -10px 0 !important;
}

.testimonial-quote {
  color: #334155 !important;
  font-size: 0.98rem !important;
  line-height: 1.68 !important;
  font-weight: 400 !important;
  font-style: normal !important;
  margin: 0 !important;
  min-height: 110px !important;
}

.testimonial-author-box {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  margin-top: 22px !important;
  padding-top: 18px !important;
  border-top: 1px solid #F1F5F9 !important;
}

.testimonial-avatar {
  width: 52px !important;
  height: 52px !important;
  border-radius: 50% !important;
  border: 2.5px solid #F59E0B !important;
  object-fit: cover !important;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.25) !important;
  flex-shrink: 0 !important;
}

.author-details {
  display: flex !important;
  flex-direction: column !important;
}

.author-name {
  font-size: 1.05rem !important;
  font-weight: 800 !important;
  color: #0A1A3F !important;
  line-height: 1.2 !important;
}

.author-role {
  font-size: 0.82rem !important;
  color: #64748B !important;
  font-weight: 600 !important;
  margin-top: 2px !important;
}

.author-badge-pill {
  display: inline-block !important;
  font-size: 0.68rem !important;
  font-weight: 700 !important;
  color: #1D4ED8 !important;
  background: #EFF6FF !important;
  border: 1px solid #BFDBFE !important;
  border-radius: 6px !important;
  padding: 2px 8px !important;
  margin-top: 6px !important;
  width: fit-content !important;
}

@media (max-width: 1024px) {
  .testimonials-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
  }
  .testimonial-quote {
    min-height: auto !important;
  }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Appended testimonial card CSS successfully!")

