from datetime import datetime, timedelta
import csv
import json


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


def get_unique_ids_has_statistics(source_file, encoding='utf-8'):
    """
       Retrieve unique tournament IDs that have statistics available.

       Parameters:
       - source_file (str): The path to the JSON file containing tournament data.
       - encoding (str, optional): The encoding of the JSON file. Defaults to 'utf-8'.

       Returns:
       - set: A set of unique tournament IDs that have associated statistics.

    """
    unique_tournaments = set()
    with open(source_file, 'r', encoding=encoding) as json_file:
        data = json.load(json_file)
        for entry in data:
            if entry.get('has_statistics') != -1:
                unique_tournaments.add(entry.get('id'))
    return unique_tournaments


def get_unique_ids_has_highlight(source_file, encoding='utf-8'):
    """
        Retrieve unique tournament IDs that have global highlights.

        Parameters:
        - source_file (str): The path to the JSON file containing tournament data.
        - encoding (str, optional): The encoding of the JSON file. Defaults to 'utf-8'.

        Returns:
        - set: A set of unique tournament IDs that have global highlights.

    """
    unique_tournaments = set()
    with open(source_file, 'r', encoding=encoding) as json_file:
        data = json.load(json_file)
        for entry in data:
            if entry.get('has_global_highlights') != -1:
                unique_tournaments.add(entry.get('id'))
    return unique_tournaments


def get_unique_ids(source_file, encoding='utf-8'):
    """
        Retrieve unique tournament IDs from a JSON file.

        Parameters:
        - source_file (str): The path to the JSON file containing tournament data.
        - encoding (str, optional): The encoding of the JSON file. Defaults to 'utf-8'.

        Returns:
        - set: A set of unique tournament IDs.

    """
    unique_tournaments = set()
    with open(source_file, 'r', encoding=encoding) as json_file:
        data = json.load(json_file)
        for entry in data:
            unique_tournaments.add(entry.get('id'))
    return unique_tournaments
