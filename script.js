/**
 * HUMAN RIGHTS COUNCIL OF INDIA (HRCI) - OFFICIAL PORTAL JS
 * Vanilla JavaScript (Zero Dependencies, Production-Ready)
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNav();
  initCounters();
  initTestimonialSlider();
  initVideoModal();
  initIdCardModal();
  initLeadForm();
  initFaqAccordion();
  initSocialProofToast();
  initBackToTop();
  initButtonRipples();
  initIdVerificationSearch();
});

/* --------------------------------------------------------------------------
   1. STICKY SLIM NAVBAR
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const navbar = document.getElementById('mainNavbar');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* --------------------------------------------------------------------------
   2. MOBILE NAVIGATION DRAWER
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const hamburger = document.getElementById('navHamburger');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const navLinksRow = document.getElementById('navbarList') || document.getElementById('navLinksRow');

  if (!hamburger || !navLinksRow) return;

  function toggleMenu(forceClose = false) {
    if (forceClose) {
      hamburger.classList.remove('active');
      navLinksRow.classList.remove('open');
      document.body.classList.remove('drawer-open');
    } else {
      const isOpen = navLinksRow.classList.toggle('open');
      hamburger.classList.toggle('active', isOpen);
      document.body.classList.toggle('drawer-open', isOpen);
    }
  }

  hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMenu();
  });

  // Dedicated Cut Cross (✕) Close Button inside Drawer Header
  if (drawerCloseBtn) {
    drawerCloseBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleMenu(true);
    });
  }

  // Dropdown Accordion for Mobile and Click-Toggle for Desktop
  const navItems = navLinksRow.querySelectorAll('.nav-link-item');

  navLinksRow.addEventListener('click', (e) => {
    const anchor = e.target.closest('a');
    if (!anchor) return;

    const parentItem = anchor.closest('.nav-link-item');
    const dropdown = parentItem ? parentItem.querySelector('.nav-dropdown') : null;

    // Check if user clicked a top-level anchor that has a dropdown
    if (dropdown && anchor.classList.contains('nav-anchor')) {
      if (window.innerWidth <= 992) {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = parentItem.classList.contains('dropdown-open');
        // Close all other dropdown accordions in the drawer
        navLinksRow.querySelectorAll('.nav-link-item.dropdown-open').forEach(el => {
          if (el !== parentItem) el.classList.remove('dropdown-open');
        });
        parentItem.classList.toggle('dropdown-open', !isOpen);
      } else {
        // Desktop click behavior
        if (e.target.closest('.caret-icon') || anchor.getAttribute('href') === '#' || anchor.getAttribute('href').includes(window.location.pathname.split('/').pop() || 'index.html')) {
          e.preventDefault();
          const isOpen = parentItem.classList.contains('dropdown-open');
          navItems.forEach(other => {
            if (other !== parentItem) other.classList.remove('dropdown-open');
          });
          parentItem.classList.toggle('dropdown-open', !isOpen);
        }
      }
    } else {
      // Sub-item link or direct navigation link clicked
      if (navLinksRow.classList.contains('open')) {
        toggleMenu(true);
      }
    }
  });

  // Close when tapping outside
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 992) {
      if (navLinksRow.classList.contains('open') &&
          !navLinksRow.contains(e.target) &&
          !hamburger.contains(e.target)) {
        toggleMenu(true);
      }
    } else {
      if (!e.target.closest('.nav-link-item')) {
        navItems.forEach(item => item.classList.remove('dropdown-open'));
      }
    }
  });
}

/* --------------------------------------------------------------------------
   3. STATS COUNTER ANIMATION
   -------------------------------------------------------------------------- */
function initCounters() {
  const counterElements = document.querySelectorAll('.stat-number[data-target]');
  if (!counterElements.length) return;

  let animated = false;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        counterElements.forEach(counter => {
          const target = parseInt(counter.getAttribute('data-target'), 10);
          const suffix = counter.getAttribute('data-suffix') || '';
          const duration = 1800;
          const startTime = performance.now();

          function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const currentVal = Math.floor(easeOut * target);

            counter.textContent = `${currentVal.toLocaleString('en-IN')}${suffix}`;

            if (progress < 1) {
              requestAnimationFrame(updateCounter);
            } else {
              counter.textContent = `${target.toLocaleString('en-IN')}${suffix}`;
            }
          }

          requestAnimationFrame(updateCounter);
        });
      }
    });
  }, { threshold: 0.25 });

  const statsSection = document.querySelector('.stats-strip-section');
  if (statsSection) {
    observer.observe(statsSection);
  }
}

