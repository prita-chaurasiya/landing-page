import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Phone, Mail, Youtube, ArrowRight, Menu, X, MessageCircle } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 40);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <>
      {/* 1. TOP UTILITY STRIP (Authoritative Government-Grade Strip) */}
      <div className="bg-[#12275A] text-[#FAF8F3]/90 text-xs py-2 border-b border-[#FAF8F3]/10 hidden md:block">
        <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
          <div className="flex items-center space-x-6">
            <a 
              href={`tel:${siteData.organization.helplinePhone}`}
              className="flex items-center space-x-1.5 hover:text-[#E8BE55] transition-colors"
            >
              <Phone className="w-3.5 h-3.5 text-[#E8BE55]" />
              <span>Helpline: <strong className="text-white font-bold">{siteData.organization.helplinePhone}</strong></span>
            </a>
            <span className="text-[#FAF8F3]/30">•</span>
            <a 
              href={`mailto:${siteData.organization.email}`}
              className="flex items-center space-x-1.5 hover:text-[#E8BE55] transition-colors"
            >
              <Mail className="w-3.5 h-3.5 text-[#E8BE55]" />
              <span>{siteData.organization.email}</span>
            </a>
          </div>

          <div className="flex items-center space-x-4">
            <span className="text-[#FAF8F3]/80 font-medium text-[11px]">
              Registered under Govt. of India MCA – Section 8 Company
            </span>
            <span className="text-[#FAF8F3]/30">•</span>
            <span className="inline-flex items-center px-2 py-0.5 rounded-full bg-white/10 text-[#E8BE55] font-semibold text-[11px]">
              Estd. 11 Jan 2013
            </span>
            <span className="text-[#FAF8F3]/30">•</span>
            <a 
              href={siteData.organization.youtubeUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-1 bg-white/10 hover:bg-[#C9971C] hover:text-[#12275A] text-[#E8BE55] px-2.5 py-0.5 rounded-full transition-colors text-[11px] font-bold"
            >
              <Youtube className="w-3 h-3" />
              <span>HRCI4India</span>
            </a>
          </div>
        </div>
      </div>

      {/* 2. MAIN NAVBAR: Clean White/Ivory with Navy Text & Gold Join Button */}
      <header
        className={`sticky top-0 z-50 transition-all duration-300 ${
          isScrolled 
            ? 'bg-white/95 backdrop-blur-md border-b border-[#ECE6D8] shadow-[0_4px_20px_rgba(18,39,90,0.06)] py-3' 
            : 'bg-[#FAF8F3]/95 backdrop-blur-sm border-b border-[#ECE6D8] py-4'
        }`}
      >
        <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
          
          {/* Logo & Bilingual Brand Name */}
          <a href="#hero" className="flex items-center space-x-3 group">
            <div className="w-11 h-11 rounded-full p-0.5 bg-gradient-to-tr from-[#C9971C] to-[#E8BE55] shadow-sm flex-shrink-0">
              <div className="w-full h-full rounded-full bg-white flex items-center justify-center overflow-hidden">
                <img 
                  src="assets/images/hrci-navbar-logo.svg" 
                  alt="HRCI Emblem" 
                  className="w-8 h-8 object-contain"
                  onError={(e) => {
                    e.target.onerror = null;
                    e.target.src = "assets/images/hrci-emblem-exact.png";
                  }}
                />
              </div>
            </div>
            <div className="flex flex-col">
              <span className="font-heading font-bold text-sm sm:text-base text-[#12275A] tracking-tight group-hover:text-[#C9971C] transition-colors">
                HUMAN RIGHTS COUNCIL OF INDIA
              </span>
              <span className="font-devanagari text-[11px] sm:text-xs text-[#C9971C] font-semibold">
                भारतीय मानवाधिकार परिषद
              </span>
            </div>
          </a>

          {/* Desktop Navigation Links (Navy text with Gold Hover Underline) */}
          <nav className="hidden lg:flex items-center space-x-7">
            {siteData.navLinks.map((link) => (
              <a
                key={link.name}
                href={link.href}
                className="text-[#12275A] hover:text-[#C9971C] text-sm font-semibold tracking-wide transition-colors relative py-1 group"
              >
                {link.name}
                <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] transition-all duration-300 group-hover:w-full" />
              </a>
            ))}
          </nav>

          {/* Right Action: National Desk + Gold Join Button */}
          <div className="flex items-center space-x-4">
            <div className="hidden sm:flex flex-col text-right">
              <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">National Desk</span>
              <a href={`tel:${siteData.organization.helplinePhone}`} className="text-xs font-bold text-[#12275A] hover:text-[#C9971C] transition-colors">
                {siteData.organization.helplinePhone}
              </a>
            </div>

            <a
              href="#membership-form"
              className="btn-gold-primary px-5 py-2.5 rounded-full text-xs sm:text-sm font-bold flex items-center space-x-2 shadow-sm group cursor-pointer"
            >
              <span>Join Membership</span>
              <ArrowRight className="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" />
            </a>

            {/* Mobile Hamburger Toggle */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-2 rounded-xl border border-[#ECE6D8] text-[#12275A] hover:bg-[#FAF8F3] transition-colors"
              aria-label="Toggle Navigation Menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        {/* Mobile Dropdown Drawer */}
        <AnimatePresence>
          {mobileMenuOpen && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="lg:hidden bg-white border-b border-[#ECE6D8] shadow-lg overflow-hidden"
            >
              <div className="max-w-[1200px] mx-auto px-5 py-6 space-y-4">
                <div className="text-xs text-slate-500 border-b border-[#ECE6D8] pb-2 font-medium">
                  {siteData.organization.registrationBadge}
                </div>

                <div className="grid grid-cols-2 gap-3 pt-2">
                  {siteData.navLinks.map((link) => (
                    <a
                      key={link.name}
                      href={link.href}
                      onClick={() => setMobileMenuOpen(false)}
                      className="px-3 py-2 rounded-xl text-sm font-semibold text-[#12275A] hover:bg-[#FAF8F3] hover:text-[#C9971C] transition-colors"
                    >
                      {link.name}
                    </a>
                  ))}
                </div>

                <div className="pt-4 border-t border-[#ECE6D8] flex flex-col space-y-3">
                  <a
                    href="#membership-form"
                    onClick={() => setMobileMenuOpen(false)}
                    className="btn-gold-primary w-full py-3 rounded-full text-sm font-bold text-center flex items-center justify-center space-x-2 shadow-sm"
                  >
                    <span>Join HRCI Membership</span>
                    <ArrowRight className="w-4 h-4" />
                  </a>

                  <a
                    href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="w-full py-2.5 rounded-full border-2 border-[#12275A] text-[#12275A] text-sm font-bold flex items-center justify-center space-x-2 hover:bg-[#12275A] hover:text-white transition-colors"
                  >
                    <MessageCircle className="w-4 h-4 text-[#C9971C]" />
                    <span>WhatsApp Secretariat</span>
                  </a>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </header>
    </>
  );
}
