import pymongo
from itemadapter import ItemAdapter
import mysql.connector


class TournamentMongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofascore_2023"
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


class IncidentMongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofascore_2023"
    mongo_collection = "incidents"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


class StatisticMongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofascore_2023"
    mongo_collection = "statistics"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


class BestPlayerMongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofascore_2023"
    mongo_collection = "best_players"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


class LineupsMongoDBPipeline(object):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db = "sofascore_2023"
    mongo_collection = "lineups"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


class TournamentsMySqlPipeline(object):
    mysql_host = "localhost"
    mysql_port = 3306
    mysql_db = "sofascore2023"
    mysql_user = "root"
    mysql_password = "admin"

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = mysql.connector.connect(
            host=self.mysql_host,
            port=self.mysql_port,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_db
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """
            INSERT INTO tournaments
            VALUES (
            %s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s
            )
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
                item.get('tournament_home_score_normal_time'),
                item.get('tournament_home_score_extra1'),
                item.get('tournament_home_score_extra2'),
                item.get('tournament_away_score'),
                item.get('tournament_away_score_period_1'),
                item.get('tournament_away_score_period_2'),
                item.get('tournament_away_score_overtime'),
                item.get('tournament_away_score_normal_time'),
                item.get('tournament_away_score_extra1'),
                item.get('tournament_away_score_extra2'),
                item.get('tournament_time_1'),
                item.get('tournament_time_2'),
                item.get('tournament_time_3'),
                item.get('tournament_time_4'),
                item.get('tournament_current_period_start_timestamp'),
                item.get('tournament_has_global_highlights'),
                item.get('tournament_start_timestamp'),
                item.get('url'),

            )
        )
        self.connection.commit()


class LineupsMySqlPipeline(object):
    mysql_host = "localhost"
    mysql_port = 3306
    mysql_db = "sofascore2023"
    mysql_user = "root"
    mysql_password = "admin"

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = mysql.connector.connect(
            host=self.mysql_host,
            port=self.mysql_port,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_db
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """
            INSERT INTO lineups
            VALUES (
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s
            )
            """
            , (
                item.get('tournament_id'),
                item.get('lineup_confirmed'),
                item.get('team'),
                item.get('player_id'),
                item.get('name'),
                item.get('short_name'),
                item.get('date_of_birth'),
                item.get('country'),
                item.get('user_count'),
                item.get('shirt_number'),
                item.get('position'),
                item.get('substitute'),
                item.get('total_pass'),
                item.get('accurate_pass'),
                item.get('total_long_balls'),
                item.get('error_lead_to_a_goal'),
                item.get('accurate_long_balls'),
                item.get('aerial_lost'),
                item.get('aerial_won'),
                item.get('interception_won'),
                item.get('fouls'),
                item.get('good_high_claim'),
                item.get('total_cross'),
                item.get('accurate_cross'),
                item.get('duel_lost'),
                item.get('duel_won'),
                item.get('challenge_lost'),
                item.get('total_contest'),
                item.get('won_contest'),
                item.get('big_chance_missed'),
                item.get('short_of_target'),
                item.get('blocked_scoring_attempt'),
                item.get('hit_woodwork'),
                item.get('total_clearance'),
                item.get('total_tackle'),
                item.get('was_fouled'),
                item.get('saved_shots_from_inside_the_box'),
                item.get('saves'),
                item.get('total_keeper_sweeper'),
                item.get('accurate_keeper_sweeper'),
                item.get('minutes_played'),
                item.get('touches'),
                item.get('expected_goals'),
                item.get('key_passes'),
                item.get('rating_version'),
                item.get('rating'),
                item.get('possession_lost_ctrl'),
                item.get('goals_prevented'),
                item.get('expected_assists'),
                item.get('big_chance_created'),
                item.get('url'),

            )
        )
        self.connection.commit()
