# -*- coding: utf-8 -*-

import pytest
from afwf_md5.hashes import main


class TestMain:
    def test_empty_query_returns_ten_random_hashes(self):
        sf = main(query="", hash_algo="md5")
        assert len(sf.items) == 10
        for item in sf.items:
            assert len(item.title) == 32  # md5 hex digest is 32 chars

    def test_empty_query_sha256(self):
        sf = main(query="", hash_algo="sha256")
        assert len(sf.items) == 10
        for item in sf.items:
            assert len(item.title) == 64  # sha256 hex digest is 64 chars

    def test_empty_query_sha512(self):
        sf = main(query="", hash_algo="sha512")
        assert len(sf.items) == 10
        for item in sf.items:
            assert len(item.title) == 128  # sha512 hex digest is 128 chars

    def test_whitespace_query_treated_as_empty(self):
        sf = main(query="   ", hash_algo="md5")
        assert len(sf.items) == 10

    def test_existing_file_returns_checksum(self, tmp_path):
        p = tmp_path / "test.txt"
        p.write_text("hello")
        sf = main(query=str(p), hash_algo="md5")
        assert len(sf.items) == 1
        item = sf.items[0]
        assert len(item.title) == 32
        assert item.arg == item.title

    def test_same_file_produces_same_checksum(self, tmp_path):
        p = tmp_path / "test.txt"
        p.write_text("hello")
        sf1 = main(query=str(p), hash_algo="sha256")
        sf2 = main(query=str(p), hash_algo="sha256")
        assert sf1.items[0].title == sf2.items[0].title

    def test_directory_returns_error_item(self, tmp_path):
        sf = main(query=str(tmp_path), hash_algo="md5")
        assert len(sf.items) == 1
        item = sf.items[0]
        assert "directory" in item.title
        assert item.valid is False
        assert item.icon is not None

    def test_nonexistent_path_returns_error_item(self, tmp_path):
        missing = str(tmp_path / "does_not_exist.txt")
        sf = main(query=missing, hash_algo="md5")
        assert len(sf.items) == 1
        item = sf.items[0]
        assert "does not exist" in item.title
        assert item.valid is False
        assert item.icon is not None

    def test_random_hashes_differ_between_calls(self):
        sf1 = main(query="", hash_algo="md5")
        sf2 = main(query="", hash_algo="md5")
        titles1 = {item.title for item in sf1.items}
        titles2 = {item.title for item in sf2.items}
        assert titles1 != titles2


if __name__ == "__main__":
    from afwf_md5.tests import run_cov_test

    run_cov_test(
        __file__,
        "afwf_md5.hashes",
        preview=False,
    )
