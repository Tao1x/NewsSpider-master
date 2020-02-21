# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from lxml import etree
from scrapy.http import Request
from scrapy import cmdline, selector
from scrapyspider.items import newsItem,commentItem
import re
from scrapyspider.spiders.tools import tools_spider
spider_tools = tools_spider()
import time
news_item=newsItem()
class NewspengpaiSpider(CrawlSpider):
    # 爬虫名称
    name = "pengpainews"
    #澎湃全网
    allowed_domains = ["https://www.thepaper.cn/" ]
    #新闻版
    def start_requests(self):
        # start_urls1 = ['channels']
        # for url in start_urls1:
        #     yield Request(url=url,callback=self.)
        start_urls2 = [
            # 时事栏目
            # 'channel_25950',
            #中南海
            'list_25488',
            # 中国政库
            'list_25462',
            # 舆论场
            'list_25489',
            # 打虎记
            'list_25490',
            # 人事风向
            'list_25423',
            # 法治中国
            'list_25426',
            # 一号专案
            'list_25424',
            # 港台来信
            'list_25463',
            # 长三角政商
            'list_25491',
            # 直击现场
            'list_25428',
            # 公益湃
            'list_68750',
            # 暖闻
            'list_27604',
            # 澎湃质量报告
            'list_25464',
            # 绿政公署
            'list_25425',
            # 澎湃国际
            'list_25429',
            # 外交学人
            'list_25481',
            # 澎湃防务
            'list_25430',
            # 唐人街
            'list_25678',
            # 澎湃人物
            'list_25427',
            # 浦江头条
            'list_25422',
            # 教育家
            'list_25487',
            # 全景现场
            'list_25634',
            # 美数课
            'list_25635',
            # 快看
            'list_25600'
        ]
        for list_id in start_urls2:
            # print(url)
            for i in range(2,3):
                time.sleep(2)
                # print(url.split("list_")[1])
                id_lanmu = list_id.split("list_")[1]
                if id_lanmu:
                    url = 'https://www.thepaper.cn/load_index.jsp?nodeids=' + id_lanmu +"&topCids=&pageidx="+str(i)+"&isList=true"
                    if url == 'https://www.thepaper.cn/channel_25950':
                        yield Request(url=url,callback=self.parse_lanmu, dont_filter=True)
                    else:
                        yield Request(url=url,callback=self.parse_detail,dont_filter=True)
    def parse_detail(self,response):
        xpath_shishi = '//div[@class="news_li"]/h2/a/@href'
        url_news = response.xpath(xpath_shishi).extract()
        for url in url_news:
            url_news1 = "http://www.thepaper.cn/" + url
            # 新闻链接
            news_item['strPickUrl'] = url_news1
            yield Request(url=url_news1,callback=self.parse_content,dont_filter=True)
    def parse_lanmu(self, response):

        resp = response
        tree = etree.HTML(resp.body)
        path_link = '//*[@id="listContent"]/div/h2/a/@href'
        url_news = tree.xpath(path_link)
        for url in url_news:
            url_news1 = "http://www.thepaper.cn/" + url
            news_item['strPickUrl'] = url_news1
            yield Request(url=url_news1,callback=self.parse_content,dont_filter=True)
    def parse_content(self,response):

        # news_item['strTitle']
        #带div的数据
        xpath_allpage = '//div[@class="newscontent"]'
        html_page = response.xpath(xpath_allpage).extract()[0]
        # news_item['html_page'] = html_page
        #作者
        xpath_author = '//div[@class="clearfix"]'
        # 发布时间
        xpath_pubdate = '//div[@class="news_about"]/p[2]'
        news_item['strPubDate'] = spider_tools.str_tool_html(response.xpath(xpath_pubdate).extract()[0].split("来")[0])

        # 文章标题
        xpath_title = '//div[@class="newscontent"]/h1'
        title_html = response.xpath(xpath_title).extract()[0]
        title_result1 = spider_tools.str_tool_html(title_html)
        news_item['strTitle'] = title_result1
        # 文章正文
        xpath_detail4 = '//div[@class="news_txt"]'
        xpath_content = xpath_detail4
        content_selector = spider_tools.str_tool_html(response.xpath(xpath_content).extract()[0])
        news_item['strComment'] = content_selector

        #文章来源
        xpath_source = '//div[@class="news_about"]/p[1]'
        try:
            content_source = response.xpath(xpath_source).extract()[0]
            if content_source:
                content_source =spider_tools.str_tool_html(content_source)
                news_item['content_source'] = content_source
                # print(news_item['content_source'])
        except Exception as e:
            pass
        # 采集时间戳
        news_item['strPickDate'] = time.asctime(time.localtime(time.time()))
        # 新闻分类
        news_item['strType'] = ''
        # 来源网站，例如新浪微博，
        news_item['strName']='澎湃新闻'
        # 部委名称
        news_item['strDepartment'] = ''
        # 是否有评论，默认1
        xpath_strHasComment = '//*[@id="comm_span"]/span'
        commentnum = response.xpath(xpath_strHasComment).extract()[0]
        print(commentnum)
        commentnum = int(str(commentnum).split("（")[1].split("）")[0])
        print(commentnum)
        if commentnum > 0:
            news_item['strHasComment'] = '1'
        # 地区代码，默认000000
        news_item['strCityCode'] = '000000'
        # 地区，默认中国
        news_item['strArea'] = '中国'
        # 新闻分类的5大类
        news_item['strClass'] = ''
        # targetid
        news_item['strId'] = "5da57ac5efe0b4fd03fe9c20"
        news_item['strTargetId'] = ''
        # templateurl, 不存在默认为空
        news_item['strCommentTemplateUrl'] = ''
        # 新闻评论
        news_item['strComment'] = ''
        # 阅读数
        news_item['intReadNum'] = ''
        # 状态
        news_item['strState'] = '1'
        # 转发数
        news_item['intTranspondNum'] = ''
        # 点赞数
        news_item['intUpNum'] = ''
        # 评论数
        news_item['intCommentNum'] = commentnum






if __name__ == "__main__":
    cmdline.execute('scrapy crawl pengpainews'.split())




    


