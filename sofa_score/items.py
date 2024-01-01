# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TournamentItem(scrapy.Item):
    _id = scrapy.Field()
    tournament_id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    season = scrapy.Field()
    year = scrapy.Field()
    unique_tournament_name = scrapy.Field()
    unique_tournament_category = scrapy.Field()
    unique_tournament_id = scrapy.Field()
    round = scrapy.Field()
    status_code = scrapy.Field()
    winner_code = scrapy.Field()
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    home_score = scrapy.Field()
    home_period1 = scrapy.Field()
    home_period2 = scrapy.Field()
    away_score = scrapy.Field()
    away_period1 = scrapy.Field()
    away_period2 = scrapy.Field()
    time_injury_time1 = scrapy.Field()
    time_injury_time2 = scrapy.Field()
    has_global_highlights = scrapy.Field()
    has_event_player_statistics = scrapy.Field()
    has_event_player_heat_map = scrapy.Field()
    start_timestamp = scrapy.Field()
    statistic_period = scrapy.Field()
    statistic_group = scrapy.Field()
    statistic_name = scrapy.Field()
    statistic_type = scrapy.Field()
    statistic_home_value = scrapy.Field()
    statistic_away_value = scrapy.Field()
    statistic_compare_code = scrapy.Field()


class StatisticItem(scrapy.Item):
    period_name = scrapy.Field(),
    # group_name = scrapy.Field(),
    # name = scrapy.Field(),
    # home = scrapy.Field(),
    # away = scrapy.Field(),
    # compare_code = scrapy.Field(),
    # statistics_type = scrapy.Field(),
    # value_type = scrapy.Field(),
