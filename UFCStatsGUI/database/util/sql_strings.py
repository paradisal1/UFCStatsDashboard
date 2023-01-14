create_FIGHTS_table_sql_string = """
    CREATE TABLE IF NOT EXISTS fights
        (EventName text, Weight_Class text, Method text,
        Round text, Time text, TimeFormat text,
        Referee text, Fighter1 text, Fighter1_Nickname,
        Fighter2 text, Fighter2_Nickname,
        Fighter1_KD text,  Fighter2_KD text,
        Fighter1_SIG_STR text,  Fighter2_SIG_STR text,
        Fighter1_SIG_STR_pct text,  Fighter2_SIG_STR_pct text,
        Fighter1_TOTAL_STR text,  Fighter2_TOTAL_STR text,
        Fighter1_TD text,  Fighter2_TD text,
        Fighter1_TD_pct text,  Fighter2_TD_pct text,
        Fighter1_SUB_ATT text,  Fighter2_SUB_ATT text,
        Fighter1_REV text,  Fighter2_REV text,
        Fighter1_CTRL text,  Fighter2_CTRL text,
        Fighter1_HEAD text,  Fighter2_HEAD text,
        Fighter1_BODY text,  Fighter2_BODY text,
        Fighter1_LEG text,  Fighter2_LEG text,
        Fighter1_DISTANCE text,  Fighter2_DISTANCE text,
        Fighter1_CLINCH text,  Fighter2_CLINCH text,
        Fighter1_GROUND text,  Fighter2_GROUND text,
        Judge1 text,  Judge1_Score text, Judge2 text,
        Judge2_Score text,  Judge3 text,  Judge3_Score text,
        Winner text, perf_bonus text, fight_bonus text,
        sub_bonus text, ko_bonus text);
"""

create_FIGHTERS_table_sql_string = """
    CREATE TABLE IF NOT EXISTS fighters
        (Fighter_Name text,  Nickname text,  Record text,
        Height text,  Listed_Weight text,  Reach text,
        DoB text, Stance text,  SSLpM text,  SSAcc text,
        SSApM text,  SSDef text,  TDavg text,
        TDAcc text,  TDDef text,  SubAvg text);
"""

create_EVENTS_table_sql_string = """
    CREATE TABLE IF NOT EXISTS events
        (EventName text,  EventDate text,  Location text)

"""

create_DEFAULT_table_sql_string = ""

create_OFFICIALUFCFIGHTERS_table_sql_string = """
    CREATE TABLE IF NOT EXISTS officialufcfighters
        (Fighter_Name text, Nickname text, Division text,
        Activity text, Title_Holder text, PFP_Rank text,
        Listed_Fighting_Style text, Trains_At text,
        Standing_Strikes text, Clinch_Strikes text,
        Ground_Strikes text, PlaceOfBirth text,
        Record text)
"""