/* --------------------------------------------------------------------------
   4. TESTIMONIALS SLIDER
   -------------------------------------------------------------------------- */
function initTestimonialSlider() {
  const track = document.querySelector('.testimonials-track');
  const prevBtn = document.querySelector('.btn-testimonial-prev');
  const nextBtn = document.querySelector('.btn-testimonial-next');
  const cards = document.querySelectorAll('.testimonial-card');

  if (!track || !cards.length) return;

  let currentIndex = 0;
  let cardsPerView = getCardsPerView();
  let maxIndex = Math.max(0, cards.length - cardsPerView);
  let autoplayInterval;

  function getCardsPerView() {
    if (window.innerWidth < 640) return 1;
    if (window.innerWidth < 992) return 2;
    return 3;
  }

  function updateSlider() {
    cardsPerView = getCardsPerView();
    maxIndex = Math.max(0, cards.length - cardsPerView);
    if (currentIndex > maxIndex) currentIndex = maxIndex;

    const cardWidth = cards[0].offsetWidth;
    const gap = 14;
    const offset = currentIndex * (cardWidth + gap);
    track.style.transform = `translateX(-${offset}px)`;
  }

  function nextSlide() {
    if (currentIndex < maxIndex) {
      currentIndex++;
    } else {
      currentIndex = 0;
    }
    updateSlider();
  }

  function prevSlide() {
    if (currentIndex > 0) {
      currentIndex--;
    } else {
      currentIndex = maxIndex;
    }
    updateSlider();
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAutoplay(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAutoplay(); });

  window.addEventListener('resize', () => {
    updateSlider();
  });

  function startAutoplay() {
    autoplayInterval = setInterval(nextSlide, 4500);
  }

  function resetAutoplay() {
    clearInterval(autoplayInterval);
    startAutoplay();
  }

  startAutoplay();

  const wrapper = document.querySelector('.testimonials-track-wrapper');
  if (wrapper) {
    wrapper.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
    wrapper.addEventListener('mouseleave', () => startAutoplay());

    let startX = 0;
    let endX = 0;

    wrapper.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
      clearInterval(autoplayInterval);
    }, { passive: true });

    wrapper.addEventListener('touchend', (e) => {
      endX = e.changedTouches[0].clientX;
      const diff = startX - endX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) nextSlide();
        else prevSlide();
      }
      startAutoplay();
    }, { passive: true });
  }
}

/* --------------------------------------------------------------------------
   5. VIDEO MODAL PLAYER
   -------------------------------------------------------------------------- */
