import logging

def get_logger(name: str = __name__) -> logging.Logger:
    # 建立 logger（紀錄器）
    logger = logging.getLogger(name)  #  參數 name
    logger.setLevel(logging.DEBUG)

    # 避免重複掛上 handler
    if not logger.handlers:

        # 建立處理器：Console
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        # 建立處理器：File
        fileHandler = logging.FileHandler(filename='appdemo.log', encoding='utf-8')
        fileHandler.setLevel(logging.INFO)

        # 格式設定
        formatter = logging.Formatter(
            fmt="%(asctime)s|%(levelname)-8s|%(name)s|%(filename)s:%(lineno)d|%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # 設定 formatter 到 handler 上
        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        # 將 handler 加到 logger 上
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)

        # 加入過濾器（可選）
        flt = logging.Filter(name.split('.')[0])  # 只要首層模組名
        logger.addFilter(flt)

    return logger
