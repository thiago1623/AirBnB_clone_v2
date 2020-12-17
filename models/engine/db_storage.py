"""
this is a documentation
"""


from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"City": City, "State": State, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """ this is a documentation """
    __engine = None
    __session = None

    def __init__(self):
        """ this is a documentation """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user,
                                              password,
                                              host,
                                              database), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ this is a documentation """
        dicc = {}
        if cls:
            query = self.__session.query(cls) ## eval en el quiery
            for clase in query:
                key = "{}.{}".format(type(clase).__name__, clase.id)
                dicc[key] = clase
        else:
            lista_clases = [User, State, City, Amenity, Place, Review]
            for clase in lista_clases:
                query = self.__session.query(clase)
                for obj in query:
                    key = "{}.{}".format(type(obj)._name_, obj.id)
                    dicc[key] = obj
        return dicc

    def new(self, obj):
        """ this is a documentation """
        self.__session.add(obj)

    def save(self):
        """ this is a documentation """
        self.__session.commit()

    def delete(self, obj=None):
        """ this is a documentation """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ this is a documentation """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
