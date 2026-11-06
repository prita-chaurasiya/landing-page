import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Play, Youtube, ArrowRight } from 'lucide-react';
import { siteData } from '../config/siteData';
import VideoModal from './VideoModal';

export default function VideosSection() {
  const [selectedVideo, setSelectedVideo] = useState(null);

  return (
    <section id="videos" className="py-14 lg:py-24 bg-white relative">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading Pattern */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-bold uppercase tracking-widest text-[#C9971C] block mb-2">
            DOCUMENTED FIELD ACTIVITIES
          </span>
          <h2 className="font-heading font-bold text-3xl sm:text-[40px] text-[#12275A] tracking-tight leading-tight">
            Watch HRCI in Action
          </h2>
          <div className="w-16 h-1 bg-gradient-to-r from-[#C9971C] to-[#E8BE55] mx-auto rounded-full mt-3.5 mb-4" />
          <p className="text-[#475569] text-base leading-relaxed">
            Real events, national conventions, legal awareness camps, and social impact documentaries on YouTube.
          </p>
        </div>

        {/* 4 Video Cards Grid (Pure White, 20px radius, 1px border #ECE6D8, 28px gaps) */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-7">
          {siteData.videos.map((vid) => (
            <motion.div
              key={vid.id}
              whileHover={{ y: -4 }}
              transition={{ duration: 0.25 }}
              onClick={() => setSelectedVideo(vid)}
              className="white-card overflow-hidden cursor-pointer flex flex-col justify-between group"
            >
              {/* Thumbnail with Zoom Effect */}
              <div className="relative aspect-video w-full overflow-hidden bg-slate-900">
                <img
                  src={vid.image}
                  alt={vid.title}
                  className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-108"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-slate-900/30 group-hover:bg-slate-900/15 transition-colors" />

                {/* Animated Play Button Ring */}
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="w-11 h-11 rounded-full bg-gradient-to-tr from-[#C9971C] to-[#E8BE55] flex items-center justify-center text-[#12275A] shadow-md transition-transform duration-300 group-hover:scale-110">
                    <Play className="w-4 h-4 fill-[#12275A] translate-x-0.5" />
                  </div>
                </div>

                {/* Duration Badge */}
                <div className="absolute bottom-2.5 right-2.5 px-2 py-0.5 rounded bg-black/80 backdrop-blur-sm text-[11px] font-mono font-bold text-white">
                  {vid.duration}
                </div>
              </div>

              {/* Video Title & Tagline */}
              <div className="p-5 flex-1 flex flex-col justify-between">
                <div>
                  <h4 className="font-heading font-bold text-base text-[#12275A] group-hover:text-[#C9971C] transition-colors line-clamp-2">
                    {vid.title}
                  </h4>
                  <p className="text-xs text-[#475569] mt-1.5 line-clamp-2 leading-relaxed">
                    {vid.tagline}
                  </p>
                </div>

                <div className="mt-4 pt-3 border-t border-[#ECE6D8] flex items-center justify-between text-xs text-[#C9971C] font-bold">
                  <span>Watch Video</span>
                  <ArrowRight className="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-1" />
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* View All Videos Button */}
        <div className="mt-12 text-center">
          <a
            href={siteData.organization.youtubeUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="btn-navy-outline px-6 py-3 rounded-full text-sm font-bold inline-flex items-center space-x-2"
          >
            <Youtube className="w-4 h-4 text-[#C9971C]" />
            <span>Watch Full Video Library on @HRCI4India</span>
          </a>
        </div>

      </div>

      {/* Lightbox Modal */}
      <VideoModal
        isOpen={!!selectedVideo}
        video={selectedVideo}
        onClose={() => setSelectedVideo(null)}
      />
    </section>
  );
}
