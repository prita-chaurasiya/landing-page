import React from 'react';
import { motion } from 'framer-motion';
import { Building2, CalendarCheck, MapPin, ShieldCheck, Award } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function TrustStrip() {
  const icons = [
    <Building2 className="w-5 h-5 text-gold" />,
    <CalendarCheck className="w-5 h-5 text-gold" />,
    <MapPin className="w-5 h-5 text-gold" />,
    <ShieldCheck className="w-5 h-5 text-gold" />,
    <Award className="w-5 h-5 text-gold" />
  ];

  return (
    <section className="py-12 bg-navy-900 border-y border-gold/15">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div 
          className="rounded-[24px] bg-navy-950/90 border border-gold/30 p-6 sm:p-7 backdrop-blur-xl shadow-gold-glow"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 lg:gap-6 divide-y md:divide-y-0 md:divide-x divide-gold/15">
            {siteData.trustStrip.map((item, idx) => (
              <div 
                key={item.title}
                className={`flex flex-col items-center text-center px-2 py-2 sm:py-0 ${
                  idx > 0 ? 'pt-4 sm:pt-0' : ''
                } ${idx === 4 ? 'col-span-2 md:col-span-1' : ''}`}
              >
                <div className="w-10 h-10 rounded-full bg-gold/15 border border-gold/30 flex items-center justify-center mb-2 shadow-inner">
                  {icons[idx]}
                </div>
                <h4 className="font-heading font-bold text-sm text-ivory">
                  {item.title}
                </h4>
                <p className="text-xs text-gold/80 font-medium mt-0.5">
                  {item.subtitle}
                </p>
              </div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
}

