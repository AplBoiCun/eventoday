import urllib
from urllib import request,parse
import json

url = 'https://events.clock-up.jp/api/events?'

param = {
    #'area':'1',  #北海道
    'date': '20180525',       #イベント年月日
        'limit': '10',        #表示件数
}

paramStr = urllib.parse.urlencode(param)
#print(paramStr)

readObj = urllib.request.urlopen(url + paramStr)

res = readObj.read().decode()

data =json.loads(res)
#print(data)
event_info=data['events']
#print(type(event_info))
#print(event_info)
#print(event_info['title'])
for k in range(0,len(event_info)):
    print(event_info[k]['title'])   #イベント名
    print(event_info[k]['starts_at'])  #イベント開始日
    print(str(event_info[k]['lat']) + " " + str(event_info[k]['lng']))       #イベント場所
    #print(event_info[k]['categories'])  #イベントカテゴリー
    print()