import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X } from 'lucide-react';

export default function VideoModal({ isOpen, onClose, video }) {
  if (!isOpen || !video) return null;

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/85 backdrop-blur-md">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.95 }}
          transition={{ duration: 0.3 }}
          className="relative w-full max-w-3xl rounded-[24px] bg-navy-900 border border-gold/40 shadow-2xl overflow-hidden p-2"
        >
          {/* Close Button */}
          <button
            onClick={onClose}
            className="absolute top-4 right-4 z-20 w-9 h-9 rounded-full bg-navy-950/80 border border-gold/40 text-gold hover:bg-gold hover:text-navy-950 flex items-center justify-center transition-colors"
            aria-label="Close video"
          >
            <X className="w-5 h-5" />
          </button>

          {/* Video Title Header */}
          <div className="px-4 py-3 border-b border-gold/20 flex items-center space-x-2">
            <span className="w-2.5 h-2.5 rounded-full bg-gold animate-ping" />
            <span className="font-heading font-bold text-sm text-ivory">
              {video.title}
            </span>
          </div>

          {/* Video Player Frame / YouTube Embed */}
          <div className="relative aspect-video rounded-xl overflow-hidden bg-black mt-2">
            <iframe
              src={`https://www.youtube-nocookie.com/embed/${video.youtubeId}?autoplay=1&rel=0`}
              title={video.title}
              className="w-full h-full border-0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            />
          </div>

          <div className="p-3 text-right">
            <a
              href="https://youtube.com/@HRCI4India"
              target="_blank"
              rel="noopener noreferrer"
              className="text-xs text-gold hover:underline font-semibold"
            >
              Watch more videos on official YouTube Channel @HRCI4India →
            </a>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
}

