import pandas as pd
import sqlite3
from pathlib import Path
import logging
import sys

try:
    logger = logging.getLogger(__name__)
except:
    logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))


class DBInterface(object):
    f = "__file__" if __name__ == "__main__" else __name__

    def __init__(self, db):
        try:
            db_path = Path(self.f).parent.parent / f"{db}.db"
        except:
            db_path = Path(self.f).parent.parent / f"{db}.db"
        self.conn = sqlite3.connect(db_path)

    def Pdf(self, table_name, close=False):
        df = pd.read_sql(f"SELECT * FROM {table_name}", self.conn)
        if close:
            self.close()
        return df

    def __call__(self, query=None, **kwargs):
        try:
            if kwargs['table']:
                if kwargs['column']:
                    if kwargs['value']:
                        data = pd.read_sql_query(f"SELECT * FROM {kwargs['table']} WHERE {kwargs['column']} = {kwargs['value']}", self.conn)
                    data = pd.read_sql_query(f"SELECT {kwargs['column']} FROM {kwargs['table']}", self.conn)
                data = pd.read_sql_query(f"SELECT * FROM {kwargs['table']}", self.conn)
        except Exception:
            if query == None:
                raise Exception("Query is None")
            else:
                self.conn.cursor().execute(query)
                data = None
        self.conn.commit()
        return data


        # print(arguments_not_provided, flush=True)
        # cur = self.conn.cursor()
        # if arguments_not_provided == 3:
        #     data = cur.execute(query)
        #     self.conn.commit()
        #     try:
        #         return data
        #     except:
        #         return "Success"
        # if arguments_not_provided == 2:
        #     data = pd.read_sql_query(f"SELECT {kwargs['column']} FROM {kwargs['table']}", self.conn)
        #     self.conn.commit()
        #     return data
        # if arguments_not_provided == 1:
        #     data = pd.read_sql_query(f"SELECT * FROM {kwargs['table']}", self.conn)
        #     self.conn.commit()
        #     return data
        # data = pd.read_sql_query(f"SELECT * FROM {kwargs['table']} WHERE {kwargs['column']} = {kwargs['value']}", self.conn)
        # self.conn.commit()
        # return data

    def to_table(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists="replace")
        self.conn.commit()

    def close(self):
        self.conn.close()

    # def __str__(self):
    #     fpath = self("PRAGMA database_list")["file"][0]
    #     db_name = Path(fpath).stem
    #     try:
    #         for table in self._get_tables()["name"].values:
    #             print(table)
    #     except Exception:
    #         print("No database found")
    #         return None
    #     return db_name

    # def __repr__(self):
    #     if f"DBInterface({self.__str__()}.db)":
    #         return f"DBInterface({self.__str__()}.db)"
    #     return f'DBInterface("No database found")'

    def _get_tables(self):
        return self("SELECT name FROM sqlite_master WHERE type='table';")


if __name__ == "__main__":
    def first_last_split(df, col, sep=' '):
        '''
        Split first and last name into two columns
            df: dataframe
            col: column to split
            sep: separator
        Returns dataframe
        '''
        drop_words = ["junior","de","dos","da","jr.","jr","júnior","júnior",None,"del","van","von",]
        df['FIRST_NAME'] = df[col].str.lower().apply(lambda x: [word for word in x.split(sep) if word not in drop_words][0])
        df['LAST_NAME'] = df[col].str.lower().apply(lambda x: [word for word in x.split(sep) if word not in drop_words][1:])
        return df

    db = DBInterface('UFCStatsGUI/database/ufc_raw')

    # db.conn.cursor().execute('create TABLE test(id integer, name text);')
    # db.conn.commit()
    # db.conn.close()

    df = db.Pdf('fighters')
    df
    df[df.duplicated('Fighter_Name', False)]
    dff = df['Fighter_Name'].str.split(' ', expand=True)[2].notnull()
    dfff = first_last_split(df[dff], 'Fighter_Name')
