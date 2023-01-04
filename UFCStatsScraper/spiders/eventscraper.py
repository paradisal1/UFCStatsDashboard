from scrapy.spiders import Spider
from UFCStatsScraper.scrapy_itemloaders import EventLoader

# import logging


class EventScraper(Spider):
    name = "events"

    start_urls = ["http://www.ufcstats.com/statistics/events/completed?page=all"]

    def parse(self, response):
        """Parse event pages from the main events browser page"""
        base_xpath = "*//tr[@class='b-statistics__table-row']"

        for event in response.xpath(base_xpath):
            yield EventLoader(event).load_item()

            # logging.info(event.xpath("//a/text()").getall())
        # logging.info(event.xpath("//a/text()"))


if __name__ == "__main__":
    pass
