#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pecan import hooks
from webdemo.db import api as db_api


class DBHook(hooks.PecanHook):

    def before(self, state):
        state.request.db_conn = db_api.Connection()
