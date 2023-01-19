from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
import logging
from scrapy.exceptions import StopDownload



from UFCStatsScraper.scrapy_itemloaders import ESPNLoader

logger = logging.getLogger(__name__)

class ESPNFighterScraper(Spider):
    name = 'espn'

    start_urls = [f'http://www.espn.com/mma/fighters?search={chr(letter)}' for letter in range(65, 91)]
    fighter_links = LinkExtractor(allow=r'/mma/fighter/_/id/.*')

    def parse(self, response):
        fighter_links = self.fighter_links.extract_links(response)
        yield from response.follow_all(fighter_links, self.parse_fighter_pages)

    def parse_fighter_pages(self, response):
        item = ESPNLoader(response).load_item()
        bio_page = 'https://www.espn.com' + response.xpath('//li[contains(@class, "Nav__Secondary__Menu__Item")]/a[span="Bio"]/@href')
        # response.xpath("//nav[@class='Nav__Secondary bg-clr-white brdr-clr-gray-03']//li[4]/a/@href").get()

        yield response.follow(bio_page, self.parse_bio_page, cb_kwargs={'item': item})



        # bio = response.xpath('//div[@class="bio"]')
        # item['bio'] = bio
        # return item