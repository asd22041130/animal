# logging是python內建的套件專門紀錄是日誌的一種
import logging

# 這是logging 所有參數全域設定，只要開啟程式時設定一次就夠了
logging.basicConfig(filename='demo.log',filemode='w',level=logging.DEBUG)
logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log1")
