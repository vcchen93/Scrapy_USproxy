# Scrapy_USproxy
This scrapy crawler get proxies from https://www.us-proxy.org/. They provide 200 free proxies and check/update them every 10 mins.

This works well with [scrapy-proxies](https://github.com/aivarsk/scrapy-proxies), which enable random proxies on Scrapy.

## Usage
At the path you place "USproxy" folder and "scrapy.cfg", run:
```
scrapy crawl proxy_US
```

## Output
Proxies.txt is an example of the output. you can change the file name and the output path by modifying pipeline.py
```
self.file = open('Proxies.txt', 'w')
```
