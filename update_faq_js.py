# update_faq_js.py

js_addon = """
/* FAQ MODERN ACCORDION HANDLER */
document.addEventListener('DOMContentLoaded', () => {
  const modernFaqButtons = document.querySelectorAll('.faq-modern-btn');
  modernFaqButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item-modern');
      if (!item) return;
      const answer = item.querySelector('.faq-modern-answer');
      const icon = btn.querySelector('.faq-toggle-icon');
      const isExpanded = item.classList.contains('active');

      // Close all other items
      document.querySelectorAll('.faq-item-modern').forEach(other => {
        other.classList.remove('active');
        const otherAns = other.querySelector('.faq-modern-answer');
        const otherIco = other.querySelector('.faq-toggle-icon');
        if (otherAns) otherAns.style.display = 'none';
        if (otherIco) otherIco.textContent = '+';
        const otherBtn = other.querySelector('.faq-modern-btn');
        if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
      });

      if (!isExpanded) {
        item.classList.add('active');
        if (answer) answer.style.display = 'block';
        if (icon) icon.textContent = '✕';
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });
});
"""

with open('script.js', 'a', encoding='utf-8') as f:
    f.write('\n' + js_addon)

print("Updated script.js with modern FAQ accordion handler successfully!")

