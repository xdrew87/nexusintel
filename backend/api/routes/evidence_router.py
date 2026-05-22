"""
Evidence upload and management routes
"""
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.config import settings
import os

router = APIRouter(prefix="/evidence")


@router.post("/{investigation_id}/upload", status_code=status.HTTP_201_CREATED)
async def upload_evidence(
    investigation_id: str,
    file: UploadFile = File(...),
    description: str = "",
    db: Session = Depends(get_db)
):
    """Upload evidence file"""
    
    file_content = await file.read()
    file_size = len(file_content)
    
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File too large"
        )
    
    file_ext = file.filename.split('.')[-1].lower() if '.' in file.filename else ''
    if file_ext not in settings.ALLOWED_UPLOAD_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"File type .{file_ext} not allowed"
        )
    
    upload_dir = f"backend/uploads/{investigation_id}"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(file_content)
    
    import hashlib
    sha256_hash = hashlib.sha256(file_content).hexdigest()
    
    return {
        "status": "uploaded",
        "filename": file.filename,
        "size": file_size,
        "sha256": sha256_hash,
        "message": "Evidence stored successfully"
    }
