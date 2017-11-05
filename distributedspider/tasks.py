import requests
from bs4 import BeautifulSoup
from workers import app
@app.task
def crawl(url):
    print('正在抓取链接{}'.format(url))
    try:
        resp_text = requests.get(url, timeout=10).text
    except:
        print('超时间了！～')
        return
    soup = BeautifulSoup(resp_text, 'html.parser')
    return soup.find('h1').text
