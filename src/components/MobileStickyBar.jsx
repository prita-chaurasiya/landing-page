import React from 'react';
import { ArrowRight, MessageCircle } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function MobileStickyBar() {
  return (
    <div className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-navy-950/95 border-t border-gold/30 backdrop-blur-xl px-4 py-2.5 shadow-[0_-8px_25px_rgba(6,16,40,0.8)]">
      <div className="flex items-center space-x-3">
        {/* WhatsApp Button */}
        <a
          href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI%20Secretariat,%20I%20want%20to%20join%20HRCI`}
          target="_blank"
          rel="noopener noreferrer"
          className="w-12 h-11 rounded-full border border-gold/40 bg-navy-900 text-gold flex items-center justify-center flex-shrink-0 shadow-sm"
          aria-label="WhatsApp Secretariat"
        >
          <MessageCircle className="w-5 h-5" />
        </a>

        {/* Join Now Primary Gold Button */}
        <a
          href="#membership-form"
          className="btn-gold-luxury flex-1 py-3 px-4 rounded-full text-xs sm:text-sm font-bold flex items-center justify-center space-x-2 shadow-gold-glow"
        >
          <span>Join HRCI Membership</span>
          <ArrowRight className="w-4 h-4" />
        </a>
      </div>
    </div>
  );
}

