from typing import List

from argparser import argparser
from io import importer, exporter
from database import sqlmanager, student
import sys


def parse_sql_connection(filename: str) -> dict:
    """
    Parse SQL connection file into a dictionary
    :param filename: file name to parse
    :return: a dictionary of sql connection information
    """
    result = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.split()
            result[int(key)] = val
    return result


def load_file(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read().replace('\n', '')


def write_file(filename: str, lines: List[str]) -> None:
    with open(filename, 'w') as file:
        return file.writelines(lines)


if __name__ == '__main__':
    # Parse arguments
    parser = argparser.ArgParser(sys.argv[1:])

    # Create a SQL manager
    connection = parse_sql_connection(parser.get_sql_connection())
    sql_mgr = sqlmanager.MySQLManager(host=connection.get("host"), database=connection.get("database"),
                                      user=connection.get("user"), password=connection.get("pass"))

    # If import
    if parser.get_is_import():
        # Creates a SQL formatter
        sql_formatter = importer.SQLFormatter()
        # Formats in SQL commands
        formatted_commands: List[student.Student] = sql_formatter.get_formatted_data()
        # Persists in MySQL database
        sql_mgr.persist(formatted_commands)

    # If export
    else:
        # Loads from SQL
        data: List[dict] = sql_mgr.load()
        # Formats to HTML
        html_formatter = exporter.HtmlFormatter(data, load_file(parser.get_html_template()))
        # Exports HTML file
        formatted_data: List[str] = html_formatter.get_formatted_html()
        # Write file
        write_file(parser.get_output_html(), formatted_data)

