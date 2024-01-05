import json

import scrapy
from ..items import IncidentVarItem, IncidentInjuryTimeItem, IncidentGoalItem, \
    IncidentCardItem, IncidentPeriodItem, IncidentSubstitutionItem
from scrapy.spidermiddlewares.httperror import HttpError
from ..my_functions import get_unique_ids


class IncidentsSpider(scrapy.Spider):
    name = "incidents"
    allowed_domains = ["www.sofascore.com"]
    tournaments_id = get_unique_ids("./tournaments2023.json")

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/incidents',
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_httpbin,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        data = json.loads(response.body)
        incidents = data.get('incidents', [])
        tournament_id = response.meta['tournament_id']
        url = response.url
        for incident in incidents:
            incident_type = incident.get('incidentType')
            if incident_type == 'period':
                yield self.parse_period(incident, url, tournament_id)
            elif incident_type == 'card':
                yield self.parse_card(incident, url, tournament_id)
            elif incident_type == 'substitution':
                yield self.parse_substitution(incident, url, tournament_id)
            elif incident_type == 'goal':
                yield self.parse_goal(incident, url, tournament_id)
            elif incident_type == 'injuryTime':
                yield self.parse_injury_time(incident, url, tournament_id)
            elif incident_type == 'varDecision':
                yield self.parse_varDecision(incident, url, tournament_id)

    def parse_period(self, incident, url, tournament_id):
        period = IncidentPeriodItem()
        period['tournament_id'] = tournament_id
        period['incident_type'] = 'period'
        period['text'] = incident.get('text')
        period['home_score'] = incident.get('homeScore')
        period['away_score'] = incident.get('awayScore')
        period['is_live'] = incident.get('isLive')
        period['time'] = incident.get('time')
        period['added_time'] = incident.get('addedTime')
        period['reversed_period_time'] = incident.get('reversedPeriodTime')
        period['url'] = url
        return period

    def parse_card(self, incident, url, tournament_id):
        # Extract details for card incidents
        card = IncidentCardItem()
        player_info = incident.get('player', {})

        card['tournament_id'] = tournament_id
        card['incident_type'] = 'card'
        card['player_name'] = player_info.get('name')
        card['player_id'] = player_info.get('id')
        card['reason'] = incident.get('reason')
        card['is_home'] = incident.get('isHome')
        card['incident_class'] = incident.get('incidentClass')
        card['time'] = incident.get('time')
        card['reversed_period_time'] = incident.get('reversedPeriodTime')
        card['url'] = url
        return card

    def parse_substitution(self, incident, url, tournament_id):
        # Extract details for substitution incidents
        substitution = IncidentSubstitutionItem()
        player_in = incident.get('playerIn', {})
        player_out = incident.get('playerOut', {})

        substitution['tournament_id'] = tournament_id
        substitution['incident_type'] = 'substitution'
        substitution['player_in'] = player_in.get('name')
        substitution['player_in_id'] = player_in.get('id')
        substitution['player_out'] = player_out.get('name')
        substitution['player_out_id'] = player_out.get('id')
        substitution['is_home'] = incident.get('isHome')
        substitution['incident_class'] = incident.get('incidentClass')
        substitution['time'] = incident.get('time')
        substitution['reversed_period_time'] = incident.get('reversedPeriodTime')
        substitution['url'] = url
        return substitution

    def parse_goal(self, incident, url, tournament_id):
        # Extract details for goal incidents
        goal = IncidentGoalItem()
        scorer_info = incident.get('player', {})
        assist_info = incident.get('assist1', {})

        goal['tournament_id'] = tournament_id
        goal['incident_type'] = 'goal'
        goal['scorer'] = scorer_info.get('name')
        goal['scorer_id'] = scorer_info.get('id')
        goal['assist'] = assist_info.get('name') if assist_info else None
        goal['assist_id'] = assist_info.get('id') if assist_info else None
        goal['is_home'] = incident.get('isHome')
        goal['incident_class'] = incident.get('incidentClass')
        goal['time'] = incident.get('time')
        goal['reversed_period_time'] = incident.get('reversedPeriodTime')
        goal['url'] = url

        return goal

    def parse_injury_time(self, incident, url, tournament_id):
        # Extract details for injury time incidents
        injury = IncidentInjuryTimeItem()

        injury['tournament_id'] = tournament_id
        injury['incident_type'] = 'injury_time'
        injury['length'] = incident.get('length')
        injury['time'] = incident.get('time')
        injury['added_time'] = incident.get('addedTime')
        injury['reversed_period_time'] = incident.get('reversedPeriodTime')
        injury["url"] = url

        return injury

    def parse_varDecision(self, incident, url, tournament_id):
        # Extract details for varDecision incidents
        var = IncidentVarItem()

        var['tournament_id'] = tournament_id
        var['incident_type'] = 'varDecision'
        var['decision'] = incident.get('incidentClass')
        var['time'] = incident.get('time')
        var['player_id'] = incident.get('player', {}).get('id')
        var['player_name'] = incident.get('player', {}).get('name')
        var['reversed_period_time'] = incident.get('reversedPeriodTime')
        var['is_home'] = incident.get('isHome')
        var['url'] = url

        return var

    def errback_httpbin(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)
