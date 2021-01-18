import os
from SSheet import SongSheet, serveGuid
import Database


# 获取所有json文件名称
def getJsonFileNameList():
    path = "./jsonFileList/"
    dirs = os.listdir(path)
    res = []
    for file in dirs:
        res.append(file[:-5])
    return res


# 导入所有json数据----重新建立数据库
def importAllJsonData():
    database = Database.Database()
    res = getJsonFileNameList()
    for item in res:
        print('item:', item)
        sheet = SongSheet('1', item, '1')
        database.create_table(sheet)
        database.insert_data(sheet)
        database.record_basicInfo(sheet)


# 爬取和保存数据完整操作----一次完整操作的封装
def allSteps():
    # 建立数据库链接
    database = Database.Database()
    # 服务导航
    sheet, method = serveGuid()
    if method == 'internet':
        # 从网络初始化对象
        sheet.connInternet()
    elif method == 'local':
        sheet.outputInfo()
        return
    # 输出对象信息
    sheet.outputInfo()
    # 根据对象创建表格
    database.create_table(sheet.fileName)
    # 从对象中获取数据，存储到对应表格中
    database.insert_data(sheet)
    # 完善索引表
    database.record_basicInfo(sheet)


allSteps()
# database = Database.Database()
# database.deleteAllTable()
# importAllJsonData()

# 7095885579
# 这里有，翻不完的夏天
