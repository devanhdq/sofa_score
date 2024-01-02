import json

import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from ..my_functions import get_unique_tournaments
from ..items import LineupItem


class LineupsSpider(scrapy.Spider):
    name = "lineups"
    allowed_domains = ["api.sofascore.com"]
    tournaments_id = get_unique_tournaments("./tournaments.csv")

    # tournaments_id = [11352586]

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/lineups',
                callback=self.parse,
                dont_filter=True,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        json_response = json.loads(response.body)
        confirmed = json_response.get("confirmed", None)
        home = json_response.get("home", None)
        away = json_response.get("away", None)
        home_players = []
        away_players = []
        for player in home.get('players', []):
            home_players.append(self.parse_player(player))
        for player in away.get('players', []):
            away_players.append(self.parse_player(player))
        yield {
            "tournament_id": response.meta.get("tournament_id"),
            "confirmed": confirmed,
            "home_players": home_players,
            "away_players": away_players,
        }

    def parse_player(self, player):
        id_ = player.get("player", None).get("id", None)
        name = player.get("player", None).get("name", None)
        short_name = player.get("player", None).get("shortName", None)
        date_of_birth = player.get("player", None).get("dateOfBirthTimestamp", None)
        country = player.get("player", None).get("country", None).get("name", None)

        user_count = player.get("player", None).get("userCount", None)
        shirt_number = player.get("shirtNumber", None)
        position = player.get("player", None).get("position", None)
        substitute = player.get("substitute", None)

        statistics = player.get("statistics", {})
        total_pass = statistics.get("totalPass", None)
        accurate_pass = statistics.get("accuratePass", None)
        total_long_balls = statistics.get("totalLongBalls", None)
        error_lead_to_a_goal = statistics.get("errorLeadToAGoal", None)
        accurate_long_balls = statistics.get("accurateLongBalls", None)
        aerial_lost = statistics.get("aerialLost", None)
        aerial_won = statistics.get("aerialWon", None)
        interception_won = statistics.get("interceptionWon", None)
        fouls = statistics.get("fouls", None)
        good_high_claim = statistics.get("goodHighClaim", None)
        total_cross = statistics.get("totalCross", None)
        accurate_cross = statistics.get("accurateCross", None)

        duel_lost = statistics.get("duelLost", None)
        duel_won = statistics.get("duelWon", None)
        challenge_lost = statistics.get("challengeLost", None)

        total_contest = statistics.get("totalContest", None)
        won_contest = statistics.get("wonContest", None)
        big_chance_missed = statistics.get("bigChanceMissed", None)
        short_of_target = statistics.get("shotOffTarget", None)
        blocked_scoring_attempt = statistics.get("blockedScoringAttempt", None)

        hit_woodwork = statistics.get("hitWoodwork", None)
        total_clearance = statistics.get("totalClearance", None)
        total_tackle = statistics.get("totalTackle", None)
        was_fouled = statistics.get("wasFouled", None)
        saved_shots_from_inside_the_box = statistics.get("savedShotsFromInsideTheBox", None)

        saves = statistics.get("saves", None)
        total_keeper_sweeper = statistics.get("totalKeeperSweeper", None)
        accurate_keeper_sweeper = statistics.get("accurateKeeperSweeper", None)
        minutes_played = statistics.get("minutesPlayed", None)
        touches = statistics.get("touches", None)
        expected_goals = statistics.get("expectedGoals", None)
        key_passes = statistics.get("keyPasses", None)

        rating_version = statistics.get("ratingVersions", {}).get('original', None)

        rating = statistics.get("rating", None)
        possession_lost_ctrl = statistics.get("possessionLostCtrl", None)

        goals_prevented = statistics.get("goalsPrevented", None)
        expected_assists = statistics.get("expectedAssists", None)
        big_chance_created = statistics.get("bigChanceCreated", None)
        return {

            "id_": id_,
            "aerial_lost": aerial_lost,
            "aerial_won": aerial_won,
            "accurate_cross": accurate_cross,
            "accurate_keeper_sweeper": accurate_keeper_sweeper,
            "accurate_long_balls": accurate_long_balls,
            'accurate_pass': accurate_pass,
            "blocked_scoring_attempt": blocked_scoring_attempt,
            "big_chance_missed": big_chance_missed,
            "challenge_lost": challenge_lost,
            "big_chance_created": big_chance_created,
            "country": country,
            "date_of_birth": date_of_birth,
            "duel_lost": duel_lost,
            "duel_won": duel_won,
            "error_lead_to_a_goal": error_lead_to_a_goal,
            "expected_assists": expected_assists,
            "expected_goals": expected_goals,
            "fouls": fouls,
            "goals_prevented": goals_prevented,
            "good_high_claim": good_high_claim,
            "hit_woodwork": hit_woodwork,
            "interception_won": interception_won,
            "key_passes": key_passes,
            "minutes_played": minutes_played,
            "name": name,
            "possession_lost_ctrl": possession_lost_ctrl,
            "position": position,
            "rating": rating,
            "rating_version": rating_version,
            "saved_shots_from_inside_the_box": saved_shots_from_inside_the_box,
            "saves": saves,
            "shirt_number": shirt_number,
            "short_name": short_name,
            "short_of_target": short_of_target,
            "substitute": substitute,
            "total_clearance": total_clearance,
            "total_contest": total_contest,
            "total_cross": total_cross,
            "total_keeper_sweeper": total_keeper_sweeper,
            "total_long_balls": total_long_balls,
            "total_pass": total_pass,
            "total_tackle": total_tackle,
            "touches": touches,
            "user_count": user_count,
            "was_fouled": was_fouled,
            "won_contest": won_contest
        }

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
