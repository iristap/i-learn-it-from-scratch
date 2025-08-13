import logging

# Create a main logger
# (ใช้ __name__ เพื่อให้ชื่อ logger ตรงกับชื่อไฟล์)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Handler for console output
# แสดง log ตั้งแต่ INFO ขึ้นไป
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Handler for file output
# save log ลง app.log
# append mode
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s" # asctime: timestamp, levelname: log level, filename: name of the file, lineno: line number 
    # example: 2025-08-13 23:20:33,917 - DEBUG - step2_logging.py:31 - Loading config completed
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# get start logger
logger.debug("Loading config completed")
logger.info("System is starting")
logger.warning("Some information is missing")
logger.error("Database connection failed")
logger.critical("System is completely down")
