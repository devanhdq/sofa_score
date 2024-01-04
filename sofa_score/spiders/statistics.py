import scrapy
import json
from ..items import StatisticItem
from ..my_functions import get_unique_tournaments
from scrapy.spidermiddlewares.httperror import HttpError


class StatisticsSpider(scrapy.Spider):
    name = "statistics"
    allowed_domains = ["api.sofascore.com"]

    tournaments_id = get_unique_tournaments("./tournaments2023.csv")

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
        """
                Parses the JSON response and yields statistical data.

                Parameters:
                - response (scrapy.http.Response): The response object containing JSON data.

                Yields:
                - StatisticItem: An item containing statistical information for further processing.
                """
        json_response = json.loads(response.body)
        statistics_item = StatisticItem()
        statistics = json_response.get("statistics", [])
        for statistic in statistics:
            statistics_item['period'] = statistic.get("period", None)
            groups = statistic.get("groups", [])
            for group in groups:
                statistics_item['group_name'] = group.get("groupName", None)
                for group_statistics_items in group.get('statisticsItems', []):
                    statistics_item['tournament_id'] = response.meta.get("tournament_id", None)
                    statistics_item['name'] = group_statistics_items.get("name", None)
                    statistics_item['home_value'] = group_statistics_items.get("homeValue", None)
                    statistics_item['away_value'] = group_statistics_items.get("awayValue", None)
                    statistics_item['type'] = group_statistics_items.get("statisticsType", None)
                    statistics_item['compare_code'] = group_statistics_items.get("compareCode", None)
                    statistics_item['url'] = response.url
                    yield statistics_item

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
