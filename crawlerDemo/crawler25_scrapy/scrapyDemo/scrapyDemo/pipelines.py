# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 提交的item类型的对象最终会提交给优先级高的管道类
class ScrapydemoPipeline:
    fb = None
    # 重写父类方法,该方法只在开始爬虫时调用一次
    def open_spider(self, spider):
        print('开始。。。。')
        self.fb = open('./qiushi.txt', 'a', encoding='utf-8')

    # 专门用来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fb.write(f"author: {author}, content: {content}\n")
        # return会将item传递给即将要执行的管道类
        return item

    def close_spider(self, spider):
        print('结束。。。')
        self.fb.close()


# 可以定义多个管道类处理不同的数据,一个管道类对应将一组数据存储到一个平台或载体中
class TestPipeline(object):
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        print(f"author: {author}, content: {content}\n")
        return item

