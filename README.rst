
.. image:: https://github.com/MacHu-GWU/afwf_md5-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/afwf_md5-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/afwf_md5-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/afwf_md5-project

.. image:: https://img.shields.io/pypi/v/afwf-md5.svg
    :target: https://pypi.python.org/pypi/afwf-md5

.. image:: https://img.shields.io/pypi/l/afwf-md5.svg
    :target: https://pypi.python.org/pypi/afwf-md5

.. image:: https://img.shields.io/pypi/pyversions/afwf-md5.svg
    :target: https://pypi.python.org/pypi/afwf-md5

.. image:: https://img.shields.io/badge/✍️_Release_History!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/afwf_md5-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/⭐_Star_me_on_GitHub!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/afwf_md5-project

------

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_md5-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_md5-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_md5-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/afwf-md5#files


``afwf_md5`` — MD5 / SHA-256 / SHA-512 Alfred Workflow
==============================================================================

An `Alfred Workflow <https://www.alfredapp.com/workflows/>`_ that computes MD5, SHA-256, and SHA-512 checksums of local files directly from Alfred. No terminal needed — type a path, get a hash, copy it with ⌘C.

When the query is empty, the workflow generates 10 random hashes so you can use it as a secure random string generator.


Install
------------------------------------------------------------------------------

1. Make sure you have `Alfred 5+ <https://www.alfredapp.com/>`_ installed with the `Power Pack <https://www.alfredapp.com/shop/>`_.
2. Go to `Releases <https://github.com/MacHu-GWU/afwf_md5-project/releases>`_ and download the latest ``.alfredworkflow`` file.
3. Double-click the file to install.


Usage
------------------------------------------------------------------------------

Compute MD5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type ``md5`` followed by an absolute file path::

    md5 /path/to/file.zip

- **File found** — returns the MD5 hex digest. Press ⌘C to copy.
- **Empty query** — generates 10 random MD5 hashes (useful as secure random strings).
- **Directory** — shows an error item (directories are not supported).
- **Path not found** — shows an error item.

Compute SHA-256
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type ``sha256`` followed by a path::

    sha256 /path/to/file.zip

Compute SHA-512
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type ``sha512`` followed by a path::

    sha512 /path/to/file.zip


CLI Reference
------------------------------------------------------------------------------

The workflow is backed by a Python CLI (``afwf-md5``) with one subcommand per algorithm. Alfred's Script Filter calls these directly.

.. list-table::
    :header-rows: 1
    :widths: 50 20 30

    * - Subcommand
      - Alfred keyword
      - Output
    * - ``afwf-md5 md5 --query '{query}'``
      - ``md5``
      - MD5 hex digest (32 chars)
    * - ``afwf-md5 sha256 --query '{query}'``
      - ``sha256``
      - SHA-256 hex digest (64 chars)
    * - ``afwf-md5 sha512 --query '{query}'``
      - ``sha512``
      - SHA-512 hex digest (128 chars)

**Dev Script field** (local ``.venv``):

.. code-block:: bash

    .venv/bin/afwf-md5 md5 --query '{query}'

**Production Script field** (via ``uvx``, no virtualenv needed):

.. code-block:: bash

    ~/.local/bin/uvx --from afwf_md5==0.1.1 afwf-md5 md5 --query '{query}'


Error Log
------------------------------------------------------------------------------

Runtime errors are written to::

    ~/.alfred-afwf/afwf_md5/error.log

If a Script Filter returns an error item, pressing Enter opens the log file directly.


Development
------------------------------------------------------------------------------

.. code-block:: bash

    # Install dependencies
    mise run inst

    # Run tests with coverage
    mise run cov

The core logic lives in two files:

- ``afwf_md5/hashes.py`` — pure function ``main(query, hash_algo)`` → ``ScriptFilter``, no Alfred dependency, fully unit-testable.
- ``afwf_md5/cli.py`` — ``Command`` class wired to ``fire.Fire``; each method calls ``hashes.main()`` and sends feedback to Alfred.
