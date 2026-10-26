import importlib.util
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "raik-ui" / "scripts" / "contrast.py"
spec = importlib.util.spec_from_file_location("contrast", SCRIPT)
contrast = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contrast)


def run(*args: str) -> tuple[int, str]:
    out = StringIO()
    with redirect_stdout(out):
        code = contrast.main(list(args))
    return code, out.getvalue()


class ContrastTest(unittest.TestCase):
    def test_known_ratios(self) -> None:
        self.assertAlmostEqual(contrast.ratio("#000000", "#ffffff"), 21.0, places=2)
        self.assertAlmostEqual(contrast.ratio("#fff", "#fff"), 1.0, places=2)
        # #767676 on white is the classic AA threshold (4.54:1).
        self.assertAlmostEqual(contrast.ratio("#767676", "#ffffff"), 4.54, places=2)

    def test_exit_code_reflects_the_minimum(self) -> None:
        self.assertEqual(run("#767676", "#ffffff")[0], 0)
        self.assertEqual(run("#777777", "#ffffff")[0], 1)
        self.assertEqual(run("--min", "3", "#777777", "#ffffff")[0], 0)

    def test_resolves_token_names_from_css(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            css = Path(tmp) / "index.css"
            css.write_text(":root { --color-ink: #1f2421; --paper: #ffffff; }", encoding="utf-8")
            code, output = run("--tokens", str(css), "ink", "paper")
        self.assertEqual(code, 0)
        self.assertIn("ink on paper", output)

    def test_rejects_unknown_tokens(self) -> None:
        with self.assertRaises(SystemExit):
            run("nope", "#ffffff")


if __name__ == "__main__":
    unittest.main()