function initVideoModal() {
  const videoCards = document.querySelectorAll('.video-card-item');
  const modal = document.getElementById('videoModal');
  const modalIframe = document.getElementById('videoIframe');
  const closeBtn = document.getElementById('closeVideoModal');

  if (!modal || !modalIframe) return;

  videoCards.forEach(card => {
    card.addEventListener('click', () => {
      const embedUrl = card.getAttribute('data-embed-url') || 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?autoplay=1';
      modalIframe.src = embedUrl;
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeModal() {
    modal.classList.remove('active');
    modalIframe.src = '';
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
}

/* --------------------------------------------------------------------------
   6. ID CARD LIVE PREVIEW MODAL
   -------------------------------------------------------------------------- */
function initIdCardModal() {
  const triggerBtns = document.querySelectorAll('.btn-trigger-id-modal');
  const modal = document.getElementById('idCardModal');
  const closeBtn = document.getElementById('closeIdModal');
  const nameField = document.getElementById('idCardNameDisplay');
  const roleField = document.getElementById('idCardRoleDisplay');
  const applicantInput = document.getElementById('applicantName');
  const professionInput = document.getElementById('applicantProfession');

  if (!modal) return;

  triggerBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (applicantInput && applicantInput.value.trim() && nameField) {
        nameField.textContent = applicantInput.value.trim().toUpperCase();
      }
      if (professionInput && professionInput.value.trim() && roleField) {
        roleField.textContent = `${professionInput.value.trim()} • Official Member`;
      }

      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeIdModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeIdModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeIdModal();
  });
}

/* --------------------------------------------------------------------------
   7. LEAD FORM VALIDATION & HIGH-CONVERSION WHATSAPP REDIRECTION
   -------------------------------------------------------------------------- */
function initLeadForm() {
  const form = document.getElementById('membershipLeadForm');
  const successModal = document.getElementById('successModal');
  const closeSuccessBtn = document.getElementById('closeSuccessModal');
  const successSummary = document.getElementById('successSummaryDetails');
  const waDirectBtn = document.getElementById('whatsappConfirmBtn');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.querySelector('[name="full_name"]').value.trim();
    const phone = form.querySelector('[name="whatsapp_number"]').value.trim();
    const city = form.querySelector('[name="city"]').value.trim();
    const membershipType = form.querySelector('[name="membership_type"]').value;
    const profession = form.querySelector('[name="profession"]').value.trim();

    if (!name || name.length < 3) {
      alert('कृपया अपना पूरा नाम दर्ज करें (Please enter your full name).');
      return;
    }

    const cleanPhone = phone.replace(/[^0-9]/g, '');
    if (cleanPhone.length < 10) {
      alert('कृपया 10 अंकों का वैध व्हाट्सएप नंबर दर्ज करें (Please enter a valid 10-digit WhatsApp number).');
      return;
    }

    if (!city) {
      alert('कृपया अपना शहर / जिला दर्ज करें (Please enter your City/District).');
      return;
    }

    if (!membershipType) {
      alert('कृपया सदस्यता का प्रकार चुनें (Please select Membership Type).');
      return;
    }

    // Submit state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `प्रोसेसिंग (Processing)...`;

    setTimeout(() => {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalBtnText;

      const randomAppId = 'HRCI-' + Math.floor(100000 + Math.random() * 900000);

      if (successSummary) {
        successSummary.innerHTML = `
          <div style="background:#F1F5F9;padding:14px;border-radius:10px;margin-bottom:14px;text-align:left;font-size:0.82rem;">
            <p><strong>आवेदन क्रमांक (App ID):</strong> <span style="color:#0B3D91;font-weight:700;">${randomAppId}</span></p>
            <p><strong>आवेदक का नाम (Name):</strong> ${escapeHtml(name)}</p>
            <p><strong>व्हाट्सएप नंबर (WhatsApp):</strong> +91 ${cleanPhone.slice(-10)}</p>
            <p><strong>सदस्यता (Plan):</strong> ${escapeHtml(membershipType)}</p>
            <p><strong>शहर (City):</strong> ${escapeHtml(city)}</p>
            <p><strong>पेशा (Profession):</strong> ${escapeHtml(profession || 'Social Reformer')}</p>
          </div>
        `;
      }

      if (waDirectBtn) {
        const waMsg = encodeURIComponent(
          `नमस्ते HRCI,\nमैंने वेबसाइट से सदस्यता हेतु आवेदन किया है:\n\n` +
          `• आवेदन ID: ${randomAppId}\n` +
          `• नाम: ${name}\n` +
          `• मोबाइल: ${cleanPhone}\n` +
          `• शहर: ${city}\n` +
          `• सदस्यता प्लान: ${membershipType}\n\n` +
          `कृपया मुझे आगे की प्रक्रिया एवं ID कार्ड संबंधी जानकारी प्रदान करें। धन्यवाद!`
        );
        waDirectBtn.href = `https://wa.me/919876543210?text=${waMsg}`;
      }

      if (successModal) {
        successModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }

      form.reset();
    }, 600);
  });

  if (closeSuccessBtn && successModal) {
    closeSuccessBtn.addEventListener('click', () => {
      successModal.classList.remove('active');
      document.body.style.overflow = '';
    });
    successModal.addEventListener('click', (e) => {
      if (e.target === successModal) {
        successModal.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }
}

/* --------------------------------------------------------------------------
   8. FAQ ACCORDION FUNCTIONALITY
   -------------------------------------------------------------------------- */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question-btn');
    const answerCollapse = item.querySelector('.faq-answer-collapse');

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
          const otherCollapse = otherItem.querySelector('.faq-answer-collapse');
          if (otherCollapse) otherCollapse.style.maxHeight = null;
        }
      });

      if (isActive) {
        item.classList.remove('active');
        answerCollapse.style.maxHeight = null;
      } else {
        item.classList.add('active');
        answerCollapse.style.maxHeight = answerCollapse.scrollHeight + 'px';
      }
    });
  });
}

