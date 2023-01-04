import pandas as pd
import sqlite3
from pathlib import Path


class DBInterface(object):
    f = "__file__" if __name__ == "__main__" else __name__

    def __init__(self, db):
        db_path = Path(__file__).parent.parent / f"{db}.db"
        self.conn = sqlite3.connect(db_path)

    def Pdf(self, table_name):
        return pd.read_sql(f"SELECT * FROM {table_name}", self.conn)

    def query(self, query):
        query_result = pd.read_sql_query(query, self.conn)
        return query_result

    def to_table(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists="replace")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __str__(self):
        fpath = self.query("PRAGMA database_list")["file"][0]
        db_name = Path(fpath).stem
        # print("Tables:")
        for table in self._get_tables()["name"].values:
            print(table)
        return db_name

    def __repr__(self):
        return f"DBInterface({self.__str__()}.db)"

    def __call__(self, query):
        return self.query(query)

    def _get_tables(self):
        return self.query("SELECT name FROM sqlite_master WHERE type='table';")


if __name__ == "__main__":
    db = DBInterface()
    db("select * from fights limit 10")
    db
    sqlite3.connect("app/database/ufcstats.db")
