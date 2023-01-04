# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

# from itemloaders.processors import TakeFirst

# from UFCStatsScraper.utils.preprocessing import (
#     remove_newlines,
#     remove_whitespace,
#     replace_empty_string,
# )
class EventItem(Item):
    """Item for fields on the event page & judging details"""

    fields_of_interest = [("EventName", {}), ("EventDate", {}), ("Location", {})]
    for field in fields_of_interest:
        locals()[field[0]] = Field(**field[1])


class FighterItem(Item):
    """Item for fields on the fighter page"""

    # default_in_processors = [
    #     remove_whitespace,
    #     remove_newlines,
    #     replace_empty_string,
    # ]
    # default_out_processors = [TakeFirst()]
    fields_of_interest = [
        ("Fighter_Name", {}),
        ("Nickname", {}),
        (
            "Record",
            {},
        ),
        (
            "Height",
            {},
        ),
        (
            "Listed_Weight",
            {},
        ),
        (
            "Reach",
            {},
        ),
        (
            "DoB",
            {},
        ),
        ("Stance", {}),
        (
            "SSLpM",
            {},
        ),
        (
            "SSAcc",
            {},
        ),
        (
            "SSApM",
            {},
        ),
        (
            "SSDef",
            {},
        ),
        (
            "TDavg",
            {},
        ),
        (
            "TDAcc",
            {},
        ),
        (
            "TDDef",
            {},
        ),
        (
            "SubAvg",
            {},
        ),
    ]

    for field in fields_of_interest:
        locals()[field[0]] = Field(**field[1])


class FightItem(Item):
    """Item for fields on the fight page"""

    # default_in_processors = [
    #     remove_whitespace,
    #     remove_newlines,
    #     replace_empty_string,
    # ]
    # default_out_processors = [TakeFirst()]
    fields_of_interest = [
        ("EventName", {}),
        ("Weight_Class", {}),
        ("Method", {}),
        (
            "Round",
            {},
        ),
        ("Time", {}),
        ("TimeFormat", {}),
        ("Referee", {}),
        ("Fighter1", {}),
        ("Fighter1_Nickname", {}),
        ("Fighter2", {}),
        ("Fighter2_Nickname", {}),
        (
            "Fighter1_KD",
            {},
        ),
        (
            "Fighter2_KD",
            {},
        ),
        (
            "Fighter1_SIG_STR",
            {},
        ),
        (
            "Fighter2_SIG_STR",
            {},
        ),
        (
            "Fighter1_SIG_STR_pct",
            {},
        ),
        (
            "Fighter2_SIG_STR_pct",
            {},
        ),
        (
            "Fighter1_TOTAL_STR",
            {},
        ),
        (
            "Fighter2_TOTAL_STR",
            {},
        ),
        (
            "Fighter1_TD",
            {},
        ),
        (
            "Fighter2_TD",
            {},
        ),
        (
            "Fighter1_TD_pct",
            {},
        ),
        (
            "Fighter2_TD_pct",
            {},
        ),
        (
            "Fighter1_SUB_ATT",
            {},
        ),
        (
            "Fighter2_SUB_ATT",
            {},
        ),
        (
            "Fighter1_REV",
            {},
        ),
        (
            "Fighter2_REV",
            {},
        ),
        (
            "Fighter1_CTRL",
            {},
        ),
        (
            "Fighter2_CTRL",
            {},
        ),
        (
            "Fighter1_HEAD",
            {},
        ),
        (
            "Fighter2_HEAD",
            {},
        ),
        (
            "Fighter1_BODY",
            {},
        ),
        (
            "Fighter2_BODY",
            {},
        ),
        (
            "Fighter1_LEG",
            {},
        ),
        (
            "Fighter2_LEG",
            {},
        ),
        (
            "Fighter1_DISTANCE",
            {},
        ),
        (
            "Fighter2_DISTANCE",
            {},
        ),
        (
            "Fighter1_CLINCH",
            {},
        ),
        (
            "Fighter2_CLINCH",
            {},
        ),
        (
            "Fighter1_GROUND",
            {},
        ),
        (
            "Fighter2_GROUND",
            {},
        ),
        ("Judge1", {}),
        ("Judge1_Score", {}),
        ("Judge2", {}),
        ("Judge2_Score", {}),
        ("Judge3", {}),
        ("Judge3_Score", {}),
        ("Winner", {}),
        ("perf_bonus", {}),
        ("fight_bonus", {}),
        ("sub_bonus", {}),
        ("ko_bonus", {}),
    ]
    for field in fields_of_interest:
        locals()[field[0]] = Field(**field[1])


class OfficialUFCFighter(Item):

    image_urls = Field()
    images = Field()
    fields_of_interest = [
        "Fighter_Name",
        "Nickname",
        "Division",
        "Activity",
        "Title_Holder",
        "PFP_Rank",
        "Listed_Fighting_Style",
        "Trains_At",
        "Standing_Strikes",
        "Clinch_Strikes",
        "Ground_Strikes",
    ]
    for field in fields_of_interest:
        locals()[field] = Field()


class FighterImageItem(Item):
    image_urls = Field()
    images = Field()
    f_name = Field()
    f_nickname = Field()
