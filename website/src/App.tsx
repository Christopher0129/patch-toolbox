import { Routes, Route } from 'react-router-dom';
import { LanguageProvider } from '@/i18n/LanguageContext';
import Layout from '@/components/Layout';
import Home from '@/pages/Home';
import NetworkSecurity from '@/pages/NetworkSecurity';
import SystemVulnerabilities from '@/pages/SystemVulnerabilities';
import SystemTroubleshooting from '@/pages/SystemTroubleshooting';
import About from '@/pages/About';
import Contributing from '@/pages/Contributing';

export default function App() {
  return (
    <LanguageProvider>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/network-security" element={<NetworkSecurity />} />
          <Route path="/system-vulnerabilities" element={<SystemVulnerabilities />} />
          <Route path="/system-troubleshooting" element={<SystemTroubleshooting />} />
          <Route path="/about" element={<About />} />
          <Route path="/contributing" element={<Contributing />} />
        </Routes>
      </Layout>
    </LanguageProvider>
  );
}
