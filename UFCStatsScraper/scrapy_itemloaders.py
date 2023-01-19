from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
import logging
from scrapy import Request
from scrapy.exceptions import IgnoreRequest


from UFCStatsScraper.items import (
    FighterItem,
    FightItem,
    EventItem,
    OfficialUFCFighter,
    ESPNFighter,
    ESPNBouts
)
from UFCStatsScraper.utils.preprocessing import (
    remove_whitespace,
    remove_newlines,
    replace_empty_string,
)

logger = logging.getLogger(__name__)


class ESPNBoutLoader(ItemLoader):
    ''' ItemLoader for ESPNFighterItem '''
    default_input_processor = MapCompose(remove_whitespace, replace_empty_string)
    default_output_processor = TakeFirst()

    bout_xpath_dict = {
        'Date': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[1]/text()",
        'Opponent': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[2]/a/text()",
        'Event': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[3]/a/text()",
        'Result': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[4]/div/text()",
        'EventURL': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[3]/a/@href",
        ###############################
        'Dist_Sig_Bdy_Strk_Prop': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[5]/text()",
        'Dist_Sig_Head_Strk_Prop': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[6]/text()",
        'Dist_Sig_Leg_Strk_Prop': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[7]/text()",
        'Tot_Strk_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[8]/text()",
        'Tot_Strk_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[9]/text()",
        'Sig_Strk_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[10]/text()",
        'Sig_Strk_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[11]/text()",
        'Tot_Strk_Prop': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[12]/text()",
        'Knockdowns': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[13]/text()",
        'Body_Percentage': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[14]/text()",
        'Head_Percentage': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[15]/text()",
        'Leg_Percentage': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[1]/td[16]/text()",
        ###############################
        'Sig_Clnch_Bdy_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[5]/text()",
        'Sig_Clnch_Bdy_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[6]/text()",
        'Sig_Clnch_Head_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[7]/text()",
        'Sig_Clnch_Head_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[8]/text()",
        'Sig_Clnch_Leg_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[9]/text()",
        'Sig_Clnch_Leg_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[10]/text()",
        'Reversals': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[11]/text()",
        'Slam_Rate': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[12]/text()",
        'Tkdwn_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[13]/text()",
        'Tkdwn_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[14]/text()",
        'Tkdwn_Slams': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[15]/text()",
        'Tkdwn_Acc': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[2]/td[16]/text()",
        ###############################
        'Sig_Grnd_Bdy_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[5]/text()",
        'Sig_Grnd_Bdy_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[6]/text()",
        'Sig_Grnd_Head_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[7]/text()",
        'Sig_Grnd_Head_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[8]/text()",
        'Sig_Grnd_Leg_Lnd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[9]/text()",
        'Sig_Grnd_Leg_Atmpt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[10]/text()",
        'Advances': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[11]/text()",
        'Adv_To_Back': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[12]/text()",
        'Adv_To_Hlf_Gd': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[13]/text()",
        'Adv_To_Mnt': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[14]/text()",
        'Adv_To_Side': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[15]/text()",
        'Submissions': f"(.//tr[contains(@class, 'Table__TR')][@data-idx=$idx])[3]/td[16]/text()",
    }

    def _init__(self, response, *args, **kwargs):
        super().__init__(response=response, item=ESPNBouts(), *args, **kwargs)

        fname = locals()['Fighter_Name'] = kwargs['Fighter_Name'] or '---'
        bout_list = response.xpath("//tr[contains(@class, 'Table__TR')][@data-idx]")
        max_idx = len(bout_list) / 3

        all_bout_data = []
        for i in range(max_idx):
            single_bout_data = {}
            single_bout_data['Fighter_Name'] = fname

            for key, xpth in self.bout_xpaths.items():
                single_bout_data[key] = response.xpath(xpth, idx=i).get('---')
            all_bout_data.append(single_bout_data)






