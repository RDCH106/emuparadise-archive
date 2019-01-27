# -*- coding: utf-8 -*-

from requests import get


response = get('https://www.emuparadise.me/roms/get-download.php?gid=153422&test=true', headers={'Referer':'https://www.emuparadise.me'}, allow_redirects=False)
print(response)  #print(response.status_code)
print(response.url)
print(response.headers)
print(response.headers['Location'])
