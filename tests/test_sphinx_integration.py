"""Integration tests for the sphinx-ymmsl Sphinx directive."""

import textwrap
from pathlib import Path

import pytest
from sphinx.application import Sphinx


@pytest.fixture
def sphinx_srcdir(tmp_path):
    """Create a minimal Sphinx project for integration testing."""
    (tmp_path / "conf.py").write_text(
        textwrap.dedent("""\
            extensions = ['sphinx_ymmsl']
            master_doc = 'index'
            exclude_patterns = ['_build']
        """)
    )

    (tmp_path / "test_model.ymmsl").write_text(
        textwrap.dedent("""\
            ymmsl_version: v0.2

            description: A test model description

            models:
              my_model:
                description: A model component
        """)
    )

    (tmp_path / "index.rst").write_text(
        textwrap.dedent("""\
            Test
            ====

            .. ymmsl:: test_model.ymmsl
        """)
    )

    return tmp_path


def test_sphinx_directive_builds(sphinx_srcdir, tmp_path):
    """Test that the ymmsl directive builds documentation without error.

    Install the package under test with:
        pip install git+https://github.com/multiscale/sphinx-ymmsl.git@main
    """
    outdir = tmp_path / "_build" / "html"
    doctreedir = tmp_path / "_build" / ".doctrees"

    app = Sphinx(
        srcdir=str(sphinx_srcdir),
        confdir=str(sphinx_srcdir),
        outdir=str(outdir),
        doctreedir=str(doctreedir),
        buildername="html",
        freshenv=True,
    )
    app.build()

    html = (outdir / "index.html").read_text()
    # Title is derived from the filename: test_model -> "Test Model"
    assert "Test Model" in html
    assert "A test model description" in html
    assert "A model component" in html
