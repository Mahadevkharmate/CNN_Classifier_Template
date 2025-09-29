import logging
import os
import sys
from datetime import datetime

# Create logs directory
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)
# Log file path
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)



logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)