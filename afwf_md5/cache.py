# -*- coding: utf-8 -*-

from diskcache import Cache
from .paths import path_enum

cache = Cache(str(path_enum.dir_cache))
