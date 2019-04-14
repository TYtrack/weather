# -*- coding: utf-8 -*-

import urllib.request

import json
import gzip

#cityname = input('你想查询的城市?\n')
citys=[["常德","武汉","岳阳","长沙","娄底"],["常德","深圳","梅州","广州","怀化","宁波","武汉"],["株洲","长沙","南京","廊坊","武汉"],["宜昌","武汉"]]
choose=int(input("请输入选择城市群类型"))
first=0
for cityname in citys[choose]:
    #访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityname)
    #发出请求并读取到weather_data
    weather_data = urllib.request.urlopen(url).read()
    #以utf-8的编码方式解压数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #将json数据转化为dict数据
    weather_dict = json.loads(weather_data)
    
    if weather_dict.get('desc') == 'invilad-citykey':
        print("输入的城市名有误")
    elif weather_dict.get('desc') =='OK' :
        forecast = weather_dict.get('data').get('forecast')
        if first==0:
            print ('明日天气预报：'+forecast[1].get('date')+'\n')
        first+=1
        one_day    ='城市：'+weather_dict.get('data').get('city') +'      ' \
                   +'天气：'+forecast[1].get('type')+'      '\
                   +'温度：'+forecast[1].get('low')[3:]+'至'+forecast[1].get('high')[3:]+'\n' \
                   +'感冒：'+weather_dict.get('data').get('ganmao') + '\n'
                    # +'风向：'+forecast[1].get('fengxiang')+'\n'\
        print(one_day)
