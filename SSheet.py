import urllib.request
import json
from prettytable import PrettyTable
from UserAgent import get_User_Agent as user_agent
import re
from os import rename


class SongSheet:
    id = ''
    name = ''
    fileName = ''
    length = 0
    introduction = ''
    url = ''
    isSave = ''

    def _initFileName(self, fileName):
        if fileName:
            pat = re.compile(r'[\u4e00-\u9fa5A-Za-z0-9_]')
            # 替换有意义字符为合法字符
            fileName = re.sub(r'[-|,，:：丨·]', '_', fileName)
            # 去除无意义非法字符
            fileName = ''.join(pat.findall(fileName))
            # 判断开头是否为数字
            if fileName[0].isdigit():
                fileName = '歌单_' + fileName
            self.fileName = fileName

    def init(self, url, id, isSave=1, fileName=''):
        self.id = id
        self.url = url
        self.isSave = isSave
        self._initFileName(fileName)

    def getJsonText(self, filePath=''):
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            try:
                with open('./jsonFileList/' + self.fileName + '.json', 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open('./jsonFileList/' + self.fileName + '.json', 'r', encoding='gbk') as f:
                    content = f.read()
        jsonText = json.loads(content)
        return jsonText

    def completeOperation(self):
        header = user_agent()
        print('URL：', self.url)
        print('header：', header)
        request = urllib.request.Request(self.url, headers=header, method='GET')
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # 保存json文件，方便以后无网络恢复数据
        if self.isSave:
            with open('./jsonFileList/' + self.id + '.json', 'w', encoding='utf-8') as f:
                f.write(content)
            print('{} 文件保存成功！'.format(self.fileName))
        else:
            print(content)
        # 从获取到的json内容中初始化参数
        jsonText = json.loads(content)
        baseInfo = self.baseInfo(jsonText)
        songList = self.songList(jsonText)
        rename('./jsonFileList/{}.json'.format(self.id), './jsonFileList/{}.json'.format(self.fileName))
        return baseInfo, songList

    def songList(self, jsonText):
        songList = []
        try:
            target = jsonText['data']['cdlist'][0]['songlist']
            self.length = jsonText['data']['cdlist'][0]['songnum']
        except KeyError:
            target = jsonText['response']['cdlist'][0]['songlist']
            self.length = jsonText['response']['cdlist'][0]['songnum']
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

    def baseInfo(self, jsonText, outFormat='list'):
        try:
            self.id = jsonText['data']['cdlist'][0]['disstid']
            self.name = jsonText['data']['cdlist'][0]['dissname']
            self.length = jsonText['data']['cdlist'][0]['songnum']
            self.introduction = jsonText['data']['cdlist'][0]['desc'].replace('<br>', ' ')
        except KeyError:
            self.id = jsonText['response']['cdlist'][0]['disstid']
            self.name = jsonText['response']['cdlist'][0]['dissname']
            self.length = jsonText['response']['cdlist'][0]['songnum']
            self.introduction = jsonText['response']['cdlist'][0]['desc'].replace('<br>', ' ')
        if not self.fileName:
            self._initFileName(self.name)
        if outFormat == 'list':
            return [self.id, self.name, self.fileName, self.length, self.introduction]
        elif outFormat == 'tuple':
            return self.id, self.name, self.fileName, self.length, self.introduction

    def outputInfo(self, songList):
        print('*' * 120)
        print('id：', self.id)
        print('name：', self.name)
        print('fileName：', self.fileName)
        print('length：', self.length)
        print('introduction：', self.introduction)
        songTable = PrettyTable()
        # 确定输出表格的列名
        songTable.field_names = ['id', 'name', 'paid', 'singer']
        # 调整名称和歌手列的显示格式
        songTable.align['name'] = 'l'
        songTable.align['singer'] = 'l'
        for song in songList:
            songTable.add_row(song.list())
        print(songTable)


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