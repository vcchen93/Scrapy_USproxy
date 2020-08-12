#引用item.py裡面的項目，需以scrapy crawl 爬蟲名 -o 輸出.json/csv
from USproxy.items import USproxyItem
import scrapy

#這個class名不太重要，括弧裡的是設定使用哪一種scrapy爬蟲格式
class USproxySpider(scrapy.Spider):
    #設定爬蟲名，初始url、要爬的域名
    name = 'proxy_US'
    
    #設定要get的頁面資訊(可以設定header那些)，會得到response(頁面資訊)。callback是設定頁面資訊的後續處理方式。
    #也可以直接再class裡面設定，跳過這段start_requests，
    def start_requests(self):
        urls = ['https://www.us-proxy.org/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #response的處理方式
    def parse(self, response):
        #載入我們設定好要輸出的項目
        item = USproxyItem()

        #以我們熟悉的迴圈解析頁面資訊，這邊選用xpath而非之前用的css。也可以用css處理再丟bs4分析。
        for i, info in enumerate(response.xpath('//tbody/tr')):
            
            ip = info.xpath('//td[1]/text()').getall()
            port = info.xpath('//td[2]/text()').getall()
            https = info.xpath('//td[7]/text()').getall()
            
            if https[i] == 'no':
                item['proxy'] = ('http://'+ip[i]+':'+port[i])
            elif https[i] == 'yes':
                item['proxy'] = ('https://'+ip[i]+':'+port[i])
            else:
                pass
            #回傳我們的item值，值會被輸出成為檔案內容。

            
            yield item
