import importlib.util
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "raik-ship" / "scripts" / "archive_links.py"
spec = importlib.util.spec_from_file_location("archive_links", SCRIPT)
archive_links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archive_links)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ArchiveLinksTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        archived = self.root / "openspec/changes/archive/2026-10-25-show-net"
        write(self.root / "docs/roadmap.md", "See [change](../openspec/changes/show-net/proposal.md).\n")
        write(self.root / "docs/review.md", "Old: `openspec/changes/show-net/` and [other](../openspec/changes/show-network/x.md).\n")
        write(archived / "proposal.md", "[review](../../../docs/review.md#gaps) and [design](design.md) and [web](https://x.dev/a).\n")
        write(archived / "design.md", "Design.\n")
        write(archived / "specs/net/spec.md", "[proposal](../../proposal.md) [gone](../../../../missing.md)\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def run_script(self, *extra: str) -> str:
        out = StringIO()
        with redirect_stdout(out):
            archive_links.main(["show-net", "--root", str(self.root), *extra])
        return out.getvalue()

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def test_adds_a_level_to_links_leaving_the_change(self) -> None:
        self.run_script()
        text = self.read("openspec/changes/archive/2026-10-25-show-net/proposal.md")
        self.assertIn("](../../../../docs/review.md#gaps)", text)
        self.assertIn("](design.md)", text)
        self.assertIn("](https://x.dev/a)", text)

    def test_keeps_links_inside_the_change_and_reports_broken_ones(self) -> None:
        output = self.run_script()
        text = self.read("openspec/changes/archive/2026-10-25-show-net/specs/net/spec.md")
        self.assertIn("](../../proposal.md)", text)
        self.assertIn("broken before archiving", output)

    def test_points_outside_references_at_the_archive_without_touching_similar_names(self) -> None:
        self.run_script()
        self.assertIn("../openspec/changes/archive/2026-10-25-show-net/proposal.md", self.read("docs/roadmap.md"))
        review = self.read("docs/review.md")
        self.assertIn("`openspec/changes/archive/2026-10-25-show-net/`", review)
        self.assertIn("changes/show-network/x.md", review)

    def test_dry_run_writes_nothing(self) -> None:
        before = self.read("docs/roadmap.md")
        self.run_script("--dry-run")
        self.assertEqual(before, self.read("docs/roadmap.md"))

    def test_is_idempotent(self) -> None:
        self.run_script()
        first = self.read("openspec/changes/archive/2026-10-25-show-net/proposal.md")
        output = self.run_script()
        self.assertEqual(first, self.read("openspec/changes/archive/2026-10-25-show-net/proposal.md"))
        self.assertIn("0 file(s) fixed", output)


if __name__ == "__main__":
    unittest.main()
