import React, { useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { Check, ArrowRight, MessageCircle, ShieldCheck, Award, Star } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function Hero() {
  const canvasRef = useRef(null);

  // Subtle Floating Gold Dust Particles
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationFrameId;

    let width = (canvas.width = canvas.parentElement.offsetWidth);
    let height = (canvas.height = canvas.parentElement.offsetHeight);

    const onResize = () => {
      if (!canvas || !canvas.parentElement) return;
      width = canvas.width = canvas.parentElement.offsetWidth;
      height = canvas.height = canvas.parentElement.offsetHeight;
    };
    window.addEventListener('resize', onResize);

    const particleCount = 35;
    const particles = Array.from({ length: particleCount }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      radius: Math.random() * 1.5 + 0.5,
      vx: (Math.random() - 0.5) * 0.3,
      vy: -Math.random() * 0.5 - 0.15,
      alpha: Math.random() * 0.5 + 0.2,
    }));

    const render = () => {
      ctx.clearRect(0, 0, width, height);

      particles.forEach((p) => {
        p.y += p.vy;
        p.x += p.vx;

        if (p.y < 0) {
          p.y = height + 10;
          p.x = Math.random() * width;
        }
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(232, 190, 85, ${p.alpha})`;
        ctx.fill();
      });

      animationFrameId = requestAnimationFrame(render);
    };
    render();

    return () => {
      window.removeEventListener('resize', onResize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <section id="hero" className="relative bg-gradient-to-br from-[#12275A] via-[#173273] to-[#1E3F8C] text-white overflow-hidden pt-12 pb-20 lg:py-24">
      
      {/* 1. Very Faint Tricolor Corner Accent (Strictly Subtle) */}
      <div 
        className="absolute top-0 right-0 w-80 h-80 pointer-events-none opacity-10 overflow-hidden z-0"
        aria-hidden="true"
      >
        <svg viewBox="0 0 300 300" className="w-full h-full fill-none">
          <path d="M40,-40 C160,60 250,140 340,190" stroke="#FF9933" strokeWidth="6" strokeLinecap="round" />
          <path d="M60,-20 C180,80 270,160 360,210" stroke="#FFFFFF" strokeWidth="6" strokeLinecap="round" />
          <path d="M80,0 C200,100 290,180 380,230" stroke="#138808" strokeWidth="6" strokeLinecap="round" />
        </svg>
      </div>

      {/* 2. Soft Gold Ambient Light Rays */}
      <div 
        className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-96 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#E8BE55]/15 via-transparent to-transparent pointer-events-none" 
        aria-hidden="true" 
      />

      {/* 3. Gold Dust Particle Canvas */}
      <canvas 
        ref={canvasRef} 
        className="absolute inset-0 w-full h-full pointer-events-none z-10" 
      />

      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 relative z-20 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          
          {/* LEFT COLUMN: Text with Soft Dark Overlay Backdrop for Perfect Readability */}
          <motion.div 
            className="lg:col-span-7 flex flex-col space-y-6 text-left relative p-2 sm:p-4 rounded-2xl"
            initial={{ opacity: 0, y: 25 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Soft dark overlay backdrop behind text */}
            <div className="absolute inset-0 bg-[#0C1C40]/30 rounded-2xl backdrop-blur-[2px] -z-10 pointer-events-none" />

            {/* National Badge Pill */}
            <div className="inline-flex items-center">
              <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/10 border border-[#E8BE55]/40 backdrop-blur-md">
                <span className="w-2 h-2 rounded-full bg-[#E8BE55] animate-pulse" />
                <span className="text-xs sm:text-sm font-medium tracking-wide text-[#FAF8F3]">
                  {siteData.hero.badge}
                </span>
              </div>
            </div>

            {/* Headline: H1 64px on desktop */}
            <h1 className="font-heading font-bold text-4xl sm:text-5xl lg:text-[64px] tracking-tight leading-[1.08] text-white">
              <span>{siteData.hero.titlePrefix} </span>
              <br className="hidden sm:inline" />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#C9971C] via-[#F5D27A] to-[#E8BE55]">
                {siteData.hero.titleHighlight}
              </span>
            </h1>

            {/* Gold Ribbon Callout */}
            <div className="inline-flex">
              <div className="px-4 py-1.5 rounded-xl bg-gradient-to-r from-[#C9971C] to-[#E8BE55] text-[#12275A] font-heading font-bold text-xs sm:text-sm uppercase tracking-wider shadow-sm flex items-center space-x-2">
                <Award className="w-4 h-4 text-[#12275A]" />
                <span>{siteData.hero.goldRibbon}</span>
              </div>
            </div>

            {/* Subtext (min 16px, line-height 1.7) */}
            <p className="text-[#FAF8F3]/90 text-base sm:text-lg max-w-xl leading-[1.7] font-normal">
              {siteData.hero.subtitle}
            </p>

            {/* 3 Gold Check Pills */}
            <div className="flex flex-wrap gap-2.5 sm:gap-3 pt-1">
              {siteData.hero.checkPills.map((pill) => (
                <div 
                  key={pill} 
                  className="flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-[#FAF8F3] text-xs sm:text-sm font-medium backdrop-blur-sm"
                >
                  <div className="w-4 h-4 rounded-full bg-[#C9971C]/30 flex items-center justify-center text-[#E8BE55]">
                    <Check className="w-3 h-3 stroke-[3]" />
                  </div>
                  <span>{pill}</span>
                </div>
              ))}
            </div>

            {/* Primary & Secondary Action Buttons */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 pt-3">
              <a 
                href="#membership-form" 
                className="btn-gold-primary px-8 py-4 rounded-full text-sm sm:text-base font-bold flex items-center justify-center space-x-3 shadow-md group"
              >
                <span>{siteData.hero.primaryCta}</span>
                <ArrowRight className="w-5 h-5 transition-transform duration-300 group-hover:translate-x-1.5" />
              </a>

              <a 
                href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI,%20I%20want%20to%20know%20more%20about%20Membership`}
                target="_blank"
                rel="noopener noreferrer"
                className="px-7 py-4 rounded-full border-2 border-white/80 hover:border-[#E8BE55] hover:text-[#E8BE55] text-white text-sm sm:text-base font-semibold flex items-center justify-center space-x-2.5 backdrop-blur-sm hover:bg-white/10 transition-all duration-300 shadow-sm"
              >
                <MessageCircle className="w-5 h-5 text-[#E8BE55]" />
                <span>{siteData.hero.secondaryCta}</span>
              </a>
            </div>

            {/* Trust Badges Strip Under CTA */}
            <div className="pt-2 flex items-center space-x-4 text-xs text-[#FAF8F3]/75 font-medium">
              {siteData.hero.trustBadges.map((badge, idx) => (
                <React.Fragment key={badge}>
                  <div className="flex items-center space-x-1.5">
                    <ShieldCheck className="w-3.5 h-3.5 text-[#E8BE55]" />
                    <span>{badge}</span>
                  </div>
                  {idx < siteData.hero.trustBadges.length - 1 && (
                    <span className="text-white/30">•</span>
                  )}
                </React.Fragment>
              ))}
            </div>

          </motion.div>

          {/* RIGHT COLUMN: Lady Justice Artwork Composition */}
          <motion.div 
            className="lg:col-span-5 relative flex items-center justify-center"
            initial={{ opacity: 0, scale: 0.96 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            {/* Artwork Container */}
            <div className="relative w-full rounded-[20px] overflow-hidden border border-white/20 bg-white/5 backdrop-blur-md shadow-2xl p-2 sm:p-3">
              
              {/* Floating Pill Top Left */}
              <div className="absolute top-4 left-4 z-20 flex items-center space-x-2 px-3 py-1.5 rounded-full bg-[#12275A]/90 border border-[#E8BE55]/40 backdrop-blur-md text-[11px] sm:text-xs text-white shadow-md">
                <span className="text-[#E8BE55]">🛡️</span>
                <span className="font-semibold">Govt. Regd. NGO (MCA Sec 8)</span>
              </div>

              {/* Floating Pill Bottom Right */}
              <div className="absolute bottom-4 right-4 z-20 flex items-center space-x-1.5 px-3 py-1.5 rounded-full bg-[#12275A]/90 border border-[#E8BE55]/40 backdrop-blur-md text-[11px] sm:text-xs text-[#E8BE55] shadow-md font-bold">
                <Star className="w-3.5 h-3.5 fill-[#E8BE55]" />
                <span>70,000+ Members Pan-India</span>
              </div>

              {/* Ultra-HD Master Artwork */}
              <img 
                src="assets/images/hero_statue_ultra_hd_seamless.png" 
                alt="Golden Lady Justice, Indian Flag, Cheering Crowd and HRCI Peace Award Trophy" 
                className="w-full h-auto object-cover rounded-[16px] transition-transform duration-700 hover:scale-[1.02]"
                fetchpriority="high"
                loading="eager"
              />
            </div>
          </motion.div>

        </div>
      </div>
    </section>
  );
}
