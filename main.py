import os
from SSheet import SongSheet
from Guid import serveGuid
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
    nameList = getJsonFileNameList()
    for name in nameList:
        print('开始记录 {} 文件'.format(name))
        sheet = SongSheet()
        sheet.fileName = name
        # 创建表
        database.create_table(name)
        # 获取json数据
        jsonText = sheet.getJsonText()
        # 记录歌单基本信息
        baseInfo = sheet.baseInfo(jsonText)
        database.record_basicInfo(baseInfo)
        # 记录歌曲信息
        songList = sheet.songList(jsonText)
        database.insert_data(name, songList)
        print('{} 文件记录成功！\n'.format(name))


# 爬取和保存数据完整操作----一次完整操作的封装
def allSteps():
    # 建立数据库链接
    database = Database.Database()
    # 服务导航
    baseInfo, songList, sheet = serveGuid()
    # 输出对象信息
    sheet.outputInfo(songList)
    # 根据对象创建表格
    database.create_table(sheet.fileName)
    # 从对象中获取数据，存储到对应表格中
    database.insert_data(sheet.fileName, songList)
    # 完善索引表
    database.record_basicInfo(baseInfo)


allSteps()
# database = Database.Database()
# database.deleteAllTable()
# importAllJsonData()


# 耳机分你一个_想和你开启好心情
# ./jsonFileList/7444822840.json
