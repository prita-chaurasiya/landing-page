import React, { useState, useEffect } from 'react';
import { motion, useInView } from 'framer-motion';
import { Users, MapPin, HeartHandshake, CalendarCheck, Award } from 'lucide-react';
import { siteData } from '../config/siteData';

function CountUpNumber({ target, suffix = '', duration = 2 }) {
  const [count, setCount] = useState(0);
  const ref = React.useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-50px" });

  useEffect(() => {
    if (!isInView || typeof target !== 'number') return;
    let start = 0;
    const end = target;
    const totalFrames = Math.round(duration * 60);
    let frame = 0;

    const timer = setInterval(() => {
      frame++;
      const progress = frame / totalFrames;
      const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      const current = Math.round(easeProgress * end);
      setCount(current);

      if (frame >= totalFrames) {
        clearInterval(timer);
        setCount(end);
      }
    }, 1000 / 60);

    return () => clearInterval(timer);
  }, [isInView, target, duration]);

  return (
    <span ref={ref} className="font-heading font-bold">
      {typeof target === 'number' ? count.toLocaleString('en-IN') : target}
      {suffix}
    </span>
  );
}

export default function StatsStrip() {
  const icons = [
    <Users className="w-5 h-5 text-[#E8BE55]" />,
    <MapPin className="w-5 h-5 text-[#E8BE55]" />,
    <HeartHandshake className="w-5 h-5 text-[#E8BE55]" />,
    <CalendarCheck className="w-5 h-5 text-[#E8BE55]" />,
    <Award className="w-5 h-5 text-[#E8BE55]" />
  ];

  return (
    <section className="relative z-30 -mt-10 px-4 sm:px-6 lg:px-8 max-w-[1200px] mx-auto">
      {/* Soft Navy Gradient Bar (#12275A → #1E3F8C) with 20px radius, gold accents */}
      <motion.div 
        className="rounded-[20px] bg-gradient-to-r from-[#12275A] via-[#173273] to-[#1E3F8C] border border-white/20 p-6 sm:p-8 text-white shadow-[0_15px_40px_rgba(18,39,90,0.18)]"
        initial={{ opacity: 0, y: 25 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-40px" }}
        transition={{ duration: 0.6 }}
      >
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6 divide-y md:divide-y-0 md:divide-x divide-white/15">
          
          {siteData.stats.map((item, idx) => (
            <div 
              key={item.id} 
              className={`flex flex-col items-center text-center px-3 ${
                idx > 0 ? 'pt-4 sm:pt-0' : ''
              } ${idx === 4 ? 'col-span-2 md:col-span-1' : ''}`}
            >
              <div className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center mb-2.5">
                {icons[idx]}
              </div>

              <div className="text-2xl sm:text-3xl font-bold font-heading text-white tracking-tight">
                {item.isStatic ? (
                  <span>{item.valText}</span>
                ) : (
                  <CountUpNumber target={item.number} suffix={item.suffix} />
                )}
              </div>

              <span className="text-xs sm:text-sm font-semibold text-[#E8BE55] tracking-wide mt-1">
                {item.label}
              </span>

              <span className="text-[11px] text-[#FAF8F3]/75 font-medium mt-0.5">
                {item.sublabel}
              </span>
            </div>
          ))}

        </div>
      </motion.div>
    </section>
  );
}
