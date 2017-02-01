# -*- coding: utf-8 -*-

"""
.. module:: options.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Library overrideable options.

.. moduleauthor:: David Hassel <david.hassell@ncas.ac.uk>


"""
import os

from cdf2cim import constants



# I/O directory.
IO_DIR = os.getenv(constants.ENV_VAR_IO_DIR, "{}/.esdoc/cdf2cim".format(os.getenv("HOME")))

# Web-service GitHub user.
WS_USER = os.getenv(constants.ENV_VAR_GH_USER)

# Web-service GitHub access token.
WS_ACCESS_TOKEN = os.getenv(constants.ENV_VAR_GH_ACCESS_TOKEN)

# Web-service host.
WS_HOST = os.getenv(constants.ENV_VAR_WS_HOST, constants.DEFAULT_WS_HOST)
