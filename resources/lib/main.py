import re
import json

class HeuteJournal():
  def __init__(self, name_, mp4link_):
        self.name = name_
        self.mp4link = mp4link_

def getCurrentHeuteJournalLink(bytes):
    return "https://www.zdf.de" + str(re.compile("href=\"(.+)\" title=\"heute journal").findall(bytes.decode('utf-8'))[0])

def getCurrentHeuteJournalJson(bytes):
    return str(re.compile("contentUrl\": \"(.+)\"").findall(bytes.decode('utf-8'))[0])

def getCurrentHeuteJournalMp4(bytes):
    b = json.loads(bytes)
    return b["priorityList"][0]["formitaeten"][0]["qualities"][0]["audio"]["tracks"][0]["uri"]

def getCurrentHeuteJournalTitle(bytes):
    return str(re.compile("title\" content=\"(.+)\" />").findall(bytes.decode('utf-8'))[0])
    