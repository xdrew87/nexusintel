"""
Investigation routes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.database import Investigation
from api.schemas import InvestigationCreate, InvestigationUpdate, InvestigationResponse

router = APIRouter(prefix="/investigations")


@router.get("/", response_model=list[InvestigationResponse])
async def list_investigations(db: Session = Depends(get_db)):
    """List all investigations"""
    investigations = db.query(Investigation).all()
    return investigations


@router.post("/", response_model=InvestigationResponse, status_code=status.HTTP_201_CREATED)
async def create_investigation(
    investigation: InvestigationCreate,
    db: Session = Depends(get_db)
):
    """Create new investigation"""
    db_investigation = Investigation(
        title=investigation.title,
        description=investigation.description,
        risk_level=investigation.risk_level,
    )
    db.add(db_investigation)
    db.commit()
    db.refresh(db_investigation)
    return db_investigation


@router.get("/{investigation_id}", response_model=InvestigationResponse)
async def get_investigation(
    investigation_id: str,
    db: Session = Depends(get_db)
):
    """Get investigation by ID"""
    investigation = db.query(Investigation).filter(
        Investigation.id == investigation_id
    ).first()
    
    if not investigation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investigation not found"
        )
    
    return investigation


@router.put("/{investigation_id}", response_model=InvestigationResponse)
async def update_investigation(
    investigation_id: str,
    update_data: InvestigationUpdate,
    db: Session = Depends(get_db)
):
    """Update investigation"""
    investigation = db.query(Investigation).filter(
        Investigation.id == investigation_id
    ).first()
    
    if not investigation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investigation not found"
        )
    
    # Update fields
    update_dict = update_data.dict(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(investigation, key, value)
    
    db.commit()
    db.refresh(investigation)
    return investigation


@router.delete("/{investigation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_investigation(
    investigation_id: str,
    db: Session = Depends(get_db)
):
    """Delete investigation"""
    investigation = db.query(Investigation).filter(
        Investigation.id == investigation_id
    ).first()
    
    if not investigation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investigation not found"
        )
    
    db.delete(investigation)
    db.commit()
