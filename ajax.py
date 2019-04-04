from urllib.request import quote, unquote
import random
import requests

keyword = quote('Python').strip()

city = quote('杭州').strip()

s = requests.session()

s.get('https://www.lagou.com/', headers={'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})

refer_url = 'https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=' % (keyword, city)

ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false' % city

user_agents = [
    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
]

data = {
    'first': 'true',
    'pn': '1',
    'kd': keyword,
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': refer_url,
    'User-Agent': random.choice(user_agents),
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}
resp = s.post(ajax_url, data=data, headers=headers)

result = resp.json()
print(result)

if result:
    item = result['content']['positionResult']['result'][0]
    print(item)
# item就是单个招聘条目信息
print("程序结束")