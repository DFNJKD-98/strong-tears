from Database import Database
from AudioUrl import AudioUrl
from SSheet import SongSheet


def localHost_api(dbType, sheetId, fileName='', isSave=1):
    # 创建数据库对象
    db = Database(dbType=dbType)
    # 检查是否已经导入过歌单
    db.check_repetitive_sheet(sheetId)
    # 构建链接地址
    urlTool = AudioUrl()
    audioUrl = urlTool.getSongListDetail(sheetId)
    # 创建歌单对象
    sheet = SongSheet()
    # 歌单初始化
    sheet.init(audioUrl, sheetId, isSave, fileName)
    # 获取歌单<基础信息>和<歌曲列表>
    baseInfo, songList = sheet.completeOperation()
    # 输出对象信息
    # sheet.outputInfo(songList)
    # 根据对象创建表格
    db.create_table(sheet.fileName)
    # 从对象中获取数据，存储到对应表格中
    db.insert_data(sheet.fileName, songList)
    # 完善索引表
    db.record_basicInfo(baseInfo)


def localFile_api(dbType, filePath):
    # 创建数据库对象
    db = Database(dbType=dbType)
    # 创建歌单对象
    sheet = SongSheet()
    jsonText = sheet.getJsonText(filePath)
    # 获取歌单基本信息
    baseInfo = sheet.baseInfo(jsonText)
    # 检查是否导入过歌单
    db.check_repetitive_sheet(sheet.id)
    # 获取歌曲列表
    songList = sheet.songList(jsonText)
    # 输出对象信息
    # sheet.outputInfo(songList)
    # 根据对象创建表格
    db.create_table(sheet.fileName)
    # 从对象中获取数据，存储到对应表格中
    db.insert_data(sheet.fileName, songList)
    # 完善索引表
    db.record_basicInfo(baseInfo)


def internet_api(dbType, sheetId, fileName='', isSave=1):
    # 创建数据库对象
    db = Database(dbType=dbType)
    # 检查是否已经导入过歌单
    db.check_repetitive_sheet(sheetId)
    # 构建链接地址
    urlTool = AudioUrl()
    audioUrl = urlTool.getSongListDetailByOfficial(sheetId)
    # 创建歌单对象
    sheet = SongSheet()
    # 歌单初始化
    sheet.init(audioUrl, sheetId, isSave, fileName)
    # 获取歌单<基础信息>和<歌曲列表>
    baseInfo, songList = sheet.completeOperation()
    # 输出对象信息
    # sheet.outputInfo(songList)
    # 根据对象创建表格
    db.create_table(sheet.fileName)
    # 从对象中获取数据，存储到对应表格中
    db.insert_data(sheet.fileName, songList)
    # 完善索引表
    db.record_basicInfo(baseInfo)
