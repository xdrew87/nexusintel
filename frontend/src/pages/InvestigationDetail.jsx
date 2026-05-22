import { useParams } from 'react-router-dom'

export default function InvestigationDetail() {
  const { id } = useParams()

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Investigation {id}</h1>
      <div className="grid grid-cols-3 gap-4">
        {/* Graph */}
        <div className="col-span-2 glassmorphism p-6 rounded-lg">
          <h2 className="text-xl font-bold mb-4">Relationship Graph</h2>
          <div className="bg-slate-800 rounded h-96 flex items-center justify-center">
            <p className="text-gray-500">Graph visualization will appear here</p>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-4">
          {/* Indicators */}
          <div className="glassmorphism p-6 rounded-lg">
            <h2 className="text-xl font-bold mb-4">Indicators</h2>
            <div className="text-gray-400">No indicators added</div>
          </div>

          {/* Evidence */}
          <div className="glassmorphism p-6 rounded-lg">
            <h2 className="text-xl font-bold mb-4">Evidence</h2>
            <div className="text-gray-400">No evidence uploaded</div>
          </div>
        </div>
      </div>
    </div>
  )
}
