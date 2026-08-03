from loguru import logger

logger.remove()

logger.add(
    "logs/firewall.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    encoding="utf-8"
)

logger.add(
    lambda msg: print(msg, end=""),
    level="INFO"
)
