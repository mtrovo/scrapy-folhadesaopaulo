# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Artigo(Item):
    nome=Field()
    url=Field()
    conteudo=Field()

    def __str__(self):
        return "Artigo [nome=%s; conteudo=%s]" % (self["nome"], self["conteudo"][:200])
