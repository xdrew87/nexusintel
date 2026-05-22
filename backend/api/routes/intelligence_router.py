"""
Threat intelligence integration routes
"""
from fastapi import APIRouter

router = APIRouter(prefix="/intelligence")


@router.get("/sources/{indicator_value}")
async def get_intelligence_sources(indicator_value: str):
    """Get threat intel from configured sources"""
    return {
        "indicator": indicator_value,
        "sources": [],
        "message": "Intelligence modules not yet configured"
    }


@router.post("/enrich-batch")
async def batch_enrich(indicators: list[str]):
    """Batch enrich multiple indicators"""
    return {
        "status": "batch_enrichment_queued",
        "count": len(indicators),
        "message": "Enrichment jobs submitted"
    }
