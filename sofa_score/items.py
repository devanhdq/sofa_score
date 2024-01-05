import scrapy


def null_value(value):
    if value:
        return value
    else:
        return -1


class TournamentItem(scrapy.Item):
    id = scrapy.Field(serializer=null_value)

    category_name = scrapy.Field(serializer=null_value)
    category_id = scrapy.Field(serializer=null_value)
    category_flag = scrapy.Field(serializer=null_value)
    category_alpha2 = scrapy.Field(serializer=null_value)

    unique_id = scrapy.Field(serializer=null_value)
    unique_name = scrapy.Field(serializer=null_value)
    has_statistics = scrapy.Field(serializer=null_value)

    session_id = scrapy.Field(serializer=null_value)
    session_name = scrapy.Field(serializer=null_value)
    session_year = scrapy.Field(serializer=null_value)

    round = scrapy.Field(serializer=null_value)
    round_name = scrapy.Field(serializer=null_value)

    status_code = scrapy.Field(serializer=null_value)
    status_description = scrapy.Field(serializer=null_value)
    status_type = scrapy.Field(serializer=null_value)

    winner_code = scrapy.Field(serializer=null_value)

    home_team_id = scrapy.Field(serializer=null_value)
    home_team_name = scrapy.Field(serializer=null_value)
    home_team_short_name = scrapy.Field(serializer=null_value)
    home_team_country = scrapy.Field(serializer=null_value)
    home_team_color_primary = scrapy.Field(serializer=null_value)
    home_team_color_secondary = scrapy.Field(serializer=null_value)

    away_team_name = scrapy.Field(serializer=null_value)
    away_team_short_name = scrapy.Field(serializer=null_value)
    away_team_country = scrapy.Field(serializer=null_value)
    away_team_id = scrapy.Field(serializer=null_value)
    away_team_color_primary = scrapy.Field(serializer=null_value)
    away_team_color_secondary = scrapy.Field(serializer=null_value)

    home_score = scrapy.Field(serializer=null_value)
    home_score_period_1 = scrapy.Field(serializer=null_value)
    home_score_period_2 = scrapy.Field(serializer=null_value)
    home_score_overtime = scrapy.Field(serializer=null_value)
    home_score_extra1 = scrapy.Field(serializer=null_value)
    home_score_extra2 = scrapy.Field(serializer=null_value)
    home_score_normal_time = scrapy.Field(serializer=null_value)

    away_score = scrapy.Field(serializer=null_value)
    away_score_period_1 = scrapy.Field(serializer=null_value)
    away_score_period_2 = scrapy.Field(serializer=null_value)
    away_score_overtime = scrapy.Field(serializer=null_value)
    away_score_extra1 = scrapy.Field(serializer=null_value)
    away_score_extra2 = scrapy.Field(serializer=null_value)
    away_score_normal_time = scrapy.Field(serializer=null_value)

    time_1 = scrapy.Field(serializer=null_value)
    time_2 = scrapy.Field(serializer=null_value)
    time_3 = scrapy.Field(serializer=null_value)
    time_4 = scrapy.Field(serializer=null_value)
    current_period_start_timestamp = scrapy.Field(serializer=null_value)

    has_global_highlights = scrapy.Field(serializer=null_value)
    start_timestamp = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class StatisticItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    period = scrapy.Field(serializer=null_value)
    group_name = scrapy.Field(serializer=null_value)
    name = scrapy.Field(serializer=null_value)
    type = scrapy.Field(serializer=null_value)
    home_value = scrapy.Field(serializer=null_value)
    away_value = scrapy.Field(serializer=null_value)
    compare_code = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class LineupItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    lineup_confirmed = scrapy.Field(serializer=null_value)

    team = scrapy.Field(serializer=null_value)

    name = scrapy.Field(serializer=null_value)
    short_name = scrapy.Field(serializer=null_value)
    position = scrapy.Field(serializer=null_value)
    user_count = scrapy.Field(serializer=null_value)
    player_id = scrapy.Field(serializer=null_value)
    country = scrapy.Field(serializer=null_value)
    marketValueCurrency = scrapy.Field(serializer=null_value)
    date_of_birth = scrapy.Field(serializer=null_value)

    shirt_number = scrapy.Field(serializer=null_value)
    substitute = scrapy.Field(serializer=null_value)

    # statistics
    total_pass = scrapy.Field(serializer=null_value)
    accurate_pass = scrapy.Field(serializer=null_value)

    total_long_balls = scrapy.Field(serializer=null_value)
    accurate_long_balls = scrapy.Field(serializer=null_value)

    aerial_won = scrapy.Field(serializer=null_value)
    duel_won = scrapy.Field(serializer=null_value)
    dispossessed = scrapy.Field(serializer=null_value)

    error_lead_to_a_goal = scrapy.Field(serializer=null_value)
    aerial_lost = scrapy.Field(serializer=null_value)
    interception_won = scrapy.Field(serializer=null_value)
    fouls = scrapy.Field(serializer=null_value)
    good_high_claim = scrapy.Field(serializer=null_value)
    total_cross = scrapy.Field(serializer=null_value)
    accurate_cross = scrapy.Field(serializer=null_value)
    duel_lost = scrapy.Field(serializer=null_value)
    challenge_lost = scrapy.Field(serializer=null_value)
    total_contest = scrapy.Field(serializer=null_value)
    won_contest = scrapy.Field(serializer=null_value)
    big_chance_missed = scrapy.Field(serializer=null_value)
    short_of_target = scrapy.Field(serializer=null_value)
    blocked_scoring_attempt = scrapy.Field(serializer=null_value)
    hit_woodwork = scrapy.Field(serializer=null_value)
    total_clearance = scrapy.Field(serializer=null_value)
    total_tackle = scrapy.Field(serializer=null_value)
    was_fouled = scrapy.Field(serializer=null_value)
    saved_shots_from_inside_the_box = scrapy.Field(serializer=null_value)
    saves = scrapy.Field(serializer=null_value)
    total_keeper_sweeper = scrapy.Field(serializer=null_value)
    accurate_keeper_sweeper = scrapy.Field(serializer=null_value)
    minutes_played = scrapy.Field(serializer=null_value)
    touches = scrapy.Field(serializer=null_value)
    expected_goals = scrapy.Field(serializer=null_value)
    key_passes = scrapy.Field(serializer=null_value)
    rating_version = scrapy.Field(serializer=null_value)
    rating = scrapy.Field(serializer=null_value)
    possession_lost_ctrl = scrapy.Field(serializer=null_value)
    goals_prevented = scrapy.Field(serializer=null_value)
    expected_assists = scrapy.Field(serializer=null_value)
    big_chance_created = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class BestPlayerItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    home_value = scrapy.Field(serializer=null_value)
    home_label = scrapy.Field(serializer=null_value)
    home_player_name = scrapy.Field(serializer=null_value)
    home_player_name_slug = scrapy.Field(serializer=null_value)
    home_player_short_name = scrapy.Field(serializer=null_value)
    home_player_position = scrapy.Field(serializer=null_value)
    home_player_user_count = scrapy.Field(serializer=null_value)
    home_player_id = scrapy.Field(serializer=null_value)
    home_player_market_value_currency = scrapy.Field(serializer=null_value)
    home_player_date_of_birth_timestamp = scrapy.Field(serializer=null_value)

    away_value = scrapy.Field(serializer=null_value)
    away_label = scrapy.Field(serializer=null_value)
    away_player_name = scrapy.Field(serializer=null_value)
    away_player_name_slug = scrapy.Field(serializer=null_value)
    away_player_short_name = scrapy.Field(serializer=null_value)
    away_player_position = scrapy.Field(serializer=null_value)
    away_player_user_count = scrapy.Field(serializer=null_value)
    away_player_id = scrapy.Field(serializer=null_value)
    away_player_market_value_currency = scrapy.Field(serializer=null_value)
    away_player_date_of_birth_timestamp = scrapy.Field(serializer=null_value)

    url = scrapy.Field(serializer=null_value)


class IncidentPeriodItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    incident_type = scrapy.Field(serializer=null_value)
    text = scrapy.Field(serializer=null_value)
    home_score = scrapy.Field(serializer=null_value)
    away_score = scrapy.Field(serializer=null_value)
    is_live = scrapy.Field(serializer=null_value)
    time = scrapy.Field(serializer=null_value)
    added_time = scrapy.Field(serializer=null_value)
    reversed_period_time = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class IncidentCardItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    incident_type = scrapy.Field(serializer=null_value)
    player_name = scrapy.Field(serializer=null_value)
    player_id = scrapy.Field(serializer=null_value)
    reason = scrapy.Field(serializer=null_value)
    is_home = scrapy.Field(serializer=null_value)
    incident_class = scrapy.Field(serializer=null_value)
    time = scrapy.Field(serializer=null_value)
    reversed_period_time = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class IncidentSubstitutionItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    incident_type = scrapy.Field(serializer=null_value)
    player_in = scrapy.Field(serializer=null_value)
    player_in_id = scrapy.Field(serializer=null_value)
    player_out = scrapy.Field(serializer=null_value)
    player_out_id = scrapy.Field(serializer=null_value)
    is_home = scrapy.Field(serializer=null_value)
    incident_class = scrapy.Field(serializer=null_value)
    time = scrapy.Field(serializer=null_value)
    reversed_period_time = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class IncidentGoalItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    incident_type = scrapy.Field(serializer=null_value)
    scorer = scrapy.Field(serializer=null_value)
    scorer_id = scrapy.Field(serializer=null_value)
    assist = scrapy.Field(serializer=null_value)
    assist_id = scrapy.Field(serializer=null_value)
    is_home = scrapy.Field(serializer=null_value)
    incident_class = scrapy.Field(serializer=null_value)
    time = scrapy.Field(serializer=null_value)
    reversed_period_time = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class IncidentInjuryTimeItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    incident_type = scrapy.Field(serializer=null_value)
    length = scrapy.Field(serializer=null_value)
    time = scrapy.Field(serializer=null_value)
    added_time = scrapy.Field(serializer=null_value)
    reversed_period_time = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class IncidentVarItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    incident_type = scrapy.Field(serializer=null_value)
    decision = scrapy.Field(serializer=null_value)
    time = scrapy.Field(serializer=null_value)
    player_id = scrapy.Field(serializer=null_value)
    player_name = scrapy.Field(serializer=null_value)
    reversed_period_time = scrapy.Field(serializer=null_value)
    is_home = scrapy.Field(serializer=null_value)
    url = scrapy.Field(serializer=null_value)


class HighlightItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)
    id = scrapy.Field(serializer=null_value)

    title = scrapy.Field(serializer=null_value)
    subtitle = scrapy.Field(serializer=null_value)
    highlight_url = scrapy.Field(serializer=null_value)
    highlight_thumbnail_url = scrapy.Field(serializer=null_value)

    media_type = scrapy.Field(serializer=null_value)
    do_follow = scrapy.Field(serializer=null_value)
    key_highlight = scrapy.Field(serializer=null_value)
    created_at_timestamp = scrapy.Field(serializer=null_value)
    source_url = scrapy.Field(serializer=null_value)


class ManagerItem(scrapy.Item):
    tournament_id = scrapy.Field(serializer=null_value)

    home_manager_id = scrapy.Field(serializer=null_value)
    home_manager_name = scrapy.Field(serializer=null_value)
    home_manager_short_name = scrapy.Field(serializer=null_value)
    home_manager_slug = scrapy.Field(serializer=null_value)

    away_manager_id = scrapy.Field(serializer=null_value)
    away_manager_name = scrapy.Field(serializer=null_value)
    away_manager_short_name = scrapy.Field(serializer=null_value)
    away_manager_slug = scrapy.Field(serializer=null_value)
