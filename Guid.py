import sys
from SelfDefinedException import SheetRepeatException, CanNotBeEmpty
from AudioUrl import AudioUrl
from SSheet import SongSheet

urlTool = AudioUrl()


def guid_2(db):
    filePath = input('请输入json文件的位置：')
    try:
        if not filePath:
            raise CanNotBeEmpty('文件地址不可以为空！')
    except CanNotBeEmpty as e:
        print(e)
        sys.exit(1)
    sheet = SongSheet()
    jsonText = sheet.getJsonText(filePath)
    baseInfo = sheet.baseInfo(jsonText)
    db.check_repetitive_sheet(sheet.id)
    songList = sheet.songList(jsonText)
    return baseInfo, songList, sheet


def serveGuid(db):
    # 引导输入内容
    # localHost--1  localFile--2 internet--3
    print('localHost--1  localFile--2 internet--3')
    audioUrl = ''
    method = input('输入模式序号(默认为localHost)：')
    if method == '':
        method = '1'
    # ***************************************************************
    # 开启localFile导航
    if method == '2':
        return guid_2(db)
    # ***************************************************************
    sheetId = input('输入QQ音乐歌单id：')
    # 检测是否已经导入过歌单
    try:
        if sheetId == '':
            raise CanNotBeEmpty('歌单Id不可以为空！')
        else:
            db.check_repetitive_sheet(sheetId)
    except CanNotBeEmpty as e:
        print(e)
        sys.exit(1)
    # ***************************************************************
    # 检测选择的模式
    if method == '1':
        audioUrl = urlTool.getSongListDetail(sheetId)
    elif method == '3':
        audioUrl = urlTool.getSongListDetailByOfficial(sheetId)
    fileName = input('输入保存的文件名(默认为歌单名称)：')
    isSave = input('是否保存json文件(默认保存)?')
    print('\n')
    # ***************************************************************
    # 检测isSave参数输入的正确性
    if isSave == '':
        isSave = 1
    else:
        try:
            isSave = int(isSave)
        except ValueError as e:
            print(e)
            print('请输入布尔数字！\n')
            sys.exit()
    # ***************************************************************
    # 构建歌单对象
    sheet = SongSheet()
    sheet.init(audioUrl, sheetId, isSave, fileName)
    baseInfo, songList = sheet.completeOperation()
    return baseInfo, songList, sheet