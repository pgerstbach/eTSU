"""Plain-assert test for build_data_model_full_diagram() — no pytest dependency.

The data-model class diagram is a projection (ADR-0018): every DM page in
tests/fixtures/wiki/data-models/ becomes one mermaid class; relationships
from the `**Relationships.**` bullets and sum-type `parent:` edges (ADR-0019)
become arrows; a relationship to a page that does not exist becomes a visible
ghost class instead of being dropped silently.

Run from the dashboard dir inside a venv that has the app's requirements:
    .venv/bin/python tests/test_data_model_diagram.py
"""
import os
import re
import sys
from pathlib import Path

_FIXTURE = Path(__file__).resolve().parent / "fixtures" / "wiki"
os.environ["WIKI_DIR"] = str(_FIXTURE)
os.environ["ADR_DIR"] = str(_FIXTURE.parent / "adr")
os.environ["DASH_STARTUP_GRACE"] = "3600"
os.environ["DASH_HEARTBEAT_GRACE"] = "3600"
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # import app.py
import app  # noqa: E402


def _classes(src: str) -> set[str]:
    return set(re.findall(r"^\s{4}class (\w+)", src, re.MULTILINE))


def test_diagram_projects_pages_attributes_and_edges():
    src = app.build_data_model_full_diagram()
    assert src, "no diagram despite DM pages present"
    assert src.startswith("classDiagram\n")

    # one class per DM fixture page, named after the frontmatter id
    ids = {"DM001", "DM002", "DM003", "DM005", "DM007", "DM008", "DM009", "DM004shelf", "DM006missingtarget"}
    assert _classes(src) == ids, _classes(src)

    # attributes from the `**Attributes.**` bullet list end up in the class body
    assert re.search(r"class DM001 \{[^}]*\bisbn\b", src, re.DOTALL)
    assert re.search(r"class DM002 \{[^}]*\bstatus\b", src, re.DOTALL)
    assert re.search(r"class DM005 \{[^}]*\bcity\b", src, re.DOTALL)

    # stereotype annotations (ADR-0019)
    assert re.search(r"class DM007 \{[^}]*<<sum>>", src, re.DOTALL)
    assert re.search(r"class DM005 \{[^}]*<<value>>", src, re.DOTALL)

    # sum-type variants attach via `parent:` as inheritance arrows
    assert "DM007 <|-- DM008" in src
    assert "DM007 <|-- DM009" in src

    # relationship bullets render as labelled association arrows
    assert "DM002 --> DM001 : 1 association mandatory" in src
    assert "DM002 --> DM003 : 1 association mandatory" in src
    assert "DM001 --> DM004shelf" in src            # dangling target, still drawn

    # a dangling target gets a visible ghost class, not a silent drop
    assert "DM004shelf : missing DM page" in src


def test_empty_vault_returns_none():
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        empty = Path(td) / "wiki"
        empty.mkdir()
        app.WIKI_DIR = empty
        try:
            assert app.build_data_model_full_diagram() is None
        finally:
            app.WIKI_DIR = Path(_FIXTURE)


if __name__ == "__main__":
    test_diagram_projects_pages_attributes_and_edges()
    test_empty_vault_returns_none()
    print("all data-model diagram tests passed")
