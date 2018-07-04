import requests,json, urllib
from sendmail import send_mail
# 雅虎天气的code对应的天气描述
'''
Code	Description
0	tornado
1	tropical storm
2	hurricane
3	severe thunderstorms
4	thunderstorms
5	mixed rain and snow
6	mixed rain and sleet
7	mixed snow and sleet
8	freezing drizzle
9	drizzle
10	freezing rain
11	showers
12	showers
13	snow flurries
14	light snow showers
15	blowing snow
16	snow
17	hail
18	sleet
19	dust
20	foggy
21	haze
22	smoky
23	blustery
24	windy
25	cold
26	cloudy
27	mostly cloudy (night)
28	mostly cloudy (day)
29	partly cloudy (night)
30	partly cloudy (day)
31	clear (night)
32	sunny
33	fair (night)
34	fair (day)
35	mixed rain and hail
36	hot
37	isolated thunderstorms
38	scattered thunderstorms
39	scattered thunderstorms
40	scattered showers
41	heavy snow
42	scattered snow showers
43	heavy snow
44	partly cloudy
45	thundershowers
46	snow showers
47	isolated thundershowers
3200	not availables
'''

weather_dict = {0: '飓风', 1: '热带风暴', 2: '飓风', 3: '雷暴', 4: '雷电', }


def get_weather_url(url):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.text
    return None

def today_temp():
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select item.condition from weather.forecast where woeid=2345868"
    yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    result = get_weather_url(yql_url)
    data = json.loads(result)
    print((int(data['query']['results']['channel']['item']['condition']['temp']) - 32) / 1.8)
    temp = (int(data['query']['results']['channel']['item']['condition']['temp']) - 32) / 1.8
    return temp

def one_word_condition():
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select item.condition.code from weather.forecast where woeid=2345868"
    yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    result = get_weather_url(yql_url)
    data = json.loads(result)
    weather_code = data['query']['results']['channel']['item']['condition']['code']
    return weather_code
def tomorrow_weather():
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select item from weather.forecast where woeid=2345868"
    yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    result = get_weather_url(yql_url)
    data = json.loads(result)
    weather_code1 = data['query']['results']['channel']['item']['forecast'][0]['code']
    weather_text1 = data['query']['results']['channel']['item']['forecast'][0]['text']
    return weather_code1, weather_text1
# tomorrow_weather()
today_code = one_word_condition()
to_list = ['收件箱']
send_mail(to_list, '先测试一下今天的天气哈', '天气：'+ ' '+today_code)

