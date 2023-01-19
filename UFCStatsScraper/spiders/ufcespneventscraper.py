from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor

import logging
from datetime import datetime
from pathlib import Path



from UFCStatsScraper.scrapy_itemloaders import ESPNLoader
from UFCStatsScraper.utils import custom_request



logger = logging.getLogger(__name__)
print()

class ESPNEventScraper(Spider):
    name = 'espn_events'
    start_urls = [f"https://www.espn.com/mma/schedule/_/year/{y}/league/ufc" for y in range(1993, datetime.today().year + 1)]
    event_links = LinkExtractor(allow=r'https://www.espn.com/mma/fightcenter/_/id/\d*/league/ufc')

    i = 0

    def parse(self, response):
        present_event_links = self.event_links.extract_links(response)

        yield from response.follow_all(present_event_links, self.parse_event_pages, )

    def parse_event_pages(self, response, ):
        import re

        script_txt = response.xpath("//div[@id='espnfitt']/following-sibling::script[1]").get()

        fighter_urls = re.findall(r'(http://www.espn.com/mma/fighter/_/id/\d+/[\w+-]+)', script_txt)

        yield from response.follow_all(fighter_urls, self.parse_fighter_pages)

    def parse_fighter_pages(self, response):
        bio_page = 'https://www.espn.com' + response.xpath('//li[contains(@class, "Nav__Secondary__Menu__Item")]/a[span="Bio"]/@href')
        yield response.follow(bio_page, self.parse_bio_page, cb_kwargs={'item': item})






























    # def parse_event_pages(self, response):
    #     fighter_links = LinkExtractor(allow=r'https://www.espn.com/mma/fighter/_/id/.*', unique=True)
    #     present_fighter_links = fighter_links.extract_links(response)
    #     logger.info(present_fighter_links)
    #     with open('UFCStatsScraper/utils/present_fighter_links.txt', 'a') as f:
    #         for link in present_fighter_links:
    #             f.write(link.url + '\n')
