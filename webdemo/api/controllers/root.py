#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose
from webdemo.api.controllers.v1 import controller as v1_controller
import logging
logger = logging.getLogger(__name__)


class RootController(rest.RestController):
    v1 = v1_controller.v1Controller()

    """
    test eg:
         http://127.0.0.1:8080/
    """
    @expose.expose(wtypes.text)
    def get(self):
        logger.info("Method Get is called ...")
        return "python-web-frame: pecan & wsme "
