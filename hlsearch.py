#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto
# 2015-06-09

import os
import commands
import sys

import websearch.config as config
logfile = config.logfile

def main():
    searchword = commands.getoutput('xsel -o')
    URL = "http://ejje.weblio.jp/content/%s" % searchword

    # save the log to logfile
    date = commands.getoutput('date +%F_%T')
    log = date + ' ' + searchword + '\n'
    with open(logfile, 'a') as l:
        l.writeline(log)

    # go to webpage
    os.system("firefox -new-tab " + '"' +  URL + '"')
    sys.exit()

if __name__ == '__main__':
    main()
