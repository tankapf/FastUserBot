# Copyright (C) 2022 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Fast User Bot
#

""" Bütün modulları yükleyen init faylı """
from userbot import LOGS


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Yüklenecek modullar: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
