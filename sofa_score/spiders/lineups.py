import scrapy
from ..items import LineupItem


class LineupsSpider(scrapy.Spider):
    name = "lineups"
    allowed_domains = ["api.sofascore.com"]
    tournament_id = [11753978]

    def start_requests(self):
        for tournament_id in self.tournament_id:
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
            "id": response.meta.get("id"),
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
        total_bong_balls = statistics.get("totalLongBalls", None)
        accurate_long_balls = statistics.get("accurateLongBalls", None)

        duel_lost = statistics.get("duelLost", None)
        duel_won = statistics.get("duelWon", None)

        challenge_lost = statistics.get("challengeLost", None)
        big_chance_missed = statistics.get("bigChanceMissed", None)
        short_of_target = statistics.get("shotOffTarget", None)
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

        rating = statistics.get("ratingVersions", {}).get('original', None)

        rating = statistics.get("rating", None)
        possession_lost_ctrl = statistics.get("possessionLostCtrl", None)

        goals_prevented = statistics.get("goalsPrevented", None)
        return {
            "player_id": player_id,
            "player_name": player_name,
            "player_short_name": player_short_name,
            "player_user_count": player_user_count,
            "player_country": player_country,

            "date_of_birth": date_of_birth,
            "shirt_number": shirt_number,
            "player_position": player_position,
            "total_pass": total_pass,
            "accurate_pass": accurate_pass,
            "total_bong_balls": total_bong_balls,
            "accurate_long_balls": accurate_long_balls,
            "duel_lost": duel_lost,
            "challenge_lost": challenge_lost,
            "saved_shots_from_inside_the_box": saved_shots_from_inside_the_box,
            "saves": saves,
            "total_keeper_sweeper": total_keeper_sweeper,
            "accurate_keeper_sweeper": accurate_keeper_sweeper,
            "minutes_played": minutes_played,
            "touches": touches,
            "rating": rating,
            "possession_lost_ctrl": possession_lost_ctrl,
            "goals_prevented": goals_prevented,
        }

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
            yield {
                "id": response.meta.get("id"),
                "confirmed": None,
                "home_players": None,
                "away_players": None
            }
