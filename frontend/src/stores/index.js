import { create } from 'zustand'

export const useInvestigationStore = create((set) => ({
  investigations: [],
  currentInvestigation: null,
  
  setInvestigations: (investigations) => set({ investigations }),
  setCurrentInvestigation: (investigation) => set({ currentInvestigation: investigation }),
  addInvestigation: (investigation) => set((state) => ({
    investigations: [...state.investigations, investigation],
  })),
}))

export const useIndicatorStore = create((set) => ({
  indicators: [],
  selectedIndicators: [],
  
  setIndicators: (indicators) => set({ indicators }),
  addIndicator: (indicator) => set((state) => ({
    indicators: [...state.indicators, indicator],
  })),
  toggleIndicator: (id) => set((state) => ({
    selectedIndicators: state.selectedIndicators.includes(id)
      ? state.selectedIndicators.filter(i => i !== id)
      : [...state.selectedIndicators, id],
  })),
}))

export const useGraphStore = create((set) => ({
  nodes: [],
  edges: [],
  
  setGraph: (nodes, edges) => set({ nodes, edges }),
}))
