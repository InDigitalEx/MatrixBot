from loguru import logger
from path import Path

from bot import start_telegram_bot


def main() -> None:
    log_path = Path('logs/debug.log')
    logger.add(log_path, format="{time} {level} {message}", level="DEBUG", rotation="10:00")
    start_telegram_bot()


if __name__ == "__main__":
    main()
