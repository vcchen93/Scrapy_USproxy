# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
class ProxyPipeline:

    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)    
        Proxy = ''
        Proxy += (adapter['proxy'] + "\n")
        self.file.write(Proxy)

    def open_spider(self, spider):
        self.file = open('Proxies.txt', 'w')
    
    def close_spider(self, spider):
        self.file.close()
