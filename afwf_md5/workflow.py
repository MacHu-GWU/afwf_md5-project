# -*- coding: utf-8 -*-

import afwf

from .handlers import (
    hashes,
)

wf = afwf.Workflow()

wf.register(hashes.handler_md5)
wf.register(hashes.handler_sha256)
