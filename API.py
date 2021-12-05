from itertools import groupby
from urllib.request import urlopen
from json import loads
import datetime


def get_datetime(commit_info):
    time = commit_info['timestamp']
    return datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ').date()


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
page = "192203"

data = loads(urlopen(url).read().decode('utf8'))
page_info = data['query']['pages'][page]['revisions']

for key, group_items in groupby(page_info, key=get_datetime):
    print(key, sum(1 for _ in group_items))
