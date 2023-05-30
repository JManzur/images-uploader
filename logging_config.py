import os
import logging
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Configure logging with rotation
log_file = os.path.join(logs_dir, 'request.log')
max_file_size = 10 * 1024 * 1024  # 10 MB
backup_count = 5  # Number of backup files to keep

def configure_logging():
    handler = RotatingFileHandler(log_file, maxBytes=max_file_size, backupCount=backup_count)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s:%(lineno)d - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger