import logging
import os
from dotenv import load_dotenv

load_dotenv()

def setup_logger(name:str = "code_lens", level: int =logging.INFO) -> logging.Logger:
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    numeric_level = getattr(logging, log_level, logging.INFO)
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(numeric_level)
        logger.propagate = False
    return logger