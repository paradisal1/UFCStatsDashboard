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




class ESPNFighter(Item):
    '''Item for ESPN data'''
    fields_of_interest = ('FName', 'LName', 'Weight_Class', 'Birthdate_Age', 'Team',
                          'Nickname', 'Stance', 'WLD', '(T)KO', 'Sub', 'Ht_Wt', 'Country',
                          'Reach', 'Fighting_Style')
    for field in fields_of_interest:
        locals()[field] = Field()




class ESPNBouts(Item):
    fields_of_interest = ('Fighter', 'Opponent', 'Event', 'Round', 'Decision', 'Round', 'Time',
                          'Date', 'Opponent', 'Result', 'Method', 'Round', 'Time', 'EventURL', 'FighterURL',
                          'Dist_Sig_Bdy_Strk_Prop', 'Dist_Sig_Head_Strk_Prop', 'Dist_Sig_Leg_Strk_Prop',
                          'Tot_Strk_Atmpt', 'Tot_Strk_Lnd', 'Sig_Strk_Lnd', 'Sig_Strk_Atmpt', 'Tot_Strk_Prop',
                          'Knockdowns', 'Body_Percentage', 'Head_Percentage', 'Leg_Percentage',
                          'Sig_Clnch_Bdy_Lnd', 'Sig_Clnch_Bdy_Atmpt', 'Sig_Clnch_Head_Lnd', 'Sig_Clnch_Head_Atmpt',
                          'Sig_Clnch_Leg_Lnd', 'Sig_Clnch_Leg_Atmpt', 'Reversals', 'Slam_Rate', 'Tkdwn_Lnd',
                          'Tkdwn_Atmpt', 'Tkdwn_Slams', 'Tkdwn_Acc', 'Sig_Grnd_Bdy_Lnd', 'Sig_Grnd_Bdy_Atmpt',
                          'Sig_Grnd_Head_Lnd', 'Sig_Grnd_Head_Atmpt', 'Sig_Grnd_Leg_Lnd', 'Sig_Grnd_Leg_Atmpt',
                          'Advances', 'Adv_To_Back', 'Adv_To_Hlf_Gd', 'Adv_To_Mnt', 'Adv_To_Side', 'Submissions')
    for field in fields_of_interest:
        locals()[field] = Field()




class EventItem(Item):
    """Item for fields on the event page & judging details"""
    fields_of_interest = ('EventName', 'EventDate', 'Location')
    for field in fields_of_interest:
        locals()[field] = Field()


class FighterItem(Item):
    """Item for fields on the fighter page"""
    fields_of_interest = ('Fighter_Name', 'Nickname', 'Record', 'Height', 'Listed_Weight',
                          'Reach', 'DoB', 'Stance', 'SSLpM', 'SSAcc', 'SSApM', 'SSDef',
                          'TDavg', 'TDAcc', 'TDDef', 'SubAvg')
    for field in fields_of_interest:
        locals()[field] = Field()


class FightItem(Item):
    """Item for fields on the fight page"""
    fields_of_interest = ('EventName', 'Weight_Class', 'Method', 'Round', 'Time', 'TimeFormat',
                          'Referee', 'Fighter1', 'Fighter1_Nickname', 'Fighter2', 'Fighter2_Nickname',
                          'Fighter1_KD', 'Fighter2_KD', 'Fighter1_SIG_STR', 'Fighter2_SIG_STR', 'Fighter1_SIG_STR_pct',
                          'Fighter2_SIG_STR_pct', 'Fighter1_TOTAL_STR', 'Fighter2_TOTAL_STR', 'Fighter1_TD', 'Fighter2_TD',
                          'Fighter1_TD_pct', 'Fighter2_TD_pct', 'Fighter1_SUB_ATT', 'Fighter2_SUB_ATT', 'Fighter1_REV',
                          'Fighter2_REV', 'Fighter1_CTRL', 'Fighter2_CTRL', 'Fighter1_HEAD', 'Fighter2_HEAD', 'Fighter1_BODY'
                          'Fighter2_BODY', 'Fighter1_LEG', 'Fighter2_LEG', 'Fighter1_DISTANCE', 'Fighter2_DISTANCE',
                          'Fighter1_CLINCH', 'Fighter2_CLINCH', 'Fighter1_GROUND', 'Fighter2_GROUND', 'Judge1',
                          'Judge1_Score', 'Judge2', 'Judge2_Score', 'Judge3', 'Judge3_Score', 'Winner', 'perf_bonus',
                          'fight_bonus', 'sub_bonus', 'ko_bonus')
    for field in fields_of_interest:
        locals()[field] = Field()


class OfficialUFCFighter(Item):
    image_urls = Field()
    images = Field()
    fields_of_interest = (
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
        "Place_of_Birth",
        "Record",
        'Height',
        'Weight',
        'Reach',
        'Leg_Reach',
        'Age',
        'Head_SS',
        'Body_SS',
        'Leg_SS',
        'DoB',
        'College',
        'Foundation_Styles',
        'Head_Coach',
        'Fighting_Out_Of'
    )
    for field in fields_of_interest:
        locals()[field] = Field()


class FighterImageItem(Item):
    image_urls = Field()
    images = Field()
    f_name = Field()
    f_nickname = Field()
