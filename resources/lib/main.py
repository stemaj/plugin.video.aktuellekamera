import re
import json
import time
import datetime

class HeuteJournal():
  def __init__(self, name_, mp4link_, age_):
        self.name = name_
        self.mp4link = mp4link_
        self.age = age_

def getCurrentHeuteJournalLink(bytes):
    return "https://www.zdf.de" + str(re.compile("href=\"(.+)\" title=\"heute journal").findall(bytes.decode('utf-8'))[0])

def getCurrentHeuteJournalJson(bytes):
    return str(re.compile("contentUrl\": \"(.+)\"").findall(bytes.decode('utf-8'))[0])

def getCurrentHeuteJournalAge(bytes):
    a = str(re.compile("uploadDate\": \"(.+)\.\d\d\d\+02:00\"").findall(bytes.decode('utf-8'))[0])
    try:
        b = datetime.datetime.strptime(a, "%Y-%m-%dT%H:%M:%S")
    except TypeError:
        b = datetime.datetime(*(time.strptime(a, "%Y-%m-%dT%H:%M:%S")[0:6]))
    c = datetime.datetime.now() - b
    s = c.seconds
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    return str.format('Erschienen vor {:02} Stunden und {:02} Minuten', int(hours), int(minutes))

def getCurrentHeuteJournalMp4(bytes):
    b = json.loads(bytes)
    return b["priorityList"][0]["formitaeten"][0]["qualities"][0]["audio"]["tracks"][0]["uri"]

def getCurrentHeuteJournalTitle(bytes):
    return str(re.compile("title\" content=\"(.+)\" />").findall(bytes.decode('utf-8'))[0])
    