from .edenredpt import Edenred
from .exceptions import (
    EdenredAPIException,
    AuthenticationException
)

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())