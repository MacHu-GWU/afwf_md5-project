# -*- coding: utf-8 -*-

import fire
import afwf.api as afwf

from .hashes import main as hashes_main
from .paths import path_enum

_log_error = afwf.log_error(
    log_file=path_enum.path_error_log,
    tb_limit=10,
)


def _error_sf(exc: Exception) -> afwf.ScriptFilter:
    item = afwf.Item(
        title=f"{type(exc).__name__}: {exc}",
        subtitle=f"Press Enter to open the error log: {path_enum.path_error_log}",
        icon=afwf.Icon.from_image_file(path=afwf.IconFileEnum.error),
        valid=True,
    )
    item.open_file(str(path_enum.path_error_log))
    return afwf.ScriptFilter(items=[item])


class Command:
    def md5(self, query: str = "") -> None:
        """Script Filter: compute MD5 hash of a file or show random MD5 hashes.

        Alfred Script field (dev):
            .venv/bin/afwf-md5 md5 --query '{query}'

        Alfred Script field (prod):
            ~/.local/bin/uvx --from afwf_md5==<ver> afwf-md5 md5 --query '{query}'
        """

        @_log_error
        def _run():
            hashes_main(query=query, hash_algo="md5").send_feedback()

        try:
            _run()
        except Exception as e:
            _error_sf(e).send_feedback()

    def sha256(self, query: str = "") -> None:
        """Script Filter: compute SHA-256 hash of a file or show random SHA-256 hashes.

        Alfred Script field (dev):
            .venv/bin/afwf-md5 sha256 --query '{query}'

        Alfred Script field (prod):
            ~/.local/bin/uvx --from afwf_md5==<ver> afwf-md5 sha256 --query '{query}'
        """

        @_log_error
        def _run():
            hashes_main(query=query, hash_algo="sha256").send_feedback()

        try:
            _run()
        except Exception as e:
            _error_sf(e).send_feedback()

    def sha512(self, query: str = "") -> None:
        """Script Filter: compute SHA-512 hash of a file or show random SHA-512 hashes.

        Alfred Script field (dev):
            .venv/bin/afwf-md5 sha512 --query '{query}'

        Alfred Script field (prod):
            ~/.local/bin/uvx --from afwf_md5==<ver> afwf-md5 sha512 --query '{query}'
        """

        @_log_error
        def _run():
            hashes_main(query=query, hash_algo="sha512").send_feedback()

        try:
            _run()
        except Exception as e:
            _error_sf(e).send_feedback()


def run():
    fire.Fire(Command)
