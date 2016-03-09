import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from linkcrawl.items import *

class LinkSpider(scrapy.Spider):
	name = "linkedin"
	allowed_domains = ["linkedin.com"]
	start_urls = [
	# "https://in.linkedin.com/in/yashhrastogi",
	# "https://in.linkedin.com/in/sudhirsuguru",
	# "https://in.linkedin.com/in/liveashish",
	# "https://in.linkedin.com/in/narenkrishna",
	# "https://in.linkedin.com/pub/girish-sharma/5b/91/8a8",
	# "https://www.linkedin.com/pub/rajmohan-p/8b/501/466?trk=pub-pbmap",
	# "https://in.linkedin.com/in/gauravbarthwal",
	# "https://www.linkedin.com/pub/vikas-jagetiya/4/836/a5b?trk=pub-pbmap",
	# "https://in.linkedin.com/in/anoopmunshi",
	# "https://in.linkedin.com/pub/srinivas-reddy-kompally/33/984/483",
	# "https://ae.linkedin.com/pub/ashok-dhudla/58/113/96a",
	# "https://www.linkedin.com/pub/venugopal-voraganti/54/625/244",
	# "https://ae.linkedin.com/pub/ankit-singh-bhandari/20/160/531",
	"https://www.linkedin.com/in/kandoiabhi",

	]

	def parse(self, response):
		yield self.parse_contents(response)
		# yield self.parse_skills(response)

	def parse_contents(self, response):
		# items = []
		skills = []
		prev_company = []
		edu = {}
		proj= {}
		exp = {}
		cert = {}
		item = linkedItem()
		print response.xpath('//div[@class="profile-picture"]/a/img/@src').extract_first()
		item['imageurl'] = response.xpath('//div[@class="profile-picture"]/a/img/@src').extract_first()
		#Full Name
		print response.xpath('//span[@class="full-name"]/text()').extract_first()
		item['fullname'] = response.xpath('//span[@class="full-name"]/text()').extract_first()
		# Current Designation
		print response.xpath('//p[@class="title"]/text()').extract_first()
		item['current_designation'] = response.xpath('//p[@class="title"]/text()').extract_first()
		# Current Location
		print response.xpath('//span[@class="locality"]/text()').extract_first()
		item['current_location'] = response.xpath('//span[@class="locality"]/text()').extract_first()
		# Current Inustry
		print response.xpath('//dd[@class="industry"]/text()').extract_first()
		item['industry'] = response.xpath('//dd[@class="industry"]/text()').extract_first()
		# Total Connections
		print response.xpath('//div[@class="member-connections"]/strong/text()').extract_first()
		item['connections'] = response.xpath('//div[@class="member-connections"]/strong/text()').extract_first()
		# Summary
		print response.xpath('//p[@class="description"]/text()').extract_first()
		item['summary'] = response.xpath('//p[@class="description"]/text()').extract_first()
		# Skills
		for sel in response.xpath('//ul[@class="skills-section compact-view"]/li'):
			skills.append(sel.xpath('span/span/a/text()').extract_first())
			item['skills'] = skills
		# Previous Companies
		for sel in response.xpath('//tr[contains(@id, "overview-summary-past")]/td/ol/li/a'):
			print sel.xpath('text()').extract_first()
			prev_company.append(sel.xpath('text()').extract_first())
			item['prev_company'] = prev_company
		# Languages
		item['languages'] = response.xpath('//*[@id="background-languages"]/div/div/ol/li/h4/span/text()').extract()
		# Education
		college = []
		trade = []
		degree = []
		grade = []
		time = []
		college = response.xpath('//*[@id="background-education"]/div/div/div/header/h4/a/text()').extract()
		# print response.xpath('//*[@id="background-education"]/div/div/div/header/h4/a/text()').extract()
		college += response.xpath('//*[@id="background-education"]/div/div/div/header/h4/text()').extract()
		# print response.xpath('//*[@id="background-education"]/div/div/div/header/h4/a/text()').extract()
		degree = response.xpath('//*[@id="background-education"]/div/div/div/header/h5/span[@class="degree"]/text()').extract()
		# print response.xpath('//*[@id="background-education"]/div/div/div/header/h4/a/text()').extract()
		trade = response.xpath('//*[@id="background-education"]/div/div/div/header/h5/span/a/text()').extract() 
		# print response.xpath('//*[@id="background-education"]/div/div/div/header/h5/span/a/text()').extract()
		grade = response.xpath('//*[@id="background-education"]/div/div/div/header/h5/span[@class="grade"]/text()').extract()
		# print response.xpath('//*[@id="background-education"]/div/div/div/header/h5/span[@class="grade"]/text()').extract()
		time = response.xpath('//*[@id="background-education"]/div/div/div/span/time/text()').extract()
		edu['college'] = college
		edu['degree'] = degree
		edu['trade'] = trade
		edu['grade'] = grade
		edu['time'] = time
		item['education'] = edu
		# Projects
		project_title = []
		project_url = []
		project_duration = []
		project_summary = []
		project_title = response.xpath('//*[@id="background-projects"]/div/div/hgroup/h4/span/text()').extract()
		project_title += response.xpath('//*[@id="background-projects"]/div/div/hgroup/h4/a/span/text()').extract()
		project_title = set(project_title)
		project_title = list(project_title)
		print project_title
		project_duration = response.xpath('//*[@id="background-projects"]/div/div/span/time/text()').extract()
		print project_duration
		project_summary = response.xpath('//*[@id="background-projects"]/div/div/p/text()').extract()
		print project_summary
		project_url = response.xpath('//*[@id="background-projects"]/div/div/hgroup/h4/a/@href').extract()
		print project_url
		proj['project_title'] = project_title
		proj['project_url'] = project_url
		proj['project_duration'] = project_duration
		proj['project_summary'] = project_summary
		item['projects'] = proj
		# Experience
		position = []
		company = []
		comp_duration = []
		work_summary = []
		position = response.xpath('//*[@id="background-experience"]/div/div/header/h4/a/text()').extract()
		print position
		company = response.xpath('//*[@id="background-experience"]/div/div/header/h5/a/text()').extract()
		print company
		comp_duration = response.xpath('//*[@id="background-experience"]/div/div/span/text()').extract()
		print comp_duration
		work_summary = response.xpath('//*[@id="background-experience"]/div/div/p/text()').extract()
		print work_summary
		exp['position'] = position
		exp['company'] = company
		exp['work_summary'] = work_summary
		exp['comp_duration'] = comp_duration
		item['experience'] = exp
		# Certifications
		institute = []
		certificatename = []
		certificatename = response.xpath('//*[@id="background-certifications"]/div/div/hgroup/h4/a/text()').extract()
		print certificatename
		institute = response.xpath('//*[@id="background-certifications"]/div/div/hgroup/h5/a/text()').extract()
		print institute
		cert['institute'] = institute
		cert['certificatename'] = certificatename
		item['certifications'] = cert
		return item
