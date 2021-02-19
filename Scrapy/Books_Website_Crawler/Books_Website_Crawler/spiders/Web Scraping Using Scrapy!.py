#!/usr/bin/env python
import scrapy

class Web_Scraping_Spider(scrapy.Spider):
    name = "Books"
    start_urls = [
        "http://books.toscrape.com",
        "http://books.toscrape.com/catalogue/category/books/science_22/index.html",
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "books-%s.html" % page
        with open(filename, "wb") as f:
            f.write(response.body)
