import random
import time

from urllib import request
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup

PAGE = 1

head_list = [
    {'User-Agent': 'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23'},
    {'User-Agent': 'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)'},
    {'User-Agent': 'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)'},
    {'User-Agent': 'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)'},
    {'User-Agent': 'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)'},
    {'User-Agent': 'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0'},
    {'User-Agent': 'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)'},
    {'User-Agent': 'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'},
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'},
    {'User-Agent': 'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'}
]

driver = WebDriver()

def parser(page = 1):

    req = request.Request('https://hangzhou.anjuke.com/tycoon/p%s/' % str(page), headers=random.choice(head_list))

    response = request.urlopen(req)

    soup = BeautifulSoup(response.read(), 'html.parser')

    time.sleep(2)

    is_last = soup.find(class_='aNxt')

    lists = soup.find_all(class_="jjr-itemmod")

    for list in lists:
        a = list.find_all('a')

        href = a[0].get('href')

        driver.get(href)

        time.sleep(1)

        phone = driver.find_element_by_id('broker-nav-phone')

        phone.click()

        time.sleep(0.5)

        number = driver.find_element_by_xpath('//*[@id="broker-nav-phone"]/span').text.replace(' ', '')

        name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/a').text.split('的')[0]

        with open('item', 'a', encoding='utf-8') as f:
            f.write(name)
            f.write(":")
            f.write(number)
            f.write('\n')




    if is_last:
        page = page + 1

        parser(page)

        time.sleep(10)
    else:
        driver.close()


if __name__ =="__main__":
    parser()

