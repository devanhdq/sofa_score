import json
from datetime import datetime

import scrapy
from ..items import TournamentItem
from ..my_functions import generate_dates
import logging


class TournamentsSpider(scrapy.Spider):
    name = "tournaments"
    allowed_domains = ["api.sofascore.com"]
    main_url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/"

    days = generate_dates(start_date=datetime(1990, 1, 1))

    urls = []

    for days in days:
        urls.append(f"{main_url}{days}")

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                dont_filter=True,
                meta={
                    "url": url
                }
            )

    def parse(self, response):
        json_response = json.loads(response.body)
        events = json_response.get("events", [])
        if len(events) != 0:
            for event in events:
                tournament_item = TournamentItem()
                tournament = event.get("tournament", {})
                tournament_item['tournament_name'] = tournament.get("name", None)
                tournament_item['tournament_category_name'] = tournament.get("category", {}).get("name", None)
                tournament_item['tournament_category_id'] = tournament.get("category", {}).get("id", None)
                tournament_item['tournament_unique_name'] = tournament.get("uniqueTournament", {}).get("name", None)
                tournament_has_statistics = tournament.get("uniqueTournament", {}).get(
                    "hasEventPlayerStatistics", None)

                tournament_item['tournament_has_statistics'] = tournament_has_statistics

                season = event.get("season", {})
                tournament_item['tournament_session_name'] = season.get("name", None)
                tournament_item['tournament_session_year'] = season.get("year", None)
                tournament_item['tournament_session_id'] = season.get("id", None)

                round_info = event.get("roundInfo", {})
                tournament_item['tournament_round'] = round_info.get("round", None)
                tournament_item['tournament_round_name'] = round_info.get("name", None)

                status = event.get("status", {})
                tournament_item['tournament_status_code'] = status.get("code", None)
                tournament_item['tournament_status_description'] = status.get("description", None)

                tournament_item['tournament_winner_code'] = event.get("winnerCode", None)

                home_team = event.get("homeTeam", {})
                tournament_item['tournament_home_team_name'] = home_team.get("name", None)
                tournament_item['tournament_home_team_country'] = home_team.get("country", {}).get("name", None)
                tournament_item['tournament_home_team_id'] = home_team.get("id", None)
                tournament_item['tournament_home_team_color_primary'] = home_team.get("teamColors", {}).get("primary",
                                                                                                            None)
                tournament_item['tournament_home_team_color_secondary'] = home_team.get("teamColors", {}).get(
                    "secondary", None)

                away_team = event.get("awayTeam", {})
                tournament_item['tournament_away_team_name'] = away_team.get("name", None)
                tournament_item['tournament_away_team_country'] = away_team.get("country", {}).get("name", None)
                tournament_item['tournament_away_team_id'] = away_team.get("id", None)
                tournament_item['tournament_away_team_color_primary'] = away_team.get("teamColors", {}).get("primary",
                                                                                                            None)
                tournament_item['tournament_away_team_color_secondary'] = away_team.get("teamColors", {}).get(
                    "secondary", None)

                home_score = event.get("homeScore", {})
                tournament_item['tournament_home_score'] = home_score.get("display", None)
                tournament_item['tournament_home_score_period_1'] = home_score.get("period1", None)
                tournament_item['tournament_home_score_period_2'] = home_score.get("period2", None)
                tournament_item['tournament_home_score_overtime'] = home_score.get("overtime", None)
                tournament_item['tournament_home_score_extra1'] = home_score.get("extra1", None)
                tournament_item['tournament_home_score_extra2'] = home_score.get("extra2", None)

                away_score = event.get("awayScore", {})
                tournament_item['tournament_away_score'] = away_score.get("display", None)
                tournament_item['tournament_away_score_period_1'] = away_score.get("period1", None)
                tournament_item['tournament_away_score_period_2'] = away_score.get("period2", None)
                tournament_item['tournament_away_score_overtime'] = away_score.get("overtime", None)
                tournament_item['tournament_home_score_extra1'] = away_score.get("extra1", None)
                tournament_item['tournament_home_score_extra2'] = away_score.get("extra2", None)

                time = event.get("time", {})
                tournament_item['tournament_time_1'] = time.get("injuryTime1", None)
                tournament_item['tournament_time_2'] = time.get("injuryTime2", None)
                tournament_item['tournament_time_3'] = time.get("injuryTime3", None)
                tournament_item['tournament_time_4'] = time.get("injuryTime4", None)

                tournament_item['tournament_has_global_highlights'] = event.get("hasGlobalHighlights", None)
                tournament_id = event.get("id", None)
                tournament_item['tournament_id'] = tournament_id
                tournament_item['tournament_start_timestamp'] = event.get("startTimestamp", None)

                yield tournament_item
