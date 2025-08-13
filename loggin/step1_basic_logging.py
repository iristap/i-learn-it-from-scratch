import logging

# set up basic configuration: show logs from INFO level and above (DEBUG will not be shown)
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.DEBUG,  # set to DEBUG to see all messages
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",  # asctime: timestamp, levelname: log level, filename: name of the file, lineno: line number
    # example: 2025-08-13 23:15:28 - DEBUG - step1_basic_logging.py:14 - DEBUG: massage นี้ยังไม่ขึ้นถ้า (level=logging.INFO) only for debugging
    datefmt="%Y-%m-%d %H:%M:%S",  # date format
    filename="./app.log",  # log to a file named app.log
    filemode="a",  # append mode, so logs will be added to the end of the file
    encoding="utf-8", # handle Thai characters
)

logging.debug("DEBUG: massage นี้ยังไม่ขึ้น ถ้า (level=logging.INFO) only for debugging")
logging.info("INFO: Starting the application")
logging.warning("WARNING: This is a warning")
logging.error("ERROR: An error occurred")
logging.critical("CRITICAL: A critical error occurred")
