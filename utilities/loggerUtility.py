import logging

class LoggerUtility:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        filehandler = logging.FileHandler('.\\logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger