# -*- coding: utf-8 -*-

"""
"""

import typing as T
import hashlib
from pathlib_mate import Path
import attrs
from attrs_mate import AttrsClass

import afwf.api as afwf

from ..utils import get_file_fingerprint, get_text_fingerprint, random_string


hash_algo_mapper = {
    "md5": hashlib.md5,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


@attrs.define
class Handler(afwf.Handler):
    hash_algo = AttrsClass.ib_str(nullable=False)

    def main(self, path: T.Optional[str]) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        hash_algo = hash_algo_mapper[self.hash_algo]
        if path is None:
            for _ in range(10):
                checksum = get_text_fingerprint(random_string(32), hash_algo)
                item = afwf.Item(
                    title=checksum,
                    subtitle=f"Tap CMD + C to copy to clipboard",
                    arg=checksum,
                )
                sf.items.append(item)
            return sf

        p = Path(path)
        if p.exists():
            if p.is_file():
                checksum = get_file_fingerprint(path, hash_algo)
                item = afwf.Item(
                    title=checksum,
                    subtitle=f"Tap CMD + C to copy to clipboard",
                    arg=checksum,
                )
                sf.items.append(item)
            elif p.is_dir():
                item = afwf.Item(
                    title=f"'{path}' is a directory!",
                    icon=afwf.Icon.from_image_file(afwf.IconFileEnum.error),
                )
                sf.items.append(item)
        else:
            item = afwf.Item(
                title=f"'{path}' does not exists!",
                icon=afwf.Icon.from_image_file(afwf.IconFileEnum.error),
            )
            sf.items.append(item)
        return sf

    def parse_query(self, query: str):
        if len(query.strip()):
            return {"path": query.strip()}
        else:
            return {"path": None}


handler_md5 = Handler(id="md5", hash_algo="md5")
handler_sha256 = Handler(id="sha256", hash_algo="sha256")
