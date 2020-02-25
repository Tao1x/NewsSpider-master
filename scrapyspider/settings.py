# -*- coding: utf-8 -*-

# Scrapy settings for scrapyspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import sys
# 这里改成爬虫项目的绝对路径，防止出现路径搜索的bug
# sys.path.append('/home/lis/Desktop/测试用/NewsSpider-master\scrapyspider')

BOT_NAME = 'scrapyspider'

SPIDER_MODULES = ['scrapyspider.spiders']
NEWSPIDER_MODULE = 'scrapyspider.spiders'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 设置是否服从网站的爬虫规则
ROBOTSTXT_OBEY = False
REDIRECT_ENABLED = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 同时并发请求数，越大则爬取越快同时负载也大
CONCURRENT_REQUESTS = 10
DOWNLOAD_DELAY = 0.5
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#禁止cookies,防止被ban
COOKIES_ENABLED = False
REDIRECT_ENABLED = False                       # 关掉重定向, 不会重定向到新的地址
# HTTPERROR_ALLOWED_CODES = [200]     # 返回301, 302时, 按正常返回对待, 可以正常写入cookie
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapyspider.middlewares.ScrapyspiderSpiderMiddleware': 543,
#}
# LOCAL_MONGO_HOST = '192.168.1.127'
LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'pengpai_test'
LOCAL_MONGO_HOST1 = '192.168.1.127'
LOCAL_MONGO_PORT1 = 27017
DB_NAME1 = 'pengpai_test'
local_mongo_host = '127.0.0.1'
local_mongo_port = 27017
DB_NAME2 = 'pengpai_test'

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scrapyspider.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapyspider.middlewares.ProxyDownloadMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {

    'scrapyspider.pipelines.MongoDBPipeline': 300,
    'scrapyspider.pipelines.MongoDBPipeline1': 301,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapyspider.pipelines.ScrapyspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 输出的编码格式，由于Excel默认是ANSI编码，所以这里保持一致
# 如果有其他编码需求如utf-8等可自行更改
# FEED_EXPORT_ENCODING = 'ANSI'

# 增加爬取延迟，降低被爬网站服务器压力
# DOWNLOAD_DELAY = 0.1

# # 爬取的新闻条数上限
# CLOSESPIDER_ITEMCOUNT = 500
# # 下载超时设定，超过10秒没响应则放弃当前URL
# DOWNLOAD_TIMEOUT = 100
# ITEM_PIPELINES = {'scrapyspider.pipelines.ScrapyspiderPipeline': 300,# pipeline中的类名 }

