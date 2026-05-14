# -*- coding: utf-8 -*-

import hashlib
from pathlib import Path

import afwf.api as afwf

from .utils import get_file_fingerprint, get_text_fingerprint, random_string

_HASH_ALGO_MAPPER = {
    "md5": hashlib.md5,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


def main(query: str, hash_algo: str) -> afwf.ScriptFilter:
    algo = _HASH_ALGO_MAPPER[hash_algo]

    if not query.strip():
        items = []
        for _ in range(10):
            checksum = get_text_fingerprint(random_string(32), algo)
            item = afwf.Item(
                title=checksum,
                subtitle="Tap CMD + C to copy to clipboard",
                arg=checksum,
            )
            items.append(item)
        return afwf.ScriptFilter(items=items)

    path = query.strip()
    p = Path(path)

    if p.exists():
        if p.is_file():
            checksum = get_file_fingerprint(path, algo)
            item = afwf.Item(
                title=checksum,
                subtitle="Tap CMD + C to copy to clipboard",
                arg=checksum,
            )
        else:
            item = afwf.Item(
                title=f"'{path}' is a directory!",
                icon=afwf.Icon.from_image_file(path=afwf.IconFileEnum.error),
                valid=False,
            )
    else:
        item = afwf.Item(
            title=f"'{path}' does not exist!",
            icon=afwf.Icon.from_image_file(path=afwf.IconFileEnum.error),
            valid=False,
        )

    return afwf.ScriptFilter(items=[item])
