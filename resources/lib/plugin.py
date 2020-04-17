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
    c = main.getCurrentHeuteJournalJson(b)
    return main.HeuteJournal(main.getCurrentHeuteJournalTitle(b), main.getCurrentHeuteJournalMp4(c))

@plugin.route('/')
def index():

    hj = loadHeuteJournal()
    addDirectoryItem(plugin.handle, hj.mp4link, ListItem(hj.name))

    addDirectoryItem(plugin.handle, plugin.url_for(
        show_category, "one"), ListItem("Category One"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(
        show_category, "two"), ListItem("Category Two"), True)
    endOfDirectory(plugin.handle)


@plugin.route('/category/<category_id>')
def show_category(category_id):
    addDirectoryItem(
        plugin.handle, "", ListItem("Hello category %s!" % category_id))
    endOfDirectory(plugin.handle)

def run(argv):
    plugin.run(argv=argv)
