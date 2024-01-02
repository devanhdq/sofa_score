import json

import scrapy
from ..my_functions import get_unique_tournaments


class IncidentsSpider(scrapy.Spider):
    name = "incidents"
    allowed_domains = ["www.sofascore.com"]
    # tournaments_id = get_unique_tournaments("./tournaments.csv")
    tournaments_id = [11352586]

    def start_requests(self):
        for tournament_id in self.tournaments_id:
            yield scrapy.Request(
                url=f'https://api.sofascore.com/api/v1/event/{tournament_id}/incidents',
                callback=self.parse,
                dont_filter=True,
                meta={
                    "tournament_id": tournament_id,
                }
            )

    def parse(self, response):
        data = json.loads(response.text)
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
            elif incident_type == 'injury' and incident.get('id'):
                yield self.parse_injury_substitution(incident, url, tournament_id)

    def parse_period(self, incident, url, tournament_id):
        # Extract details for period incidents
        return {
            'tournament_id': tournament_id,
            'incident_type': 'period',
            'home_score': incident.get('homeScore'),
            'away_score': incident.get('awayScore'),
            'is_live': incident.get('isLive'),
            'time': incident.get('time'),
            'added_time': incident.get('addedTime'),
            'reversed_period_time': incident.get('reversedPeriodTime'),
            'url': url
        }

    def parse_card(self, incident, url, tournament_id):
        # Extract details for card incidents
        player_info = incident.get('player', {})
        return {
            'tournament_id': tournament_id,
            'incident_type': 'card',
            'player_name': player_info.get('name'),
            'reason': incident.get('reason'),
            'is_home': incident.get('isHome'),
            'incident_class': incident.get('incidentClass'),
            'time': incident.get('time'),
            'added_time': incident.get('addedTime'),
            'reversed_period_time': incident.get('reversedPeriodTime'),
            url: url
        }

    def parse_substitution(self, incident, url, tournament_id):
        # Extract details for substitution incidents
        player_in = incident.get('playerIn', {})
        player_out = incident.get('playerOut', {})
        return {
            'tournament_id': tournament_id,
            'incident_type': 'substitution',
            'player_in': player_in.get('name'),
            'player_out': player_out.get('name'),
            'is_home': incident.get('isHome'),
            'incident_class': incident.get('incidentClass'),
            'time': incident.get('time'),
            'reversed_period_time': incident.get('reversedPeriodTime'),
            'url': url
        }

    def parse_goal(self, incident, url, tournament_id):
        # Extract details for goal incidents
        scorer_info = incident.get('player', {})
        assist_info = incident.get('assist1', {})
        return {
            'tournament_id': tournament_id,
            'incident_type': 'goal',
            'scorer': scorer_info.get('name'),
            'assist': assist_info.get('name') if assist_info else None,
            'is_home': incident.get('isHome'),
            'incident_class': incident.get('incidentClass'),
            'time': incident.get('time'),
            'reversed_period_time': incident.get('reversedPeriodTime'),
            'url': url
        }

    def parse_injury_time(self, incident, url, tournament_id):
        # Extract details for injury time incidents
        return {
            'tournament_id': tournament_id,
            'incident_type': 'injury_time',
            'length': incident.get('length'),
            'time': incident.get('time'),
            'added_time': incident.get('addedTime'),
            'reversed_period_time': incident.get('reversedPeriodTime'),
            "url": url
        }

    def parse_injury_substitution(self, incident, url, tournament_id):
        # Extract details for injury substitution incidents
        player_in = incident.get('playerIn', {})
        player_out = incident.get('playerOut', {})
        return {
            'tournament_id': tournament_id,
            'incident_type': 'injury_substitution',
            'player_in': player_in.get('name'),
            'player_out': player_out.get('name'),
            'is_home': incident.get('isHome'),
            'incident_class': incident.get('incidentClass'),
            'time': incident.get('time'),
            'reversed_period_time': incident.get('reversedPeriodTime'),
            'url': url
        }
