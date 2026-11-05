/**
 * HUMAN RIGHTS COUNCIL OF INDIA (HRCI) / भारतीय मानवाधिकार परिषद
 * SINGLE HIGH-CONVERTING CRO LANDING PAGE - VANILLA JS ENGINE
 * Zero dependencies, ultra-fast, cross-browser, accessible
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNav();
  initSmoothScroll();
  initScrollReveal();
  initHero3DParallax();
  init3DCardTilt();
  initCounters();
  initTestimonialSlider();
  initPlanSelectors();
  initVideoModal();
  initIdCardModal();
  initLeadForm();
  initFaqAccordion();
  initSocialProofToast();
  initBackToTop();
  initButtonRipples();
});

/* --------------------------------------------------------------------------
   1. STICKY NAVBAR WITH BACKDROP GLASSMORPHISM
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const navbar = document.getElementById('mainNavbar');
  if (!navbar) return;

  const handleScroll = () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* --------------------------------------------------------------------------
   2. MOBILE NAVIGATION DRAWER & EXIT CROSS (✕)
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const hamburger = document.getElementById('navHamburger');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const navList = document.getElementById('navbarList');

  if (!hamburger || !navList) return;

  function toggleMenu(forceClose = false) {
    if (forceClose) {
      hamburger.classList.remove('active');
      navList.classList.remove('open');
      document.body.classList.remove('drawer-open');
    } else {
      const isOpen = navList.classList.toggle('open');
      hamburger.classList.toggle('active', isOpen);
      document.body.classList.toggle('drawer-open', isOpen);
    }
  }

  hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMenu();
  });

  if (drawerCloseBtn) {
    drawerCloseBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleMenu(true);
    });
  }

  // Auto-close drawer when clicking any anchor link
  navList.addEventListener('click', (e) => {
    const anchor = e.target.closest('a');
    if (anchor && navList.classList.contains('open')) {
      toggleMenu(true);
    }
  });

  // Close when tapping outside the open drawer
  document.addEventListener('click', (e) => {
    if (navList.classList.contains('open') &&
        !navList.contains(e.target) &&
        !hamburger.contains(e.target)) {
      toggleMenu(true);
    }
  });
}

/* --------------------------------------------------------------------------
   3. IN-PAGE SMOOTH SCROLL WITH NAVBAR OFFSET
   -------------------------------------------------------------------------- */
function initSmoothScroll() {
  const navLinks = document.querySelectorAll('a[href^="#"]');

  navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (!targetId || targetId === '#') return;

      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const navbar = document.getElementById('mainNavbar');
        const navHeight = navbar ? navbar.offsetHeight : 46;
        const targetPos = targetEl.getBoundingClientRect().top + window.pageYOffset - navHeight - 10;

        window.scrollTo({
          top: targetPos,
          behavior: 'smooth'
        });

        // Update active class in navbar
        document.querySelectorAll('.nav-anchor').forEach(a => a.classList.remove('active-home'));
        if (this.classList.contains('nav-anchor')) {
          this.classList.add('active-home');
        }
      }
    });
  });
}

/* --------------------------------------------------------------------------
   4. STATS COUNTER ANIMATION (TABULAR NUMS & ZERO JITTER)
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
            // Ease out cubic
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
  }, { threshold: 0.2 });

  const statsSection = document.getElementById('stats');
  if (statsSection) {
    observer.observe(statsSection);
  }
}

/* --------------------------------------------------------------------------
   5. TESTIMONIALS SLIDER (TOUCH + AUTO-PLAY + ARROWS)
   -------------------------------------------------------------------------- */
