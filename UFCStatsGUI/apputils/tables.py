from app.database.DBInterface import DBInterface

db = DBInterface("database/ufc_silver")

combatants = db.Pdf("combatants")


class Tables:
    def __init__(self, db=None):
        if db == None:
            self.db = DBInterface("database/ufc_silver")
        self.db = db

    def radar_chart_data(self, fighter):
        offense_cols = ["SSLPM", "TDAVG", "SUBAVG", "CTRL_RATIO"]

        def _radar_chart_maxes():
            maxes = {}
