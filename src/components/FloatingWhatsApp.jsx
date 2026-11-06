import React from 'react';
import { MessageCircle } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function FloatingWhatsApp() {
  return (
    <aside aria-label="WhatsApp Support" className="hidden md:block fixed bottom-6 right-6 z-40">
      <a
        href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI%20Secretariat`}
        target="_blank"
        rel="noopener noreferrer"
        className="group relative flex items-center justify-center w-14 h-14 rounded-full bg-gradient-to-tr from-gold-dark via-gold-light to-gold-dark text-navy-950 shadow-gold-glow transition-transform duration-300 hover:scale-110"
        aria-label="Chat on WhatsApp with HRCI Secretariat"
      >
        {/* Animated Gold Ripple Rings */}
        <span className="absolute inset-0 rounded-full border-2 border-gold animate-ping opacity-60 pointer-events-none" />
        <span className="absolute -inset-1.5 rounded-full border border-gold/40 animate-pulse pointer-events-none" />

        <MessageCircle className="w-7 h-7 fill-navy-950 text-navy-950 relative z-10" />

        {/* Hover Tooltip */}
        <span className="absolute right-16 px-3 py-1.5 rounded-xl bg-navy-950/95 border border-gold/40 text-ivory text-xs font-semibold whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none shadow-lg">
          Chat with HRCI Secretariat
        </span>
      </a>
    </aside>
  );
}

