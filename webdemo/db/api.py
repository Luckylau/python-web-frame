from sqlalchemy import create_engine
import logging
from webdemo.db import models as db_models
import sqlalchemy.orm
logger = logging.getLogger(__name__)
Domain = "sqlalchemy"


_ENGINE = None
_SESSION_MAKER = None


def get_engine():
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE
    _ENGINE = create_engine('sqlite://')
    db_models.Base.metadata.create_all(_ENGINE)


def get_session_maker(engine):
    global _SESSION_MAKER
    if _SESSION_MAKER is not None:
        return _SESSION_MAKER
    _SESSION_MAKER = sqlalchemy.orm.sessionmaker(bind=engine)
    return _SESSION_MAKER


def get_session():
    engine = get_engine()
    maker = get_session_maker(engine)
    session = maker()
    return session


class Connection(object):

    def __init__(self):
        pass

    def get_user(self,user_id):
        query = get_session().query(db_models.User).filter_by(user_id=user_id)
        try:
            user = query.one()
        except Exception ,e:
            print("query error"+e.message)
        return user

    def list_users(self):
        query=get_session().query(db_models.User)
        try:
            users = query.all()
        except Exception ,e:
            print("query error"+e.message)
        return users

    def update_user(self, user):
        pass

    def delete_user(self, user):
        pass
