"""
Global search routes
"""
from fastapi import APIRouter

router = APIRouter(prefix="/search")


@router.get("/")
async def global_search(q: str, limit: int = 20):
    """Global search across investigations, indicators, notes, evidence"""
    return {
        "query": q,
        "results": [],
        "total": 0,
        "message": "Search index not yet built"
    }
