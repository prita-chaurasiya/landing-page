import React from 'react';
import { ArrowRight, MessageCircle, Shield } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function MidPageCtaBand() {
  return (
    <section className="py-16 bg-gradient-to-r from-[#12275A] via-[#173273] to-[#1E3F8C] text-white relative overflow-hidden">
      {/* Subtle gold ambient glow */}
      <div className="absolute top-0 right-1/4 w-96 h-96 bg-[#E8BE55]/10 rounded-full blur-3xl pointer-events-none" />

      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="flex flex-col lg:flex-row items-center justify-between gap-8 text-center lg:text-left">
          
          <div className="max-w-2xl space-y-3">
            <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-white/10 text-[#E8BE55] text-xs font-bold uppercase tracking-wider">
              <Shield className="w-3.5 h-3.5" />
              <span>NATIONWIDE CITIZEN ALLIANCE</span>
            </div>
            
            <h2 className="font-heading font-bold text-3xl sm:text-4xl text-white tracking-tight leading-tight">
              Join 70,000+ Members Making a Difference
            </h2>

            <p className="text-[#FAF8F3]/85 text-base sm:text-lg leading-relaxed">
              Stand up for justice, equality, and civil rights. Get an official membership ID card and lead social initiatives in your district.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center gap-4 flex-shrink-0">
            <a
              href="#membership-form"
              className="btn-gold-primary px-8 py-4 rounded-full text-sm sm:text-base font-bold flex items-center justify-center space-x-2.5 shadow-lg group"
            >
              <span>Join HRCI Membership Now</span>
              <ArrowRight className="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" />
            </a>

            <a
              href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI%20Secretariat`}
              target="_blank"
              rel="noopener noreferrer"
              className="px-6 py-4 rounded-full border-2 border-white/80 hover:border-[#E8BE55] hover:text-[#E8BE55] text-white text-sm sm:text-base font-semibold flex items-center justify-center space-x-2 transition-colors"
            >
              <MessageCircle className="w-4 h-4 text-[#E8BE55]" />
              <span>WhatsApp Us</span>
            </a>
          </div>

        </div>
      </div>
    </section>
  );
}