class ESPNLoader(ItemLoader):
    ''' ItemLoader for ESPNFighterItem '''
    default_input_processor = MapCompose(
        remove_whitespace,
        replace_empty_string)
    default_output_processor = TakeFirst()

    overview_xpaths = {
        'FName': "//span[@class='truncate min-w-0 fw-light']/text()",
        'LName': "//span[@class='truncate min-w-0']/text()",
        'Weight_Class': "//div[contains(@class, 'PlayerHeader__Main_Aside')]/div//li[2]/text()",
        'Birthdate_Age': "//ul[contains(@class, 'PlayerHeader__Bio_List')]/li[2]/div[2]/div/text()",
        'Team': "//ul[contains(@class, 'PlayerHeader__Bio_List')]/li[3]/div[2]/div/text()",
        'Nickname': "//ul[contains(@class, 'PlayerHeader__Bio_List')]/li[4]/div[2]/div/text()",
        'Stance': "//ul[contains(@class, 'PlayerHeader__Bio_List')]/li[5]/div[2]/div/text()",
        'WLD': "//div[contains(@class, 'PlayerHeader__Right flex align-center')]//li[1]/div/div[2]/text()",
        '(T)KO': "//div[contains(@class, 'PlayerHeader__Right flex align-center')]//li[2]/div/div[2]/text()",
        'Sub': "//div[contains(@class, 'PlayerHeader__Right flex align-center')]//li[3]/div/div[2]/text()",
        'Ht_Wt': "//ul[contains(@class, 'PlayerHeader__Bio_List')]/li[1]/div[2]/div/text()",
        'Country': "//div[contains(@class, 'PlayerHeader__Main_Aside')]/div//li[1]/text()"
    }

    def __init__(self, response, *args, **kwargs):
        super().__init__(response=response, item=ESPNFighter(), *args, **kwargs)
        if response.xpath('//ul[contains(@class, "PlayerHeader__Bio_List")][li]'):
            for key, xpth in self.overview_xpaths.items():
                # Check the xpath exists before adding it to the item
                if response.xpath(xpth).get():
                    # Check if the item already has a value for the key
                    if self.item[key] == '---':
                        # Replace it if it does
                        locals()[key] = self.replace_xpath(key, xpth)
                        # Otherwise add it
                    else: locals()[key] = self.add_xpath(key, xpth)
                # If the xpath doesn't exist, put a placeholder in the item
                else: locals()[key] = self.add_value(key, '---')
            self.load_item()
        else:
            pass






    # def load_bio_fields(self, response):
    #     for key, value in self.bio_xpaths.items():
    #         self.add_xpath(key, value)
    #     self.load_item()

    # def load_other_fields(self, response):
    #     if not ['FName']:
    #         locals()['FName'] = ''
    #     if not locals()['LName']:
    #         locals()['LName'] = ''
    #     full_name = (locals()['FName'] + ' ' + locals()['LName']).title()
    #     logger.info(full_name)

    #     # Additional fields
    #     self.add_xpath('Fighting_Style', f'//a[@class="AnchorLink"]/following-sibling::div//tr[@class="Table__TR Table__TR--sm Table__even"][td="{full_name}"]/td[2]/text()')
    #     self.add_value('Full_Name', full_name)
    #     self.add_value('FighterURL', response.url)

    #     self.load_item()


class FighterLoader(ItemLoader):
    """ItemLoader for FighterItem"""

    default_input_processor = MapCompose(
        remove_whitespace,
        replace_empty_string,
    )
    default_output_processor = TakeFirst()
    field_xpaths = [
        (
            "Fighter_Name",
            'normalize-space(//*[@class="b-content__title-highlight"]//text())',
        ),
        ("Nickname", 'normalize-space(//*[@class="b-content__Nickname"]//text())'),
        ("Record", 'normalize-space(//*[@class="b-content__title-record"]//text())'),
        (
            "Height",
            'normalize-space(//*[@class="b-list__box-list"]/li[contains(i/text(), "Height")]/text()[2])',
        ),
        (
            "Listed_Weight",
            'normalize-space(//*[@class="b-list__box-list"]/li[contains(i/text(), "Weight")]/text()[2])',
        ),
        (
            "Reach",
            'normalize-space(//*[@class="b-list__box-list"]/li[contains(i/text(), "Reach")]/text()[2])',
        ),
        (
            "DoB",
            'normalize-space(//*[@class="b-list__box-list"]/li[contains(i/text(), "DOB")]/text()[2])',
        ),
        (
            "Stance",
            'normalize-space(//*[@class="b-list__box-list"]/li[contains(i/text(), "STANCE")]/text()[2])',
        ),
        (
            "SSLpM",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "SLpM")]/text()[2])',
        ),
        (
            "SSAcc",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "Str. Acc")]/text()[2])',
        ),
        (
            "SSApM",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "SApM")]/text()[2])',
        ),
        (
            "SSDef",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "Str. Def")]/text()[2])',
        ),
        (
            "TDavg",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "TD Avg")]/text()[2])',
        ),
        (
            "TDAcc",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "TD Acc")]/text()[2])',
        ),
        (
            "TDDef",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "TD Def")]/text()[2])',
        ),
        (
            "SubAvg",
            'normalize-space(//*[@class="b-list__info-box-left clearfix"]//li[contains(i/text(), "Sub. Avg")]/text()[2])',
        ),
    ]

    def __init__(self, response, *args, **kwargs):
        super().__init__(response=response, item=FighterItem(), *args, **kwargs)
        self.response = response
        for field, xpath in self.field_xpaths:
            locals()[field] = self.add_xpath(field, xpath)
        self.load_item()


