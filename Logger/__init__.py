import logging
import tqdm


import tqdm

class TqdmLoggingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg)
            self.flush()
        except Exception:
            self.handleError(record)

def set_up_logger(name="logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    ch = TqdmLoggingHandler()
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    return logger




class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    black = "\u001b[30;20m"
    green = "\u001b[32;20m"
    Blue = "\u001b[34;20m"
    Magenta = "\u001b[35;20m"
    Cyan = "\u001b[36;20m"
    White = "\u001b[37;20m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: Blue + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: Magenta + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)