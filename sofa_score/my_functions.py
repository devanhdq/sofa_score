import json
from datetime import datetime, timedelta
import csv


def generate_dates(start_date=datetime(2009, 1, 1), end_date=datetime.now()):
    # Generate a list of dates in the format 'YYYY-MM-DD' within a specified date range.
    #
    # Parameters:
    #     start_date (datetime, optional): The start date of the date range. Defaults to January 1, 2009.
    #     end_date (datetime, optional): The end date of the date range. Defaults to the current date.
    #
    # Returns:
    #     list: A list of dates in the format 'YYYY-MM-DD' within the specified date range.
    #
    # Example:
    #     >>> generate_dates()
    #     ['2009-01-01', '2009-01-02', ..., '2023-12-28']
    #
    #     >>> generate_dates(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 1, 10))
    #     ['2023-01-01', '2023-01-02', ..., '2023-01-10']
    #
    current_date = start_date
    date_list = []

    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")
        date_list.append(formatted_date)
        current_date += timedelta(days=1)

    return date_list


def get_tournaments_id(source_file):
    tournaments_id = []
    with open(source_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row.get('tournament_has_statistics', '').lower() == 'true':
                tournaments_id.append(row.get('tournament_id'))
    return tournaments_id
