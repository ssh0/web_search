#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, September 2014

logfile = '/home/shotaro/Dropbox/log.txt'

# choose the default browser by comment out
# or you can edit to any browser
browser = {'default':
           'firefox -new-tab '
#           'chromium-browser -new-tab '
#           'google-chrome -new-tab '
#           'opera -newtab '
            ,
           }

site = {
        # default: Google検索
        'default-search': r'https://www.google.co.jp/#q=%s',

        # 'w': Wikipedia
        '-w': r'https:ja.wikipedia.org/wiki/%s',

        # 'n': niconico動画
        '-n': r'http://www.nicovideo.jp/search/%s',

        # 'p': Google画像検索
        #'-p': r'https://www.google.com/search?q=%s&um=1&ie=UTF-8&hl=ja&tbm=isch&source=og&sa=N&tab=wi',

        # 'y': Youtubeで検索
        '-y': r'http://www.youtube.com/results?search_query=%s&sm=3',

        # 'rt' Yahooリアルタイム検索
        '-rt': r'http://realtime.search.yahoo.co.jp/search?p=%s&ei=UTF-8',

        # 'sc' Google Scholar検索
        '-sc': r'http://scholar.google.co.jp/scholar?q=%s&hl=ja&as_sdt=0,5',

        # '-t': 翻訳
        '-t': r'http://ejje.weblio.jp/content/%s'
        }