class FightLoader(ItemLoader):
    """ItemLoader for FightItem"""

    default_input_processor = MapCompose(
        remove_whitespace,
        remove_newlines,
        replace_empty_string,
    )
    default_output_processor = TakeFirst()

    field_xpaths = [
        ("EventName", "//*[@class='b-content__title']/a/text()"),
        ("Weight_Class", "//*[@class='b-fight-details__fight-title']/text()[last()]"),
        ("Method", '//*[@class="b-fight-details__text"][1]/i[1]/i[2]/text()'),
        ("Round", '//*[@class="b-fight-details__text"][1]/i[2]/text()[2]'),
        ("Time", '//*[@class="b-fight-details__text"][1]/i[3]/text()[2]'),
        ("TimeFormat", '//*[@class="b-fight-details__text"][1]/i[4]/text()[2]'),
        ("Referee", '//*[@class="b-fight-details__text"][1]/i[5]/span/text()'),
        (
            "Fighter1",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//p[1]/a/text()',
        ),
        (
            "Fighter1_Nickname",
            "//*[@class='b-fight-details']//*[@class='b-fight-details__person'][1]//p/text()",
        ),
        (
            "Fighter2",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//p[2]/a/text()',
        ),
        (
            "Fighter2_Nickname",
            "//*[@class='b-fight-details']//*[@class='b-fight-details__person'][2]//p/text()",
        ),
        (
            "Fighter1_KD",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[2]/p[1]/text()',
        ),
        (
            "Fighter2_KD",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[2]/p[2]/text()',
        ),
        (
            "Fighter1_SIG_STR",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[3]/p[1]/text()',
        ),
        (
            "Fighter2_SIG_STR",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[3]/p[2]/text()',
        ),
        (
            "Fighter1_SIG_STR_pct",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[4]/p[1]/text()',
        ),
        (
            "Fighter2_SIG_STR_pct",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[4]/p[2]/text()',
        ),
        (
            "Fighter1_TOTAL_STR",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[5]/p[1]/text()',
        ),
        (
            "Fighter2_TOTAL_STR",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[5]/p[2]/text()',
        ),
        (
            "Fighter1_TD",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[6]/p[1]/text()',
        ),
        (
            "Fighter2_TD",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[6]/p[2]/text()',
        ),
        (
            "Fighter1_TD_pct",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[7]/p[1]/text()',
        ),
        (
            "Fighter2_TD_pct",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[7]/p[2]/text()',
        ),
        (
            "Fighter1_SUB_ATT",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[8]/p[1]/text()',
        ),
        (
            "Fighter2_SUB_ATT",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[8]/p[2]/text()',
        ),
        (
            "Fighter1_REV",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[9]/p[1]/text()',
        ),
        (
            "Fighter2_REV",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[9]/p[2]/text()',
        ),
        (
            "Fighter1_CTRL",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[10]/p[1]/text()',
        ),
        (
            "Fighter2_CTRL",
            '*//section[@class="b-fight-details__section js-fight-section"][2]//tbody//td[10]/p[2]/text()',
        ),
        (
            "Fighter1_HEAD",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[4]/p[1]/text()',
        ),
        (
            "Fighter2_HEAD",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[4]/p[2]/text()',
        ),
        (
            "Fighter1_BODY",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[5]/p[1]/text()',
        ),
        (
            "Fighter2_BODY",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[5]/p[2]/text()',
        ),
        (
            "Fighter1_LEG",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[6]/p[1]/text()',
        ),
        (
            "Fighter2_LEG",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[6]/p[2]/text()',
        ),
        (
            "Fighter1_DISTANCE",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[7]/p[1]/text()',
        ),
        (
            "Fighter2_DISTANCE",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[7]/p[2]/text()',
        ),
        (
            "Fighter1_CLINCH",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[8]/p[1]/text()',
        ),
        (
            "Fighter2_CLINCH",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[8]/p[2]/text()',
        ),
        (
            "Fighter1_GROUND",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[9]/p[1]/text()',
        ),
        (
            "Fighter2_GROUND",
            '*//section[@class="b-fight-details__section js-fight-section"][4]/following-sibling::table/tbody//td[9]/p[2]/text()',
        ),
    ]

    judge_xpaths = [
        (
            "Judge1",
            "normalize-space(//*[@class='b-fight-details__fight']//p[2]/i[2]/span/text())",
        ),
        (
            "Judge1_Score",
            "normalize-space(//*[@class='b-fight-details__fight']//p[2]/i[2]/text()[2])",
        ),
        (
            "Judge2",
            "normalize-space(//*[@class='b-fight-details__fight']//p[2]/i[3]/span/text())",
        ),
        (
            "Judge2_Score",
            "normalize-space(//*[@class='b-fight-details__fight']//p[2]/i[3]/text()[2])",
        ),
        (
            "Judge3",
            "normalize-space(//*[@class='b-fight-details__fight']//p[2]/i[4]/span/text())",
        ),
        (
            "Judge3_Score",
            "normalize-space(//*[@class='b-fight-details__fight']//p[2]/i[4]/text()[2])",
        ),
    ]

    def __init__(self, response, *args, **kwargs):
        bonus_labels = ["perf", "fight", "sub", "ko"]

        super().__init__(response=response, item=FightItem(), *args, **kwargs)
        self.response = response
        for field, xpath in self.field_xpaths:
            try:
                locals()[field] = self.add_xpath(field, xpath)
            except Exception:
                locals()[field] = self.add_value(field, "---")

        for field, xpath in self.judge_xpaths:
            try:
                locals()[field] = self.add_xpath(field, xpath)
            except Exception as e:
                locals()[field] = self.add_value(field, "---")
                self.logger.error(e)

        try:
            locals()["Winner"] = self.add_xpath(
                "Winner",
                "*//i[@class='b-fight-details__person-status b-fight-details__person-status_style_green']/following-sibling::div//a/text()",
            )
        except Exception as e:
            locals()["Winner"] = self.add_value("Winner", "---")
            self.logger.error(e)
        else:
            if locals()["Winner"]:
                locals()["Winner"] = self.add_value("Winner", locals()["Winner"])
            else:
                locals()["Winner"] = self.add_value("Winner", "---")

        for bonus in bonus_labels:
            try:
                bonus_present_bool = response.xpath(
                    f"*//img[contains(@src, '{bonus}.png')]"
                ) not in (None, [], "")
            except Exception:
                locals()[f"{bonus}_bonus"] = self.add_value(f"{bonus}_bonus", "0")
            else:
                if bonus_present_bool:
                    locals()[f"{bonus}_bonus"] = self.add_value(f"{bonus}_bonus", "1")
                else:
                    locals()[f"{bonus}_bonus"] = self.add_value(f"{bonus}_bonus", "0")


