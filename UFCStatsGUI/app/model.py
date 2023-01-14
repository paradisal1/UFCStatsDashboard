try:
    from database.DBInterface import DBInterface
except:
    from UFCStatsGUI.database.DBInterface import DBInterface



class FighterDisplay:
    def __init__(self, focused_fighter):
        self.focused_fighter = focused_fighter




if __name__ == '__main__':
    FighterDisplay('Amanda Nunes').retrieve_fighter_data()
