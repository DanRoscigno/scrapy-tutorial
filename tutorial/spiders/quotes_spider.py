from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

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
        page = response.url.split("/")[-2]
        #filename = f"quotes-{page}.html"
        #Path(filename).write_bytes(response.body)
        self.log(f"checked URL {page}")

