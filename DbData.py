import SSheet
import sqlite3


class DbData:
    dbPath = 'songSheet.db'

    def _conn(self):
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        return conn, c

    # 获取一张表的全部数据
    def all_data(self, table='myfav', index=False):
        if index:
            table = '所有歌单基本信息表'
        else:
            if isinstance(table, SSheet.SongSheet):
                table = table.fileName
        conn, c = self._conn()
        sql = 'select * from ' + table
        c.execute(sql)
        data = c.fetchall()
        c.close()
        conn.close()
        return data

    # 获取一张表的一列
    def col_data(self, colName, table='myfav', index=False):
        conn, c = self._conn()
        if index:
            table = '所有歌单基本信息表'
        else:
            if isinstance(table, SSheet.SongSheet):
                table = table.fileName
        sql = 'select ' + colName + ' from ' + table
        try:
            c.execute(sql)
        except Exception as e:
            print(e)
        data = c.fetchall()
        c.close()
        conn.close()
        return list(data)

    # 根据info获取一张表中的一行
    def row_data(self, info, table='myfav', index=False):
        all_data = self.all_data(table=table, index=index)
        for row_data in all_data:
            if info in row_data:
                return list(row_data)
        return []
