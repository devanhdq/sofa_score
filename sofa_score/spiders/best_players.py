import json

import scrapy
from ..my_functions import get_unique_tournaments
from ..items import BestPlayerItem
from scrapy.spidermiddlewares.httperror import HttpError


class BestPlayersSpider(scrapy.Spider):
    name = "best-players"
    allowed_domains = ["api.sofascore.com"]
    tournaments_id = get_unique_tournaments("./tournaments2023.csv")

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/best-players',
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_httpbin,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        data = json.loads(response.body)
        best_player = BestPlayerItem()

        home = data.get('bestHomeTeamPlayer', {})
        away = data.get('bestAwayTeamPlayer', {})

        best_player['tournament_id'] = response.meta.get('tournament_id')

        best_player['home_value'] = home.get('value')
        best_player['home_label'] = home.get('label')
        best_player['home_player_name'] = home.get('player', {}).get('name')
        best_player['home_player_name_slug'] = home.get('player', {}).get('nameSlug')
        best_player['home_player_short_name'] = home.get('player', {}).get('shortName')
        best_player['home_player_position'] = home.get('player', {}).get('position')
        best_player['home_player_user_count'] = home.get('player', {}).get('userCount')
        best_player['home_player_id'] = home.get('player', {}).get('id')
        best_player['home_player_market_value_currency'] = home.get('player', {}).get('marketValueCurrency')
        best_player['home_player_date_of_birth_timestamp'] = home.get('player', {}).get('dateOfBirthTimestamp')

        best_player['away_value'] = away.get('value')
        best_player['away_label'] = away.get('label')
        best_player['away_player_name'] = away.get('player', {}).get('name')
        best_player['away_player_name_slug'] = away.get('player', {}).get('nameSlug')
        best_player['away_player_short_name'] = away.get('player', {}).get('shortName')
        best_player['away_player_position'] = away.get('player', {}).get('position')
        best_player['away_player_user_count'] = away.get('player', {}).get('userCount')
        best_player['away_player_id'] = away.get('player', {}).get('id')
        best_player['away_player_market_value_currency'] = away.get('player', {}).get('marketValueCurrency')
        best_player['away_player_date_of_birth_timestamp'] = away.get('player', {}).get('dateOfBirthTimestamp')

        best_player['url'] = response.url
        yield best_player

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
