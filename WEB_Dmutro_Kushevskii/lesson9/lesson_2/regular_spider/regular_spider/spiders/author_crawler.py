import scrapy.spiders
import scrapy.linkextractors

from regular_spider.items import RegularSpiderItem

class AuthorsCrawler(scrapy.spiders.CrawlSpider):
    name = "author_crawler"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    rules = (
        scrapy.spiders.Rule(
            scrapy.linkextractors.LinkExtractor(
                allow=("page"), deny=("tag")
            ),
            callback='parse_authors',
            follow=True
        ),
    )

    def parse_authors(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            item = RegularSpiderItem(
                author=quote.xpath("span/small/text()").extract()[0],
                quote=quote.xpath("span[@class='text']/text()").get()
            )

            yield item
