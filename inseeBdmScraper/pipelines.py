# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
import pandas as pd

class CsvExportPipeline(object):
	""" A pipeline for exporting data to csv
		The two first lines of the csv contains informations about the data downloaded by the
		scraper. You may have to skip these lines when reading the file, e.g. with pandas.
	"""
	def __init__(self):
		self.files = {}

	# @classmethod
	# def from_crawler(cls, crawler):
	# 	pipeline = cls()
	# 	crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
	# 	crawler.signals.connect(pipeline.spider_closed, signals.spidegr_closed)
	# 	return pipeline

	# def spider_opened(self, spider):
	# 	file = open('insee_idBank_%s.csv' % spider.idBank, 'w+b')
	# 	self.files[spider] = file
	# 	self.exporter = CsvItemExporter(file, encoding='utf8', fields_to_export=['year', 'month', 'values'])
	# 	self.exporter.start_exporting()

	# def spider_closed(self, spider):
	# 	self.exporter.finish_exporting()
	# 	file = self.files.pop(spider)
	# 	file.close()

	# def process_item(self, item, spider):
	# 	self.exporter.export_item(item)
	# 	return item

	def process_item(self, item, spider):
		with open('scraped_data/insee_idBank_'+spider.idBank+'.csv', 'w') as f:
			f.write('idBank: '+item['idBank']+'\n')
			f.write('Informations: '+item['series_info']+'\n')
			f.write('Source: INSEE\n')
			# f.write('URL: '+spider.start_urls+'\n\n')
			data = pd.DataFrame({'year':item['year'], 'month':item['month'], spider.idBank:item['values']})
			data.to_csv(f, index=False, encoding='utf8')
		return item