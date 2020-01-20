# -*- coding: utf-8 -*-
from datetime import time

import requests
import scrapy
from bs4 import BeautifulSoup

from taxSpider.items import TaxspiderItem


# hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
hdrs = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
}
url = "http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_isAgg=0&_pageSize=20&_template=index"


class ChinaTaxSpider(scrapy.Spider):
    name = 'chinaTax'
    allowed_domains = ['chinatax.gov.cn']
    start_urls = ['http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_isAgg=0&_pageSize=20&_template=index']

    # 爬取数据
    def parse(self, response):
        r = requests.get(url, headers=hdrs)
        soup = BeautifulSoup(r.content.decode('utf8', 'ignore'), 'html.parser')
        # 获取指定class下的ul
        ul_list = soup.find('ul', class_='list')
        print(ul_list)
        # 获取所有的a标签
        href_list = ul_list.find_all('a')
        # 获取所有span标签
        span_list = ul_list.find_all('span')

        count = 0
        for each in ul_list:
            hre = href_list[count]['href']  # 链接
            source = span_list[count].contents[0]  # 来源
            title = href_list[count].contents[0]  # 标题
            count = count + 1
            print(title + "    " + source)
            print(count)
            print("--------------------------------------------------------------------------")
            # 获取content，postTime
            r = requests.get(hre, headers=hdrs)
            soup2 = BeautifulSoup(r.content.decode('utf8', 'ignore'), 'html.parser')
            div_list = soup2.find_all('div', class_='text')
            content = ""
            postTime = ""
            if (len(div_list) >= 1):
                contentAll = div_list[1]  # fontzoom 文章正文内容<p>
                p_list = contentAll.find_all('p')
                length = len(p_list)
                cnt = 0
                for i in p_list:
                    c = i.text.strip()
                    if (cnt == (length - 2)):
                        postTime = c
                    if (cnt == (length - 1)):
                        break
                    content = content + c #拼接内容
                    cnt += 1
            item = TaxspiderItem()
            item['title'] = title
            item['url'] = hre
            item['source'] = source
            item['postTime'] = postTime
            item['content'] = content
            yield item


