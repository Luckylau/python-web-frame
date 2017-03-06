#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pecan
from pecan import rest
from wsme import types as wtypes
import logging
from webdemo.api import expose
from pecan import request
logger = logging.getLogger(__name__)


class Person(wtypes.Base):
    user_id = wtypes.text
    name = wtypes.text
    gender = wtypes.text
    age = int
    email = wtypes.text
    phone = wtypes.ArrayType(wtypes.text)


class Users(wtypes.Base):
    users = [Person]


class UsersController(rest.RestController):

    '''
       None 表示这个方法没有返回值
       status_code 表示这个API的响应状态码是201
       test eg:
       curl -X POST http://localhost:8080/v1/users -H "Content-Type: application/json" -d '{"phone": ["1000860","100876"], "age": 24, "user_id": "133", "name": "kile", "email": "111@163.com"}' -v

    '''
    @expose.expose(None, body=Person, status_code=201)
    def post(self, user):
        db_conn = request.db_conn
        db_conn.add_user(user)

    @expose.expose(Users)
    def get(self):
        logger.info("Get all users Method is called ...")
        """

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
        """
        db_conn = request.db_conn
        users = db_conn.list_users()
        if len(users) == 0:
            return Users()
        users_list = []
        for user in users:
            u = Person()
            u.user_id = user.user_id
            u.age = user.age
            u.email = user.email
            u.name = user.name
            phones = []
            for tel in user.telephone:
                logger.info(
                    "user.id %s ... tel.user_id %s" %
                    (user.id, tel.user_id))
                if user.id == tel.user_id:
                    phones.append(tel.telnumber)
            u.phone = phones
            users_list.append(u)
        return Users(users=users_list)

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder


class UserController(rest.RestController):

    def __init__(self, user_id):
        self.user_id = int(user_id)

    """
    test eg:
         http://127.0.0.1:8080/v1/users/abc
    """
    @expose.expose(Person)
    def get(self):
        """
         logger.info("v1 UserController Get Method is called ...")
        user_info = {
            'id': self.user_id,
            'name': 'Alice',
            'age': 30,
        }
        """
        logger.info("user_id %s" % self.user_id)
        db_conn = request.db_conn
        user = db_conn.get_user(self.user_id)
        if user is None:
            logger.info("user by user_id is not found...")
            return Person()
        else:
            logger.info(
                "user by user_id is found ...%s %s %s " %
                (user.user_id, user.name, user.email))
            person = Person()
            person.id = user.id
            person.user_id = user.user_id
            person.email = user.email
            person.name = user.name
            person.age = user.age
            person.gender = user.gender
            phones = []
            for tel in user.telephone:
                phones.append(tel.telnumber)
            person.phone = phones
            return person

    """
    test eg:
         curl -X PUT http://localhost:8080/v1/users/12 -H "Content-Type: application/json" -d '{"user_id": "12","name": "Cook", "age":50}'
    """
    @expose.expose(Person, body=Person)
    def put(self, user):
        logger.info("v1 UserController Put Method is called ...")
        """
                user_info = {
            'user_id': user.user_id,
            'name': user.name,
            'age': user.age + 1
        }
        return Person(**user_info)
        """
        db_conn = request.db_conn
        person = db_conn.update_user(user)
        return person

    """
    test eg:
         curl -X DELETE http://localhost:8080/v1/users/123
    """

    @expose.expose()
    def delete(self):
        logger.info("v1 UserController Delete Method is called ...")
        print('Delete user_id: %s' % self.user_id)
        db_conn = request.db_conn
        db_conn.delete_user(self.user_id)
