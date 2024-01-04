import json

import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from ..my_functions import get_unique_tournaments
from ..items import LineupItem


class LineupsSpider(scrapy.Spider):
    name = "lineups"
    allowed_domains = ["api.sofascore.com"]
    tournaments_id = get_unique_tournaments("./tournaments2023.csv")

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

        home_team = json_response.get('home', {})
        home_players = home_team.get('players', [])

        for player in home_players:
            yield self.parse_player(player, confirmed, team="home", url=response.url,
                                    tournament_id=response.meta.get("tournament_id"))

        away_team = json_response.get('away', {})
        away_players = away_team.get('players', [])
        for player in away_players:
            yield self.parse_player(player, confirmed, team="away", url=response.url,
                                    tournament_id=response.meta.get("tournament_id"))

    def parse_player(self, player, confirm, team, url, tournament_id):
        lineup_item = LineupItem()
        lineup_item['tournament_id'] = tournament_id

        lineup_item['lineup_confirmed'] = confirm

        lineup_item['team'] = team

        lineup_item['name'] = player.get("player", None).get("name", None)
        lineup_item['short_name'] = player.get("player", None).get("shortName", None)
        lineup_item['position'] = player.get("player", None).get("position", None)
        lineup_item['user_count'] = player.get("player", None).get("userCount", None)
        lineup_item['player_id'] = player.get("player", None).get("id", None)
        lineup_item['country'] = player.get("player", None).get("country", None).get("name", None)
        lineup_item['date_of_birth'] = player.get("player", None).get("dateOfBirthTimestamp", None)
        lineup_item['marketValueCurrency'] = player.get("player", None).get("marketValueCurrency", None)

        lineup_item['substitute'] = player.get("substitute", None)
        lineup_item['shirt_number'] = player.get("shirtNumber", None)

        statistics = player.get("statistics", {})
        lineup_item['total_pass'] = statistics.get("totalPass", None)
        lineup_item['accurate_pass'] = statistics.get("accuratePass", None)

        lineup_item['total_long_balls'] = statistics.get("totalLongBalls", None)
        lineup_item['accurate_long_balls'] = statistics.get("accurateLongBalls", None)

        lineup_item['aerial_lost'] = statistics.get("aerialLost", None)
        lineup_item['aerial_won'] = statistics.get("aerialWon", None)

        lineup_item['error_lead_to_a_goal'] = statistics.get("errorLeadToAGoal", None)
        lineup_item['interception_won'] = statistics.get("interceptionWon", None)
        lineup_item['fouls'] = statistics.get("fouls", None)
        lineup_item['good_high_claim'] = statistics.get("goodHighClaim", None)
        lineup_item['total_cross'] = statistics.get("totalCross", None)
        lineup_item['accurate_cross'] = statistics.get("accurateCross", None)

        lineup_item['duel_lost'] = statistics.get("duelLost", None)
        lineup_item['duel_won'] = statistics.get("duelWon", None)
        lineup_item['challenge_lost'] = statistics.get("challengeLost", None)

        lineup_item['total_contest'] = statistics.get("totalContest", None)
        lineup_item['won_contest'] = statistics.get("wonContest", None)
        lineup_item['big_chance_missed'] = statistics.get("bigChanceMissed", None)
        lineup_item['short_of_target'] = statistics.get("shotOffTarget", None)
        lineup_item['blocked_scoring_attempt'] = statistics.get("blockedScoringAttempt", None)

        lineup_item['hit_woodwork'] = statistics.get("hitWoodwork", None)
        lineup_item['total_clearance'] = statistics.get("totalClearance", None)
        lineup_item['total_tackle'] = statistics.get("totalTackle", None)
        lineup_item['was_fouled'] = statistics.get("wasFouled", None)
        lineup_item['saved_shots_from_inside_the_box'] = statistics.get("savedShotsFromInsideTheBox", None)

        lineup_item['saves'] = statistics.get("saves", None)
        lineup_item['total_keeper_sweeper'] = statistics.get("totalKeeperSweeper", None)
        lineup_item['accurate_keeper_sweeper'] = statistics.get("accurateKeeperSweeper", None)
        lineup_item['minutes_played'] = statistics.get("minutesPlayed", None)
        lineup_item['touches'] = statistics.get("touches", None)
        lineup_item['expected_goals'] = statistics.get("expectedGoals", None)
        lineup_item['key_passes'] = statistics.get("keyPasses", None)

        lineup_item['rating_version'] = statistics.get("ratingVersions", {}).get('original', None)

        lineup_item['rating'] = statistics.get("rating", None)
        lineup_item['possession_lost_ctrl'] = statistics.get("possessionLostCtrl", None)

        lineup_item['goals_prevented'] = statistics.get("goalsPrevented", None)
        lineup_item['expected_assists'] = statistics.get("expectedAssists", None)
        lineup_item['big_chance_created'] = statistics.get("bigChanceCreated", None)
        lineup_item['url'] = url
        return lineup_item

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
