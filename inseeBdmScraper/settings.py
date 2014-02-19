# Scrapy settings for inseeBdmScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'inseeBdmScraper'

SPIDER_MODULES = ['inseeBdmScraper.spiders']
NEWSPIDER_MODULE = 'inseeBdmScraper.spiders'
ITEM_PIPELINES = {'inseeBdmScraper.pipelines.CsvExportPipeline':100}
# FEED_FORMAT = 'csv'
LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'inseeBdmScraper (+http://www.yourdomain.com)'
