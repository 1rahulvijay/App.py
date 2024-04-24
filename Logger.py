import logging
from logging.handlers import RotatingFileHandler

def setup_advanced_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a formatter for the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler for writing logs to a file
    file_handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=5)  # Rotate log files when they reach 100KB, keep up to 5 backups
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Create a console handler to display logs on the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Only display logs with INFO level or higher on the console
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Usage example:
logger = setup_advanced_logger()
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
