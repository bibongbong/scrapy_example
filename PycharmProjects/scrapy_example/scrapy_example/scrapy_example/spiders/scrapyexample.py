import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy_example.items import ScrapyExampleItem

class Myspider(scrapy.Spider):

    name = 'scrapy_example'
    allowed_domains = ['ting55.com']
    bash_url = 'https://ting55.com/category/'

    def start_requests(self):

        #循环分析每个子题材页面
        #for i in range(1, 3):
        #    url = self.bash_url+str(i)
        #    yield Request(url, self.parse)

        url = self.bash_url + str(1)
        yield Request(url, self.parse)


    #分析当前子题材页面
    def parse(self, response):

        #提取页面底端“末页”元素
        last_page_url = BeautifulSoup(response.text, "html.parser").find('div', class_='left').find_all('a')[-1]['href']
        last_page_index = last_page_url.rindex('/')
        last_page_num = int(last_page_url[last_page_index + 1:])
        #print("last_page_url %s, last_page_num %d" % (last_page_url, last_page_num))


        # 提取页面底端“下一页”元素
        next_page_url = BeautifulSoup(response.text, "html.parser").find('div', class_='left').find_all('a')[-2]['href']
        next_page_index = next_page_url.rindex('/')
        next_page_num = int(next_page_url[next_page_index + 1:])
        #print("next_page_url %s, next_page_num %d" % (next_page_url, next_page_num))



        #抓取网页各个项目的内容
        #1. 找到所有所有小说对应的div
        allNovelDiv = BeautifulSoup(response.text, "html.parser").find_all('div', class_='info')


        #2. 对每个小说的
        for novelDiv in allNovelDiv:
            yield self.getNovleInfo(novelDiv)

        #3. 当前子类题材/当前页 找完，继续抓取 当前子类题材/下一页
        if(next_page_num <= 10):
            yield Request(next_page_url, self.parse)

    def getNovleInfo(self, novelDiv):
        novel = ScrapyExampleItem()
        novel['novelname'] = novelDiv.a['title']
        novel['novelurl'] = novelDiv.a['href']
        novel['author'] = novelDiv.find_all('p')[1].string
        #print("%s " % novel['novelname']),
        #print("     %s " % novel['novelurl']),
        #print("     %s " % novel['author']),
        #print("")
        return novel




