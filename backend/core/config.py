"""
Core configuration for NexusIntel
"""
from typing import List
import os
from functools import lru_cache


class Settings:
    """Application settings from environment"""
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./nexusintel.db"
    )
    
    # Application
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
    ]
    
    # API Keys (optional)
    SHODAN_API_KEY: str = os.getenv("SHODAN_API_KEY", "")
    ABUSEIPDB_API_KEY: str = os.getenv("ABUSEIPDB_API_KEY", "")
    VIRUSTOTAL_API_KEY: str = os.getenv("VIRUSTOTAL_API_KEY", "")
    CENSYS_API_KEY: str = os.getenv("CENSYS_API_KEY", "")
    GREYNOISE_API_KEY: str = os.getenv("GREYNOISE_API_KEY", "")
    OTX_API_KEY: str = os.getenv("OTX_API_KEY", "")
    
    # Features
    ENABLE_ENRICHMENT: bool = os.getenv("ENABLE_ENRICHMENT", "true").lower() == "true"
    ENABLE_GRAPH_ENGINE: bool = os.getenv("ENABLE_GRAPH_ENGINE", "true").lower() == "true"
    ENABLE_AUTONOMOUS_PIVOTING: bool = os.getenv("ENABLE_AUTONOMOUS_PIVOTING", "false").lower() == "true"
    ENABLE_CAMPAIGN_CLUSTERING: bool = os.getenv("ENABLE_CAMPAIGN_CLUSTERING", "true").lower() == "true"
    ENABLE_THREAT_INTEL: bool = os.getenv("ENABLE_THREAT_INTEL", "true").lower() == "true"
    
    # File uploads
    MAX_UPLOAD_SIZE: int = int(os.getenv("MAX_UPLOAD_SIZE", "52428800"))  # 50MB
    ALLOWED_UPLOAD_TYPES: List[str] = os.getenv(
        "ALLOWED_UPLOAD_TYPES",
        "jpg,jpeg,png,gif,pdf,txt,json,csv,log,zip"
    ).split(",")
    
    # Rate limiting
    RATE_LIMIT_ENABLED: bool = os.getenv("RATE_LIMIT_ENABLED", "true").lower() == "true"
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "100"))
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))
    
    # Timeouts
    DNS_TIMEOUT: int = int(os.getenv("DNS_TIMEOUT", "5"))
    WHOIS_TIMEOUT: int = int(os.getenv("WHOIS_TIMEOUT", "10"))
    HTTP_TIMEOUT: int = int(os.getenv("HTTP_TIMEOUT", "10"))
    ENRICHMENT_MAX_WORKERS: int = int(os.getenv("ENRICHMENT_MAX_WORKERS", "10"))


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


settings = get_settings()
