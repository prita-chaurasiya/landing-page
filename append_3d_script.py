code = '''

/* --------------------------------------------------------------------------
   17. HERO SHOWCASE 3D PARALLAX & RESTORED TILT FOR ALL SECTION CARDS
   -------------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', () => {
  const heroSec = document.getElementById('home');
  const heroCard = document.querySelector('.hero-composition-card');

  if (heroSec && heroCard && window.innerWidth > 992) {
    heroSec.addEventListener('mousemove', (e) => {
      const rect = heroSec.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;

      const tiltX = -y * 14; // max 7 deg
      const tiltY = x * 18;  // max 9 deg

      heroCard.style.animation = 'none';
      heroCard.style.transform = `perspective(1200px) rotateX(${tiltX.toFixed(2)}deg) rotateY(${tiltY.toFixed(2)}deg) translateY(-8px) scale3d(1.02, 1.02, 1.02)`;
    });

    heroSec.addEventListener('mouseleave', () => {
      heroCard.style.transform = '';
      heroCard.style.animation = 'heroCardFloat3D 6s ease-in-out infinite alternate';
    });
  }

  // Add 3D Tilt to all modern restructured cards
  const modernCards = document.querySelectorAll('.focus-card-horizontal, .pricing-card-luxury, .contact-card-premium, .step-item-card, .testimonial-card-white');
  modernCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      const rx = -y * 8;
      const ry = x * 8;
      card.style.transform = `perspective(800px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateY(-8px) scale3d(1.015, 1.015, 1.015)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
});
'''

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(code)

print("Appended enhanced 3D tilt to script.js")

