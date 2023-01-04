import sqlite3
import scrapy
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
import logging

import app.database.util.sql_strings as sql
import configs as cfg
from scrapy.pipelines.images import ImagesPipeline
from UFCStatsScraper.items import FighterImageItem


class SQLPipeline:
    def check_if_table_exists(self, table_name):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = [t[0] for t in self.c.fetchall()]
        if table_name in table_names:
            return True
        else:
            return False

    def process_item(self, item, spider):
        if isinstance(item, FighterImageItem):
            return item
        column_count = len(item)
        table_name = spider.name
        _ = self.c.execute(
            f"""
            INSERT INTO {table_name} VALUES ({(column_count - 1) * "?, " + '?'})
            """,
            tuple(item.values()),
        )

        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()

    def open_spider(self, spider):

        table_name = spider.name
        sql_script = eval(f"sql.create_{table_name.upper()}_table_sql_string")

        self.conn = sqlite3.connect(cfg.DB_PATH / "ufc_raw.db")
        self.c = self.conn.cursor()

        self.c.executescript(sql_script)


class MyImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *arg, item):
        filename = self.format_filename(item["f_name"], item["f_nickname"], request)

        if isinstance(item, FighterImageItem):
            return filename

    def get_media_requests(self, item, info):
        if isinstance(item, FighterImageItem):
            for image_url in item["image_urls"]:
                yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        if not isinstance(item, FighterImageItem):
            return item
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        adapter = ItemAdapter(item)
        adapter["images"] = image_paths
        return item

    def format_filename(self, fighter_name, fighter_nickname, request):
        import hashlib

        fighter_name = fighter_name.replace(" ", "")
        fighter_nickname = fighter_nickname.replace('"', "").replace(" ", "")[6]
        if not fighter_nickname:
            fighter_nickname = ""
        fighter = fighter_name + fighter_nickname
        url = request.url
        folder = None
        if "upper_" in url:
            folder = "upper_body"
        elif "full_body" in url:
            folder = "full_body"
        elif "tease" in url:
            folder = "headshot"
        else:
            folder = "other"
        filename = hashlib.sha1(url.encode()).hexdigest()[10] + ".png"
        path = folder + "/" + fighter + "_" + filename

        return path


# class SQLitePipeline(object):
#     def __init__(self):
#         self.conn = sqlite3.connect("ufcstats.db")
#         self.c = self.conn.cursor()
#         self.c.executescript(sql.create_delete_FIGHTS_table_sql_string)
#         self.conn.commit()

#     def process_item(self, item, spider):
#         if len(item) == 38:
#             self.c.execute(
#                 """
#                 INSERT INTO fights VALUES (
#                     ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
#                     ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
#                     ?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
#                 (
#                     item["EventName"],
#                     item["Method"],
#                     item["Round"],
#                     item["Time"],
#                     item["TimeFormat"],
#                     item["Referee"],
#                     item["Judge1"],
#                     item["Judge1_Score"],
#                     item["Judge2"],
#                     item["Judge2_Score"],
#                     item["Judge3"],
#                     item["Judge3_Score"],
#                     item["Fighter1"],
#                     item["Fighter2"],
#                     item["Fighter1_KD"],
#                     item["Fighter2_KD"],
#                     item["Fighter1_SIG_STR"],
#                     item["Fighter2_SIG_STR"],
#                     item["Fighter1_SIG_STR_pct"],
#                     item["Fighter2_SIG_STR_pct"],
#                     item["Fighter1_TOTAL_STR"],
#                     item["Fighter2_TOTAL_STR"],
#                     item["Fighter1_TD"],
#                     item["Fighter2_TD"],
#                     item["Fighter1_TD_pct"],
#                     item["Fighter2_TD_pct"],
#                     item["Fighter1_SUB_ATT"],
#                     item["Fighter2_SUB_ATT"],
#                     item["Fighter1_REV"],
#                     item["Fighter2_REV"],
#                     item["Fighter1_CTRL"],
#                     item["Fighter2_CTRL"],
#                     item["Fighter1_HEAD"],
#                     item["Fighter2_HEAD"],
#                     item["Fighter1_BODY"],
#                     item["Fighter2_BODY"],
#                     item["Fighter1_LEG"],
#                     item["Fighter2_LEG"],
#                     item["Fighter1_DISTANCE"],
#                     item["Fighter2_DISTANCE"],
#                     item["Fighter1_CLINCH"],
#                     item["Fighter2_CLINCH"],
#                     item["Fighter1_GROUND"],
#                     item["Fighter2_GROUND"],
#                 ),
#             )
#         if len(item) == 16:
#             self.c.execute(
#                 "INSERT INTO fighters VALUES (?,?,?,?,?,?,?,\
#                                               ?,?,?,?,?,?,?,?,?)",
#                 (
#                     item["Fighter_Name"],
#                     item["Nickname"],
#                     item["Record"],
#                     item["Height"],
#                     item["Listed_Weight"],
#                     item["Reach"],
#                     item["Stance"],
#                     item["DoB"],
#                     item["SSLpM"],
#                     item["SSAcc"],
#                     item["SSApM"],
#                     item["SSDef"],
#                     item["TDavg"],
#                     item["TDAcc"],
#                     item["TDDef"],
#                     item["SubAvg"],
#                 ),
#             )
#         self.conn.commit()
#         return item

#     def close_spider(self, spider):
#         self.conn.close()
if __name__ == "__main__":
    # # "".join(["gregg", None])
    # all(["None", "gregg", [1, 2, 3, 4]])

    # rew = ["None", [1, 2, 3, 4]]
    # all([item is not None for item in rew])
    # new_dir = cfg.IMGS_PATH / "gregg"
    # new_dir.mkdir(parents=True, exist_ok=True)
    # class test:
    #     url = "https://google.com"

    # MyImagePipeline.format_filename(MyImagePipeline, "Gregg", "Bushy", request=test.url)
    # test.url
    pass
