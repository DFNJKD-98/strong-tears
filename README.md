<h2 align="center">项目说明</h2>


### 功能概述

- 根据歌单ID ，爬取歌单所有歌曲信息，并保存到数据库中
- 去重排序，筛选出适合自己的歌单列表(这个功能还没有做好)

### 功能详解

- 程序从main.py文件进入
- 支持从默认路径下的json文件建立数据库
- 对于所有步骤封装好了一个函数`allsteps()`，函数分为三个模式——localhost、localFile、internet
  - localhost——启动本地服务器后，访问本地服务器地址，获取歌单信息
  - localFile——从某个json文件中，导入一个歌单
  - Internet——从网络地址中，进行爬虫并保存json数据，获取歌单信息
- 对于所有的歌单进行数据库保存
- 对所有歌单中的所有歌曲进行**去重**和**重复次序的排序**

---
<h2 align="center">数据含义解析</h2>

### Json数据解析

---

### 歌曲的字段说明

- singer_name：歌手名称，数组形式，因为一首歌可能由多名歌手合唱
- song_name：歌曲名称
- subtitle：歌曲的子标题
- album_name：专辑名称
- singer_id：歌手id，数组形式
- singer_mid：歌手的mid，数组形式
- song_time_public：歌曲发行时间
- song_type：歌曲类型
- language：歌曲语种
- song_id：歌曲id
- song_mid：歌曲mid
- song_url：歌曲播放的url
- lyric：歌词
- hot_comments：歌曲的精彩评论(此处只爬取了歌曲的精彩评论，部分比较冷门的歌曲有最新评论，但是没有精彩评论)，数组形式。若无精彩评论，置为"null"
  -   comment_name：评论者的昵称
  -   comment_text：评论内容



### URL参数解析

- 域名+虚拟路径——`c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg`
- cv=10000
- ct=19
- newsong=1
- tpl=wk
- id=7277345291——歌单ID
- g_tk=1922747963
- platform=mac
- g_tk_new_20200303
- loginUin=0——登录的QQ账户
- hostUin=0
- format=json——请求格式
- inCharset=GB2312
- outCharset=utf-8
- notice=0
- platform=jqspaframe.json
- needNewCode=0

