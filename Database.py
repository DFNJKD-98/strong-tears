import sqlite3
from SSheet import SongSheet
from DbData import DbData


class Database:
    dbPath = 'songSheet.db'

    def __init__(self):
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        sql = 'create table ' + '所有歌单基本信息表' + '''
                            (id text not null,
                             name text not null,
                             tbl_name text not null,
                             length int not null,
                             introduction text not null);
                        '''
        try:
            c.execute(sql)
        except sqlite3.OperationalError as e:
            print(e)
        finally:
            conn.commit()
            c.close()
            conn.close()
            print('初始化数据库完成!')

    def _conn(self):
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        return conn, c

    def create_table(self, table):
        if isinstance(table, SongSheet):
            table = table.fileName
        conn, c = self._conn()
        sql = 'create table ' + table + '''
            (id text not null,
             name text not null,
             paid int not null,
             singer text not null);
        '''
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()
        print('成功建表')
        return True

    def record_basicInfo(self, baseInfo):
        conn, c = self._conn()
        sql = 'insert into 所有歌单基本信息表 ' + 'values(?, ?, ?, ?, ?)'
        c.execute(sql, tuple(baseInfo))
        conn.commit()
        c.close()
        conn.close()

    def insert_data(self, tableName, songList):
        conn, c = self._conn()
        sql = 'insert into ' + tableName + ' values(?, ?, ?, ?)'
        for song in songList:
            c.execute(sql, song.tuple())
        conn.commit()
        c.close()
        conn.close()
        print('往 ' + tableName + '表 插入数据成功!')

    def delete_table(self, table):
        if isinstance(table, SongSheet):
            table = table.fileName
        conn, c = self._conn()
        sql = "delete from 所有歌单基本信息表 where tbl_name='{}'".format(table)
        c.execute(sql)
        conn.commit()
        print('更新完成 所有歌曲基本信息表')
        sql = 'drop table ' + table
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()
        print('成功删除 ' + table + '表')

    def deleteAllTable(self):
        tool = DbData()
        res = tool.all_data(index=True)
        for item in res:
            self.delete_table(item[2])
        self.delete_table('所有歌单基本信息表')
