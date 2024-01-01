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

    # days = generate_dates(start_date=datetime(2023, 12, 31))

    urls = ["https://api.sofascore.com/api/v1/sport/football/scheduled-events/2000-06-14"]

    # urls = ["https://api.sofascore.com/api/v1/sport/football/scheduled-events/2000-06-23"]

    #
    # for days in days:
    #     urls.append(f"{main_url}{days}")

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
        tournament_item = TournamentItem()

        events = json_response.get("events")
        if len(events) != 0:
            for event in events:
                tournament_item['tournament_id'] = event.get("id", None)
                tournament_item['country'] = (
                    event.get("tournament", {}).get("category", {}).get("name", None)
                )
                tournament_item['name'] = event.get("tournament", {}).get("name", None)
                tournament_item['season'] = event.get("season", {}).get("name", None)

                tournament_item['year'] = event.get("season", {}).get("year", None)
                tournament_item['round'] = event.get("roundInfo", {}).get("round", None)
                tournament_item['status_code'] = event.get("status", {}).get("code", None)
                tournament_item['winner_code'] = event.get("winnerCode", None)
                tournament_item['home_team'] = event.get("homeTeam", {}).get("name", None)
                tournament_item['away_team'] = event.get("awayTeam", {}).get("name", None)
                tournament_item['home_score'] = event.get("homeScore", {}).get("current", None)
                tournament_item['home_period1'] = event.get("homeScore", {}).get("period1", None)
                tournament_item['home_period2'] = event.get("homeScore", {}).get("period2", None)
                tournament_item['away_score'] = event.get("awayScore", {}).get("current", None)
                tournament_item['away_period1'] = event.get("awayScore", {}).get("period1", None)
                tournament_item['away_period2'] = event.get("awayScore", {}).get("period2", None)
                tournament_item['time_injury_time1'] = event.get("time", {}).get("injuryTime1", None)
                tournament_item['time_injury_time2'] = event.get("time", {}).get("injuryTime2", None)
                tournament_item['has_global_highlights'] = event.get("hasGlobalHighlights", None)
                tournament_item['has_event_player_statistics'] = event.get("hasEventPlayerStatistics", None)
                tournament_item['has_event_player_heat_map'] = event.get("hasEventPlayerHeatMap", None)
                tournament_item['start_timestamp'] = event.get("startTimestamp", None)
                tournament_item['url'] = response.meta.get("url")
                yield tournament_item

