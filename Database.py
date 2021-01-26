from SSheet import SongSheet
from SqlHelper import helper as mysql
from SqliteHelper import helper as sqlite
import sys
from SelfDefinedException import SheetRepeatException


class Database:
    def __init__(self, dbType='sqlite'):
        self.dbType = dbType
        sql = 'create table ' + '所有歌单基本信息表' + '''
                            (id text not null unique,
                             name text not null,
                             tbl_name text not null,
                             length int not null,
                             introduction text not null);
                    '''
        self._execute(sql)
        print('初始化数据库完成!')

    def _execute(self, sql, data=None, res=False):
        if self.dbType == 'sqlite':
            return sqlite(sql, data, res)
        elif self.dbType == 'mysql':
            return mysql(sql, data, res)

    def create_table(self, table):
        if isinstance(table, SongSheet):
            table = table.fileName
        sql = 'create table ' + table + '''
            (id text not null,
             name text not null,
             paid int not null,
             singer text not null);
        '''
        self._execute(sql)
        print('成功建表')
        return True

    def record_basicInfo(self, baseInfo):
        if self.dbType == 'sqlite':
            sql = 'insert into 所有歌单基本信息表 values(?, ?, ?, ?, ?)'
        elif self.dbType == 'mysql':
            sql = 'insert into 所有歌单基本信息表 values(%s, %s, %s, %s, %s)'
        self._execute(sql, tuple(baseInfo))

    def insert_data(self, tableName, songList):
        if self.dbType == 'sqlite':
            sql = 'insert into ' + tableName + ' values(?, ?, ?, ?)'
        elif self.dbType == 'mysql':
            sql = 'insert into ' + tableName + ' values(%s, %s, %s, %s)'
        data = []
        for song in songList:
            data.append(song.tuple())
        self._execute(sql, data)
        print('往 ' + tableName + '表 插入数据成功!')

    def delete_table(self, table):
        if isinstance(table, SongSheet):
            table = table.fileName
        sql = "delete from 所有歌单基本信息表 where tbl_name='{}'".format(table)
        self._execute(sql)
        print('更新完成 所有歌曲基本信息表')
        sql = 'drop table ' + table
        self._execute(sql)
        print('成功删除 ' + table + '表')

    def deleteAllTable(self):
        sql = 'select tbl_name from 所有歌单基本信息表'
        nameList = self._execute(sql, res=True)
        for name in nameList:
            self.delete_table(name[0])
        self.delete_table('所有歌单基本信息表')

    def check_repetitive_sheet(self, sheetId):
        sql = 'select id from 所有歌单基本信息表'
        sheet_id_list = self._execute(sql, res=True)
        for sheet_id in sheet_id_list:
            try:
                if sheetId == sheet_id[0]:
                    raise SheetRepeatException("已经导入该歌单！！！\n")
            except SheetRepeatException as e:
                print(e)
                sys.exit(1)
        return False

    def get_name_by_id(self, sheetId):
        sql = 'select tbl_name from 所有歌单基本信息表 where id={}'.format(sheetId)
        tbl_name = self._execute(sql, res=True)
        return tbl_name[0]
