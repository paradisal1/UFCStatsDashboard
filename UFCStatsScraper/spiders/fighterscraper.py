from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from UFCStatsScraper.scrapy_itemloaders import FighterLoader


class FighterScraper(Spider):
    name = "fighters"
    start_urls = [
        # "http://www.ufcstats.com/statistics/fighters?char=a&page=all"
        f"http://www.ufcstats.com/statistics/fighters?char={letter}&page=all"
        for letter in "abcdefghijklmnopqrstuvwxyz"
    ]
    # populate fighter links to follow
    fighter_linkextractor = LinkExtractor(allow=r"/fighter-details/.*")

    def parse(self, response):
        """Parse fighter pages from the main fighters browser page"""
        # get fighter links
        fighter_links = self.fighter_linkextractor.extract_links(response)
        # follow fighter links, callback to parse_fighter_pages
        yield from response.follow_all(fighter_links, self.parse_fighter_pages)

    def parse_fighter_pages(self, response):
        """Parses fighter pages for fight details"""
        # return the loaded fighter item
        return FighterLoader(response).load_item()
