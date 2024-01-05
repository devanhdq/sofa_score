import scrapy
import json

from scrapy.spidermiddlewares.httperror import HttpError
from ..items import ManagerItem
from ..my_functions import get_unique_ids


# from ..items import get_unique_ids


class ManagersSpider(scrapy.Spider):
    name = "managers"
    allowed_domains = ["api.sofascore.com"]
    tournaments_id = get_unique_ids("./tournaments2023.json")

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/managers',
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_httpbin,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        json_response = json.loads(response.body)
        manager_item = ManagerItem()
        home = json_response.get("homeManager", {})
        away = json_response.get("awayManager", {})

        manager_item['tournament_id'] = response.meta.get('tournament_id')

        manager_item['home_manager_id'] = home.get('id')
        manager_item['home_manager_name'] = home.get('name')
        manager_item['home_manager_short_name'] = home.get('shortName')
        manager_item['home_manager_slug'] = home.get('slug')

        manager_item['away_manager_id'] = away.get('id')
        manager_item['away_manager_name'] = away.get('name')
        manager_item['away_manager_short_name'] = away.get('shortName')
        manager_item['away_manager_slug'] = away.get('slug')
        yield manager_item

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
