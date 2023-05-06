import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OTH\\Pytest - Copy\\testCases\\automationLog.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(funcName)s : %(lineno)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.INFO)
        return logger

# getlog	logging.getLogger
# file	logging.FileHandler
# format	logging.Formatter
# file-->format	setFormatter
# log-->file	addHandler
