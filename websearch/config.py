#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, September 2014

import os

logfile = os.path.expanduser("~/Dropbox/log.txt")
use_prediction = False

# browser option and setting toggle logging
browser = {"=": ("luakit -n ", True),
           "=firefox": ("firefox --new-tab ", True),
           "=s": ("firefox --new-tab ", False),
           "=silent": ("firefox --new-tab ", False),
           "=w": ("firefox --new-window ", True),
           "=window": ("firefox --new-window ", True),
           "=p": ("firefox --private-window ", False),
           "=private": ("firefox --private-window ", False),
           "=chromium": ("chromium-browser -new-tab ", True),
           "=chrome": ("google-chrome -new-tab ", True),
           "=opera": ("opera -newtab ", True),
           "=operaprivate": ("opera -newprivatetab ", False),
           "=luakit": ("luakit -n ", True),
           "=w3m": ("urxvtc -e w3m ", True),
           }

site = {
        # default: Google検索
        "default-search": (r"https://www.google.co.jp/search?q=%s", 1),

        # I'm feeling lucky!
        "-!": (r"https://www.google.co.jp/search?q=%s&btnI=I", 1),

        # "w": Wikipedia
        "-w": (r"https:ja.wikipedia.org/wiki/%s", 1),

        # "n": niconico動画
        "-n": (r"http://www.nicovideo.jp/search/%s", 1),

        # "nd": ニコニコ大百科
        "-nd": (r"http://dic.nicovideo.jp/s/al/a/%s", 1),

        # "p": Google画像検索
        "-p": (r"http://www.google.com/search?hl=ja&site=imghp&tbm=isch&source=hp&q=%s&oq=%s", 2),

        # "m": Google Map
        "-m": (r"https://www.google.com/maps/place/%s", 1),

        # "mfh": Google Map Navigation "from Home to ***"
        # if you set the searching language 'English',
        # then replace "自宅" to "Home"
        "-mfh": (r"https://www.google.com/maps/dir/自宅/%s", 1),

        # "mfw": Google Map Navigation "from Work to ***"
        # if you set the searching language 'English',
        # then replace "職場" to "Work"
        "-mfw": (r"https://www.google.com/maps/dir/職場/%s", 1),

        # "mfh": Google Map Navigation "from *** to Home"
        # if you set the searching language 'English',
        # then replace "自宅" to "Home"
        "-mth": (r"https://www.google.com/maps/dir/%s/自宅", 1),

        # "mfw": Google Map Navigation "from *** to Work"
        # if you set the searching language 'English',
        # then replace "職場" to "Work"
        "-mtw": (r"https://www.google.com/maps/dir/%s/職場", 1),

        # "ip": IP address search
        "-ip": (r"http://www.ip-adress.com/whois/%s", 1),

        # 'f': flickr
        "-f": (r"https://www.flickr.com/search/?text=%s&safe_search=3", 1),

        # "y": Youtubeで検索
        "-y": (r"http://www.youtube.com/results?search_query=%s&sm=3", 1),

        # "rt" Yahooリアルタイム検索
        "-rt": (r"http://realtime.search.yahoo.co.jp/search?p=%s&ei=UTF-8", 1),

        # "sc" Google Scholar検索
        "-sc": (r"http://scholar.google.co.jp/scholar?as_vis=1&q=%s&hl=ja&as_sdt=1,5", 1),

        # "q" Qiita 検索
        "-q": (r"http://qiita.com/search?q=%s", 1),

        # "g" Githubを検索
        "-g": (r"https://github.com/search?q=%s", 1),

        # "gu" Githubを検索(ユーザーを検索)
        "-gu": (r"https://github.com/search?q=%s&type=Users", 1),

        # "gs" Gistを検索
        "-gs": (r"https://gist.github.com/search?utf8=✓&q=%s", 1),

        # "t": 翻訳
        "-t": (r"http://ejje.weblio.jp/content/%s", 1)
        }