class EventLoader(ItemLoader):
    default_input_processor = MapCompose(
        remove_whitespace,
        remove_newlines,
        replace_empty_string,
    )
    default_output_processor = TakeFirst()

    field_xpaths = [
        ("EventName", ".//a/text()"),
        ("EventDate", ".//span/text()"),
        ("Location", ".//td[2]/text()"),
    ]

    def __init__(self, selector, *args, **kwargs):
        super().__init__(selector=selector, item=EventItem(), *args, **kwargs)
        self.selector = selector
        for field, xpath in self.field_xpaths:
            locals()[field] = self.add_xpath(field, xpath)
        self.load_item()


class OfficialUFCFighterLoader(ItemLoader):
    default_output_processor = TakeFirst()
    field_xpaths = [
        ("Fighter_Name", "//h1[@class='hero-profile__name']/text()"),
        ("Nickname", "//p[@class='hero-profile__nickname']/text()"),
        (
            "Division",
            "normalize-space(//p[@class='hero-profile__tag'][contains(text(), 'Division')]/text())",
        ),
        (
            "Activity",
            "//p[@class='hero-profile__tag'][text()='Active' or text()='Not Fighting']/text()",
        ),
        (
            "Title_Holder",
            "//p[@class='hero-profile__tag'][contains(text(), 'Title Holder')]/text()",
        ),
        (
            "PFP_Rank",
            "//p[@class='hero-profile__tag'][contains(text(), 'PFP')]/text()",
        ),
        (
            "Listed_Fighting_Style",
            "//div[@class='c-bio__label'][contains(text(),'Fighting style')]/following-sibling::div/text()",
        ),
        (
            "Trains_At",
            "//div[@class='c-bio__label'][contains(text(),'Trains at')]/following-sibling::div/text()",
        ),
        (
            "Standing_Strikes",
            "//div[@class='c-stat-3bar__group']/div[contains(text(),'Standing')]/following-sibling::div/text()",
        ),
        (
            "Clinch_Strikes",
            "//div[@class='c-stat-3bar__group']/div[contains(text(),'Clinch')]/following-sibling::div/text()",
        ),
        (
            "Ground_Strikes",
            "//div[@class='c-stat-3bar__group']/div[contains(text(),'Ground')]/following-sibling::div/text()",
        ),
        (
            "Place_of_Birth",
            "//div[@class='c-bio__field c-bio__field--border-bottom-small-screens']/div[2]/text()",
        ),
        (
            "Record",
            "//p[@class='hero-profile__division-body']/text()"
        ),
        (
            'Height',
            "//div[@class = 'c-bio__label'][text() = 'Height'] /following-sibling::div/text()"
        ),
        (
            'Weight',
            "//div[@class = 'c-bio__label'][text() = 'Weight'] /following-sibling::div/text()"
        ),
        (
            'Reach',
            "//div[@class = 'c-bio__label'][text() = 'Reach'] /following-sibling::div/text()"
        ),
        (
            'Leg_Reach',
            '//div[@class = "c-bio__label"][text() = "Leg reach"] /following-sibling::div/text()'
        ),
        (
            'Age',
            'normalize-space(//div[@class = "c-bio__label"][text() = "Age"] /following-sibling::div/text())'
        ),
        (
            'Head_SS',
            '//*[@id="e-stat-body_x5F__x5F_head_value"]/text()'
        ),
        (
            'Body_SS',
            '//*[@id="e-stat-body_x5F__x5F_body_value"]/text()'
        ),
        (
            'Leg_SS',
            '//*[@id="e-stat-body_x5F__x5F_leg_value"]/text()'
        )


    ]

    def __init__(self, response, *args, **kwargs):
        super().__init__(response=response, item=OfficialUFCFighter(), *args, **kwargs)
        self.response = response
        for field, xpath in self.field_xpaths:
            try:
                locals()[field] = self.add_xpath(field, xpath)
            except Exception:
                locals()[field] = self.add_value(field, "---")
            else:
                if locals()[field] in [None, [], ""]:
                    locals()[field] = self.add_value(field, "---")
        # Placeholder for manually added items.
        for field in ['DoB', 'College', 'Foundation_Styles', 'Head_Coach', 'Fighting_Out_Of']:
            locals()[field] = self.add_value(field, "---")

        self.load_item()


class FighterImageLoader(ItemLoader):
    pass


#     default_output_processor = TakeFirst()

#     def __init__(self, response, f_name, f_nickname, image_urls):
#         super().__init__(
#             response=response,
#             item=FighterImageItem(),
#         )
#         self.item["f_name"] = self.add_value("f_name", f_name)
#         self.item["f_nickname"] = self.add_value("f_nickname", f_nickname)
#         image_urls.append(
#             response.xpath("//div[@class='hero-profile__image-wrap']/img/@src").get()
#         )
#         image_urls = [image_url for image_url in image_urls if image_url]
#         self.item["image_urls"] = self.add_value("image_urls", image_urls)
#         self.load_item()


if __name__ == "__main__":
    pass
