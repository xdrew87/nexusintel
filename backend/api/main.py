"""
NexusIntel Backend - FastAPI Main Application
Enterprise-grade cyber investigation platform
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZIPMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

from core.config import settings
from core.database import engine, Base
from core.logger import logger
from api.routes import (
    investigations_router,
    indicators_router,
    graph_router,
    evidence_router,
    intelligence_router,
    notes_router,
    search_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle manager"""
    # Startup
    logger.info("🚀 NexusIntel Backend Starting...")
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    logger.info("✓ Database initialized")
    
    yield
    
    # Shutdown
    logger.info("🛑 NexusIntel Backend Shutting Down...")


# Create FastAPI app
app = FastAPI(
    title="NexusIntel API",
    description="Enterprise Cyber Investigation & Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZIP Middleware
app.add_middleware(GZIPMiddleware, minimum_size=1000)

# API v1 Routes
app.include_router(investigations_router.router, prefix="/api/v1", tags=["Investigations"])
app.include_router(indicators_router.router, prefix="/api/v1", tags=["Indicators"])
app.include_router(graph_router.router, prefix="/api/v1", tags=["Graph"])
app.include_router(evidence_router.router, prefix="/api/v1", tags=["Evidence"])
app.include_router(intelligence_router.router, prefix="/api/v1", tags=["Intelligence"])
app.include_router(notes_router.router, prefix="/api/v1", tags=["Notes"])
app.include_router(search_router.router, prefix="/api/v1", tags=["Search"])


@app.get("/")
async def root():
    """API health check"""
    return {
        "name": "NexusIntel API",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
