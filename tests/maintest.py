import unittest
from resources.lib import read
from resources.lib import main

class Test_ParseFiles(unittest.TestCase):

    def test_file000(self):
        a = read.load_file('000')
        b = main.getCurrentHeuteJournalLink(a)
        self.assertEqual(b,"https://www.zdf.de/nachrichten/heute-journal/heute-journal-vom-16-april-2020-100.html")

    def test_file001(self):
        a = read.load_file('001')
        b = main.getCurrentHeuteJournalTitle(a)
        self.assertEqual(b,"heute journal vom 16.04.2020")
        c = main.getCurrentHeuteJournalJson(a)
        self.assertEqual(c,"https://api.zdf.de/tmd/2/zdf_pd_download_1/vod/ptmd/mediathek/200416_sendung_hjo")
        d = main.getCurrentHeuteJournalAge(a)
        self.assertEqual(d[:15],"Erschienen vor ")

    def test_file002(self):
        a = read.load_file('002')
        c = main.getCurrentHeuteJournalMp4(a)
        self.assertEqual(c, "https://downloadzdf-a.akamaihd.net/mp4/zdf/20/04/200416_sendung_hjo/4/200416_sendung_hjo_3328k_p15v15.mp4")

    def test_file003(self):
        a = read.load_file('003')
        c = main.getCurrentHeuteJournalJson(a)
        self.assertEqual(c,"https://api.zdf.de/tmd/2/zdf_pd_download_1/vod/ptmd/mediathek/200417_1949_hko")

    def test_file004(self):
        a = read.load_file('004')
        b = main.getCurrentHeute19UhrLink(a)
        self.assertEqual(b,"https://www.zdf.de/nachrichten/heute-19-uhr/200501-heute-sendung-19-uhr-100.html")

    def test_file005(self):
        a = read.load_file('005')
        b = main.getCurrentHeuteJournalTitle(a)
        self.assertEqual(b,"ZDF heute Sendung vom 01.05.2020")
        c = main.getCurrentHeuteJournalJson(a)
        self.assertEqual(c,"https://api.zdf.de/tmd/2/zdf_pd_download_1/vod/ptmd/mediathek/200501_sendung_h19")
        d = main.getCurrentHeuteJournalAge(a)
        self.assertEqual(d[:15],"Erschienen vor ")


    def test_date(self):
        dmy = main.getDayMonthYearFromTitle("ZDF heute Sendung vom 01.05.2020")
        self.assertEqual(dmy[0], "01")
        self.assertEqual(dmy[1], "05")
        self.assertEqual(dmy[2], "20")


