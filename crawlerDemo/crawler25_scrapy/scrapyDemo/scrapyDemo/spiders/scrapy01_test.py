import scrapy

from ..items import ScrapydemoItem

"""
安装scrapy
1. 安装 twisted
下载地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
选择对应python版本下载 如：
下载后通过pip install 文件路径
2. 安装scrapy
pip install scrapy

使用scrapy
1. 创建scrapy工程 
scrapy startproject 工程名
2. spiders子目录中创建一个爬虫文件 
2.1 cd 工程目录下
2.2 scrapy genspider 爬虫文件名 www.xxx.com
3. 执行工程命令
scrapy crawl 爬虫文件名(scrapy01_test)
scrapy crawl scrapy01_test --nolog   不显示任何log
修改配置文件settings.py，LOG_LEVEL = 'ERROR' 只显示error等级的log

数据解析
parse()方法用来解析数据

持久化存储
1. 基于终端指令：
    只可以将parse方法的返回值存储到本地的文件中
    存储的文本文件类型只能是：json，jsonlines, jl, csv, xml, marshal, pickle
    指令：scrapy crawl xxx -o filePath
2. 基于管道
    在item类（item.py文件中）中定义相关属性
    将解析的数据封装存储到item类型的对象中
    将item类型的对象提交给管道进行持久化存储的操作
    在管道类(pipelines.py)的process_item()方法中要将其接收到的item对象中存储的数据进行持久化存储操作
    在配置文件中默认开启管道,settings.py中的ITEM_PIPELINES部分
    执行：scrapy crawl xxx
item只会传递给第一个执行的管道类，然后由管道类的return item传递给下一个要执行的管道类
"""


class Scrapy01TestSpider(scrapy.Spider):
    # 爬虫文件的名称，爬虫源文件的一个唯一标识
    name = 'scrapy01_test'
    # 允许的域名, 用来限定start_urls列表中哪些url可以进行请求发送
    allowed_domains = ['www.qiushibaike.com']
    # 起始的url列表,该列表中的url会自动被scrapy请求
    # start_urls = ['https://www.baidu.com/', 'http://www.people.com.cn/']
    start_urls = ['https://www.qiushibaike.com/text/']

    """ 终端持久化存储 """
    # 数据解析，response表示请求成功后的响应对象，每一次请求调用parse一次
    # def parse(self, response):
    #     items = []
    #     # 解析作者名称和段子内容
    #     div_list = response.xpath('//div[@class="article block untagged mb15 typs_hot"]')
    #     for div in div_list:
    #         # author = div.xpath('./div[@class="author clearfix"]//h2/text()')[0].extract()
    #         # 列表中第一个元素extract
    #         author = div.xpath('./div[@class="author clearfix"]//h2/text()').extract_first()
    #         author = author.replace('\n', '')
    #         # print(author)
    #         # 内容中有br标签，所以将span中text全部保存
    #         contents = div.xpath('.//div[@class="content"]/span/text()').extract()
    #         content = ''.join(contents).replace('查看全文', '').replace('\n', '')
    #         # print(content)
    #         item = {
    #             'author': author,
    #             'content': content
    #         }
    #         items.append(item)
    #     print(items)
    #
    #     # 终端持久化存储，必须有返回值
    #     return items


    """ 管道持久化存储 """
    def parse(self, response):
        div_list = response.xpath('//div[@class="article block untagged mb15 typs_hot"]')
        for div in div_list:
            author = div.xpath('./div[@class="author clearfix"]//h2/text()').extract_first()
            author = author.replace('\n', '')
            contents = div.xpath('.//div[@class="content"]/span/text()').extract()
            content = ''.join(contents).replace('查看全文', '').replace('\n', '')

            item = ScrapydemoItem()
            item['author'] = author
            item['content'] = content

            # 将item提交给管道
            yield item


