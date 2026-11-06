import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import StatsStrip from './components/StatsStrip';
import FocusAreas from './components/FocusAreas';
import AboutWhyJoin from './components/AboutWhyJoin';
import VideosSection from './components/VideosSection';
import MembershipForm from './components/MembershipForm';
import Testimonials from './components/Testimonials';
import MembershipPlans from './components/MembershipPlans';
import MembershipProcess from './components/MembershipProcess';
import TrustStrip from './components/TrustStrip';
import FaqSection from './components/FaqSection';
import Footer from './components/Footer';
import FloatingWhatsApp from './components/FloatingWhatsApp';
import MobileStickyBar from './components/MobileStickyBar';

export default function App() {
  return (
    <div className="min-h-screen bg-navy-900 text-ivory flex flex-col font-sans selection:bg-gold selection:text-navy-950 pb-16 md:pb-0">
      
      {/* 1. TOP BAR + NAVBAR */}
      <Navbar />

      <main className="flex-grow">
        {/* 2. HERO SECTION */}
        <Hero />

        {/* 3. STATS STRIP (Ivory Floating Glass Bar) */}
        <StatsStrip />

        {/* 4. OUR FOCUS AREAS */}
        <FocusAreas />

        {/* TWO-COLUMN CONVERSION CONTAINER FOR SECTIONS 5, 6, 7, 8, 9, 10 */}
        <section className="py-16 sm:py-20 bg-navy-900 relative">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start">
              
              {/* LEFT COLUMN: About & Why Join, Videos, Testimonials, Membership Plans */}
              <div className="lg:col-span-7 space-y-12">
                {/* 5. ABOUT HRCI + WHY JOIN HRCI? */}
                <AboutWhyJoin />

                {/* 6. WATCH HRCI IN ACTION */}
                <VideosSection />

                {/* ON MOBILE: Form appears here in natural sequence (Section 7) */}
                <div className="block lg:hidden">
                  <MembershipForm />
                </div>

                {/* 8. WHAT OUR MEMBERS SAY */}
                <Testimonials />

                {/* 9. OUR MEMBERSHIP PLANS */}
                <MembershipPlans />

                {/* ON MOBILE: Process appears after plans */}
                <div className="block lg:hidden">
                  <MembershipProcess />
                </div>
              </div>

              {/* RIGHT COLUMN (DESKTOP STICKY): 7. Join Form + 10. Process */}
              <div className="hidden lg:block lg:col-span-5 lg:sticky lg:top-24 space-y-6">
                {/* 7. JOIN HRCI TODAY FORM */}
                <MembershipForm />

                {/* 10. SIMPLE MEMBERSHIP PROCESS */}
                <MembershipProcess />
              </div>

            </div>
          </div>
        </section>

        {/* 11. TRUST STRIP (Credentials Bar) */}
        <TrustStrip />

        {/* 12. FAQ ACCORDION (Hindi + English) */}
        <FaqSection />
      </main>

      {/* 13. FOOTER (Deep Navy) */}
      <Footer />

      {/* FLOATING WHATSAPP BUTTON (Desktop with ripple) */}
      <FloatingWhatsApp />

      {/* STICKY MOBILE BOTTOM CTA BAR */}
      <MobileStickyBar />

    </div>
  );
}

