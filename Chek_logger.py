import logging
import os

def app_logger(name: str) -> logging.Logger:
    try:
        # Check if the logger already exists
        if name in logging.Logger.manager.loggerDict:
            return logging.getLogger(name)
        
        path = os.path.dirname(os.path.realpath(__file__))
        log_dir = os.path.join(path, "logs")
        log_file = os.path.join(log_dir, f"{name}.log")
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_formatter = logging.Formatter("%(levelname)s -- %(message)s")

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Adjust the level to your preference
        console_handler.setFormatter(console_formatter)

        logger = logging.getLogger(name)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.setLevel(logging.DEBUG)
        return logger
    except OSError:
        raise RuntimeError("Unable to Load App Logger")
