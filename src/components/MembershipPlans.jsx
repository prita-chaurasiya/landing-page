import React from 'react';
import { motion } from 'framer-motion';
import { Check, Star, ArrowRight } from 'lucide-react';
import { siteData } from '../config/siteData';

export default function MembershipPlans() {
  return (
    <section id="plans" className="py-14 lg:py-24 bg-white relative">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading Pattern */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-bold uppercase tracking-widest text-[#C9971C] block mb-2">
            MEMBERSHIP TIERS
          </span>
          <h2 className="font-heading font-bold text-3xl sm:text-[40px] text-[#12275A] tracking-tight leading-tight">
            Our Membership Plans
          </h2>
          <div className="w-16 h-1 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] mx-auto rounded-full mt-3.5 mb-4" />
          <p className="text-[#475569] text-base leading-relaxed">
            Choose the membership tier that aligns with your leadership aspirations and social welfare mission.
          </p>
        </div>

        {/* 3 Equal-Width Cards in One Row (grid-cols-3, gap 28px, padding 36px, equal height) */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-7 items-stretch">
          {siteData.plans.map((plan) => {
            const isFeatured = plan.featured;

            return (
              <motion.div
                key={plan.id}
                whileHover={{ y: -4 }}
                transition={{ duration: 0.25 }}
                className={`relative rounded-[20px] p-9 flex flex-col justify-between h-full transition-all duration-300 min-w-[320px] ${
                  isFeatured
                    ? 'bg-white border-2 border-[#C9971C] shadow-[0_15px_40px_rgba(201,151,28,0.18)] lg:scale-[1.03] z-10'
                    : 'bg-white border border-[#ECE6D8] shadow-[0_10px_30px_rgba(18,39,90,0.08)]'
                }`}
              >
                {/* Most Popular Gold Badge (Middle Card) */}
                {plan.badge && (
                  <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 z-20">
                    <div className="px-4 py-1 rounded-full bg-gradient-to-r from-[#C9971C] to-[#E8BE55] text-[#12275A] font-heading font-bold text-xs uppercase tracking-wider shadow-sm flex items-center space-x-1.5">
                      <Star className="w-3 h-3 fill-[#12275A]" />
                      <span>{plan.badge}</span>
                    </div>
                  </div>
                )}

                {/* Top Part: Plan Name, Price, and Features List */}
                <div>
                  {/* Plan Name: 14px Uppercase Gold Label */}
                  <div className="text-center pb-4">
                    <span className="text-sm font-bold uppercase tracking-wider text-[#C9971C] block">
                      {plan.name}
                    </span>
                    <span className="font-devanagari text-xs text-slate-500 font-medium">
                      {plan.nameHi}
                    </span>

                    {/* Price Block: 44px Bold Navy (or 28px for "As per Designation") */}
                    <div className="mt-3 flex flex-col items-center">
                      {plan.price.includes('Designation') ? (
                        <span className="text-[28px] font-heading font-bold text-[#12275A] leading-tight whitespace-nowrap">
                          {plan.price}
                        </span>
                      ) : (
                        <span className="text-[44px] font-heading font-bold text-[#12275A] leading-none">
                          {plan.price}
                        </span>
                      )}
                      <span className="text-xs text-slate-400 mt-1.5 font-medium">
                        {plan.period}
                      </span>
                    </div>
                  </div>

                  {/* Thin Divider Above Features List */}
                  <div className="border-t border-[#ECE6D8] pt-5 my-2" />

                  {/* Feature Rows: 15px text, gold check icon, 12px row gap (space-y-3) */}
                  <ul className="space-y-3 text-left">
                    {plan.features.map((feat, fIdx) => (
                      <li key={fIdx} className="flex items-start space-x-3 text-[15px] text-[#475569] leading-snug">
                        <div className="w-4 h-4 rounded-full bg-[#FAF8F3] border border-[#C9971C]/40 flex items-center justify-center text-[#C9971C] flex-shrink-0 mt-0.5">
                          <Check className="w-3 h-3 stroke-[3]" />
                        </div>
                        <span>{feat}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Bottom CTA Button: Pinned to Bottom with margin-top: auto */}
                <div className="mt-auto pt-8">
                  {isFeatured ? (
                    <a
                      href="#membership-form"
                      className="btn-gold-primary w-full py-3.5 px-6 rounded-full text-sm font-bold flex items-center justify-center space-x-2 shadow-md"
                    >
                      <span>{plan.ctaText}</span>
                      <ArrowRight className="w-4 h-4" />
                    </a>
                  ) : (
                    <a
                      href="#membership-form"
                      className="btn-navy-outline w-full py-3.5 px-6 rounded-full text-sm font-bold flex items-center justify-center space-x-2"
                    >
                      <span>{plan.ctaText}</span>
                      <ArrowRight className="w-4 h-4" />
                    </a>
                  )}
                </div>

              </motion.div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
