import React from 'react';
import { motion } from 'framer-motion';
import { FileText, PhoneCall, CheckSquare, Award } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function MembershipProcess() {
  const stepIcons = [
    <FileText className="w-5 h-5 text-[#12275A]" />,
    <PhoneCall className="w-5 h-5 text-[#12275A]" />,
    <CheckSquare className="w-5 h-5 text-[#12275A]" />,
    <Award className="w-5 h-5 text-[#12275A]" />
  ];

  return (
    <section id="process" className="py-14 lg:py-24 bg-[#FAF8F3] relative overflow-hidden">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading Pattern */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-bold uppercase tracking-widest text-[#C9971C] block mb-2">
            FAST &amp; STREAMLINED
          </span>
          <h2 className="font-heading font-bold text-3xl sm:text-[40px] text-[#12275A] tracking-tight leading-tight">
            Simple Membership Process
          </h2>
          <div className="w-16 h-1 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] mx-auto rounded-full mt-3.5 mb-4" />
          <p className="text-[#475569] text-base leading-relaxed">
            Four simple steps to verify your credentials and become an official accredited member of HRCI.
          </p>
        </div>

        {/* 4 Equal Columns in a Horizontal Row with Dotted Gold Connecting Line */}
        <div className="relative">
          
          {/* Dotted Gold Connecting Line across the top of cards (Hidden on mobile) */}
          <div 
            className="hidden lg:block absolute top-7 left-16 right-16 gold-dotted-line z-0" 
            aria-hidden="true" 
          />

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-7 relative z-10">
            {siteData.processSteps.map((step, idx) => (
              <motion.div
                key={step.step}
                whileHover={{ y: -4 }}
                transition={{ duration: 0.25 }}
                className="white-card p-7 flex flex-col items-center text-center relative group"
              >
                {/* Numbered Gold Circle (1-4) with Line Icon */}
                <div className="relative mb-5">
                  <div className="w-14 h-14 rounded-full bg-gradient-to-tr from-[#C9971C] to-[#E8BE55] text-[#12275A] font-heading font-bold text-base flex items-center justify-center shadow-md">
                    {stepIcons[idx]}
                  </div>
                  <span className="absolute -top-1.5 -right-1.5 w-6 h-6 rounded-full bg-[#12275A] text-white text-xs font-bold flex items-center justify-center border-2 border-white shadow-sm">
                    {idx + 1}
                  </span>
                </div>

                {/* English Title & Hindi Subtitle */}
                <h3 className="font-heading font-bold text-lg text-[#12275A] group-hover:text-[#C9971C] transition-colors">
                  {step.title}
                </h3>
                <span className="font-devanagari text-xs text-[#C9971C] font-semibold mt-0.5 mb-2.5">
                  {step.titleHi}
                </span>

                {/* 1-2 Line Description (max 14px) */}
                <p className="text-sm text-[#475569] leading-relaxed">
                  {step.description}
                </p>

                {/* Step Marker Badge */}
                <div className="mt-5 pt-3 border-t border-[#ECE6D8] w-full text-[11px] text-slate-400 font-bold uppercase tracking-wider">
                  Step 0{idx + 1}
                </div>
              </motion.div>
            ))}
          </div>

        </div>

      </div>
    </section>
  );
}
