import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { motion } from 'framer-motion'

// Pages
import Dashboard from './pages/Dashboard'
import InvestigationsList from './pages/InvestigationsList'
import InvestigationDetail from './pages/InvestigationDetail'

export default function App() {
  return (
    <Router>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/investigations" element={<InvestigationsList />} />
          <Route path="/investigation/:id" element={<InvestigationDetail />} />
        </Routes>
      </motion.div>
    </Router>
  )
}