#     for event in events:
#         tournament_item['tournament_id'] = event.get("id", None)
#         tournament_item['country'] = (
#             event.get("tournament", {}).get("category", {}).get("name", None)
#         )
#         tournament_item['name'] = event.get("tournament", {}).get("name", None)
#         tournament_item['season'] = event.get("season", {}).get("name", None)
#         tournament_item['year'] = event.get("season", {}).get("year", None)
#         tournament_item['round'] = event.get("roundInfo", {}).get("round", None)
#         tournament_item['status_code'] = event.get("status", {}).get("code", None)
#         tournament_item['winner_code'] = event.get("winnerCode", None)
#         tournament_item['home_team'] = event.get("homeTeam", {}).get("name", None)
#         tournament_item['away_team'] = event.get("awayTeam", {}).get("name", None)
#         tournament_item['home_score'] = event.get("homeScore", {}).get("current", None)
#         tournament_item['home_period1'] = event.get("homeScore", {}).get("period1", None)
#         tournament_item['home_period2'] = event.get("homeScore", {}).get("period2", None)
#         tournament_item['away_score'] = event.get("awayScore", {}).get("current", None)
#         tournament_item['away_period1'] = event.get("awayScore", {}).get("period1", None)
#         tournament_item['away_period2'] = event.get("awayScore", {}).get("period2", None)
#         tournament_item['time_injury_time1'] = event.get("time", {}).get("injuryTime1", None)
#         tournament_item['time_injury_time2'] = event.get("time", {}).get("injuryTime2", None)
#         tournament_item['has_global_highlights'] = event.get("hasGlobalHighlights", None)
#         tournament_item['has_event_player_statistics'] = event.get("hasEventPlayerStatistics", None)
#         tournament_item['has_event_player_heat_map'] = event.get("hasEventPlayerHeatMap", None)
#         tournament_item['start_timestamp'] = event.get("startTimestamp", None)
#         tournament_item['url'] = response.meta.get("url")
#
#         if tournament_item['has_event_player_statistics']:
#             logging.info("True**********")
#             yield scrapy.Request(
#                 url=f"https://api.sofascore.com/api/v1/event/{tournament_item['tournament_id']}/statistics",
#                 callback=self.parse_statistics,
#                 # errback=self.errback_httpbin_statistics,
#                 meta={
#                     "tournament_item": tournament_item,
#                 }
#             )
#         else:
#             tournament_item['statistic_period'] = None
#             tournament_item['statistic_group'] = None
#             tournament_item['statistic_name'] = None
#             tournament_item['statistic_type'] = None
#             tournament_item['statistic_home_value'] = None
#             tournament_item['statistic_away_value'] = None
#             tournament_item['statistic_compare_code'] = None
#             yield tournament_item
#
# def parse_statistics(self, response):
#     json_response = json.loads(response.body)
#     statistics = json_response.get("statistics", [])
#     tournament_item = response.meta.get("tournament_item")
#     for statistic in statistics:
#         period = statistic.get("period", None)
#         for group in statistic.get("groups", []):
#             statistic_name = group.get("groupName", None)
#             for statistic_item in group.get("statisticsItems", []):
#                 tournament_item["statistic_period"]: period
#                 tournament_item["statistic_group"]: statistic_name
#                 tournament_item["statistic_name"]: statistic_item.get("name", None)
#                 tournament_item["statistic_type"]: statistic_item.get("statisticsType", None)
#                 tournament_item["statistic_home_value"]: statistic_item.get("homeValue", None)
#                 tournament_item["statistic_away_value"]: statistic_item.get("awayValue", None)
#                 tournament_item["statistic_compare_code"]: statistic_item.get("compareCode", None)
#             yield tournament_item

# def errback_httpbin_statistics(self, failure):
#     if failure.check(HttpError):
#         yield {
#             "tournament_id": response.meta.get("tournament_item"),
#             "period": None,
#             "group_name": None,
#             "statistic": None,
#             "statistic_home_value": None,
#             "statistic_away_value": None,
#             "statistic_compare_code": None,
#
#         }

# "tournament_id": tournament_item.get("tournament_id"),
# "name": tournament_item.get("name"),
# "country": tournament_item.get("country"),
# "season": tournament_item.get("season"),
# "year": tournament_item.get("year"),
# "round": tournament_item.get("round"),
# "status_code": tournament_item.get("status_code"),
# "winner_code": tournament_item.get("winner_code"),
# "home_team": tournament_item.get("home_team"),
# "away_team": tournament_item.get("away_team"),
# "home_score": tournament_item.get("home_score"),
# "home_period1": tournament_item.get("home_period1"),
# "home_period2": tournament_item.get("home_period2"),
# "away_score": tournament_item.get("away_score"),
# "away_period1": tournament_item.get("away_period1"),
# "away_period2": tournament_item.get("away_period2"),
# "time_injury_time1": tournament_item.get("time_injury_time1"),
# "time_injury_time2": tournament_item.get("time_injury_time2"),
# "has_global_highlights": tournament_item.get("has_global_highlights"),
# "has_event_player_statistics": tournament_item.get("has_event_player_statistics"),
# "has_event_player_heat_map": tournament_item.get("has_event_player_heat_map"),
# "start_timestamp": tournament_item.get("start_timestamp"),
# "url": tournament_item.get("url"),
