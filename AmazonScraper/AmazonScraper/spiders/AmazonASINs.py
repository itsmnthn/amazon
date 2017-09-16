# -*- coding: utf-8 -*-
import scrapy
from AmazonScraper.items import AmazonScraperItem
import csv
import sys

# reload(sys)  
# sys.setdefaultencoding('utf8')

class AmazonasinsSpider(scrapy.Spider):
	name = 'AmazonASINs'
	allowed_domains = ['https://www.amazon.ca']
	
	def start_requests(self):
		url = self.url
		yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		asinignore = ''
		with open("ASINsToIgnore.csv", 'rbU') as csv_file:
			keywordsignore = csv.reader(csv_file)
			for keys in keywordsignore:
				asinignore = asinignore + ' '+ keys[0].decode('latin-1')

		item = AmazonScraperItem()
		# Extracting ASINs from the page
		asins = response.xpath(
			'.//li[@class="s-result-item  celwidget "]/@data-asin').extract()
		for asin in asins:
			if asin in asinignore:
				print 'ignoring....'
			else:
				item['ASINs'] = asin
				yield item

		# Requesting next page if there available
		next_page = response.xpath(
			'.//a[@class="pagnNext"]/@href').extract_first()
		if next_page is not None:
			next_page = 'https://www.amazon.ca' + next_page
			yield scrapy.Request(
				url=next_page,
				callback=self.parse,
				dont_filter=True)