function initTestimonialSlider() {
  const track = document.querySelector('.testimonials-track');
  const prevBtn = document.querySelector('.btn-testimonial-prev');
  const nextBtn = document.querySelector('.btn-testimonial-next');
  const cards = document.querySelectorAll('.testimonial-card');

  if (!track || !cards.length) return;

  let currentIndex = 0;
  let autoplayInterval;

  function getCardsPerView() {
    if (window.innerWidth < 640) return 1;
    if (window.innerWidth < 992) return 2;
    return 3;
  }

  function updateSlider() {
    const cardsPerView = getCardsPerView();
    const maxIndex = Math.max(0, cards.length - cardsPerView);
    if (currentIndex > maxIndex) currentIndex = maxIndex;

    const cardWidth = cards[0].offsetWidth;
    const gap = 14;
    const offset = currentIndex * (cardWidth + gap);
    track.style.transform = `translateX(-${offset}px)`;
  }

  function nextSlide() {
    const cardsPerView = getCardsPerView();
    const maxIndex = Math.max(0, cards.length - cardsPerView);
    if (currentIndex < maxIndex) {
      currentIndex++;
    } else {
      currentIndex = 0;
    }
    updateSlider();
  }

  function prevSlide() {
    const cardsPerView = getCardsPerView();
    const maxIndex = Math.max(0, cards.length - cardsPerView);
    if (currentIndex > 0) {
      currentIndex--;
    } else {
      currentIndex = maxIndex;
    }
    updateSlider();
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAutoplay(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAutoplay(); });

  window.addEventListener('resize', updateSlider);

  function startAutoplay() {
    autoplayInterval = setInterval(nextSlide, 5000);
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
   6. PLAN SELECTION BUTTONS -> FORM PRE-FILL & SMOOTH SCROLL
   -------------------------------------------------------------------------- */
function initPlanSelectors() {
  const planButtons = document.querySelectorAll('.btn-plan-select');
  const membershipSelect = document.getElementById('membershipType');
  const formCard = document.querySelector('.lead-form-card');

  planButtons.forEach(btn => {
    btn.addEventListener('click', function (e) {
      const planName = this.getAttribute('data-plan');
      if (membershipSelect && planName) {
        // Try to match select option
        for (let i = 0; i < membershipSelect.options.length; i++) {
          if (membershipSelect.options[i].value === planName ||
              membershipSelect.options[i].text.includes(planName.split(' ')[0])) {
            membershipSelect.selectedIndex = i;
            break;
          }
        }
      }

      // Highlight form with glowing flash
      if (formCard) {
        formCard.style.transition = 'box-shadow 0.3s ease, border-color 0.3s ease';
        formCard.style.borderColor = '#D90429';
        formCard.style.boxShadow = '0 0 0 4px rgba(217, 4, 41, 0.35), 0 20px 40px rgba(0, 0, 0, 0.2)';
        setTimeout(() => {
          formCard.style.borderColor = '';
          formCard.style.boxShadow = '';
        }, 1800);
      }
    });
  });
}

/* --------------------------------------------------------------------------
   7. YOUTUBE VIDEO POPUP MODAL
   -------------------------------------------------------------------------- */
function initVideoModal() {
  const videoCards = document.querySelectorAll('.video-card-item');
  const modal = document.getElementById('videoModal');
  const modalIframe = document.getElementById('videoIframe');
  const closeBtn = document.getElementById('videoModalCloseBtn');
  const modalTitle = document.getElementById('videoModalTitle');

  if (!modal || !modalIframe) return;

  // Video embed mappings
  const videoUrls = {
    'dQw4w9WgXcQ': 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?autoplay=1'
  };

  videoCards.forEach(card => {
    card.addEventListener('click', () => {
      const videoId = card.getAttribute('data-video-id') || 'dQw4w9WgXcQ';
      const title = card.getAttribute('data-video-title') || 'HRCI Official Event Video';
      
      if (modalTitle) modalTitle.textContent = title;
      modalIframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1`;
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
   8. OFFICIAL PVC MEMBERSHIP ID CARD MODAL
   -------------------------------------------------------------------------- */
function initIdCardModal() {
  const triggerBtns = document.querySelectorAll('.btn-trigger-id-modal');
  const modal = document.getElementById('idCardModal');
  const closeBtn = document.getElementById('idModalCloseBtn');
  const claimBtn = document.getElementById('btnClaimIdCard');

  if (!modal) return;

  function openModal() {
    // Dynamic preview from form input if entered
    const nameInput = document.getElementById('fullName');
    const roleInput = document.getElementById('profession');
    const pvcNameVal = document.querySelector('.pvc-detail-row:nth-child(1) .pvc-val');
    const pvcDesigVal = document.querySelector('.pvc-detail-row:nth-child(3) .pvc-val');

    if (nameInput && nameInput.value.trim() && pvcNameVal) {
      pvcNameVal.textContent = nameInput.value.trim().toUpperCase();
    }
    if (roleInput && roleInput.value.trim() && pvcDesigVal) {
      pvcDesigVal.textContent = roleInput.value.trim().toUpperCase();
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  triggerBtns.forEach(btn => btn.addEventListener('click', openModal));

  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  if (claimBtn) {
    claimBtn.addEventListener('click', () => {
      closeModal();
    });
  }

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
   9. MEMBERSHIP LEAD FORM (HIGH-CONVERSION WHATSAPP DISPATCH)
   -------------------------------------------------------------------------- */
function initLeadForm() {
  const form = document.getElementById('hrciLeadForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const fullName = document.getElementById('fullName').value.trim();
    const whatsappNumber = document.getElementById('whatsappNumber').value.trim();
    const cityState = document.getElementById('cityState').value.trim();
    const membershipType = document.getElementById('membershipType').value;
    const profession = document.getElementById('profession').value.trim();

    if (!fullName || fullName.length < 3) {
      alert('कृपया अपना पूरा नाम दर्ज करें (Please enter your full name).');
      return;
    }

    const cleanPhone = whatsappNumber.replace(/[^0-9]/g, '');
    if (cleanPhone.length < 10) {
      alert('कृपया 10 अंकों का वैध व्हाट्सएप नंबर दर्ज करें (Please enter a valid 10-digit WhatsApp number).');
      return;
    }

    if (!cityState) {
      alert('कृपया अपना शहर एवं राज्य दर्ज करें (Please enter your City & State).');
      return;
    }

    if (!membershipType) {
      alert('कृपया सदस्यता प्रकार का चयन करें (Please select a Membership Type).');
      return;
    }

    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `<span>पंजीकरण जारी है... (Processing)</span>`;

    setTimeout(() => {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;

      const randomAppId = 'HRCI-' + Math.floor(100000 + Math.random() * 900000);

      // Pre-filled WhatsApp message directly to HRCI Official Desk (+91 95944 41319)
      const waMsg = encodeURIComponent(
        `🏛️ *HRCI OFFICIAL MEMBERSHIP APPLICATION*\n\n` +
        `• *Application ID:* ${randomAppId}\n` +
        `• *Name:* ${fullName}\n` +
        `• *WhatsApp:* +91 ${cleanPhone.slice(-10)}\n` +
        `• *City / State:* ${cityState}\n` +
        `• *Membership Plan:* ${membershipType}\n` +
        `• *Profession:* ${profession || 'Citizen Advocate'}\n\n` +
        `Namaste HRCI Team, I have submitted my registration details online. Please provide verification steps & official PVC ID card details. Thank you!`
      );

      // Open WhatsApp in new tab
      window.open(`https://wa.me/919594441319?text=${waMsg}`, '_blank');

      alert(
        `🎉 आवेदन सफलतापूर्वक प्राप्त हुआ! (APPLICATION RECEIVED)\n\n` +
        `• आवेदन क्रमांक: ${randomAppId}\n` +
        `• आवेदक का नाम: ${fullName}\n` +
        `• चयनित सदस्यता: ${membershipType}\n\n` +
        `HRCI सदस्यता डेस्क (+91 95944 41319) से आपको व्हाट्सएप पर तत्काल पुष्टि प्राप्त होगी। धन्यवाद!`
      );

      form.reset();
    }, 600);
  });
}

/* --------------------------------------------------------------------------
   10. FAQ ACCORDION FUNCTIONALITY
   -------------------------------------------------------------------------- */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question-btn');
    const answerCollapse = item.querySelector('.faq-answer-collapse');

    if (!questionBtn || !answerCollapse) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other accordions
      faqItems.forEach(other => {
        if (other !== item) {
          other.classList.remove('active');
          const otherCollapse = other.querySelector('.faq-answer-collapse');
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
   11. LIVE SOCIAL PROOF TOAST
   -------------------------------------------------------------------------- */
function initSocialProofToast() {
  const toast = document.getElementById('socialProofToast');
  const toastName = document.getElementById('toastName');
  const toastAction = document.getElementById('toastAction');
  const toastCloseBtn = document.getElementById('toastCloseBtn');

  if (!toast) return;

  const joinEvents = [
    { name: 'Adv. Amit Sharma (Jaipur)', action: 'Joined Lifetime Membership • 2 मिनट पहले' },
    { name: 'Dr. Neha Verma (Lucknow)', action: 'Registered for Executive Wing • 4 मिनट पहले' },
    { name: 'Rohan Deshmukh (Pune)', action: 'Joined Annual Membership • अभी-अभी' },
    { name: 'Adv. Suresh Patel (Ahmedabad)', action: 'Joined Lifetime Membership • 7 मिनट पहले' },
    { name: 'Kavita Kumari (Patna)', action: 'Received Official PVC ID Card • 11 मिनट पहले' },
    { name: 'Manish Rawat (Dehradun)', action: 'Joined Lifetime Membership • 14 मिनट पहले' }
  ];

  let eventIndex = 0;

  function showNextToast() {
    const current = joinEvents[eventIndex];
    if (toastName) toastName.textContent = current.name;
    if (toastAction) toastAction.textContent = current.action;

    toast.classList.add('show');

    setTimeout(() => {
      toast.classList.remove('show');
    }, 4500);

    eventIndex = (eventIndex + 1) % joinEvents.length;
  }

  setTimeout(showNextToast, 3500);
  setInterval(showNextToast, 13000);

  if (toastCloseBtn) {
    toastCloseBtn.addEventListener('click', () => {
      toast.classList.remove('show');
    });
  }
}

/* --------------------------------------------------------------------------
   12. BACK TO TOP BUTTON
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
   13. BUTTON RIPPLE EFFECT
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
   14. BUTTER-SMOOTH SCROLL-REVEAL ENGINE (VANILLA AOS ALTERNATIVE)
   -------------------------------------------------------------------------- */
function initScrollReveal() {
  // Immediately reveal all above-the-fold hero elements
  document.querySelectorAll('#home [data-aos]').forEach(el => {
    el.classList.add('aos-animate');
  });
  const animatedElements = document.querySelectorAll('[data-aos]');
  if (!animatedElements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = parseInt(el.getAttribute('data-aos-delay') || '0', 10);
        
        if (delay > 0) {
          setTimeout(() => {
            el.classList.add('aos-animate');
          }, delay);
        } else {
          el.classList.add('aos-animate');
        }
        observer.unobserve(el);
      }
    });
  }, {
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.1
  });

  animatedElements.forEach(el => observer.observe(el));
}

/* --------------------------------------------------------------------------
   15. HERO 3D PARALLAX & AMBIENT DEPTH
   -------------------------------------------------------------------------- */
function initHero3DParallax() {
  const heroSection = document.querySelector('.hero-section');
  const heroCard = document.querySelector('.hero-composition-card');
  const heroRays = document.querySelector('.hero-light-rays');
  if (!heroSection || !heroCard) return;

  if (window.matchMedia('(pointer: fine)').matches && window.innerWidth > 992) {
    heroSection.addEventListener('mousemove', (e) => {
      const rect = heroSection.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;

      const tiltX = -y * 12;
      const tiltY = x * 15;
      const moveX = x * 18;
      const moveY = y * 14;

      heroCard.style.transform = `perspective(1000px) rotateX(${tiltX.toFixed(2)}deg) rotateY(${tiltY.toFixed(2)}deg) translate3d(${moveX.toFixed(1)}px, ${moveY.toFixed(1)}px, 15px)`;
      if (heroRays) {
        heroRays.style.transform = `translate3d(${-moveX * 1.5}px, ${-moveY * 1.5}px, 0)`;
      }
    });

    heroSection.addEventListener('mouseleave', () => {
      heroCard.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translate3d(0, 0, 0)';
      if (heroRays) {
        heroRays.style.transform = 'translate3d(0, 0, 0)';
      }
    });
  }
}

/* --------------------------------------------------------------------------
   16. INTERACTIVE 3D CARD TILT WITH DYNAMIC REFLECTION
   -------------------------------------------------------------------------- */
function init3DCardTilt() {
  if (!window.matchMedia('(pointer: fine)').matches || window.innerWidth < 992) return;

  const tiltTargets = document.querySelectorAll('.pricing-card, .lead-form-card, .why-feature-card, .contact-card-box, .stat-card, .about-img-frame');

  tiltTargets.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -5.5;
      const rotateY = ((x - centerX) / centerX) * 5.5;

      card.style.transform = `perspective(800px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-6px) scale3d(1.015, 1.015, 1.015)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0) scale3d(1, 1, 1)';
    });
  });
}
