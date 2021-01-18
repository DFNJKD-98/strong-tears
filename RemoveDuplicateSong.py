import Database
import SSheet
from prettytable import PrettyTable
import sqlite3
from DbData import DbData


class DuplicatesPipeline(object):
    """
    根据音乐的song_id，对爬取过的音乐进行去重
    """

    def __init__(self):
        self.song_ids = set()
        self.cfSong = {}

    def process_item(self, item, songList):
        if item[0] in self.song_ids:
            if item[0] in self.cfSong.keys():
                self.cfSong[item[0]][1] += 1
            else:
                self.cfSong[item[0]] = [item, 1]
        else:
            self.song_ids.add(item[0])
            songList.append(item)


database = Database.Database()


# 获取所有歌曲数据
def getSongDatas():
    tool = DbData()
    tableName = tool.col_data('name', index=True)
    sheetData = []
    for item in tableName:
        sheetData.append(tool.all_data(table=item))
    return sheetData


# 存储去重后的歌曲信息
def duplicate_removal_and_save(isSave=False):
    sheet = SSheet.SongSheet('1', '去重歌曲表', '1')
    tool = DuplicatesPipeline()
    data = getSongDatas()
    for table in data:
        for song in table:
            tool.process_item(song, sheet.songList)
    if isSave:
        database.create_table(sheet.fileName)
        database.insert_data(sheet)
    return tool.cfSong


# 存储重复歌曲信息
def duplicateSongs_sort(songs):
    conn = sqlite3.connect('songSheet.db')
    c = conn.cursor()
    sql = 'create table 去重歌曲排名表 ' + '''
                (id text not null,
                 name text not null,
                 paidSong int not null,
                 singer text not null,
                 重复次数 int not null);
        '''
    c.execute(sql)
    sql = 'insert into 去重歌曲排名表 values(?, ?, ?, ?, ?) '
    songTable = PrettyTable()
    songTable.field_names = ['歌曲ID', '歌曲名称', '付费', '歌手', '重复次数']
    for key in songs.keys():
        x = list(songs[key][0])
        x.append(songs[key][1])
        c.execute(sql, tuple(x))
        songTable.add_row(x)
    songTable.align["歌曲名称"] = 'l'
    print(songTable.get_string(sortby="重复次数", reversesort=True))
    conn.commit()
    c.close()
    conn.close()


def Flush():
    database.delete_table('去重歌曲排名表')
    database.delete_table('去重歌曲表')
    duplicateSongs_sort(duplicate_removal_and_save(isSave=True))


Flush()
