import scrapy


class TournamentItem(scrapy.Item):
    id = scrapy.Field()

    category_name = scrapy.Field()
    category_id = scrapy.Field()
    category_flag = scrapy.Field()
    category_alpha2 = scrapy.Field()

    unique_id = scrapy.Field()
    unique_name = scrapy.Field()
    has_statistics = scrapy.Field()

    session_id = scrapy.Field()
    session_name = scrapy.Field()
    session_year = scrapy.Field()

    round = scrapy.Field()
    round_name = scrapy.Field()

    status_code = scrapy.Field()
    status_description = scrapy.Field()
    status_type = scrapy.Field()

    winner_code = scrapy.Field()

    home_team_id = scrapy.Field()
    home_team_name = scrapy.Field()
    home_team_short_name = scrapy.Field()
    home_team_country = scrapy.Field()
    home_team_color_primary = scrapy.Field()
    home_team_color_secondary = scrapy.Field()

    away_team_name = scrapy.Field()
    away_team_short_name = scrapy.Field()
    away_team_country = scrapy.Field()
    away_team_id = scrapy.Field()
    away_team_color_primary = scrapy.Field()
    away_team_color_secondary = scrapy.Field()

    home_score = scrapy.Field()
    home_score_period_1 = scrapy.Field()
    home_score_period_2 = scrapy.Field()
    home_score_overtime = scrapy.Field()
    home_score_extra1 = scrapy.Field()
    home_score_extra2 = scrapy.Field()
    home_score_normal_time = scrapy.Field()

    away_score = scrapy.Field()
    away_score_period_1 = scrapy.Field()
    away_score_period_2 = scrapy.Field()
    away_score_overtime = scrapy.Field()
    away_score_extra1 = scrapy.Field()
    away_score_extra2 = scrapy.Field()
    away_score_normal_time = scrapy.Field()

    time_1 = scrapy.Field()
    time_2 = scrapy.Field()
    time_3 = scrapy.Field()
    time_4 = scrapy.Field()
    current_period_start_timestamp = scrapy.Field()

    has_global_highlights = scrapy.Field()
    start_timestamp = scrapy.Field()
    url = scrapy.Field()


class StatisticItem(scrapy.Item):
    url = scrapy.Field()
    tournament_id = scrapy.Field()

    period = scrapy.Field()
    group_name = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    home_value = scrapy.Field()
    away_value = scrapy.Field()
    compare_code = scrapy.Field()


class LineupItem(scrapy.Item):
    tournament_id = scrapy.Field()

    lineup_confirmed = scrapy.Field()

    team = scrapy.Field()

    name = scrapy.Field()
    short_name = scrapy.Field()
    position = scrapy.Field()
    user_count = scrapy.Field()
    player_id = scrapy.Field()
    country = scrapy.Field()
    marketValueCurrency = scrapy.Field()
    date_of_birth = scrapy.Field()

    shirt_number = scrapy.Field()
    substitute = scrapy.Field()

    # statistics
    total_pass = scrapy.Field()
    accurate_pass = scrapy.Field()

    total_long_balls = scrapy.Field()
    accurate_long_balls = scrapy.Field()

    aerial_won = scrapy.Field()
    duel_won = scrapy.Field()

    error_lead_to_a_goal = scrapy.Field()
    aerial_lost = scrapy.Field()
    interception_won = scrapy.Field()
    fouls = scrapy.Field()
    good_high_claim = scrapy.Field()
    total_cross = scrapy.Field()
    accurate_cross = scrapy.Field()
    duel_lost = scrapy.Field()
    challenge_lost = scrapy.Field()
    total_contest = scrapy.Field()
    won_contest = scrapy.Field()
    big_chance_missed = scrapy.Field()
    short_of_target = scrapy.Field()
    blocked_scoring_attempt = scrapy.Field()
    hit_woodwork = scrapy.Field()
    total_clearance = scrapy.Field()
    total_tackle = scrapy.Field()
    was_fouled = scrapy.Field()
    saved_shots_from_inside_the_box = scrapy.Field()
    saves = scrapy.Field()
    total_keeper_sweeper = scrapy.Field()
    accurate_keeper_sweeper = scrapy.Field()
    minutes_played = scrapy.Field()
    touches = scrapy.Field()
    expected_goals = scrapy.Field()
    key_passes = scrapy.Field()
    rating_version = scrapy.Field()
    rating = scrapy.Field()
    possession_lost_ctrl = scrapy.Field()
    goals_prevented = scrapy.Field()
    expected_assists = scrapy.Field()
    big_chance_created = scrapy.Field()
    url = scrapy.Field()


