import pymongo
from itemadapter import ItemAdapter
import mysql.connector


class MongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofascore"
    mongo_collection = "tournaments-1718"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


class MySqlPipeline(object):
    mysql_host = "localhost"
    mysql_port = 3306
    mysql_db = "sofa_score"
    mysql_user = "root"
    mysql_password = "admin"

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = mysql.connector.connect(
            host=self.mysql_host,
            port=self.mysql_port,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_db
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS tournaments""")
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS tournaments
                    (
                        tournament_id               INT,
                        country                     VARCHAR(255),
                        name                        VARCHAR(255),
                        season                      VARCHAR(255),
                        year                        VARCHAR(255),
                        round                       VARCHAR(255),
                        status_code                 INT,
                        winner_code                 INT,
                        home_team                   VARCHAR(255),
                        away_team                   VARCHAR(255),
                        home_score                  INT,
                        home_period1                INT,
                        home_period2                INT,
                        away_score                  INT,
                        away_period1                INT,
                        away_period2                INT,
                        time_injury_time1           INT,
                        time_injury_time2           INT,
                        has_global_highlights       BOOLEAN,
                        has_event_player_statistics BOOLEAN,
                        has_event_player_heat_map   BOOLEAN,
                        start_timestamp             INT,
                        url                         VARCHAR(255)
                    );
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("""
        INSERT INTO tournaments 
        VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)
        """, (
            item.get("tournament_id"),
            item.get("name"),
            item.get("country"),
            item.get("season"),
            item.get("year"),
            item.get("round"),
            item.get("status_code"),
            item.get("winner_code"),
            item.get("home_team"),
            item.get("away_team"),
            item.get("home_score"),
            item.get("home_period1"),
            item.get("home_period2"),
            item.get("away_score"),
            item.get("away_period1"),
            item.get("away_period2"),
            item.get("time_injury_time1"),
            item.get("time_injury_time2"),
            item.get("has_global_highlights"),
            item.get("has_event_player_statistics"),
            item.get("has_event_player_heat_map"),
            item.get("start_timestamp"),
            item.get("url")

        ))
        self.connection.commit()
