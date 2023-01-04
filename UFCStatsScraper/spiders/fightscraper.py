from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor

from UFCStatsScraper.scrapy_itemloaders import FightLoader


class FightScraper(Spider):
    name = "fights"

    start_urls = [
        # "http://www.ufcstats.com/statistics/events/completed"
        "http://www.ufcstats.com/statistics/events/completed?page=all"
    ]
    # populate event links to follow
    event_linkextractor = LinkExtractor(allow=r"/event-details/.*")
    # populate fight links to follow
    fight_linkextractor = LinkExtractor(allow=r"/fight-details/.*")

    def parse(self, response):
        """Parse event pages from the main events browser page"""
        # get event links
        event_links = self.event_linkextractor.extract_links(response)
        # follow event links, callback to parse_event_pages
        yield from response.follow_all(event_links, self.parse_event_pages)

    def parse_event_pages(self, response):
        """Parses event pages for fight details"""
        # get fight links
        fight_links = self.fight_linkextractor.extract_links(response)
        # follow fight links, callback to parse_fight_pages
        yield from response.follow_all(fight_links, self.parse_fight_pages)

    def parse_fight_pages(self, response):
        """Parses fight pages for fight details"""
        # return the loaded fight item
        return FightLoader(response).load_item()