class BestPlayerItem(scrapy.Item):
    tournament_id = scrapy.Field()

    home_value = scrapy.Field()
    home_label = scrapy.Field()
    home_player_name = scrapy.Field()
    home_player_name_slug = scrapy.Field()
    home_player_short_name = scrapy.Field()
    home_player_position = scrapy.Field()
    home_player_user_count = scrapy.Field()
    home_player_id = scrapy.Field()
    home_player_market_value_currency = scrapy.Field()
    home_player_date_of_birth_timestamp = scrapy.Field()

    away_value = scrapy.Field()
    away_label = scrapy.Field()
    away_player_name = scrapy.Field()
    away_player_name_slug = scrapy.Field()
    away_player_short_name = scrapy.Field()
    away_player_position = scrapy.Field()
    away_player_user_count = scrapy.Field()
    away_player_id = scrapy.Field()
    away_player_market_value_currency = scrapy.Field()
    away_player_date_of_birth_timestamp = scrapy.Field()

    url = scrapy.Field()


class IncidentPeriodItem(scrapy.Item):
    tournament_id = scrapy.Field()

    incident_type = scrapy.Field()
    text = scrapy.Field()
    home_score = scrapy.Field()
    away_score = scrapy.Field()
    is_live = scrapy.Field()
    time = scrapy.Field()
    added_time = scrapy.Field()
    reversed_period_time = scrapy.Field()
    url = scrapy.Field()


class IncidentCardItem(scrapy.Item):
    tournament_id = scrapy.Field()

    incident_type = scrapy.Field()
    player_name = scrapy.Field()
    player_id = scrapy.Field()
    reason = scrapy.Field()
    is_home = scrapy.Field()
    incident_class = scrapy.Field()
    time = scrapy.Field()
    added_time = scrapy.Field()
    reversed_period_time = scrapy.Field()
    url = scrapy.Field()


class IncidentSubstitutionItem(scrapy.Item):
    tournament_id = scrapy.Field()

    incident_type = scrapy.Field()
    player_in = scrapy.Field()
    player_in_id = scrapy.Field()
    player_out = scrapy.Field()
    player_out_id = scrapy.Field()
    is_home = scrapy.Field()
    incident_class = scrapy.Field()
    time = scrapy.Field()
    reversed_period_time = scrapy.Field()
    url = scrapy.Field()


class IncidentGoalItem(scrapy.Item):
    tournament_id = scrapy.Field()

    incident_type = scrapy.Field()
    scorer = scrapy.Field()
    scorer_id = scrapy.Field()
    assist = scrapy.Field()
    assist_id = scrapy.Field()
    is_home = scrapy.Field()
    incident_class = scrapy.Field()
    time = scrapy.Field()
    reversed_period_time = scrapy.Field()
    url = scrapy.Field()


class IncidentInjuryTimeItem(scrapy.Item):
    tournament_id = scrapy.Field()

    incident_type = scrapy.Field()
    length = scrapy.Field()
    time = scrapy.Field()
    added_time = scrapy.Field()
    reversed_period_time = scrapy.Field()
    url = scrapy.Field()


class IncidentVarItem(scrapy.Item):
    tournament_id = scrapy.Field()

    incident_type = scrapy.Field()
    decision = scrapy.Field()
    time = scrapy.Field()
    player_id = scrapy.Field()
    player_name = scrapy.Field()
    reversed_period_time = scrapy.Field()
    is_home = scrapy.Field()
    url = scrapy.Field()
