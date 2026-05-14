# -*- coding: utf-8 -*-

from pathlib import Path
from functools import cached_property

_dir_here = Path(__file__).absolute().parent
PACKAGE_NAME = _dir_here.name


class PathEnum:
    dir_project_root = _dir_here.parent
    dir_venv = dir_project_root / ".venv"
    dir_venv_bin = dir_venv / "bin"
    path_venv_bin_pytest = dir_venv_bin / "pytest"
    dir_htmlcov = dir_project_root / "htmlcov"
    path_cov_index_html = dir_htmlcov / "index.html"
    dir_unit_test = dir_project_root / "tests"

    @cached_property
    def dir_home(self) -> Path:
        return Path.home()

    @cached_property
    def dir_project_home(self) -> Path:
        p = self.dir_home / ".alfred-afwf" / PACKAGE_NAME
        p.mkdir(parents=True, exist_ok=True)
        return p

    @cached_property
    def dir_cache(self) -> Path:
        return self.dir_project_home / ".cache"

    @cached_property
    def path_error_log(self) -> Path:
        return self.dir_project_home / "error.log"


path_enum = PathEnum()
