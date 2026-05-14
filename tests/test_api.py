# -*- coding: utf-8 -*-

from afwf_md5 import api


def test():
    _ = api


if __name__ == "__main__":
    from afwf_md5.tests import run_cov_test

    run_cov_test(
        __file__,
        "afwf_md5.api",
        preview=False,
    )
