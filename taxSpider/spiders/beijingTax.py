import requests
import scrapy
from bs4 import BeautifulSoup
from taxSpider.items import TaxspiderItem


hdrs = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
url = "http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_isAgg=0&_pageSize=20&_template=index"

class BeijingSpider(scrapy.Spider):
    name = 'beijingTax'
    allowed_domains = ['beijing.chinatax.gov.cn']
    # 北京市税务局基层动态
    start_urls = ['http://beijing.chinatax.gov.cn/bjswjwz/xwdt/jcdt/']

    # 爬取数据
    def parse(self, response):
        r = requests.get(url, headers=hdrs)
        soup = BeautifulSoup(r.content.decode('utf8', 'ignore'), 'html.parser')
        # 获取指定div
        div_list = soup.find('div', class_='xxgk_tzgg')
        # print(div_list)
        # 获取所有的li标签
        li_list = div_list.find_all('li')
        for item in li_list:
            k = item.find_all('a')[0]  # 获取a标签
            hre = url + k.get('href')[2:]  # 链接
            title = k.get('title')  # 标题
            postTime = item.find_all('span')[0].contents[0]  # 发布时间
            source = "北京市税务局"
            # 获取文章内容
            r = requests.get(hre, headers=hdrs)
            soup2 = BeautifulSoup(r.content.decode('utf8', 'ignore'), 'html.parser')
            div_list2 = soup2.find_all('div', class_='Custom_UnionStyle')
            content = ""
            if (len(div_list2) == 0):
                continue
            else:
                span_list = div_list2[0].find_all('span')
                for item in span_list:
                    content += item.contents[0]
            item = TaxspiderItem()
            item['title'] = title
            item['url'] = hre
            item['source'] = source
            item['postTime'] = postTime
            item['content'] = content
            yield item


