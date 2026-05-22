"""
Evidence upload and management routes
"""
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.config import settings
import os
import uuid
import hashlib
from pathlib import Path

router = APIRouter(prefix="/evidence")


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent path traversal attacks"""
    if not filename:
        raise ValueError("Filename cannot be empty")
    
    # Get only the filename part (remove any path components)
    filename = Path(filename).name
    
    # Remove potentially dangerous characters
    dangerous_chars = ['..', '/', '\\', '\x00', '\n', '\r']
    for char in dangerous_chars:
        filename = filename.replace(char, '')
    
    if not filename:
        raise ValueError("Invalid filename")
    
    return filename


@router.post("/{investigation_id}/upload", status_code=status.HTTP_201_CREATED)
async def upload_evidence(
    investigation_id: str,
    file: UploadFile = File(...),
    description: str = "",
    db: Session = Depends(get_db)
):
    """Upload evidence file with path traversal protection"""
    
    # Validate investigation_id to prevent path traversal
    if '..' in investigation_id or '/' in investigation_id or '\\' in investigation_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid investigation ID"
        )
    
    file_content = await file.read()
    file_size = len(file_content)
    
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File too large"
        )
    
    # Validate file extension
    file_ext = file.filename.split('.')[-1].lower() if '.' in file.filename else ''
    if file_ext not in settings.ALLOWED_UPLOAD_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"File type .{file_ext} not allowed"
        )
    
    try:
        sanitized_filename = sanitize_filename(file.filename)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid filename: {str(e)}"
        )
    
    # Use UUID as secondary filename to prevent collisions and further sanitize
    unique_filename = f"{uuid.uuid4()}_{sanitized_filename}"
    
    # Create upload directory with absolute path to prevent escape
    upload_dir = Path("backend/uploads") / investigation_id
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    # Construct full path and verify it's within the upload directory
    file_path = upload_dir / unique_filename
    
    # Verify the resolved path is still within uploads directory
    try:
        file_path.resolve().relative_to(upload_dir.resolve())
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file path"
        )
    
    # Write file safely
    try:
        with open(file_path, "wb") as f:
            f.write(file_content)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save file"
        )
    
    sha256_hash = hashlib.sha256(file_content).hexdigest()
    
    return {
        "status": "uploaded",
        "filename": sanitized_filename,
        "stored_as": unique_filename,
        "size": file_size,
        "sha256": sha256_hash,
        "message": "Evidence stored successfully"
    }