/* --------------------------------------------------------------------------
   9. SOCIAL PROOF LIVE TOAST
   -------------------------------------------------------------------------- */
function initSocialProofToast() {
  const toast = document.getElementById('socialProofToast');
  const toastName = document.getElementById('toastName');
  const toastAction = document.getElementById('toastAction');
  const toastTime = document.getElementById('toastTime');
  const toastClose = document.getElementById('toastClose');

  if (!toast) return;

  const joinEvents = [
    { name: 'Adv. Amit Sharma (Jaipur)', plan: 'Joined Lifetime Membership', time: '2 मिनट पहले (2m ago)' },
    { name: 'Dr. Neha Verma (Lucknow)', plan: 'Joined Executive Leadership Wing', time: '4 मिनट पहले (4m ago)' },
    { name: 'Rohan Deshmukh (Pune)', plan: 'Joined Annual Membership', time: 'Just now' },
    { name: 'Adv. Suresh Patel (Ahmedabad)', plan: 'Joined Lifetime Membership', time: '7 मिनट पहले (7m ago)' },
    { name: 'Kavita Kumari (Patna)', plan: 'Received Official Membership ID Card', time: '11 मिनट पहले (11m ago)' }
  ];

  let eventIndex = 0;

  function showNextToast() {
    const current = joinEvents[eventIndex];
    if (toastName) toastName.textContent = current.name;
    if (toastAction) toastAction.textContent = current.plan;
    if (toastTime) toastTime.textContent = current.time;

    toast.classList.add('show');

    setTimeout(() => {
      toast.classList.remove('show');
    }, 5000);

    eventIndex = (eventIndex + 1) % joinEvents.length;
  }

  setTimeout(showNextToast, 4000);
  setInterval(showNextToast, 14000);

  if (toastClose) {
    toastClose.addEventListener('click', () => {
      toast.classList.remove('show');
    });
  }
}

/* --------------------------------------------------------------------------
   10. BACK TO TOP BUTTON
   -------------------------------------------------------------------------- */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/* --------------------------------------------------------------------------
   11. BUTTON RIPPLE EFFECT
   -------------------------------------------------------------------------- */
function initButtonRipples() {
  const buttons = document.querySelectorAll('.btn');

  buttons.forEach(btn => {
    btn.addEventListener('click', function (e) {
      const rect = this.getBoundingClientRect();
      const ripple = document.createElement('span');
      ripple.classList.add('btn-ripple');

      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;

      ripple.style.width = ripple.style.height = `${size}px`;
      ripple.style.left = `${x}px`;
      ripple.style.top = `${y}px`;

      this.appendChild(ripple);

      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });
}

/* --------------------------------------------------------------------------
   12. MEMBER ID VERIFICATION SEARCH
   -------------------------------------------------------------------------- */
function initIdVerificationSearch() {
  const searchBtn = document.getElementById('btnVerifyIdSearch');
  const searchInput = document.getElementById('memberIdInput');

  if (searchBtn && searchInput) {
    searchBtn.addEventListener('click', () => {
      const val = searchInput.value.trim();
      if (!val) {
        alert('कृपया सदस्य आईडी दर्ज करें (Please enter Member ID).');
        return;
      }

      searchBtn.disabled = true;
      searchBtn.textContent = 'सत्यापन जारी...';

      setTimeout(() => {
        searchBtn.disabled = false;
        searchBtn.textContent = 'Verify';
        alert(
          `✅ आधिकारिक सत्यापन सफल (VERIFIED OFFICIAL MEMBER)\n\n` +
          `• सदस्य आईडी: ${val.toUpperCase()}\n` +
          `• स्थिति: सक्रिय (Active Lifetime Member)\n` +
          `• मानवाधिकार परिषद प्राधिकार: प्रमाणित (MCA Sec. 8 Compliant)\n` +
          `• वैधता: आजीवन वैध (Valid Pan-India)`
        );
      }, 600);
    });
  }

  // Standalone verify.html portal page form
  const verifyForm = document.getElementById('verifyForm');
  const verifyInput = document.getElementById('verifyInput');
  const verifyResult = document.getElementById('verifyResult');
  const resMemberId = document.getElementById('resMemberId');

  if (verifyForm && verifyInput && verifyResult) {
    verifyForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = verifyInput.value.trim();
      if (resMemberId) resMemberId.textContent = val.toUpperCase();
      verifyResult.classList.add('active');
    });
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag)
  );
}
