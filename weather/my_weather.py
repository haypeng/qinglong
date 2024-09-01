import os.path
import requests
import json
import notify

url = 'http://t.weather.sojson.com/api/weather/city/'


def start(city_name: str):
    with open('city.json', 'rb') as f:
        cities = json.load(f)
        city_code = -1
        for city in cities:
            if city['city_name'] == city_name:
                city_code = city['city_code']
        if city_code == -1:
            return
        # 发送请求
        response = requests.get(url + city_code).json()
        if (response['status'] != 200):
            return
        return get_info(response)


def get_info(response):
    # print(response['data']['yesterday']['high'])
    # 获取data数据
    data = str('城市：')
    data += response['cityInfo']['city']
    data += '\n湿度：'
    data += response['data']['shidu']
    data += '\n温度'
    data += response['data']['wendu']
    data += '\n最高温度：'
    data += response['data']['forecast'][0]['high']
    data += '\n最低温度：'
    data += response['data']['forecast'][0]['low']
    data += '\n天气类型：'
    data += response['data']['forecast'][0]['type']
    data += '\n注意事项：'
    data += response['data']['forecast'][0]['notice']
    # print(data)
    return data


if __name__ == '__main__':
    if not os.path.exists('info.json'):
        exit()
    if not os.path.exists('city.json'):
        exit()
    with open('info.json', 'rb') as f:
        infos = json.load(f)
        weather_info = '以下是查询的所有天气信息：\n\n'
        for info in infos:
            # print(info['city_name'])
            weather_info += start(str(info['city_name']))
            weather_info += '\n\n'

        print(weather_info)
        # QLAPI.notify('今日天气预报', data)
