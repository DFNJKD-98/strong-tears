import sqlite3

dbPath = 'songSheet.db'


def conn_c():
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    return conn, c


def helper(sql, data=None, res=False):
    if data is None:
        data = ()
    conn, c = conn_c()
    try:
        if data == ():
            c.execute(sql, data)
        elif isinstance(data, list):
            c.executemany(sql, data)
        else:
            c.execute(sql, data)
        if res:
            res = c.fetchall()
            return res
    except Exception as e:
        print(e)
    finally:
        conn.commit()
        c.close()
        conn.close()
    return []
