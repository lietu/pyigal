#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2013 Janne Enberg
    :license: new BSD, and MIT
"""

# Imports
import config
from Pyigal.Launcher import Launcher

# Boilerplate, if this file is being run
if __name__ == "__main__":

    # TODO: This is stupid, converting module to config object
    parsedConfig = {}
    for key in config.__dict__:
        if not key.startswith("__"):
            parsedConfig[key] = config.__dict__[key]

    launcher = Launcher()
    launcher.set_config(config=parsedConfig)
    launcher.start()
