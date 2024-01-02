import scrapy


class TournamentItem(scrapy.Item):
    tournament_name = scrapy.Field()

    tournament_category_name = scrapy.Field()
    tournament_category_id = scrapy.Field()

    tournament_unique_name = scrapy.Field()
    tournament_has_statistics = scrapy.Field()

    tournament_session_name = scrapy.Field()
    tournament_session_year = scrapy.Field()
    tournament_session_id = scrapy.Field()

    tournament_round = scrapy.Field()
    tournament_round_name = scrapy.Field()

    tournament_status_code = scrapy.Field()
    tournament_status_description = scrapy.Field()

    tournament_winner_code = scrapy.Field()

    tournament_home_team_name = scrapy.Field()
    tournament_home_team_country = scrapy.Field()
    tournament_home_team_id = scrapy.Field()
    tournament_home_team_color_primary = scrapy.Field()
    tournament_home_team_color_secondary = scrapy.Field()

    tournament_away_team_name = scrapy.Field()
    tournament_away_team_country = scrapy.Field()
    tournament_away_team_id = scrapy.Field()
    tournament_away_team_color_primary = scrapy.Field()
    tournament_away_team_color_secondary = scrapy.Field()

    tournament_home_score = scrapy.Field()
    tournament_home_score_period_1 = scrapy.Field()
    tournament_home_score_period_2 = scrapy.Field()
    tournament_home_score_overtime = scrapy.Field()
    tournament_home_score_extra1 = scrapy.Field()
    tournament_home_score_extra2 = scrapy.Field()

    tournament_away_score = scrapy.Field()
    tournament_away_score_period_1 = scrapy.Field()
    tournament_away_score_period_2 = scrapy.Field()
    tournament_away_score_overtime = scrapy.Field()
    tournament_away_score_extra1 = scrapy.Field()
    tournament_away_score_extra2 = scrapy.Field()

    tournament_time_1 = scrapy.Field()
    tournament_time_2 = scrapy.Field()
    tournament_time_3 = scrapy.Field()
    tournament_time_4 = scrapy.Field()

    tournament_has_global_highlights = scrapy.Field()
    tournament_id = scrapy.Field()
    tournament_start_timestamp = scrapy.Field()
    tournament_has_event_player_heat_map = scrapy.Field()


class StatisticItem(scrapy.Item):
    url = scrapy.Field()
    tournament_id = scrapy.Field()

    statistic_period = scrapy.Field()
    statistic_group_name = scrapy.Field()
    statistic_name = scrapy.Field()
    statistic_type = scrapy.Field()
    statistic_home_value = scrapy.Field()
    statistic_away_value = scrapy.Field()
    statistic_compare_code = scrapy.Field()


class LineupItem(scrapy.Item):
    lineup_confirmed = scrapy.Field()

    home_player_name = scrapy.Field()
    home_player_id = scrapy.Field()
    home_player_position = scrapy.Field()
    home_player_shirt_number = scrapy.Field()
    home_player_country = scrapy.Field()
    home_player_substitute = scrapy.Field()
    home_market_value_currency = scrapy.Field()
    home_date_of_birth_timestamp = scrapy.Field()
    home_formation = scrapy.Field()
    home_player_color = scrapy.Field()
    home_goal_keeper_color = scrapy.Field()

    away_player_name = scrapy.Field()
    away_player_id = scrapy.Field()
    away_player_position = scrapy.Field()
    away_player_shirt_number = scrapy.Field()
    away_player_country = scrapy.Field()
    away_player_substitute = scrapy.Field()
    away_market_value_currency = scrapy.Field()
    away_date_of_birth_timestamp = scrapy.Field()
    away_formation = scrapy.Field()
    away_player_color = scrapy.Field()
    away_goal_keeper_color = scrapy.Field()
