# import scrapy
# import json
# from ..items import StatisticItem, TournamentItem
#
#
# class StatisticsSpider(scrapy.Spider):
#     name = "statistics"
#     allowed_domains = ["api.sofascore.com"]
#     start_urls = ["https://api.sofascore.com/api/v1/event/11352547/statistics"]
#
#     def parse(self, response):
#         json_response = json.loads(response.body)
#         statistics = json_response.get("statistics", [])
#
#         statistics_item = StatisticItem()
#         statistics_item['period'] = statistics
#         yield statistics_item
