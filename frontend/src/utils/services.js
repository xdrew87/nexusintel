import api from './api'

export const investigationsAPI = {
  list: () => api.get('/investigations'),
  get: (id) => api.get(`/investigations/${id}`),
  create: (data) => api.post('/investigations', data),
  update: (id, data) => api.put(`/investigations/${id}`, data),
  delete: (id) => api.delete(`/investigations/${id}`),
}

export const indicatorsAPI = {
  list: (investigationId) => api.get(`/indicators/${investigationId}`),
  add: (investigationId, data) => api.post(`/indicators/${investigationId}`, data),
  enrich: (data) => api.post('/indicators/enrich', data),
}

export const graphAPI = {
  get: (investigationId) => api.get(`/graph/${investigationId}`),
  pivot: (investigationId, indicatorId) => api.post(`/graph/${investigationId}/pivot`, { indicator_id: indicatorId }),
}

export const notesAPI = {
  list: (investigationId) => api.get(`/notes/${investigationId}`),
  create: (investigationId, data) => api.post(`/notes/${investigationId}`, data),
}

export const evidenceAPI = {
  upload: (investigationId, file, description) => {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('description', description)
    return api.post(`/evidence/${investigationId}/upload`, formData)
  },
}

export const searchAPI = {
  search: (query, limit = 20) => api.get('/search', { params: { q: query, limit } }),
}
