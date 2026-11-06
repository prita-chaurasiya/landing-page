import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Plus, HelpCircle } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function FaqSection() {
  const [openIndex, setOpenIndex] = useState(0);

  const toggle = (idx) => {
    setOpenIndex(openIndex === idx ? null : idx);
  };

  return (
    <section id="faq" className="py-20 bg-navy-900 relative">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="text-center mb-12">
          <div className="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-navy-950 border border-gold/30 text-gold text-xs font-bold uppercase tracking-wider mb-4 shadow-sm">
            <HelpCircle className="w-3.5 h-3.5" />
            <span>FREQUENTLY ASKED QUESTIONS</span>
          </div>
          <h2 className="font-heading font-black text-3xl sm:text-4xl text-ivory tracking-tight">
            Frequently Asked <span className="text-gold-gradient">Questions</span>
          </h2>
          <p className="mt-2 text-ivory-300 text-sm">
            Quick answers to common questions about HRCI Membership &amp; Citizen Rights.
          </p>
        </div>

        {/* Accordion List */}
        <div className="space-y-3.5">
          {siteData.faqs.map((faq, idx) => {
            const isOpen = openIndex === idx;

            return (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 15 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: idx * 0.05 }}
                className={`rounded-[20px] transition-all duration-300 border overflow-hidden ${
                  isOpen
                    ? 'bg-navy-950/95 border-gold shadow-gold-sm'
                    : 'bg-navy-950/60 border-gold/20 hover:border-gold/40'
                }`}
              >
                <button
                  onClick={() => toggle(idx)}
                  className="w-full px-6 py-4 sm:py-5 flex items-center justify-between text-left space-x-4 cursor-pointer focus:outline-none"
                  aria-expanded={isOpen}
                >
                  <div className="flex flex-col">
                    <span className="font-heading font-bold text-sm sm:text-base text-ivory">
                      {faq.questionEn}
                    </span>
                    <span className="font-devanagari text-xs text-gold/90 font-medium mt-0.5">
                      {faq.questionHi}
                    </span>
                  </div>

                  {/* + rotating to x */}
                  <div className={`w-8 h-8 rounded-full border border-gold/30 flex items-center justify-center flex-shrink-0 transition-all duration-300 ${
                    isOpen ? 'bg-gold text-navy-950 rotate-45' : 'bg-navy-900 text-gold'
                  }`}>
                    <Plus className="w-4 h-4" />
                  </div>
                </button>

                <AnimatePresence>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: 'auto', opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.3 }}
                      className="overflow-hidden"
                    >
                      <div className="px-6 pb-6 pt-2 border-t border-gold/15 space-y-2.5">
                        <p className="text-xs sm:text-sm text-ivory-200 leading-relaxed font-normal">
                          {faq.answerEn}
                        </p>
                        <p className="font-devanagari text-xs text-gold/90 leading-relaxed font-normal">
                          {faq.answerHi}
                        </p>
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>
            );
          })}
        </div>

        {/* View All FAQs Button */}
        <div className="mt-10 text-center">
          <a
            href={`https://wa.me/${siteData.organization.whatsappNumber}?text=Hello%20HRCI,%20I%20have%20a%20question%20about%20membership`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center space-x-2 px-6 py-3 rounded-full border border-gold/40 text-gold hover:bg-gold hover:text-navy-950 font-bold text-xs sm:text-sm transition-all duration-300"
          >
            <span>Have More Questions? Chat with Secretariat</span>
          </a>
        </div>

      </div>
    </section>
  );
}

