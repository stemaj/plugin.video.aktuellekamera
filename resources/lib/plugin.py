# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory

from resources.lib import main
from resources.lib import read

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


def loadHeuteJournal():
    a = read.load_url("https://www.zdf.de/nachrichten/heute-journal")
    b = main.getCurrentHeuteJournalLink(a)
    c = read.load_url(b)
    d = main.getCurrentHeuteJournalJson(c)
    e = read.load_url(d)
    return main.HeuteJournal(main.getCurrentHeuteJournalTitle(c), main.getCurrentHeuteJournalMp4(e), main.getCurrentHeuteJournalAge(c))

def loadHeuteXpress():
    c = read.load_url("https://www.zdf.de/nachrichten/heute-sendungen/videos/heute-xpress-aktuelle-sendung-100.html")
    d = main.getCurrentHeuteJournalJson(c)
    e = read.load_url(d)
    return main.HeuteJournal("heute Xpress", main.getCurrentHeuteJournalMp4(e), main.getCurrentHeuteJournalAge(c))

@plugin.route('/')
def index():

    hj = loadHeuteJournal()
    hjL = ListItem(hj.name)
    hjL.setInfo('video', infoLabels={'plot': hj.age})
    addDirectoryItem(plugin.handle, hj.mp4link, hjL)

    hx = loadHeuteXpress()
    hxL = ListItem(hx.name)
    hxL.setInfo('video', infoLabels={'plot': hx.age})
    addDirectoryItem(plugin.handle, hx.mp4link, hxL)

#    addDirectoryItem(plugin.handle, plugin.url_for(
#        show_category, "one"), ListItem("Category One"), True)
#    addDirectoryItem(plugin.handle, plugin.url_for(
#        show_category, "two"), ListItem("Category Two"), True)
    endOfDirectory(plugin.handle)


#@plugin.route('/category/<category_id>')
#def show_category(category_id):
#    addDirectoryItem(
#        plugin.handle, "", ListItem("Hello category %s!" % category_id))
#    endOfDirectory(plugin.handle)

def run(argv):
    plugin.run(argv=argv)
