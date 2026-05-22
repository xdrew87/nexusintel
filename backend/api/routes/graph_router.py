"""
Graph visualization routes
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.database import Indicator, Relationship
from api.schemas import GraphResponse, GraphNode, GraphEdge

router = APIRouter(prefix="/graph")


@router.get("/{investigation_id}", response_model=GraphResponse)
async def get_investigation_graph(
    investigation_id: str,
    db: Session = Depends(get_db)
):
    """Get graph data for investigation"""
    
    indicators = db.query(Indicator).filter(
        Indicator.investigation_id == investigation_id
    ).all()
    
    if not indicators:
        return GraphResponse(nodes=[], edges=[])
    
    nodes = []
    for indicator in indicators:
        node = GraphNode(
            id=indicator.id,
            label=indicator.value,
            node_type=indicator.indicator_type,
            data={
                "type": indicator.indicator_type,
                "status": indicator.status,
                "confidence": indicator.confidence,
                "enriched": indicator.enrichment_data is not None,
            }
        )
        nodes.append(node)
    
    indicator_ids = [i.id for i in indicators]
    relationships = db.query(Relationship).filter(
        Relationship.source_id.in_(indicator_ids)
    ).all()
    
    edges = []
    for rel in relationships:
        edge = GraphEdge(
            source=rel.source_id,
            target=rel.target_id,
            label=rel.relationship_type,
            edge_type=rel.relationship_type,
            confidence=rel.confidence,
        )
        edges.append(edge)
    
    return GraphResponse(nodes=nodes, edges=edges)


@router.post("/{investigation_id}/pivot")
async def pivot_from_indicator(
    investigation_id: str,
    indicator_id: str,
    db: Session = Depends(get_db)
):
    """Pivot to related indicators"""
    return {
        "status": "pivot_started",
        "from": indicator_id,
        "message": "Finding related indicators..."
    }
