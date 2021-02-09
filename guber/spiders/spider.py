import scrapy

from scrapy.loader import ItemLoader
from ..items import GuberItem
from itemloaders.processors import TakeFirst


class GuberSpider(scrapy.Spider):
	name = 'guber'
	start_urls = ['https://www.guber.it/news/']

	def parse(self, response):
		post_links = response.xpath('//article')
		for post_link in post_links:
			date = post_link.xpath('.//span[@class="news-date"]/text()').get()
			link = post_link.xpath('.//a[@class="news-link"]/@href').get()
			yield response.follow(link, self.parse_post, cb_kwargs=dict(date=date))

	def parse_post(self, response, date):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="entry-content container px-5"]/p/text()').getall()

		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=GuberItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
