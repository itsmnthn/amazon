# -*- coding: utf-8 -*-

from AmazonScraper.items import AmazonscraperItem
import scrapy
import csv
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

class AmazonScraperSpider(scrapy.Spider):
	name = "Amazon_Scraper"
	allowed_domains = ["https://www.amazon.com"]
	links = []

	try:
		# Getting ASINs from the given csv and put into the start_urls
		with open(sys.argv[5].split('csv=')[1], 'rbU') as csv_file:
			data = csv.reader(csv_file)
			for url in data:
				links.append("https://www.amazon.com/dp/B00IKDFL4O")
	except:
		pass

	start_urls = links

	def parse(self, response):
		item = AmazonscraperItem()
		keywordI = []
		pageTitle = response.xpath(".//title/text()").extract_first()
		try:
			if "Robot check" not in pageTitle:
				item['ASIN'] = response.xpath('.//*[@id="averageCustomerReviews"]/@data-asin').extract_first()
				item['Title'] = response.xpath('.//*[@id="productTitle"]/text()').extract_first().strip().lower()
				item['Category'] = response.xpath('//span[@class="a-list-item"]/a[@class="a-link-normal a-color-tertiary"]/text()').extract_first().strip()
				try:
					item['Price'] = response.xpath('.//*[@id="priceblock_ourprice"]/text()').extract_first().strip()
				except:
					try:
						item['Price'] = response.xpath('.//span[@class="a-color-price"]/span[@class="p13n-sc-price"]/text()').extract_first().strip()
					except:
						item['Price'] = ''
				try:
					Weight = response.xpath('.//*[contains(text(), "Shipping Weight")]/following-sibling::td/text()').extract_first()
					item['Weight'] = Weight.replace("(","").strip()
				except:
					item['Weight'] = ''
				try:
					ShipBy = response.xpath('.//div[@id="merchant-info"]').extract_first().replace("\n","").strip()
					print ".................."+ShipBy+".................."
					ShipBy = ShipBy.split(">")
					print ShipBy
					sby = ''
					for i in ShipBy:
						sby = sby + ' ' +i.split("<")[0]
					print sby
					item['ShipBy'] = sby.split(".")[0].strip()
					print item['ShipBy']
				except Exception as e:
					print e
				try:
					item['Brand'] = response.xpath('.//*[contains(text(), "Brand Name")]/following-sibling::td/text()').extract_first().strip().lower()
				except:
					try:
						item['Brand'] = response.xpath('.//a[@id="bylineInfo"]/text()').extract_first().lower()
					except:
						try:
							item['Brand'] = response.xpath('.//a[@id="brand"]/@href').extract_first().split("=")[-1]
						except Exception as e:
							print e
				try:
					item['Stock'] = response.xpath(
						'.//*[@id="availability"]/*[@class="a-size-medium a-color-success" or @class="a-size-medium a-color-state" or @class="a-size-medium a-color-price"]/text()').extract_first().strip()
				except:
					try:
						item['Stock'] = response.xpath('.//*[@id="availability"]/text()').extract_first().strip()
					except Exception as e:
						print e
				# Check if title or brand have keywords that we want to ignore
				with open("KeywordsToIgnore.csv", 'rbU') as csv_file:
					keywordsignore = csv.reader(csv_file)
					for keys in keywordsignore:
						keys = keys[0].decode('latin-1').lower()
						if keys in item['Title'] or keys in item['Brand']:
							raise Exception('Skipping because keyword filter of title or brand lokking for next')
			else:
				# rerequest if amazon gives robot check page
				yield scrapy.Request(
					url=response.url,
					callback=self.parse,
					dont_filter=True)

			# dump Data to csv file if shipby have amazon
			if 'Amazon' in item['ShipBy']:
				yield item
			else:
				print "Ship By - Doesn't Include Amazon  - "+item['ASIN']
				print item['ShipBy']
		except Exception as e:
			print e
			print item['ASIN']
