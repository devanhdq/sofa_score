import pymongo
from itemadapter import ItemAdapter
import mysql.connector


class MongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofa_score"
    mongo_collection = "tournaments"

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
    mysql_db = "sofascore"
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
    tournament_id                        INT,
    tournament_name                      VARCHAR(255),
    tournament_category_name             VARCHAR(255),
    tournament_category_id               INT,
    tournament_unique_name               VARCHAR(255),
    tournament_has_statistics            BOOLEAN,
    tournament_session_name              VARCHAR(255),
    tournament_session_year              VARCHAR(10),
    tournament_session_id                INT,
    tournament_round                     INT,
    tournament_round_name                VARCHAR(255),
    tournament_status_code               INT,
    tournament_status_description        VARCHAR(255),
    tournament_winner_code               INT,
    tournament_home_team_name            VARCHAR(255),
    tournament_home_team_country         VARCHAR(255),
    tournament_home_team_id              INT,
    tournament_home_team_color_primary   VARCHAR(7),
    tournament_home_team_color_secondary VARCHAR(7),
    tournament_away_team_name            VARCHAR(255),
    tournament_away_team_country         VARCHAR(255),
    tournament_away_team_id              INT,
    tournament_away_team_color_primary   VARCHAR(7),
    tournament_away_team_color_secondary VARCHAR(7),
    tournament_home_score                INT,
    tournament_home_score_period_1       INT,
    tournament_home_score_period_2       INT,
    tournament_home_score_overtime       INT,
    tournament_home_score_extra1         INT,
    tournament_home_score_extra2         INT,
    tournament_away_score                INT,
    tournament_away_score_period_1       INT,
    tournament_away_score_period_2       INT,
    tournament_away_score_overtime       INT,
    tournament_time_1                    INT,
    tournament_time_2                    INT,
    tournament_time_3                    INT,
    tournament_time_4                    INT,
    tournament_has_global_highlights     BOOLEAN,
    tournament_start_timestamp           INT,
    tournament_has_event_player_heat_map BOOLEAN
);        
""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """
            INSERT INTO tournaments
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            , (
                item.get('tournament_id'),
                item.get('tournament_name'),
                item.get('tournament_category_name'),
                item.get('tournament_category_id'),
                item.get('tournament_unique_name'),
                item.get('tournament_has_statistics'),
                item.get('tournament_session_name'),
                item.get('tournament_session_year'),
                item.get('tournament_session_id'),
                item.get('tournament_round'),
                item.get('tournament_round_name'),
                item.get('tournament_status_code'),
                item.get('tournament_status_description'),
                item.get('tournament_winner_code'),
                item.get('tournament_home_team_name'),
                item.get('tournament_home_team_country'),
                item.get('tournament_home_team_id'),
                item.get('tournament_home_team_color_primary'),
                item.get('tournament_home_team_color_secondary'),
                item.get('tournament_away_team_name'),
                item.get('tournament_away_team_country'),
                item.get('tournament_away_team_id'),
                item.get('tournament_away_team_color_primary'),
                item.get('tournament_away_team_color_secondary'),
                item.get('tournament_home_score'),
                item.get('tournament_home_score_period_1'),
                item.get('tournament_home_score_period_2'),
                item.get('tournament_home_score_overtime'),
                item.get('tournament_home_score_extra1'),
                item.get('tournament_home_score_extra2'),
                item.get('tournament_away_score'),
                item.get('tournament_away_score_period_1'),
                item.get('tournament_away_score_period_2'),
                item.get('tournament_away_score_overtime'),
                item.get('tournament_time_1'),
                item.get('tournament_time_2'),
                item.get('tournament_time_3'),
                item.get('tournament_time_4'),
                item.get('tournament_has_global_highlights'),
                item.get('tournament_start_timestamp'),
                item.get('tournament_has_event_player_heat_map')
            ))
        self.connection.commit()


class MySqlStatisticPipeline(object):
    mysql_host = "localhost"
    mysql_port = 3306
    mysql_db = "sofascore"
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
        self.cursor.execute("""DROP TABLE IF EXISTS statistics""")
        self.cursor.execute("""
 CREATE TABLE IF NOT EXISTS statistics
(
    tournament_id          INT,
    statistic_period       VARCHAR(255),
    statistic_group_name   VARCHAR(255),
    statistic_name         VARCHAR(255),
    statistic_home_value   DOUBLE,
    statistic_away_value   DOUBLE,
    statistic_type         VARCHAR(255),
    statistic_compare_code INT,
    url                    VARCHAR(255)
)
                            """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """
            INSERT INTO statistics(tournament_id, statistic_period, statistic_group_name,
                        statistic_name, statistic_home_value,
                       statistic_away_value, statistic_type, statistic_compare_code, url)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            , (
                item.get('tournament_id'),
                item.get('statistic_period'),
                item.get('statistic_group_name'),
                item.get('statistic_name'),
                item.get('statistic_home_value'),
                item.get('statistic_away_value'),
                item.get('statistic_type'),
                item.get('statistic_compare_code'),
                item.get('url')

            )
        )
        self.connection.commit()
