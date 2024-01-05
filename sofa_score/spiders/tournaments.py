import json
from datetime import datetime

import scrapy
from ..items import TournamentItem
from ..my_functions import generate_dates


class TournamentsSpider(scrapy.Spider):
    name = "tournaments"
    allowed_domains = ["api.sofascore.com"]
    main_url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/"

    days = generate_dates(start_date=datetime(2022, 8, 1))

    urls = []

    for days in days:
        urls.append(f"{main_url}{days}")

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                dont_filter=True,
            )

    def parse(self, response):
        json_response = json.loads(response.body)
        item = TournamentItem()
        events = json_response.get("events", [])
        for event in events:
            item['id'] = event.get("id", None)

            tournament = event.get("tournament", {})
            category = tournament.get("category", {})
            item['category_name'] = category.get("name", None)
            item['category_id'] = category.get("id", None)
            item['category_flag'] = category.get("flag", None)
            item['category_alpha2'] = category.get("alpha2", None)

            unique_tournament = tournament.get("uniqueTournament", {})
            item['unique_id'] = unique_tournament.get("id", None)
            item['unique_name'] = unique_tournament.get("name", None)
            item['has_statistics'] = unique_tournament.get("hasEventPlayerStatistics", None)

            season = event.get("season", {})
            item['session_id'] = season.get("id", None)
            item['session_name'] = season.get("name", None)
            item['session_year'] = season.get("year", None)

            round_info = event.get("roundInfo", {})
            item['round'] = round_info.get("round", None)
            item['round_name'] = round_info.get("name", None)

            status = event.get("status", {})
            item['status_code'] = status.get("code", None)
            item['status_description'] = status.get("description", None)
            item['status_type'] = status.get("type", None)

            item['winner_code'] = event.get("winnerCode", None)

            home_team = event.get("homeTeam", {})
            item['home_team_name'] = home_team.get("name", None)
            item['home_team_short_name'] = home_team.get("shortName", None)
            item['home_team_country'] = home_team.get("country", {}).get("name", None)
            item['home_team_id'] = home_team.get("id", None)

            home_color = home_team.get("teamColors", {})
            item['home_team_color_primary'] = home_color.get("primary", None)
            item['home_team_color_secondary'] = home_color.get("secondary", None)

            away_team = event.get("awayTeam", {})
            item['away_team_id'] = away_team.get("id", None)
            item['away_team_name'] = away_team.get("name", None)
            item['away_team_short_name'] = away_team.get("name", None)
            item['away_team_country'] = away_team.get("country", {}).get("name", None)

            away_color = away_team.get("teamColors", {})
            item['away_team_color_primary'] = away_color.get("primary", None)
            item['away_team_color_secondary'] = away_color.get("secondary", None)

            home_score = event.get("homeScore", {})
            item['home_score'] = home_score.get("display", None)
            item['home_score_period_1'] = home_score.get("period1", None)
            item['home_score_period_2'] = home_score.get("period2", None)
            item['home_score_overtime'] = home_score.get("overtime", None)
            item['home_score_normal_time'] = home_score.get("normaltime", None)
            item['home_score_extra1'] = home_score.get("extra1", None)
            item['home_score_extra2'] = home_score.get("extra2", None)

            away_score = event.get("awayScore", {})
            item['away_score'] = away_score.get("display", None)
            item['away_score_period_1'] = away_score.get("period1", None)
            item['away_score_period_2'] = away_score.get("period2", None)
            item['away_score_overtime'] = away_score.get("overtime", None)
            item['away_score_normal_time'] = away_score.get("normaltime", None)
            item['away_score_extra1'] = away_score.get("extra1", None)
            item['away_score_extra2'] = away_score.get("extra2", None)

            time = event.get("time", {})
            item['time_1'] = time.get("injuryTime1", None)
            item['time_2'] = time.get("injuryTime2", None)
            item['time_3'] = time.get("injuryTime3", None)
            item['time_4'] = time.get("injuryTime4", None)
            item['current_period_start_timestamp'] = time.get("currentPeriodStartTimestamp", None)

            item['has_global_highlights'] = event.get("hasGlobalHighlights", None)
            item['start_timestamp'] = event.get("startTimestamp", None)
            item['url'] = response.url

            yield item
