from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Date

base = declarative_base()


class Student(base):
    """
    Schema of students
    """
    __tablename__ = 'Students'
    StudentID = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    bday = Column(Date)
    teacher = Column(Numeric)
    start = Column(Date)
    last = Column(Date)
    level = Column(Numeric)

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)