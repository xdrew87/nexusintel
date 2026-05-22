"""
Logging configuration
"""
import logging
from core.config import settings

# Configure logger
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("nexusintel")
