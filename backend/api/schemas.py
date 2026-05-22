"""
Pydantic schemas for API request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime


# ━━━━━━━━━━━━━━━━━━━━━━━
# Investigation Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class InvestigationCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    risk_level: str = Field(default="medium", regex="^(low|medium|high|critical)$")


class InvestigationUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    risk_level: Optional[str] = None


class InvestigationResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: str
    risk_level: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# ━━━━━━━━━━━━━━━━━━━━━━━
# Indicator Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class IndicatorCreate(BaseModel):
    indicator_type: str = Field(..., regex="^(ip|domain|email|username|hash|url|asn)$")
    value: str = Field(..., min_length=1, max_length=500)
    confidence: Optional[float] = 0.5


class IndicatorEnrich(BaseModel):
    indicator_type: str
    value: str


class IndicatorResponse(BaseModel):
    id: str
    indicator_type: str
    value: str
    status: str
    confidence: float
    enrichment_data: Optional[Dict[str, Any]]
    created_at: datetime
    last_enriched: Optional[datetime]
    
    class Config:
        from_attributes = True


# ━━━━━━━━━━━━━━━━━━━━━━━
# Relationship Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class RelationshipCreate(BaseModel):
    source_id: str
    target_id: str
    relationship_type: str = Field(..., regex="^(hosted_on|resolves_to|owns|related_to|uses|shares_certificate|shares_asn)$")
    confidence: Optional[float] = 0.5


class RelationshipResponse(BaseModel):
    id: str
    source_id: str
    target_id: str
    relationship_type: str
    confidence: float
    created_at: datetime
    
    class Config:
        from_attributes = True


# ━━━━━━━━━━━━━━━━━━━━━━━
# Note Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class NoteCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=10000)
    tags: Optional[str] = None


class NoteUpdate(BaseModel):
    content: Optional[str] = None
    tags: Optional[str] = None


class NoteResponse(BaseModel):
    id: str
    investigation_id: str
    content: str
    tags: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# ━━━━━━━━━━━━━━━━━━━━━━━
# Evidence Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class EvidenceResponse(BaseModel):
    id: str
    investigation_id: str
    filename: str
    file_size: Optional[int]
    file_type: Optional[str]
    sha256_hash: Optional[str]
    description: Optional[str]
    uploaded_at: datetime
    
    class Config:
        from_attributes = True


# ━━━━━━━━━━━━━━━━━━━━━━━
# Graph Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class GraphNode(BaseModel):
    id: str
    label: str
    node_type: str
    data: Dict[str, Any]


class GraphEdge(BaseModel):
    source: str
    target: str
    label: str
    edge_type: str
    confidence: float


class GraphResponse(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]


# ━━━━━━━━━━━━━━━━━━━━━━━
# Search Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class SearchResult(BaseModel):
    result_type: str  # investigation, indicator, note, evidence
    result_id: str
    title: str
    description: Optional[str]
    matched_fields: List[str]


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]
    total_results: int


# ━━━━━━━━━━━━━━━━━━━━━━━
# Report Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class ReportGenerate(BaseModel):
    investigation_id: str
    format: str = Field(default="markdown", regex="^(markdown|json|html)$")
    include_evidence: bool = True
    include_timeline: bool = True


# ━━━━━━━━━━━━━━━━━━━━━━━
# Error Schemas
# ━━━━━━━━━━━━━━━━━━━━━━━

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    status_code: int
