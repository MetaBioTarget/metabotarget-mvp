"""
Configuration and runtime settings for MetaBioTarget AI platform.
"""
import os
from pathlib import Path
from pydantic_settings import BaseSettings

PROJECT_ROOT = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "MetaBioTarget AI Platform"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Storage and paths
    BASE_DIR: Path = PROJECT_ROOT
    DATA_DIR: Path = PROJECT_ROOT / "data"
    SYNTHETIC_DATA_DIR: Path = PROJECT_ROOT / "data" / "synthetic"
    REPORTS_DIR: Path = PROJECT_ROOT / "reports"
    LOGS_DIR: Path = PROJECT_ROOT / "logs"
    
    # Compute and Safety thresholds
    MAX_ALLOWABLE_COMPUTE_COST_USD: float = 25.0
    REQUIRE_COMPUTE_CONFIRMATION_THRESHOLD_USD: float = 5.0
    
    # Security & RBAC
    SECRET_KEY: str = "dev-insecure-secret-key-metabotarget-2026"
    DEFAULT_ROLE: str = "computational_biologist"
    
    # Model tracking
    MLFLOW_TRACKING_URI: str = "file://" + str(PROJECT_ROOT / "mlruns").replace("\\", "/")

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()

# Ensure critical directories exist
for p in [settings.DATA_DIR, settings.SYNTHETIC_DATA_DIR, settings.REPORTS_DIR, settings.LOGS_DIR]:
    p.mkdir(parents=True, exist_ok=True)
