from pathlib import Path

from loguru import logger


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "firewall.log"

logger.remove()

logger.add(
    LOG_FILE,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8"
)
