from scrapy.spiders import Spider
import logging

from UFCStatsScraper.scrapy_itemloaders import (
    OfficialUFCFighterLoader,
)
from UFCStatsScraper.items import FighterImageItem
import configs as cfg




logger = logging.getLogger(__name__)

class OfficialUFCFighterScraper(Spider):
    name = "officialufcfighters"
    start_urls = [
        "https://www.ufc.com/athletes/all?gender=All&search=&page=0",
    ]
    # populate fighter links to follow
    def parse(self, response):
        fighter_cards = response.xpath("//li[@class='l-flex__item']")
        next_page_link = response.xpath("//a[@class='button']/@href").get()
        # for fighter_card in fighter_cards:
        while fighter_cards:
            fighter_card = fighter_cards.pop()
            kwarg_dict = {"f_name": None, "f_nickname": None, "image_urls": []}

            skip_vals = ["", " ", None, [], "None"]

            if (
                f_name := fighter_card.xpath(
                    "normalize-space(.//div[@class='c-listing-athlete-flipcard__front']//span[@class='c-listing-athlete__name']/text())"
                ).get()
            ) not in skip_vals:
                kwarg_dict["f_name"] = f_name

            if (
                f_nickname := fighter_card.xpath(
                    "normalize-space(.//div[@class='c-listing-athlete-flipcard__front']//span[@class='c-listing-athlete__nickname']/div/div/text())"
                ).get()
            ) not in skip_vals:
                kwarg_dict["f_nickname"] = f_nickname
            else:
                kwarg_dict["f_nickname"] = None

            if (
                front := fighter_card.xpath(
                    ".//div[@class='c-listing-athlete-flipcard__front']//img[@class='image-style-teaser']/@src"
                ).get()
            ) not in skip_vals:
                kwarg_dict["image_urls"].append(front)

            if (
                back := fighter_card.xpath(
                    ".//div[@class='c-listing-athlete-flipcard__back']//img/@src"
                ).get()
            ) not in skip_vals:
                kwarg_dict["image_urls"].append(back)

            fighter_link = fighter_card.xpath(
                ".//a[@class='e-button--black ']/@href"
            ).get()

            if fighter_link in skip_vals:
                continue

            next_page_url = "https://www.ufc.com/athletes/all" + next_page_link
            kwarg_dict["next_page_link"] = next_page_url

            if (
                kwarg_dict["f_name"] not in skip_vals
                and kwarg_dict["f_nickname"] not in skip_vals
            ):
                if all([item not in skip_vals for item in kwarg_dict["image_urls"]]):
                    kwarg_dict["image_urls"] = [
                        url for url in kwarg_dict["image_urls"] if url is not None
                    ]
                    kwarg_dict["next_page_link"] = next_page_url
                    yield response.follow(
                        fighter_link, self.parse_ufcfighter_page, cb_kwargs=kwarg_dict
                    )
            else:
                yield response.follow(
                    fighter_link, self.parse_ufcfighter_page, cb_kwargs=kwarg_dict
                )
        yield response.follow(next_page_link, self.parse)

    def parse_ufcfighter_page(
        self, response, next_page_link, f_name=None, f_nickname=None, image_urls=None
    ):


        fighter_item = OfficialUFCFighterLoader(response)
        logger.info(fighter_item)
        # item = FighterImageItem()
        # item["f_name"] = f_name
        # item["f_nickname"] = f_nickname
        # item["image_urls"] = image_urls
        # item["image_urls"].append(
        #     response.xpath("//div[@class='hero-profile__image-wrap']/img/@src").get()
        # )
        # item["image_urls"] = [url for url in item["image_urls"] if url is not None]
        # yield item

        import requests
        from lxml import html
        fighter = '+'.join(f_name.lower().split(' '))
        search_url = f'https://www.tapology.com/search?term={fighter}&search=Submit&mainSearchFilter=fighters'

        r = requests.get(search_url)
        try:
            tree = html.fromstring(r.content)
            fighter_link = 'https://www.tapology.com' + tree.xpath("//div[@class='searchResultsFighter']//tr[2]//a/@href")[0]
        except Exception:
            fighter_link = None
        logger.info(fighter_link)


        if fighter_link:
            passthrough_arguments = {'next_page_link':next_page_link, 'fighter_item':fighter_item}
            yield response.follow(fighter_link, self.parse_tapology_fpage, cb_kwargs=passthrough_arguments)
        else:
            yield fighter_item
            yield response.follow(next_page_link, self.parse)







    def parse_tapology_fpage(self, response, **kwargs):
        next_page_link = kwargs['next_page_link']
        fighter_item = kwargs['fighter_item']
        manual_fields = {
            'DoB': "//div[@class='details details_two_columns']//li[strong='| Date of Birth:']//span[2]/text()",
            'College': "//div[@class='details details_two_columns']//li[strong='College:']/span/text()",
            'Foundation_Styles':"//div[@class='details details_two_columns']//li[strong='Foundation Style:']/span/text()",
            'Head_Coach':"//div[@class='details details_two_columns']//li[strong='Head Coach:']/span/text()",
            'Fighting_Out_Of':"normalize-space//div[@class='details details_two_columns']//li[strong='Fighting out of:']/span/text())"}

        for field, xpath in manual_fields.items():
            try:
                fighter_item[field] = response.xpath(xpath).get()
            except Exception:
                fighter_item[field] = '---'
        logger.info(fighter_item)
        # yield fighter_item
        # yield response.follow(next_page_link, self.parse)
