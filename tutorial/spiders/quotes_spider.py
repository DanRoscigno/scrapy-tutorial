from pathlib import Path
from scrapy.item import Item, Field

import scrapy

class MyItems(Item):
    referer = Field()  # where the link is extracted
    response = Field()  # url that was requested
    status = Field()  # status code received

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    handle_httpstatus_list = [301,302,400,404,500]
    handle_httpstatus_all = True

    def start_requests(self):
        with open('doc_urls.txt') as f:
            urls = [url.strip() for url in f.readlines()]
        #urls = [
            #"https://quotes.toscrape.com/page/1/",
            #"https://quotes.toscrape.com/page/2/",
        #]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        report_if = [301,302,400,404,500]
        #page = response.url.split("/")[-2]
        #filename = f"quotes-{page}.html"
        #Path(filename).write_bytes(response.body)
        #self.log(f"checked URL {page}")
        if response.status in report_if:  # if the response matches then creates a MyItem
            item = MyItems()
            item["referer"] = response.request.headers.get("Referer", None)
            item["status"] = response.status
            item["response"] = response.url
            yield item
        yield None  # return empty if response didn't match a code in `report_if`

