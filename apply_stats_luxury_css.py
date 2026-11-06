css = '''

/* ==========================================================================
   AGENCY-GRADE ULTRA-LUXURY TRUST STATS STRIP (NO PASTEL / NO AI LOOK)
   ========================================================================== */
.stats-strip-section {
  background: #FAF8F5 !important;
  padding: 42px 0 !important;
  position: relative !important;
  border-bottom: 1px solid #ECE7DE !important;
}

.stats-grid-luxury {
  display: grid !important;
  grid-template-columns: repeat(5, 1fr) !important;
  gap: 20px !important;
}

.stat-card-luxury {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  padding: 24px 20px !important;
  box-shadow: 0 10px 30px -5px rgba(10, 26, 63, 0.05), 0 2px 6px rgba(0, 0, 0, 0.02) !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  position: relative !important;
}

.stat-card-luxury::before {
  display: none !important;
}

.stat-card-luxury:hover {
  transform: translateY(-8px) scale(1.02) !important;
  border-color: #BFDBFE !important;
  box-shadow: 0 22px 45px -8px rgba(29, 78, 216, 0.12), 0 0 0 1px rgba(245, 158, 11, 0.25) !important;
}

.stat-top-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-bottom: 16px !important;
}

.stat-icon-wrap {
  width: 40px !important;
  height: 40px !important;
  border-radius: 12px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
  transition: transform 0.3s ease !important;
}

.stat-card-luxury:hover .stat-icon-wrap {
  transform: scale(1.1) rotate(4deg) !important;
}

.stat-icon-wrap.icon-navy {
  background: #EFF6FF !important;
  color: #1D4ED8 !important;
  border: 1px solid #BFDBFE !important;
}

.stat-icon-wrap.icon-gold {
  background: #FEF3C7 !important;
  color: #D97706 !important;
  border: 1px solid #FDE68A !important;
}

.stat-icon-wrap svg {
  width: 20px !important;
  height: 20px !important;
  display: block !important;
}

.stat-badge-pill {
  font-size: 0.68rem !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
  color: #64748B !important;
  background: #F8FAFC !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 9999px !important;
  padding: 3px 8px !important;
}

.stat-number-wrap {
  margin-bottom: 4px !important;
}

.stat-card-luxury .stat-number {
  font-size: clamp(26px, 2.3vw, 32px) !important;
  font-weight: 900 !important;
  color: #0A1A3F !important;
  line-height: 1.15 !important;
  letter-spacing: -0.025em !important;
  display: block !important;
  /* 3D Number Elevation */
  text-shadow: 0 1px 0 #CBD5E1, 0 2px 4px rgba(10, 26, 63, 0.08) !important;
  margin: 0 !important;
}

.stat-card-luxury .stat-number.stat-date {
  font-size: clamp(20px, 1.8vw, 24px) !important;
  letter-spacing: -0.01em !important;
}

.stat-card-luxury .stat-title {
  font-size: 0.96rem !important;
  font-weight: 800 !important;
  color: #1E293B !important;
  line-height: 1.3 !important;
  margin-top: 4px !important;
}

.stat-card-luxury .stat-subtitle {
  font-size: 0.78rem !important;
  color: #64748B !important;
  font-weight: 500 !important;
  margin-top: 2px !important;
}

@media (max-width: 1024px) {
  .stats-grid-luxury {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 16px !important;
  }
}

@media (max-width: 768px) {
  .stats-grid-luxury {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }
  .stat-card-luxury:last-child {
    grid-column: span 2 !important;
  }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Appended luxury stats CSS successfully!")

