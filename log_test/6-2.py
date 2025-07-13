# logging是python內建的套件專門紀錄是日誌的一種
import logging

# 這是logging 所有參數全域設定，只要開啟程式時設定一次就夠了
logging.basicConfig(level=logging.DEBUG)

name = "張三"

age = 18


logging.debug(f'姓名 {name} , 年齡{age}')
logging.debug("姓名: %s, 年齡: %d" %( name, age))
logging.debug("姓名: %s, 年齡: %d" , name, age)
logging.debug("姓名: {}, 年齡: {}" .format(name, age))

