import React from 'react';
import { motion } from 'framer-motion';
import { Scale, GraduationCap, HeartHandshake, Calendar, Users, CreditCard } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function FocusAreas() {
  const iconMap = {
    Scale: <Scale className="w-6 h-6 text-[#C9971C]" />,
    GraduationCap: <GraduationCap className="w-6 h-6 text-[#C9971C]" />,
    HeartHandshake: <HeartHandshake className="w-6 h-6 text-[#C9971C]" />,
    Calendar: <Calendar className="w-6 h-6 text-[#C9971C]" />,
    Users: <Users className="w-6 h-6 text-[#C9971C]" />,
    IdCard: <CreditCard className="w-6 h-6 text-[#C9971C]" />
  };

  return (
    <section id="focus-areas" className="py-14 lg:py-24 bg-white relative">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading Pattern */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-bold uppercase tracking-widest text-[#C9971C] block mb-2">
            KEY DOMAINS OF ACTION
          </span>
          <h2 className="font-heading font-bold text-3xl sm:text-[40px] text-[#12275A] tracking-tight leading-tight">
            Our Focus Areas
          </h2>
          <div className="w-16 h-1 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] mx-auto rounded-full mt-3.5 mb-4" />
          <p className="text-[#475569] text-base leading-relaxed">
            Delivering constitutional rights awareness, free legal advisory, and socio-economic welfare through grassroots chapters nationwide.
          </p>
        </div>

        {/* 6 Cards Grid: Pure White, 1px Border #ECE6D8, 20px Radius, 28px Gaps */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-7">
          {siteData.focusAreas.map((item, idx) => (
            <motion.div
              key={item.title}
              whileHover={{ y: -4 }}
              transition={{ duration: 0.25 }}
              className="white-card p-8 flex flex-col justify-between group"
            >
              <div>
                {/* Icon Container with subtle gold accent */}
                <div className="w-13 h-13 rounded-2xl bg-[#FAF8F3] border border-[#ECE6D8] flex items-center justify-center mb-6 group-hover:border-[#C9971C]/50 transition-colors shadow-sm w-12 h-12">
                  {iconMap[item.icon]}
                </div>

                <h3 className="font-heading font-bold text-lg text-[#12275A] group-hover:text-[#C9971C] transition-colors">
                  {item.title}
                </h3>
                <h4 className="font-devanagari text-xs text-[#C9971C] font-semibold mt-0.5 mb-3">
                  {item.titleHi}
                </h4>

                <p className="text-base text-[#475569] leading-[1.7]">
                  {item.description}
                </p>
              </div>

              {/* Bottom Subtle Indicator */}
              <div className="mt-6 pt-4 border-t border-[#ECE6D8] flex items-center justify-between text-xs text-slate-400 font-medium">
                <span>Recognized Initiative</span>
                <span className="font-bold text-[#12275A]">0{idx + 1}</span>
              </div>
            </motion.div>
          ))}
        </div>

      </div>
    </section>
  );
}
