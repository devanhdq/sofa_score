import scrapy
import json
from ..items import StatisticItem
from ..my_functions import get_tournaments_id
from scrapy.spidermiddlewares.httperror import HttpError


class StatisticsSpider(scrapy.Spider):
    name = "statistics"
    allowed_domains = ["api.sofascore.com"]

    tournaments_id = get_tournaments_id("./tournaments.csv")

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/statistics',
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_httpbin,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        json_response = json.loads(response.body)
        statistics_item = StatisticItem()
        statistics = json_response.get("statistics", [])
        for statistic in statistics:
            statistics_item['statistic_period'] = statistic.get("period", None)
            groups = statistic.get("groups", [])
            for group in groups:
                statistics_item['statistic_group_name'] = group.get("groupName", None)
                for group_statistics_items in group.get('statisticsItems', []):
                    statistics_item['statistic_name'] = group_statistics_items.get("name", None)
                    statistics_item['statistic_home_value'] = group_statistics_items.get("homeValue", None)
                    statistics_item['statistic_away_value'] = group_statistics_items.get("awayValue", None)
                    statistics_item['statistic_type'] = group_statistics_items.get("statisticsType", None)
                    statistics_item['statistic_compare_code'] = group_statistics_items.get("compareCode", None)
                    statistics_item['tournament_id'] = response.meta.get("tournament_id", None)
                    statistics_item['url'] = response.url
                    yield statistics_item

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
