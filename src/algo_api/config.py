import logging


def setup_logger():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s | %(message)s")
    handler.setFormatter(formatter)
    level = logging.DEBUG

    logger = logging.getLogger("algo_api")
    logger.setLevel(level)
    logger.addHandler(handler)
