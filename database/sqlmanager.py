import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from typing import List
from database import student


class MySQLManager:
    """
    SQL manager is a wrapper that provides a sql connection
    """
    def __init__(self, host: str, database: str, user: str, password: str):
        self.engine = db.create_engine(f'mysql://{user}:{password}@{host}/{database}')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.student_table = db.Table('Students', self.metadata, autoload=True, autoload_with=self.engine)

    def persist(self, students: List[student.Student]) -> None:
        """
        Persists a list of students commands such as insert and update
        :param students: a list of student objects to persist
        :return: None
        """
        session = sessionmaker(bind=self.engine)()
        for student in students:
            session.add(student)
        session.commit()

    def load(self) -> List[dict]:
        """
        Load table into a list of dictionary
        :return: a list of dictionary
        """
        query = db.select([self.student_table])
        return self.connection.execute(query).fetchall()

