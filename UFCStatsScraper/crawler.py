from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl("officialufcfighters")
process.crawl("fights")
process.crawl("events")
process.start()
