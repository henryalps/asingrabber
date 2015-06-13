import scrapy

class SearchGoodSpider(scrapy.Spider):
    name = "sgs"
    allowed_domains=["amazon.com"]
    start_urls = ['http://www.amazon.com/s/ref=sr_nr_p_6_0?fst=as%3Aoff&rh=n%3A3375251%2Cn%3A706814011%2Ck%3Aski+Goggle%2Cp_8%3A598255011%2Cp_6%3AATVPDKIKX0DER&keywords=ski+Goggle&ie=UTF8&qid=1434180441&rnid=331592011']

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
