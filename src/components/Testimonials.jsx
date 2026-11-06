import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Star, ChevronLeft, ChevronRight, Quote } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function Testimonials() {
  const [activeIndex, setActiveIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setActiveIndex((prev) => (prev + 1) % siteData.testimonials.length);
    }, 6000);
    return () => clearInterval(timer);
  }, []);

  const handlePrev = () => {
    setActiveIndex((prev) => (prev - 1 + siteData.testimonials.length) % siteData.testimonials.length);
  };

  const handleNext = () => {
    setActiveIndex((prev) => (prev + 1) % siteData.testimonials.length);
  };

  return (
    <section id="testimonials" className="py-14 lg:py-24 bg-[#FAF8F3] relative">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading Pattern */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-bold uppercase tracking-widest text-[#C9971C] block mb-2">
            VOICES OF CITIZEN CHAMPIONS
          </span>
          <h2 className="font-heading font-bold text-3xl sm:text-[40px] text-[#12275A] tracking-tight leading-tight">
            What Our Members Say
          </h2>
          <div className="w-16 h-1 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] mx-auto rounded-full mt-3.5 mb-4" />
          <p className="text-[#475569] text-base leading-relaxed">
            Real stories, real impact, and trusted experiences from verified advocates across 28 states.
          </p>
        </div>

        {/* Carousel Area with Navigation Buttons */}
        <div className="max-w-3xl mx-auto relative">
          
          <div className="relative min-h-[260px]">
            <AnimatePresence mode="wait">
              {siteData.testimonials.map((item, idx) => {
                if (idx !== activeIndex) return null;

                return (
                  <motion.div
                    key={item.name}
                    initial={{ opacity: 0, y: 15 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -15 }}
                    transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
                    className="white-card p-8 sm:p-10 relative"
                  >
                    <Quote className="absolute right-8 top-8 w-12 h-12 text-[#C9971C]/15 pointer-events-none" />

                    <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
                      {/* Avatar + Author Details */}
                      <div className="flex items-center space-x-4">
                        <div className="relative w-14 h-14 rounded-full p-0.5 bg-gradient-to-tr from-[#C9971C] to-[#E8BE55] shadow-sm flex-shrink-0">
                          <img
                            src={item.image}
                            alt={item.name}
                            className="w-full h-full rounded-full object-cover"
                            loading="lazy"
                          />
                        </div>

                        <div>
                          <h4 className="font-heading font-bold text-lg text-[#12275A]">
                            {item.name}
                          </h4>
                          <p className="text-xs font-semibold text-[#C9971C]">
                            {item.role} • {item.state}
                          </p>
                        </div>
                      </div>

                      {/* 5 Gold Stars */}
                      <div className="flex items-center space-x-1">
                        {Array.from({ length: item.stars }).map((_, s) => (
                          <Star
                            key={s}
                            className="w-4 h-4 fill-[#C9971C] text-[#C9971C]"
                          />
                        ))}
                      </div>
                    </div>

                    {/* Hindi Quote + English Translation */}
                    <div className="space-y-3 relative z-10 text-left">
                      <p className="font-devanagari text-base sm:text-lg text-[#12275A] font-semibold leading-relaxed">
                        "{item.quoteHi}"
                      </p>
                      <p className="text-sm sm:text-base text-[#475569] leading-relaxed">
                        "{item.quoteEn}"
                      </p>
                    </div>

                  </motion.div>
                );
              })}
            </AnimatePresence>
          </div>

          {/* Navigation Controls Below */}
          <div className="flex items-center justify-between mt-8">
            <div className="flex items-center space-x-2">
              {siteData.testimonials.map((_, i) => (
                <button
                  key={i}
                  onClick={() => setActiveIndex(i)}
                  className={`h-2 rounded-full transition-all duration-300 ${
                    i === activeIndex ? 'w-8 bg-[#C9971C]' : 'w-2 bg-[#ECE6D8] hover:bg-[#C9971C]/60'
                  }`}
                  aria-label={`Go to slide ${i + 1}`}
                />
              ))}
            </div>

            <div className="flex items-center space-x-2">
              <button
                onClick={handlePrev}
                className="w-10 h-10 rounded-full border border-[#ECE6D8] bg-white text-[#12275A] hover:bg-[#12275A] hover:text-white flex items-center justify-center transition-colors shadow-sm"
                aria-label="Previous Testimonial"
              >
                <ChevronLeft className="w-5 h-5" />
              </button>
              <button
                onClick={handleNext}
                className="w-10 h-10 rounded-full border border-[#ECE6D8] bg-white text-[#12275A] hover:bg-[#12275A] hover:text-white flex items-center justify-center transition-colors shadow-sm"
                aria-label="Next Testimonial"
              >
                <ChevronRight className="w-5 h-5" />
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
