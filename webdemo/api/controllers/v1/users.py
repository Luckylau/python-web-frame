from pecan import rest
from wsme import types as wtypes
import logging
from webdemo.api import expose
logger = logging.getLogger(__name__)


class User(wtypes.Base):
    name = wtypes.text
    age = int


class Users(wtypes.Base):
    users = [User]


class UsersController(rest.RestController):

    @expose.expose(Users)
    def get(self):
        logger.info("v1 UsersController Get Method is called ...")
        user_info_list = [
            {
                'name': 'Alice',
                'age': 30,
            },
            {
                'name': 'Bob',
                'age': 40,
            }
        ]
        users_list = [User(**user_info) for user_info in user_info_list]
        return Users(users=users_list)
