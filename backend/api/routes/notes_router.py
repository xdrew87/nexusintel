"""
Note and annotation routes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.database import Note, Investigation
from api.schemas import NoteCreate, NoteResponse

router = APIRouter(prefix="/notes")


@router.get("/{investigation_id}", response_model=list[NoteResponse])
async def list_notes(
    investigation_id: str,
    db: Session = Depends(get_db)
):
    """List all notes in investigation"""
    notes = db.query(Note).filter(
        Note.investigation_id == investigation_id
    ).all()
    
    return notes


@router.post("/{investigation_id}", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note(
    investigation_id: str,
    note: NoteCreate,
    db: Session = Depends(get_db)
):
    """Create note in investigation"""
    investigation = db.query(Investigation).filter(
        Investigation.id == investigation_id
    ).first()
    
    if not investigation:
        raise HTTPException(status_code=404, detail="Investigation not found")
    
    db_note = Note(
        investigation_id=investigation_id,
        content=note.content,
        tags=note.tags,
    )
    
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    
    return db_note
