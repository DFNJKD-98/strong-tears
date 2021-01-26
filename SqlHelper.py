import pymysql


def conn_c():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='dfnjkd98',
                           db='django1', charset='utf8')
    c = conn.cursor()
    return conn, c


def helper(sql, data=None, res=False):
    if data is None:
        data = []
    conn, c = conn_c()
    try:
        if not data:
            c.execute(sql, data)
        elif isinstance(data[0], tuple):
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
