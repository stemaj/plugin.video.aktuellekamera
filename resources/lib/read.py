import io
import urllib3
import time
import xbmc
import xbmcgui

def load_file(fileSuffix):
    with io.open('tests/file.'+fileSuffix, 'rb') as fo:
        data = fo.read()
    return data

def load_url(url,apiRequest = False):
    if apiRequest:
      headers = {
        'Host': 'api.zdf.de',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        }
    else:
      headers = {
      'Host': 'www.zdf.de',
      'Connection': 'keep-alive',
      'Cache-Control': 'max-age=0',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 Chrome/83.0.4103.61 Safari/537.36',
      'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Referer': 'https://www.zdf.de/nachrichten/heute-journal',
      'Accept-Encoding':'gzip, deflate, br',
      'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
      'If-None-Match': 'W/"0de8675bb3e364a1bae818dbfa63461fe"'
      }

    http = urllib3.PoolManager(maxsize=10, headers=headers)
    r = http.request('GET', url)

    if apiRequest:
      xbmc.log("request status api " + str(r.status), xbmc.LOGFATAL)
    else:
      xbmc.log("request status " + str(r.status), xbmc.LOGFATAL)

    if (r.status == 200 or r.status == 304):
        return r.data
    else:
        xbmcgui.Dialog().notification("Http Request scheiterte", "Status " + str(r.status))
