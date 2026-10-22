import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class ScopedCeilingTests(unittest.TestCase):
    def test_law_declares_three_independent_scopes_and_preserves_first_load_gate(self):
        law = (ROOT / "02-legislation.md").read_text(encoding="utf-8")
        self.assertIn("deployed chunk ceiling (25 MiB)", law)
        self.assertIn("source-piece ceiling (16,384 B)", law)
        self.assertIn("channel-event ceiling (1,024 B)", law)
        self.assertIn("strictly under 1,024 UTF-8 bytes", law)
        self.assertIn("first-load gzip gate remains a separate measured limit", law)

    def test_navigation_points_to_the_single_ceiling_law(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("scoped technical ceilings in `02-legislation.md`", agents)
        self.assertIn("scoped technical ceilings in `02-legislation.md`", readme)


if __name__ == "__main__":
    unittest.main()
