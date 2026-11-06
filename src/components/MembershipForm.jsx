import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { User, Phone, MapPin, Award, Briefcase, Lock, ArrowRight, CheckCircle2, ShieldCheck } from 'lucide-react';
import confetti from 'canvas-confetti';
import { siteData } from '../config/siteData';

export default function MembershipForm() {
  const [formData, setFormData] = useState({
    fullName: '',
    whatsappNumber: '',
    city: '',
    membershipType: siteData.formOptions.membershipTypes[1], // Default Lifetime (₹3,000)
    profession: ''
  });

  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const validate = () => {
    const errs = {};
    if (!formData.fullName.trim()) errs.fullName = 'Please enter your full name';
    if (!formData.whatsappNumber.trim()) {
      errs.whatsappNumber = 'Please enter your 10-digit WhatsApp number';
    } else if (!/^[6-9]\d{9}$/.test(formData.whatsappNumber.replace(/\D/g, '').slice(-10))) {
      errs.whatsappNumber = 'Please enter a valid 10-digit mobile number';
    }
    if (!formData.city.trim()) errs.city = 'Please enter your City and State';
    if (!formData.profession) errs.profession = 'Please select your profession';
    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validate()) return;

    setIsSubmitting(true);

    try {
      confetti({
        particleCount: 70,
        spread: 60,
        origin: { y: 0.6 },
        colors: ['#C9971C', '#E8BE55', '#12275A']
      });
    } catch (err) {}

    setTimeout(() => {
      setIsSubmitting(false);
      setIsSuccess(true);

      const message = `*HRCI Membership Application*%0A%0A*Name:* ${encodeURIComponent(formData.fullName)}%0A*WhatsApp:* ${encodeURIComponent(formData.whatsappNumber)}%0A*City/State:* ${encodeURIComponent(formData.city)}%0A*Plan:* ${encodeURIComponent(formData.membershipType)}%0A*Profession:* ${encodeURIComponent(formData.profession)}%0A%0APlease share official membership registration credentials.`;
      
      const whatsappUrl = `https://wa.me/${siteData.organization.whatsappNumber}?text=${message}`;

      setTimeout(() => {
        window.open(whatsappUrl, '_blank');
      }, 1400);
    }, 700);
  };

  return (
    <div id="membership-form" className="relative w-full max-w-xl mx-auto">
      
      {/* PURE WHITE Card with Radius 20px, 1px Border #ECE6D8, Soft Shadow */}
      <div className="bg-white rounded-[20px] border border-[#ECE6D8] shadow-[0_20px_50px_rgba(18,39,90,0.12)] p-6 sm:p-9 text-left">
        
        {/* Header Bar */}
        <div className="flex items-center space-x-3.5 pb-4 mb-6 border-b border-[#ECE6D8]">
          <div className="w-11 h-11 rounded-xl bg-[#FAF8F3] border border-[#C9971C]/30 flex items-center justify-center text-[#C9971C] shadow-sm flex-shrink-0">
            <Award className="w-6 h-6" />
          </div>
          <div>
            <h3 className="font-heading font-bold text-xl sm:text-2xl text-[#12275A] tracking-tight">
              Join HRCI <span className="text-[#C9971C]">Today</span>
            </h3>
            <p className="text-xs text-slate-500 font-medium">
              Start Your Official National Membership Journey
            </p>
          </div>
        </div>

        {/* Success Alert */}
        <AnimatePresence>
          {isSuccess && (
            <motion.div
              initial={{ opacity: 0, y: -8 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              className="mb-5 p-4 rounded-xl bg-amber-50 border border-[#C9971C]/40 text-slate-800 text-xs space-y-1 text-center"
            >
              <div className="flex items-center justify-center space-x-1.5 text-[#C9971C] font-bold text-sm">
                <CheckCircle2 className="w-4 h-4" />
                <span>Application Submitted Successfully!</span>
              </div>
              <p className="text-slate-600">
                Opening HRCI Secretariat WhatsApp for instant verification...
              </p>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Form Fields: Light Grey Inputs, Navy Labels, Gold Focus */}
        <form onSubmit={handleSubmit} className="space-y-4">
          
          {/* Full Name */}
          <div>
            <label className="block text-xs font-bold text-[#12275A] mb-1.5">
              Full Name <span className="text-[#C9971C]">*</span>
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#C9971C]">
                <User className="w-4 h-4" />
              </div>
              <input
                type="text"
                placeholder="Enter your full name"
                value={formData.fullName}
                onChange={(e) => setFormData({ ...formData, fullName: e.target.value })}
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0] text-slate-800 placeholder-slate-400 text-sm focus:outline-none focus:border-[#C9971C] focus:ring-1 focus:ring-[#C9971C] transition-all"
              />
            </div>
            {errors.fullName && <p className="text-xs text-red-500 mt-1">{errors.fullName}</p>}
          </div>

          {/* WhatsApp Number */}
          <div>
            <label className="block text-xs font-bold text-[#12275A] mb-1.5">
              WhatsApp Number <span className="text-[#C9971C]">*</span>
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#C9971C]">
                <Phone className="w-4 h-4" />
              </div>
              <input
                type="tel"
                placeholder="e.g. 9876543210"
                value={formData.whatsappNumber}
                onChange={(e) => setFormData({ ...formData, whatsappNumber: e.target.value })}
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0] text-slate-800 placeholder-slate-400 text-sm focus:outline-none focus:border-[#C9971C] focus:ring-1 focus:ring-[#C9971C] transition-all"
              />
            </div>
            {errors.whatsappNumber && <p className="text-xs text-red-500 mt-1">{errors.whatsappNumber}</p>}
          </div>

          {/* City / State */}
          <div>
            <label className="block text-xs font-bold text-[#12275A] mb-1.5">
              City / State <span className="text-[#C9971C]">*</span>
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#C9971C]">
                <MapPin className="w-4 h-4" />
              </div>
              <input
                type="text"
                placeholder="e.g. Mumbai, Maharashtra"
                value={formData.city}
                onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0] text-slate-800 placeholder-slate-400 text-sm focus:outline-none focus:border-[#C9971C] focus:ring-1 focus:ring-[#C9971C] transition-all"
              />
            </div>
            {errors.city && <p className="text-xs text-red-500 mt-1">{errors.city}</p>}
          </div>

          {/* Membership Type Dropdown */}
          <div>
            <label className="block text-xs font-bold text-[#12275A] mb-1.5">
              Membership Type <span className="text-[#C9971C]">*</span>
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#C9971C]">
                <Award className="w-4 h-4" />
              </div>
              <select
                value={formData.membershipType}
                onChange={(e) => setFormData({ ...formData, membershipType: e.target.value })}
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0] text-slate-800 text-sm focus:outline-none focus:border-[#C9971C] focus:ring-1 focus:ring-[#C9971C] transition-all appearance-none cursor-pointer"
              >
                {siteData.formOptions.membershipTypes.map((type) => (
                  <option key={type} value={type} className="text-slate-800">
                    {type}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Profession Dropdown */}
          <div>
            <label className="block text-xs font-bold text-[#12275A] mb-1.5">
              Profession / Occupation <span className="text-[#C9971C]">*</span>
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#C9971C]">
                <Briefcase className="w-4 h-4" />
              </div>
              <select
                value={formData.profession}
                onChange={(e) => setFormData({ ...formData, profession: e.target.value })}
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0] text-slate-800 text-sm focus:outline-none focus:border-[#C9971C] focus:ring-1 focus:ring-[#C9971C] transition-all appearance-none cursor-pointer"
              >
                <option value="" className="text-slate-400">Select your profession</option>
                {siteData.formOptions.professions.map((prof) => (
                  <option key={prof} value={prof} className="text-slate-800">
                    {prof}
                  </option>
                ))}
              </select>
            </div>
            <p className="text-[11px] text-slate-500 mt-1 italic">
              e.g. Doctor, Advocate, Social Worker, Business, Teacher, Politician etc.
            </p>
            {errors.profession && <p className="text-xs text-red-500 mt-1">{errors.profession}</p>}
          </div>

          {/* Full-width Gold Button */}
          <div className="pt-2">
            <button
              type="submit"
              disabled={isSubmitting}
              className="btn-gold-primary w-full py-4 rounded-xl text-sm sm:text-base font-bold flex items-center justify-center space-x-2 shadow-md group cursor-pointer disabled:opacity-75"
            >
              <span>{isSubmitting ? 'Processing...' : 'Get Membership Details'}</span>
              <ArrowRight className="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" />
            </button>
          </div>

          {/* Lock Note */}
          <div className="pt-2 flex items-center justify-center space-x-1.5 text-xs text-slate-500 font-medium">
            <Lock className="w-3.5 h-3.5 text-[#C9971C]" />
            <span>Your information is 100% safe &amp; secure.</span>
          </div>

          <div className="flex items-center justify-center space-x-4 pt-1 text-[11px] text-slate-500">
            <span className="flex items-center space-x-1">
              <ShieldCheck className="w-3.5 h-3.5 text-[#C9971C]" />
              <span>Instant WhatsApp Confirmation</span>
            </span>
            <span className="text-[#ECE6D8]">•</span>
            <span>Govt. Regd. NGO</span>
          </div>

        </form>

      </div>
    </div>
  );
}
