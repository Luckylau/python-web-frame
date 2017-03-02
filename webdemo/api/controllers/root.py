from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose
import logging
logger = logging.getLogger(__name__)


class RootController(rest.RestController):

    @expose.expose(wtypes.text)
    def get(self):
        logger.info("Method is called ...")
        return "python-web-frame: pecan & wsme "
