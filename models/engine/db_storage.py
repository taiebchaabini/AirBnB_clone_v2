from models.base_model import\
        BaseModel,\
        Base,\
        create_engine,\
        sessionmaker,\
        scoped_session,\
        getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}" .format(
                        getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        Session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
        if (getenv('HBNB_ENV') == "test"):
            self.__session.drop_all()

    def all(self, cls=None):
        """
            query on the current database session (self.__session) all objects
            depending of the class name (argument cls)
        """
        self.__objects = {}
        if (cls):
            for o in self.__session.query(eval(cls.name)).all():
                key = "{}.{}".format(cls.name, o.id)
                self.__objects[key] = o
            return self.__objects
        objects = ['City', 'State']
        for c in objects:
            for o in self.__session.query(eval(c)).all():
                key = "{}.{}".format(c, o.id)
                self.__objects[key] = o
        return self.__objects

    def new(self, obj):
        """
        add the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
            commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current database session.
        """
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        """
            create all tables in the database.
        """
        Base.metadata.create_all(self.__engine)
