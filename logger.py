import logging
import os

LOG_FILE = "agent_system.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("AgenticAI")


def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)


def log_warning(message):
    logger.warning(message)


def log_task(task):
    logger.info(f"New Task Started: {task}")


def log_completion(task):
    logger.info(f"Task Completed: {task}")
