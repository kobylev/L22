"""
Environment Variable Loader
Loads and initializes .env configuration
"""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load .env file
project_root = Path(__file__).parent.parent.parent
env_path = project_root / '.env'

if env_path.exists():
    load_dotenv(env_path)
    logger.info(f"Loaded configuration from {env_path}")
else:
    logger.warning(f".env file not found at {env_path}, using defaults")


def get_env_int(key: str, default: int) -> int:
    """Get integer from environment"""
    return int(os.getenv(key, default))


def get_env_float(key: str, default: float) -> float:
    """Get float from environment"""
    return float(os.getenv(key, default))


def get_env_bool(key: str, default: str = 'false') -> bool:
    """Get boolean from environment"""
    return os.getenv(key, default).lower() == 'true'


def get_env_list(key: str, default: str) -> list:
    """Get list from comma-separated string"""
    value = os.getenv(key, default)
    return [x.strip() for x in value.split(',')]


def get_env_str(key: str, default: str) -> str:
    """Get string from environment"""
    return os.getenv(key, default)


def initialize_random_seed():
    """Initialize random seed for reproducibility"""
    seed_str = os.getenv('RANDOM_SEED', '')
    if seed_str:
        import random
        seed = int(seed_str)
        random.seed(seed)
        logger.info(f"Random seed set to {seed}")


# Auto-initialize on import
initialize_random_seed()
