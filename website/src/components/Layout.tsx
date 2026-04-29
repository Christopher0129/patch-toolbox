import { useRef, type ReactNode } from 'react';
import { motion, useScroll, useSpring } from 'framer-motion';
import Navbar from './Navbar';
import Footer from './Footer';

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001,
  });

  return (
    <div ref={containerRef} className="relative min-h-[100dvh] bg-bg-base">
      {/* Scroll progress indicator */}
      <motion.div
        className="fixed left-0 right-0 top-0 z-[60] h-0.5 origin-left bg-accent-blue"
        style={{ scaleX }}
      />

      <Navbar />

      <main className="pt-16">{children}</main>

      <Footer />
    </div>
  );
}
