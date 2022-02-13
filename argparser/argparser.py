import argparse


class ArgParser:
    """
    Parser to parse command line arguments
    """
    def __init__(self, args):
        self.parser = argparse.ArgumentParser()
        self.set_parser()
        self.parsed_args = self.parser.parse_args(args)

    def set_parser(self) -> None:
        self.parser.add_argument('--isimport', type=bool, default=True, help='whether the task is to import files')
        self.parser.add_argument('--inputcsv', type=str,  help='input CSV file to load data')
        self.parser.add_argument('--sqltable', type=str, help='name of the sql table to read or write data')
        self.parser.add_argument('--htmltemplate', type=str, help='HTML template file to format data into')
        self.parser.add_argument('--sqlconnetion', type=str, help='file with SQL connection data')
        self.parser.add_argument('--outputhtml', type=str, help='output HTML file to write to')

    def get_is_import(self) -> bool:
        return self.parsed_args.isimport

    def get_input_data(self) -> str:
        return self.parsed_args.inputcsv

    def get_sql_table(self) -> str:
        return self.parsed_args.sqltable

    def get_html_template(self) -> str:
        return self.parsed_args.htmltemplate

    def get_sql_connection(self) -> str:
        return self.parsed_args.sqlconnection

    def get_output_html(self) -> str:
        return self.parsed_args.outputhtml