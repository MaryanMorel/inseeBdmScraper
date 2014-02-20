from scrapy.spider import Spider
from scrapy.selector import Selector

from inseeBdmScraper.items import InseeItem

class InseeSpider(Spider):
    name = "insee"
    allowed_domains = ["insee.fr"]

    def __init__(self, idBank=None, *args, **kwargs):
        super(InseeSpider, self).__init__(*args, **kwargs)
        self.idBank = str(idBank)
        self.start_urls = start_urls = ["http://www.bdm.insee.fr/bdm2/affichageSeries.action?idbank=%s" %idBank]

    def parse(self, response):
        sel= Selector(response)
        inseeItem = InseeItem()
        inseeItem['idBank'] = self.idBank
        inseeItem['series_info'] = sel.xpath('//thead//tr//th/text()').extract()[0].replace('\t', '').replace('\n','')
        inseeItem['month'] = sel.xpath('//tbody//tr//th/text()').re('[a-zA-Z]+')
        inseeItem['year'] = sel.xpath('//tbody//tr//th/text()').re('\d+')
        inseeItem['values'] = map(lambda x: x.replace(',', ''), sel.xpath('//tbody//tr//td').re('[0-9,.]+'))
        return inseeItem