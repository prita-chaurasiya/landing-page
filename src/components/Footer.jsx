import React from 'react';
import { Phone, MessageCircle, Globe, Youtube, Facebook, Instagram, Linkedin, Shield, Heart } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function Footer() {
  return (
    <footer id="footer" className="bg-navy-950 text-ivory border-t border-gold/20 pt-16 pb-12 relative overflow-hidden">
      
      {/* Background Subtle Ambient Glow */}
      <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[800px] h-[300px] bg-gold/5 blur-[160px] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Top Direct Action Banner */}
        <div className="rounded-[24px] bg-navy-900 border border-gold/30 p-6 sm:p-8 mb-12 flex flex-col md:flex-row items-center justify-between gap-6 shadow-navy-card">
          <div className="flex items-center space-x-4 text-center md:text-left">
            <div className="w-12 h-12 rounded-2xl bg-gold/15 border border-gold/30 flex items-center justify-center text-gold flex-shrink-0">
              <Shield className="w-6 h-6" />
            </div>
            <div>
              <h4 className="font-heading font-black text-lg sm:text-xl text-ivory">
                Connect Directly with National Secretariat
              </h4>
              <p className="text-xs text-ivory-400 mt-0.5">
                Available 24/7 for citizen legal grievances and membership verification.
              </p>
            </div>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-3">
            <a
              href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI%20Secretariat`}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-gold-luxury px-6 py-3 rounded-full text-xs sm:text-sm font-bold flex items-center space-x-2 shadow-gold-sm"
            >
              <MessageCircle className="w-4 h-4" />
              <span>Chat on WhatsApp</span>
            </a>

            <a
              href={`tel:${siteData.organization.helplinePhone}`}
              className="px-5 py-3 rounded-full border border-gold/40 text-gold hover:bg-gold/10 text-xs sm:text-sm font-bold flex items-center space-x-2 transition-colors"
            >
              <Phone className="w-4 h-4" />
              <span>Call Us: {siteData.organization.helplinePhone}</span>
            </a>
          </div>
        </div>

        {/* 4 Columns Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-gold/15">
          
          {/* Col 1: Organization Details & Seal */}
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-gold-dark to-gold-light shadow-gold-sm">
                <div className="w-full h-full rounded-full bg-navy-950 flex items-center justify-center overflow-hidden">
                  <img 
                    src="assets/images/hrci-navbar-logo.svg" 
                    alt="HRCI Seal" 
                    className="w-8 h-8 object-contain"
                    onError={(e) => {
                      e.target.onerror = null;
                      e.target.src = "assets/images/hrci-emblem-exact.png";
                    }}
                  />
                </div>
              </div>
              <div className="flex flex-col">
                <span className="font-heading font-bold text-sm tracking-tight text-ivory">
                  HRCI NATIONAL
                </span>
                <span className="font-devanagari text-[11px] text-gold font-medium">
                  भारतीय मानवाधिकार परिषद
                </span>
              </div>
            </div>

            <p className="text-xs text-ivory-400 leading-relaxed">
              {siteData.organization.registrationBadge}
            </p>

            <div className="text-xs text-gold font-mono font-semibold">
              CIN: {siteData.organization.cinNumber}
            </div>

            <div className="pt-1 flex items-center space-x-2 text-xs text-ivory-300">
              <Globe className="w-4 h-4 text-gold" />
              <a href="https://www.hrcofindia.org" target="_blank" rel="noopener noreferrer" className="hover:text-gold transition-colors">
                {siteData.organization.website}
              </a>
            </div>
          </div>

          {/* Col 2: Quick In-Page Jumps */}
          <div>
            <h5 className="font-heading font-bold text-sm text-gold uppercase tracking-wider mb-4">
              Quick Links
            </h5>
            <ul className="space-y-2.5 text-xs text-ivory-300">
              {siteData.navLinks.map((link) => (
                <li key={link.name}>
                  <a href={link.href} className="hover:text-gold transition-colors flex items-center space-x-1.5">
                    <span className="text-gold/40">›</span>
                    <span>{link.name}</span>
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Col 3: Secretariat Addresses */}
          <div>
            <h5 className="font-heading font-bold text-sm text-gold uppercase tracking-wider mb-4">
              Headquarters &amp; Office
            </h5>
            <div className="space-y-3 text-xs text-ivory-300">
              <div>
                <strong className="text-ivory block mb-0.5">National Headquarters:</strong>
                <p className="text-ivory-400 leading-relaxed">{siteData.organization.addressDelhi}</p>
              </div>
              <div>
                <strong className="text-ivory block mb-0.5">Western Office:</strong>
                <p className="text-ivory-400 leading-relaxed">{siteData.organization.addressMumbai}</p>
              </div>
              <div>
                <strong className="text-ivory block mb-0.5">Secretariat Email:</strong>
                <a href={`mailto:${siteData.organization.email}`} className="text-gold hover:underline">
                  {siteData.organization.email}
                </a>
              </div>
            </div>
          </div>

          {/* Col 4: Follow Us & Legal Standing */}
          <div>
            <h5 className="font-heading font-bold text-sm text-gold uppercase tracking-wider mb-4">
              Follow Us
            </h5>
            <p className="text-xs text-ivory-400 mb-4 leading-relaxed">
              Stay connected with our national human rights missions, legal camps, and awards.
            </p>

            <div className="flex items-center space-x-3 mb-6">
              <a
                href={siteData.organization.youtubeUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="w-9 h-9 rounded-full bg-navy-900 border border-gold/30 text-gold hover:bg-gold hover:text-navy-950 flex items-center justify-center transition-all duration-300 shadow-sm"
                aria-label="YouTube"
              >
                <Youtube className="w-4 h-4" />
              </a>
              <a
                href="https://facebook.com"
                target="_blank"
                rel="noopener noreferrer"
                className="w-9 h-9 rounded-full bg-navy-900 border border-gold/30 text-gold hover:bg-gold hover:text-navy-950 flex items-center justify-center transition-all duration-300 shadow-sm"
                aria-label="Facebook"
              >
                <Facebook className="w-4 h-4" />
              </a>
              <a
                href="https://instagram.com"
                target="_blank"
                rel="noopener noreferrer"
                className="w-9 h-9 rounded-full bg-navy-900 border border-gold/30 text-gold hover:bg-gold hover:text-navy-950 flex items-center justify-center transition-all duration-300 shadow-sm"
                aria-label="Instagram"
              >
                <Instagram className="w-4 h-4" />
              </a>
              <a
                href="https://linkedin.com"
                target="_blank"
                rel="noopener noreferrer"
                className="w-9 h-9 rounded-full bg-navy-900 border border-gold/30 text-gold hover:bg-gold hover:text-navy-950 flex items-center justify-center transition-all duration-300 shadow-sm"
                aria-label="LinkedIn"
              >
                <Linkedin className="w-4 h-4" />
              </a>
            </div>

            <div className="p-3 rounded-xl bg-navy-900/80 border border-gold/20 text-[11px] text-ivory-400">
              <span className="font-bold text-gold block mb-0.5">Govt. of India Section 8</span>
              A Non-Profit Entity dedicated to constitutional human rights &amp; social welfare.
            </div>
          </div>

        </div>

        {/* Bottom Bar: Copyright + Privacy/Terms */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-ivory-400 gap-4">
          <p>
            © 2013–2026 <strong className="text-ivory">Human Rights Council of India (HRCI)</strong> / भारतीय मानवाधिकार परिषद. All Rights Reserved.
          </p>

          <div className="flex items-center space-x-6">
            <a href="#hero" className="hover:text-gold transition-colors">Privacy Policy</a>
            <span className="text-gold/30">•</span>
            <a href="#hero" className="hover:text-gold transition-colors">Terms of Membership</a>
            <span className="text-gold/30">•</span>
            <a href="#hero" className="hover:text-gold transition-colors">Refund &amp; Legal Policy</a>
          </div>
        </div>

      </div>
    </footer>
  );
}

