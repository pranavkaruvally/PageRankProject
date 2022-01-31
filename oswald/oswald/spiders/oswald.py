import scrapy


class OswaldSpider(scrapy.Spider):
    name = 'oswald'
    count = -1
    start_urls = [
        # 'http://127.0.0.1:8000/health/h2',
        'http://127.0.0.1:8000/technology/t8',
        'http://127.0.0.1:8000/animals/a19',
        'http://127.0.0.1:8000/animals/a18',
        'http://127.0.0.1:8000/business/b20',
        # 'http://127.0.0.1:8000/movies/m26',
    ]
    collected_urls = list()
    prev_url = start_urls[0]

    def parse(self, response):
        next_page_url = ''
        for link in response.css('a'):
            next_page_url = link.attrib['href']
            if next_page_url not in self.collected_urls:
                self.count += 1
                self.collected_urls.append(next_page_url)
                yield {
                    # self.prev_url: next_page_url,
                    next_page_url: self.count
                }
        self.prev_url = next_page_url
        # yield response.follow(next_page_url, callback=self.parse)
        yield scrapy.Request(next_page_url)

# import scrapy


# class OswaldSpider(scrapy.Spider):
#     name = 'oswald'
#     allowed_domains = ['127.0.0.1:8000']
#     start_urls = ['http://127.0.0.1:8000/health/h1']
#     collected_urls = set()
#     count = -1

#     def parse(self, response):
#         for link in response.css('a::attr(href)'):
#             yield response.follow(link.get(), callback=self.parse_hyperlinks)

#     def parse_hyperlinks(self, response):
#         for link in response.css('a::attr(href)'):
#             self.count += 1
#             self.collected_urls.add(link.get())
#             if link.get() not in self.collected_urls:
#                 yield {
#                     link.get(): self.count,
#                 }
