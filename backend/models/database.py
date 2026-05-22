"""
SQLAlchemy models for NexusIntel
Investigation, evidence, indicators, relationships
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base
import uuid
from datetime import datetime


class Investigation(Base):
    """Investigation case model"""
    __tablename__ = "investigations"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False, index=True)
    description = Column(Text)
    status = Column(String, default="active")  # active, closed, archived
    risk_level = Column(String, default="medium")  # low, medium, high, critical
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    indicators = relationship("Indicator", back_populates="investigation")
    notes = relationship("Note", back_populates="investigation")
    evidence = relationship("Evidence", back_populates="investigation")
    
    def __repr__(self):
        return f"<Investigation {self.title}>"


class Indicator(Base):
    """Indicator model (IP, domain, email, hash, etc.)"""
    __tablename__ = "indicators"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    investigation_id = Column(String, ForeignKey("investigations.id"), nullable=False)
    indicator_type = Column(String, nullable=False, index=True)  # ip, domain, email, username, hash, url, asn
    value = Column(String, nullable=False, index=True)
    status = Column(String, default="pending")  # pending, enriched, flagged
    confidence = Column(Float, default=0.5)  # 0.0 - 1.0
    enrichment_data = Column(Text)  # JSON string
    created_at = Column(DateTime, server_default=func.now())
    last_enriched = Column(DateTime)
    
    # Relationships
    investigation = relationship("Investigation", back_populates="indicators")
    relationships = relationship("Relationship", foreign_keys="Relationship.source_id")
    
    def __repr__(self):
        return f"<Indicator {self.indicator_type}:{self.value}>"


class Relationship(Base):
    """Relationship/edge between indicators"""
    __tablename__ = "relationships"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source_id = Column(String, ForeignKey("indicators.id"), nullable=False)
    target_id = Column(String, ForeignKey("indicators.id"), nullable=False)
    relationship_type = Column(String, nullable=False)  # hosted_on, resolves_to, owns, etc.
    confidence = Column(Float, default=0.5)
    created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<Relationship {self.relationship_type}>"


class Note(Base):
    """Analyst notes within investigation"""
    __tablename__ = "notes"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    investigation_id = Column(String, ForeignKey("investigations.id"), nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(String)  # Comma-separated
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    investigation = relationship("Investigation", back_populates="notes")
    
    def __repr__(self):
        return f"<Note {self.id[:8]}>"


class Evidence(Base):
    """Uploaded evidence files"""
    __tablename__ = "evidence"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    investigation_id = Column(String, ForeignKey("investigations.id"), nullable=False)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer)
    file_type = Column(String)  # jpg, pdf, json, etc.
    sha256_hash = Column(String, unique=True, index=True)
    description = Column(Text)
    uploaded_at = Column(DateTime, server_default=func.now())
    
    investigation = relationship("Investigation", back_populates="evidence")
    
    def __repr__(self):
        return f"<Evidence {self.filename}>"


class IntelligenceSource(Base):
    """Threat intelligence source data"""
    __tablename__ = "intelligence_sources"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    indicator_value = Column(String, nullable=False, index=True)
    source = Column(String, nullable=False)  # abuseipdb, shodan, virustotal, etc.
    data = Column(Text)  # JSON
    confidence = Column(Float)
    last_checked = Column(DateTime, server_default=func.now())


class Campaign(Base):
    """Infrastructure campaigns/clusters"""
    __tablename__ = "campaigns"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    investigation_id = Column(String, ForeignKey("investigations.id"))
    name = Column(String, nullable=False)
    description = Column(Text)
    confidence = Column(Float, default=0.5)
    clustering_method = Column(String)  # shared_asn, shared_cert, shared_hosting, etc.
    created_at = Column(DateTime, server_default=func.now())
    
    investigation = relationship("Investigation")
