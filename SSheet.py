import urllib.request
import json
from prettytable import PrettyTable
from UserAgent import get_User_Agent as user_agent
import re
from DbData import DbData
import sys
from SelfDefinedException import SheetRepeatException


class SongSheet:
    id = ''
    name = ''
    fileName = ''
    length = 0
    introduction = ''
    frontUrl = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id='
    lastUrl = '&g_tk=1922747963&platform=mac&g_tk_new_20200303=1922747963&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0'
    localUrl = 'http://localhost:3200/getSongListDetail?disstid='

    def __init__(self, sheet_id, fileName, isSave):
        # self.url = self.frontUrl + sheet_id + self.lastUrl
        self.url = self.localUrl + sheet_id
        self.isSave = isSave
        pat = re.compile(r'[\u4e00-\u9fa5A-Za-z0-9_]')
        # 替换有意义字符为合法字符
        fileName = re.sub(r'[-|,，:：丨]', '_', fileName)
        # 去除无意义非法字符
        fileName = ''.join(pat.findall(fileName))
        # 判断开头是否为数字
        if fileName[0].isdigit():
            fileName = '歌单_' + fileName
        self.fileName = fileName

    def getJsonText(self):
        try:
            with open('./jsonFileList/' + self.fileName + '.json', 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open('./jsonFileList/' + self.fileName + '.json', 'r', encoding='gbk') as f:
                content = f.read()
        jsonText = json.loads(content)
        return jsonText

    def save_JsonFile(self):
        header = user_agent()
        print('URL：', self.url)
        print('header：', header)
        request = urllib.request.Request(self.url, headers=header, method='GET')
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        if self.isSave:
            with open('./jsonFileList/' + self.fileName + '.json', 'w', encoding='utf-8') as f:
                f.write(html)
        else:
            print(html)

    def songList(self):
        songList = []
        jsonText = self.getJsonText()
        target = jsonText['data']['cdlist'][0]['songlist']
        # 获取歌单长度
        self.length = len(target)
        for i in range(0, self.length):
            # 获取歌曲id
            mid = target[i]['mid']
            # 获取歌曲名称
            songName = target[i]['name']
            # 获取歌曲付费信息
            paidSong = target[i]['pay']['pay_play']
            # 获取歌曲作者信息
            singerNameList = []
            for j in range(0, len(target[i]['singer'])):
                singerNameList.append(target[i]['singer'][j]['name'])
            singerName = '/'.join(singerNameList)
            # 实例化歌曲类
            song = Song((mid, songName, paidSong, singerName))
            # 存入一首歌的信息
            songList.append(song)
        return songList

    def baseInfo(self, outFormat='list'):
        jsonText = self.getJsonText()
        self.id = jsonText['data']['cdlist'][0]['disstid']
        self.name = jsonText['data']['cdlist'][0]['dissname']
        self.length = len(jsonText['data']['cdlist'][0]['songlist'])
        self.introduction = jsonText['data']['cdlist'][0]['desc'].replace('<br>', ' ')
        if outFormat == 'list':
            return [self.id, self.name, self.fileName, self.length, self.introduction]
        elif outFormat == 'tuple':
            return self.id, self.name, self.fileName, self.length, self.introduction

    def outputInfo(self):
        print('*' * 120)
        print('id：', self.id)
        print('name：', self.name)
        print('fileName：', self.fileName)
        print('length：', self.length)
        print('introduction：', self.introduction)
        songTable = PrettyTable()
        songTable.field_names = ['id', 'name', 'paid', 'singer']
        songTable.align['name'] = 'l'
        songTable.align['singer'] = 'l'
        songList = self.songList()
        for song in songList:
            songTable.add_row(song.list())
        print(songTable)

    def connInternet(self):
        self.save_JsonFile()
        self.baseInfo()


class Song:
    def __init__(self, info):
        self.id = info[0]
        self.songName = info[1]
        self.paid = info[2]
        self.singerName = info[3]

    def tuple(self):
        return self.id, self.songName, self.paid, self.singerName

    def list(self):
        return [self.id, self.songName, self.paid, self.singerName]


def serveGuid():
    # 引导输入内容
    songSheetId = input('输入QQ音乐歌单id：')
    fileName = input('输入保存的文件名：')
    isSave = input('是否保存json文件(默认保存)?')
    print('\n')
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
    # 检测是否已经导入过歌单
    tool = DbData()
    if songSheetId == '':
        method = 'local'
    else:
        try:
            if tool.row_data(info=songSheetId, index=True):
                raise SheetRepeatException("已经导入该歌单！！！\n")
        except SheetRepeatException as e:
            print(e)
            sys.exit(1)
        else:
            method = 'internet'
    # 构建歌单对象
    sheet = SongSheet(songSheetId, fileName, isSave)
    return sheet, method
