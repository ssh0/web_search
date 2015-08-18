#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, September 2014
# 参考: https://gist.github.com/evoL/1650115

from gi.repository import Gtk
import config
logfile = config.logfile


class EntryMultiCompletion(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.completion = Gtk.EntryCompletion()

        # customize the matching function to match multiple space
        # separated words
        self.completion.set_match_func(self.match_func, None)

        # handle the match-selected signal, raised when a completion
        # is selected from popup
        self.completion.connect('match-selected', self.on_completion_match)
        self.set_completion(self.completion)

    def match_func(self, completion, key_string, iter, data):
        model = self.completion.get_model()
        modelstr = model[iter][0]

        # check if the user has typed in a space char,
        # get the last word and check if it matches something
        if ' ' in key_string:
            last_word = key_string.split()[-1]
            return modelstr.startswith(last_word)

        # we have only one word typed
        return modelstr.startswith(key_string)

    def on_completion_match(self, completion, model, iter):
        current_text = self.get_text()

        # if more than a word has been typed, we throw away the
        # last one because we want to replace it with the matching word
        # note: the user may have typed only a part of the entire word
        #       and so this step is necessary
        if ' ' in current_text:
            current_text = ' '.join(current_text.split()[:-1])
            print current_text
            current_text = '%s %s' % (current_text, model[iter][0])
            print current_text
        else:
            current_text = model[iter][0]
            print current_text

        # set back the whole text
        self.set_text(current_text)
        # move the cursor at the end
        self.set_position(-1)

        # stop the event propagation
        return True
