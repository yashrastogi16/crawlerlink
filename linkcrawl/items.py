# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class LinkcrawlItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class linkedItem(scrapy.Item):
	imageurl = scrapy.Field()
	fullname = scrapy.Field()
	current_designation = scrapy.Field()
	current_location =  scrapy.Field()
	industry = scrapy.Field()
	connections = scrapy.Field()
	summary = scrapy.Field()
	skills = scrapy.Field()
	prev_company = scrapy.Field()
	languages = scrapy.Field()
	education = scrapy.Field()
	projects = scrapy.Field()
	experience = scrapy.Field()
	certifications = scrapy.Field()
