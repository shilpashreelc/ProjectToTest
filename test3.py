import requests
import json
import urlparse
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=1))

with open('proxies.txt') as proxies:
    for line in proxies:
        proxy=json.loads(line)

    with open('urls.txt') as urls:
        for line in urls:

            url=line.rstrip()
            data=requests.get(url, proxies=proxy)
            data1=data.content
            print data1
            print {'http': line}
