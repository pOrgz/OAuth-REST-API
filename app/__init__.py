# -*- encoding: utf-8 -*-
# must require Python 3.6+ : (i) f-String, (ii) dotenv

import yaml
import logging
import logging.config

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import static

def __getLoggerName__(logLevel : int):
    """Get the Name of the logger, as defiend in YAML based on `logLevel`"""

    return {
        logging.INFO     : "infoLogger",
        logging.ERROR    : "errorLogger",
        logging.DEBUG    : "debugLogger",
        logging.CRITICAL : "criticalLogger",
        logging.WARNING  : "warnLogger",
    }.get(logLevel, __name__)

def __getLogger__(logLevel : int = logging.INFO):
    """Defination of a Logger-Functionality - can be used to Track User Sessions and Login Information"""

    # https://stackoverflow.com/questions/6028000/
    # https://stackoverflow.com/questions/56688232/
    loggerFile = pkg_resources.open_text(static, 'logger.yaml') # included static file in MANIFEST.in

    # define logger using PyYAML
    config = yaml.safe_load(loggerFile.read())
    logging.config.dictConfig(config)

    return logging.getLogger(__getLoggerName__(logLevel))

infoLogger     = __getLogger__(logLevel = logging.INFO)
errorLogger    = __getLogger__(logLevel = logging.ERROR)
debugLogger    = __getLogger__(logLevel = logging.DEBUG)
criticalLogger = __getLogger__(logLevel = logging.CRITICAL)
warnLogger     = __getLogger__(logLevel = logging.WARNING)
