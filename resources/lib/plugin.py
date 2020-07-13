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

#import xbmc

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


def loadHeuteJournal():
    a = read.load_url("https://www.zdf.de/nachrichten/heute-journal")
    b = main.getCurrentHeuteJournalLink(a)
    #xbmc.log("###xxx###" + b, xbmc.LOGFATAL)
    c = read.load_url(b)
    d = main.getCurrentHeuteJournalJson(c)
    #xbmc.log("#########" + d, xbmc.LOGFATAL)
    if len(d) > 0:
        e = read.load_url(d, True)
        if e:
          return main.HeuteJournal(main.getCurrentHeuteJournalTitle(c), main.getCurrentHeuteJournalMp4(e), main.getCurrentHeuteJournalAge(c))
        else:
          link = read.getVideoLinkByTryingFromApiLink(d,0)
          #xbmc.log("##LINK#######" + link, xbmc.LOGFATAL)
          return main.HeuteJournal(main.getCurrentHeuteJournalTitle(c), link, main.getCurrentHeuteJournalAge(c))
          
    else:
        return main.HeuteJournal("heute journal noch nicht verfügbar", "", "")

def loadHeute19Uhr():
    a = read.load_url("https://www.zdf.de/nachrichten/heute-19-uhr/")
    b = main.getCurrentHeute19UhrLink(a)
    c = read.load_url(b)
    d = main.getCurrentHeuteJournalJson(c)
    if len(d) > 0:
        e = read.load_url(d, True)
        if e:
          return main.HeuteJournal(main.getCurrentHeuteJournalTitle(c), main.getCurrentHeuteJournalMp4(e), main.getCurrentHeuteJournalAge(c))
        else:
          link = read.getVideoLinkByTryingFromApiLink(d,1)
          return main.HeuteJournal(main.getCurrentHeuteJournalTitle(c), link, main.getCurrentHeuteJournalAge(c))
    else:
        return main.HeuteJournal("heute 19 Uhr noch nicht verfügbar", "", "")

def loadHeuteXpress():
    c = read.load_url("https://www.zdf.de/nachrichten/heute-sendungen/videos/heute-xpress-aktuelle-sendung-100.html")
    d = main.getCurrentHeuteJournalJson(c)
    if len(d) > 0:
        e = read.load_url(d, True)
        if e:
          return main.HeuteJournal("heute Xpress", main.getCurrentHeuteJournalMp4(e), main.getCurrentHeuteJournalAge(c))
        else:
          link = read.getVideoLinkByTryingFromApiLink(d,2)
          return main.HeuteJournal("heute Xpress", link, main.getCurrentHeuteJournalAge(c))
    else:
        return main.HeuteJournal("heute Xpress noch nicht verfügbar", "", "")

@plugin.route('/')
def index():

    hj = loadHeuteJournal()
    hjL = ListItem(hj.name)
    hjL.setInfo('video', infoLabels={'plot': hj.age})
    addDirectoryItem(plugin.handle, hj.mp4link, hjL)

    h19 = loadHeute19Uhr()
    h19L = ListItem(h19.name)
    h19L.setInfo('video', infoLabels={'plot': h19.age})
    addDirectoryItem(plugin.handle, h19.mp4link, h19L)

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
