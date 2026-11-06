import React from 'react';
import { motion } from 'framer-motion';
import { Check, Shield, Award, Users } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function AboutWhyJoin() {
  return (
    <section id="about" className="py-14 lg:py-24 bg-[#FAF8F3] relative">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading Pattern */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-bold uppercase tracking-widest text-[#C9971C] block mb-2">
            INSTITUTIONAL PROFILE
          </span>
          <h2 className="font-heading font-bold text-3xl sm:text-[40px] text-[#12275A] tracking-tight leading-tight">
            About HRCI &amp; Our Mission
          </h2>
          <div className="w-16 h-1 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] mx-auto rounded-full mt-3.5 mb-4" />
          <p className="text-[#475569] text-base leading-relaxed">
            A national, non-political, and secular NGO operating under MCA Section 8 for constitutional rights and public welfare.
          </p>
        </div>

        {/* 2 Clean White Cards Grid (28px gap) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-7 items-stretch">
          
          {/* Card 1: About HRCI (7 Columns) */}
          <motion.div 
            whileHover={{ y: -4 }}
            transition={{ duration: 0.25 }}
            className="lg:col-span-7 white-card p-8 sm:p-9 flex flex-col justify-between"
          >
            <div>
              {/* Hands holding sapling image */}
              <div className="relative rounded-2xl overflow-hidden border border-[#ECE6D8] shadow-sm mb-6 h-56 sm:h-64">
                <img 
                  src="assets/images/hands-plant.jpg" 
                  alt="Hands holding sapling - Protecting Human Dignity" 
                  className="w-full h-full object-cover transition-transform duration-700 hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#12275A]/80 via-transparent to-transparent" />
                <div className="absolute bottom-3 left-3 right-3 text-center">
                  <span className="text-xs font-bold text-[#E8BE55] uppercase tracking-wider bg-[#12275A]/90 px-3.5 py-1 rounded-full border border-white/20">
                    13+ Years of Nationwide Service
                  </span>
                </div>
              </div>

              <div className="flex items-center space-x-2 mb-2">
                <span className="text-xs font-bold text-[#C9971C] uppercase tracking-wider">FOUNDED 11 JAN 2013</span>
                <span className="text-slate-300">•</span>
                <span className="text-xs text-slate-500 font-devanagari font-medium">पंजीकृत गैर-सरकारी संस्था</span>
              </div>

              <h3 className="font-heading font-bold text-2xl text-[#12275A] mb-3">
                Upholding Civil Liberties &amp; Justice
              </h3>

              <p className="text-base text-[#475569] leading-[1.7]">
                {siteData.about.description}
              </p>
            </div>

            <div className="pt-6 mt-6 border-t border-[#ECE6D8] flex flex-wrap gap-3 text-xs text-slate-600 font-medium">
              <span className="px-3 py-1.5 rounded-xl bg-[#FAF8F3] border border-[#ECE6D8] flex items-center space-x-1.5">
                <Shield className="w-3.5 h-3.5 text-[#C9971C]" />
                <span className="text-[#12275A] font-bold">MCA Section 8 Company</span>
              </span>
              <span className="px-3 py-1.5 rounded-xl bg-[#FAF8F3] border border-[#ECE6D8] flex items-center space-x-1.5">
                <Users className="w-3.5 h-3.5 text-[#C9971C]" />
                <span className="text-[#12275A] font-bold">28 States Pan-India</span>
              </span>
            </div>
          </motion.div>

          {/* Card 2: Why Join HRCI? (5 Columns) */}
          <motion.div 
            whileHover={{ y: -4 }}
            transition={{ duration: 0.25 }}
            className="lg:col-span-5 white-card p-8 sm:p-9 flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-12 h-12 rounded-2xl bg-[#FAF8F3] border border-[#ECE6D8] flex items-center justify-center text-[#C9971C] shadow-sm flex-shrink-0">
                  <Award className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="font-heading font-bold text-2xl text-[#12275A]">
                    Why Join HRCI?
                  </h3>
                  <p className="text-xs text-slate-500">
                    National standing &amp; institutional credentials.
                  </p>
                </div>
              </div>

              {/* Checklist with Gold Checkmarks */}
              <div className="space-y-4">
                {siteData.about.whyJoinList.map((item, idx) => (
                  <div 
                    key={idx}
                    className="flex items-start space-x-3 p-3.5 rounded-xl bg-[#FAF8F3] border border-[#ECE6D8]"
                  >
                    <div className="w-5 h-5 rounded-full bg-[#C9971C] flex items-center justify-center text-white flex-shrink-0 mt-0.5 shadow-sm">
                      <Check className="w-3.5 h-3.5 stroke-[3]" />
                    </div>
                    <p className="text-sm sm:text-[15px] text-[#475569] leading-snug font-medium">
                      {item}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            <div className="pt-6 mt-6 border-t border-[#ECE6D8]">
              <a
                href="#membership-form"
                className="btn-gold-primary w-full py-3.5 rounded-full text-sm font-bold flex items-center justify-center space-x-2 shadow-sm"
              >
                <span>Apply for Membership Today</span>
                <span className="text-[#12275A]">→</span>
              </a>
            </div>
          </motion.div>

        </div>

      </div>
    </section>
  );
}
