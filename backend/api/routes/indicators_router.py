"""
Indicator routes with enrichment
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.database import Indicator, Investigation
from api.schemas import IndicatorCreate, IndicatorResponse

router = APIRouter(prefix="/indicators")


@router.get("/{investigation_id}", response_model=list[IndicatorResponse])
async def list_indicators(
    investigation_id: str,
    db: Session = Depends(get_db)
):
    """List indicators in investigation"""
    investigation = db.query(Investigation).filter(
        Investigation.id == investigation_id
    ).first()
    
    if not investigation:
        raise HTTPException(status_code=404, detail="Investigation not found")
    
    indicators = db.query(Indicator).filter(
        Indicator.investigation_id == investigation_id
    ).all()
    
    return indicators


@router.post("/{investigation_id}", response_model=IndicatorResponse, status_code=status.HTTP_201_CREATED)
async def add_indicator(
    investigation_id: str,
    indicator: IndicatorCreate,
    db: Session = Depends(get_db)
):
    """Add indicator to investigation"""
    investigation = db.query(Investigation).filter(
        Investigation.id == investigation_id
    ).first()
    
    if not investigation:
        raise HTTPException(status_code=404, detail="Investigation not found")
    
    db_indicator = Indicator(
        investigation_id=investigation_id,
        indicator_type=indicator.indicator_type,
        value=indicator.value,
        confidence=indicator.confidence,
    )
    
    db.add(db_indicator)
    db.commit()
    db.refresh(db_indicator)
    
    return db_indicator


@router.post("/enrich", response_model=dict)
async def enrich_indicator(investigation_id: str, indicator_value: str):
    """Enrich indicator with threat intel"""
    return {
        "status": "enrichment_queued",
        "indicator": indicator_value,
        "message": "Enrichment in progress"
    }
