# -*- coding: utf-8 -*-

import pytest
import afwf.api as afwf

from afwf_md5.cli import Command


class TestMd5:
    def test_empty_query_returns_ten_random_hashes(self, monkeypatch):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        Command().md5(query="")

        assert len(captured) == 1
        assert len(captured[0].items) == 10

    def test_existing_file_returns_md5_checksum(self, monkeypatch, tmp_path):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        p = tmp_path / "file.txt"
        p.write_text("hello")
        Command().md5(query=str(p))

        assert len(captured) == 1
        assert len(captured[0].items[0].title) == 32

    def test_nonexistent_path_returns_error_item(self, monkeypatch, tmp_path):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        Command().md5(query=str(tmp_path / "no_such.txt"))

        assert len(captured) == 1
        assert captured[0].items[0].valid is False

    def test_directory_returns_error_item(self, monkeypatch, tmp_path):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        Command().md5(query=str(tmp_path))

        assert len(captured) == 1
        assert captured[0].items[0].valid is False


class TestSha256:
    def test_empty_query_returns_ten_sha256_hashes(self, monkeypatch):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        Command().sha256(query="")

        assert len(captured) == 1
        assert len(captured[0].items) == 10
        for item in captured[0].items:
            assert len(item.title) == 64

    def test_existing_file_returns_sha256_checksum(self, monkeypatch, tmp_path):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        p = tmp_path / "file.txt"
        p.write_text("hello")
        Command().sha256(query=str(p))

        assert len(captured) == 1
        assert len(captured[0].items[0].title) == 64


class TestSha512:
    def test_empty_query_returns_ten_sha512_hashes(self, monkeypatch):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        Command().sha512(query="")

        assert len(captured) == 1
        assert len(captured[0].items) == 10
        for item in captured[0].items:
            assert len(item.title) == 128

    def test_existing_file_returns_sha512_checksum(self, monkeypatch, tmp_path):
        captured = []
        monkeypatch.setattr(afwf.ScriptFilter, "send_feedback", lambda self: captured.append(self))

        p = tmp_path / "file.txt"
        p.write_text("hello")
        Command().sha512(query=str(p))

        assert len(captured) == 1
        assert len(captured[0].items[0].title) == 128


if __name__ == "__main__":
    from afwf_md5.tests import run_cov_test

    run_cov_test(
        __file__,
        "afwf_md5.cli",
        preview=False,
    )
