# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
import pandas as pd
import os

class CsvExportPipeline(object):
	""" A pipeline for exporting data to csv
		The two first lines of the csv contains informations about the data downloaded by the
		scraper. You may have to skip these lines when reading the file, e.g. with pandas.
	"""
	def __init__(self):
		self.files = {}

	@classmethod
	def from_crawler(cls, crawler):
		os.chdir(crawler.settings['OUTPUT_PATH'])
		pipeline = cls()
		return pipeline

	def process_item(self, item, spider):
		with open('insee_idBank_'+spider.idBank+'.csv', 'w') as f:
			f.write('idBank: '+item['idBank']+'\n')
			f.write('Informations: '+item['series_info']+'\n')
			f.write('Source: INSEE\n')
			# f.write('URL: '+spider.start_urls+'\n\n')
			data = pd.DataFrame({'year':item['year'], 'month':item['month'], spider.idBank:item['values']})
			data.to_csv(f, index=False, encoding='utf8')
		return item