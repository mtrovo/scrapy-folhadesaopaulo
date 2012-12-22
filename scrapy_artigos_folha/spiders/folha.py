from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy_artigos_folha.items import Artigo

from w3lib.html import remove_comments, remove_tags

class FolhaSpider(CrawlSpider):
    name = 'folha'
    allowed_domains = ['folha.uol.com.br']
    start_urls = ['http://www.folha.uol.com.br/mercado']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'folha.uol.com.br/mercado/.*\.shtml'), callback='parse_item', follow=True),
        # Rule(SgmlLinkExtractor(allow=r'www\d?.folha.uol.com.br/.*/$'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'www\d?.folha.uol.com.br/mercado/$'), follow=True),
    )

    def parse_item(self, response):
        print '*******', response.url
        hxs = HtmlXPathSelector(response)
        titles=hxs.select("//div[@id='articleNew']/h1/text()").extract()

        if len(titles) == 0: return

        title=''.join(titles).strip()

        txts=hxs.select("//div[@id='articleNew']/p").extract()
        conteudo=remove_comments(remove_tags(''.join(txts)))

        i = Artigo()
        i['url']=response.url
        i['nome']=title
        i['conteudo']=conteudo
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        yield i
