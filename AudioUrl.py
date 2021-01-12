class AudioUrl:
    localUrl = 'http://localhost:3200'
    httpFrontUrl = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id='
    httpLastUrl = '&g_tk=1922747963&platform=mac&g_tk_new_20200303=1922747963&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0'

    def _mergeUrl(self, id):
        return self.localUrl + id

    # 从官网上直接获取歌单详情
    def getSongListDetailByOfficial(self, id):
        return self.httpFrontUrl + id + self.httpLastUrl

    # 获取QQ音乐的下载地址
    def downLoadQQMusic(self):
        # return self.localUrl + '/downloadQQMusic'
        return self._mergeUrl('/downloadQQMusic')

    # 该方法可能存在问题
    # 获取歌单分类
    def getSongListCategories(self):
        return self._mergeUrl('/getSongListCategories')

    # 获取歌单列表
    def getSongLists(self, categoryId, page=1, limit=20, sortId=5):
        return self._mergeUrl('/getSongLists?categoryId={}'.format(categoryId))

    # 批量获取歌单列表
    def batchGetSongLists(self, categoryIds, page=1, limit=20, sortId=5):
        return self._mergeUrl('/batchGetSongLists')

    # 获取歌单详情
    def getSongListDetail(self, disstid):
        # return self.localUrl + '/getSongListDetail?disstid={}'.format(disstid)
        return self._mergeUrl('/getSongListDetail?disstid={}'.format(disstid))

    # 获取 MV 标签
    def getMvByTag(self):
        return self._mergeUrl('/getMvByTag')

    # 获取 MV 播放信息
    def getMvPlay(self, vid):
        return self._mergeUrl('/getMvPlay?vid={}'.format(vid))

    # 获取歌手 MV
    def getSingerMV(self, singermid, order='time', limit=5):
        return self._mergeUrl('/getSingerMV?singermid={}&order={}&limit={}'.format(singermid, order, limit))

    # 获取歌手热门歌曲
    def getSingerHotsong(self, singermid, page=0, limit=5):
        return self._mergeUrl('/getSingerHotsong?singermid={}&limit={}&page={}'.format(singermid, limit, page))

    # 获取相似歌手
    def getSimilarSinger(self, singermid):
        return self._mergeUrl('/getSimilarSinger?singermid={}'.format(singermid))

    # 获取歌手信息
    def getSingerDesc(self, singermid):
        return self._mergeUrl('/getSingerDesc?singermid={}'.format(singermid))

    # 获取歌手列表
    def getSingerList(self, area='-100', genre='-100', index='-100', sex='-100'):
        return self._mergeUrl('/getSingerList?area={}&sex={}&index={}&genre={}'.format(area, sex, index, genre))

    # 获取歌手被关注数量信息
    def getSingerStarNum(self, singermid):
        return self._mergeUrl('/getSingerStarNum?singermid={}'.format(singermid))

    # 获取电台列表
    def getRadioLists(self):
        return self._mergeUrl('/getRadioLists')

    # 获取专辑
    def getAlbumInfo(self, albummid):
        return self._mergeUrl('/getAlbumInfo?albummid={}'.format(albummid))

    # 获取数字专辑
    def getDigitalAlbumLists(self):
        return self._mergeUrl('/getDigitalAlbumLists')

    # 获取歌曲歌词
    def getLyric(self, songmid, isFormat=False):
        return self._mergeUrl('/getLyric?songmid={}'.format(songmid))

    # 获取 MV
    def getMv(self, area_id=15):
        return self._mergeUrl('/getMv')

    # 获取新碟信息
    def getNewDisks(self, page=1, limit=20):
        return self._mergeUrl('/getNewDisks')

    # 获取歌手专辑
    def getSingerAlbum(self, singermid, page=1, limit=20):
        return self._mergeUrl('/getSingerAlbum?singermid={}'.format(singermid))

    # 获取歌曲相关信息
    def getSongInfo(self, songmid):
        return self._mergeUrl('/getSongInfo?songmid={}'.format(songmid))

    # 该方法可能存在问题
    # 批量获取歌曲相关信息
    def batchGetSongInfo(self, songs):
        return self._mergeUrl('/batchGetSongInfo')

    # 获取歌曲VKey
    def getMusicVKey(self, songmid):
        return self._mergeUrl('/getMusicVKey?songmid={}'.format(songmid))

    # 获取搜索热词
    def getHotkey(self):
        return self._mergeUrl('/getHotkey')

    # 获取关键词搜索提示
    def getSmartbox(self, key):
        return self._mergeUrl('/getSmartbox?key={}'.format(key))

    # 获取搜索结果
    def getSearchByKey(self, key, remoteplace='song', page=1, limit=10):
        return self._mergeUrl('/getSearchByKey?key={}'.format(key))

    # 获取首页推荐
    def getRecommend(self):
        return self._mergeUrl('/getRecommend')

    # 获取排行榜单列表
    def getTopLists(self, page=1, limit=10):
        return self._mergeUrl('/getTopLists')

    # 获取排行榜单详情
    def getRanks(self, topId, page=1, limit=10):
        return self._mergeUrl('/getRanks')

    # 获取评论信息
    # ···································

    # 该方法存在一些问题
    # 获取歌词 + 专辑图片
    def getImageUrl(self, id, size='300*300'):
        return self._mergeUrl('/getImageUrl?id={}'.format(id))

    # 获取票务信息
    def getTicketInfo(self):
        return self._mergeUrl('/getTicketInfo')
