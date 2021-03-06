from prettytable import from_db_cursor
import sqlite3


def getSongList(tableName):
    con = sqlite3.connect('songSheet.db')
    cur = con.cursor()
    sql = "select * from " + tableName
    cur.execute(sql)
    data = from_db_cursor(cur)
    cur.close()
    con.close()
    data = data.get_html_string(sortby="重复次数", reversesort=True)
    return data


line1 = '''
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>SpiderShow</title>
    <link rel="stylesheet" href="../static/css/bootstrap.min.css">
    <link rel="stylesheet" href="../static/css/baseStyle.css">
    <style>
        nav {
            margin: 0 auto 30px auto;
            color: #f46d3e;
            text-align: center;
            letter-spacing: 2px;
            box-shadow: 0 2px 3px #c5c5c5;
        }
    </style>
    <script src="../static/js/jquery-3.5.1.min.js"></script>
    <script src="../static/js/popper.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>
</head>
<body>
    <nav class="navbar navbar-expand-sm bg-light navbar-light" id="app">
        <h3>QQ音乐歌单歌曲信息</h3>
    </nav>
    <div class="container">
'''
line2 = getSongList('去重歌曲排名表')
line3 = '''
</div>
</body>
</html>
'''
with open(file='templates/test.html', encoding='utf-8', mode='w') as f:
    f.write(line1 + line2 + line3)
