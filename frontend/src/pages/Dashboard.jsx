export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-12">
          <h1 className="text-5xl font-bold gradient-text mb-2">NexusIntel</h1>
          <p className="text-gray-400">Enterprise Cyber Investigation Platform</p>
        </div>

        {/* Quick Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          {[
            { label: 'Active Investigations', value: '0', icon: '📋' },
            { label: 'Indicators', value: '0', icon: '🎯' },
            { label: 'Evidence Files', value: '0', icon: '📁' },
            { label: 'Relationships', value: '0', icon: '🔗' },
          ].map((stat, i) => (
            <div key={i} className="glassmorphism p-6 rounded-lg border border-purple-500/20">
              <div className="text-2xl mb-2">{stat.icon}</div>
              <div className="text-gray-400 text-sm">{stat.label}</div>
              <div className="text-2xl font-bold text-green-400">{stat.value}</div>
            </div>
          ))}
        </div>

        {/* Welcome Message */}
        <div className="glassmorphism p-8 rounded-lg border border-green-400/30">
          <h2 className="text-2xl font-bold mb-4">Welcome to NexusIntel</h2>
          <p className="text-gray-400 mb-4">
            Create an investigation to begin mapping infrastructure relationships, enriching indicators, and building your threat intelligence.
          </p>
          <button className="bg-green-400 text-black px-6 py-2 rounded font-bold hover:bg-green-300 transition">
            Create Investigation
          </button>
        </div>
      </div>
    </div>
  )
}
