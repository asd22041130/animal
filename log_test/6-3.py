# logging是python內建的套件專門紀錄是日誌的一種
import logging


logging.basicConfig(format ="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",level=logging.DEBUG)

name = "小明"

age = 18

logging.debug(f'姓名 {name} , 年齡{age}')
logging.warning(f'姓名 {name} , 年齡{age}')