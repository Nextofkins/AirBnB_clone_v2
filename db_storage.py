#!/usr/bin/python3
"""Module for DBstorage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """returns all objects of cls"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = [
            State,
            City,
            User,
            Place,
            Review,
            Amenity
        ]
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """add object to db"""

