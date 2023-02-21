import os
import sys
import logging
import datetime

"""
    Tạo logger riêng để sử dụng
"""

# Tên file
CURRENT_SCRIPT_NAME = os.path.basename(__file__).split('.')[0]

# Dường dẫn
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
LOGS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Logs")

class Logger():
    def __init__(self, name, level=logging.INFO):
        # Initial construct.
        self.level = level
        self.name = name

        # Current Year-Month
        # current_year_month = datetime.datetime.now().strftime("%Y-%m")

        # # Logger file name
        # log_file_name = f"{current_year_month}_{CURRENT_SCRIPT_NAME}.log"

        # Create Logs Folder if it does not exist
        # os.makedirs(LOGS_DIRECTORY, exist_ok=True)

        # Log file path
        # log_file = os.path.join(LOGS_DIRECTORY, log_file_name)

        # File Handler
        # file_handler = logging.FileHandler(log_file)
        # file_handler.setLevel(logging.DEBUG)
        # file_handler.setFormatter(self.formatter)
        # self.logger.addHandler(file_handler)

        # Tạo format message cho log
        self.formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s', datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.stream_handler.setFormatter(self.formatter)
        
        self.log = logging.getLogger(name)
        self.log.setLevel(self.level)
        self.log.addHandler(self.stream_handler)

    def info(self, msg, extra=None):
        self.log.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.log.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.log.debug(msg, extra=extra)

    def warning(self, msg, extra=None):
        self.log.warning(msg, extra=extra)