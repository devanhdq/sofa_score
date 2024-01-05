import scrapy
import json

from scrapy.spidermiddlewares.httperror import HttpError
from ..items import HighlightItem
from ..my_functions import get_unique_ids_has_highlight


class HighlightsSpider(scrapy.Spider):
    name = "highlights"
    allowed_domains = ["api.sofascore.com"]

    tournaments_id = get_unique_ids_has_highlight("./tournaments2023.json")

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/highlights',
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_httpbin,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        json_response = json.loads(response.body)
        highlights = json_response.get("highlights", {})
        for highlight in highlights:
            item = HighlightItem()
            item['tournament_id'] = response.meta.get('tournament_id')
            item['id'] = highlight.get('id')

            item['title'] = highlight.get('title')
            item['subtitle'] = highlight.get('subtitle')
            item['highlight_url'] = highlight.get('url')
            item['highlight_thumbnail_url'] = highlight.get('thumbnailUrl')

            item['media_type'] = highlight.get('mediaType')
            item['do_follow'] = highlight.get('doFollow')
            item['key_highlight'] = highlight.get('keyHighlight')
            item['created_at_timestamp'] = highlight.get('createdAtTimestamp')
            item['source_url'] = highlight.get('sourceUrl')
            yield item

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
