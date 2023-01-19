import configs


from apputils.utils import qr, set_variable
try:
    from database.DBInterface import DBInterface
except:
    from UFCStatsGUI.database.DBInterface import DBInterface

class FighterController:
    def __init__(self, focused_fighter):
        self.focused_fighter = focused_fighter

        self.fighter_data = self.retrieve_fighter_data()
        self.fighter_bouts = self.retrieve_fighter_bouts()

    def __repr__(self):
        return f"FighterDisplay({self.focused_fighter})"

    def __str__(self):
        return f"{self.focused_fighter}: {self.fighter_data['WINS'].values[0]}-{self.fighter_data['LOSSES'].values[0]}-{self.fighter_data['DRAWS'].values[0]}"

    def _header_data(self):
        header_dict = {}
        header_data = ['F_NAME', 'NICKNAME', 'WINS', 'LOSSES', 'DRAWS', 'DOB', 'STANCE', 'HEIGHT', 'LISTED_WEIGHT', 'REACH', ''


    def retrieve_fighter_data(self, fighter=None):
        if fighter is None:
            fighter = self.focused_fighter
        data = DBInterface('database/ufc_silver').Pdf("combatants", close=True)
        return data[data['F_NAME'] == fighter]

    def retrieve_fighter_bouts(self, fighter=None):
        if fighter is None:
            fighter = self.focused_fighter
        bouts = DBInterface('database/ufc_silver').Pdf("bouts_df", close=True)
        return bouts[bouts['F'] == fighter]






if __name__ == '__main__':
    x = FighterController('Amanda Nunes')
    print(x)