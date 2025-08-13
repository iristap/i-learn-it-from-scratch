"""
# loggin/practice_challenge.py
# Challenge: Create a logging system for a CSV file loader
    If the file exists → log at INFO level that loading succeeded
    If the file does not exist → log at ERROR level and write to log file
    Log output should go to both console and file
"""

import logging
import os
import pandas as pd
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # สร้างโฟลเดอร์ถ้ายังไม่มี

log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
log_path = os.path.join(LOG_DIR, log_filename)

# Set up logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_path, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s" # asctime: timestamp, levelname: log level, filename: name of the file, lineno: line number 
    # example: 2025-08-13 23:20:33,917 - DEBUG - step2_logging.py:31 - Loading config completed
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# function load csv
def load_CSV(file_name: str):
    if os.path.exists(file_name):
        try:
            df = pd.read_csv(file_name)
            logger.info(f"load file {file_name} ได้แว้ววววว")
            return df
        except Exception as e:
            logger.error(f"can't read file {file_name}: {e}")
        
    else:
        logger.error(f"file {file_name} is not exist")

# df = load_CSV("test.csv")

if __name__ == "__main__":
    logger.info(f"=== Start ===")

    # Test loading CSV files
    df = load_CSV("./sample.csv")
    df = load_CSV("./missing.csv")

    logger.info(f"=== End ===")