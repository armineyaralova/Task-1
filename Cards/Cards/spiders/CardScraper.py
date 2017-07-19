# -*- coding: utf-8 -*-
import scrapy

class CardSpider(scrapy.Spider):
    name = "Cards"
    allowed_domains = ["giftcardmall.am"]
    start_urls = ["https://www.giftcardmall.am/en/?page=1"]

           def parse(self, response):
    for cards in response.css('div.card-copy'):
        if len(cards.css('div.card-copy p::text').re('[0-9]+'))==2:
            yield {
                "cards.css('h4 a::text').re('[A-Z].+')[0]", {
                "Price": (float(i.css('div.card-copy p::text').re('[0-9]+')[0])+float(i.css('div.card-copy p::text').re('[0-9]+')[1]))/2,              
                "Link": Cards.css('h4 a::attr(href)').extract_first(),
            }}
        else:
                yield {
	        	"cards.css('h4.card_title a::text').re('[A-Z].+')[0]", {
	        	"price" : float(cards.css('div.card-copy p::text').re('[0-9]+')[0]),
                "link" : cards.css('a::attr(href)').extract_first(), }
                }