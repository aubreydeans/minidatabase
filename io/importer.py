import csv
from typing import List
from database import student
import json

class obj:
    # constructor
    def __init__(self, dictionary):
        self.__dict__.update(dictionary)


def dict2obj(dictionary):
    # using json.loads method and passing json.dumps
    # method and custom object hook as arguments
    return json.loads(json.dumps(dictionary), object_hook=obj)


class SQLFormatter:
    """
    The SQL formatter takes file name to load from on the disk as well as sql table name to insert into.
    The file's first row should match the sql db's column name (case sensitive)
    """
    def __init__(self, file: str, table_name: str):
        self.file = file
        self.table_name = table_name
        self.col_name = []
        self.data = []
        self.load_file()
        self.formatted_data: List[student.Student] = self.format()

    def load_file(self) -> None:
        """
        Load file with col names and actual data
        :return: None
        """
        with open(self.file) as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                if i == 0:
                    self.col_name = row
                else:
                    self.data.append(row)

    def format(self) -> List[student.Student]:
        """
        Format the data into a list of INSERT SQL commands
        :return: a list of INSERT SQL commands
        """
        result = []
        for row in self.data:
            student_dict = {}
            for i, val in enumerate(row):
                student_dict[self.col_name[i]] = val
            result.append(dict2obj(student_dict))
        return result

    def get_formatted_data(self) -> List[student.Student]:
        return self.formatted_data
