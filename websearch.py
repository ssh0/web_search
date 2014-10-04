#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, September
#
# NOTE: bug: This code doesn't run correctly when the browser hasn't run.

from gi.repository import Gtk
import os
import commands
import sys

import websearch.config as config
import websearch.prediction as prediction
logfile = config.logfile


class Window(Gtk.Window):

    def __init__(self):
        self.window = Gtk.Window.__init__(self, title="search")

        # list data for completion from logfile
        lists = []
        with open(logfile) as f:
            for s in f.readlines():
                lists += unicode(s, 'utf-8').split()[1:]
        lists = set(lists)
        liststore = Gtk.ListStore(str)
        for match in lists:
            liststore.append([match])

        self.entry = prediction.EntryMultiCompletion()
        self.entry.completion.set_model(liststore)
        self.entry.completion.set_text_column(0)
        self.entry.completion.set_popup_completion(popup_completion=True)
        self.entry.connect("activate", self.enter_callback)
        self.add(self.entry)

    def enter_callback(self, event):
        # get text from entry widget
        search_term = self.entry.get_text().split()

        # if text is None, do nothing
        if len(search_term) == 0:
            return 0

        # in config.py, site must be dictionary that
        # key is option argument and value is website's address
        site = config.site

        # find option
        option= search_term[0]
        if option in site:
            goto = site[option][0]
            n = site[option][1]
            del search_term[0]
            if len(search_term) == 0:
                return 0
        # if there is no option, go to default site
        else:
            goto = site['default-search'][0]
            n = site['default-search'][1]

        # join search terms
        if len(search_term) > 1:
            t = ' '.join(search_term)
        else:
            t = search_term[0]

        # save the log to logfile
        date = commands.getoutput('date +%F_%T')
        log =  date + ' ' + t + '\n'
        with open(logfile, 'a') as l:
            l.writelines(log)

        # go to website
        base = config.browser['default']
        words = tuple([t for i in range(n)])
        goto = goto % words
        os.system(base + '"' + goto + '"')
        sys.exit()


def main():
    win = Window()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
