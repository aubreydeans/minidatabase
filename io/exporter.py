import string
from typing import List, Set


class HtmlFormatter:
    """
    HTML Formatter is a formatter class that is responsible for converting the CSV data into HTML format.

    Data should be provided as an list of dict where all dicts should have the same set of key representing the
    column names and values representing the values on that column.

    It also accepts an HTML template string with placeholder names with a newline symbol. The placeholder names should match the keys in the data dict.
    """
    def __init__(self, data: List[dict], html: str, newline: str = "\\n"):
        self.data = data
        self.html = html
        self.newline = newline
        self.formatted_html = self.format()

    def validate_input(self) -> bool:
        """
        Validate if the keys in dict are consistent and whether they match the placeholders in html
        :return: True if matches, and throws errors if not
        """
        if not any(self.data):
            raise Exception("data is empty.")
        keys = set(self.data[0].keys())
        for i, row in enumerate(self.data):
            if i == 0:
                continue
            if keys != set(row.keys()):
                raise Exception(f'keys are not consistent starting row {i}')
        if self.__extract_placeholder_names_from_html() != keys:
            raise Exception("Keys in the data do not match placeholders in html")
        return True

    def __extract_placeholder_names_from_html(self) -> Set[str]:
        """
        Extract placeholder names in the html string
        :return: a set of placeholdr names
        """
        return set([name for _, name, _, _ in string.Formatter().parse(self.html)])

    def format(self) -> List[str]:
        """
        Format the data by the HTML template
        :return:
        """
        result = list()
        for row in self.data:
            result.append(self.newline.join(map(lambda d: self.html.format(d), self.data)))
        return result

    def get_formatted_html(self) -> List[str]:
        return self.formatted_html


