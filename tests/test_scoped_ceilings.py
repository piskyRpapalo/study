import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class ScopedCeilingTests(unittest.TestCase):
    def test_current_law_has_three_active_size_domains_no_legacy_source_cap(self):
        law = (ROOT / "02-legislation.md").read_text(encoding="utf-8")
        self.assertIn("The former 16,384-byte source-file ceiling has no current force", law)
        self.assertIn("25 MiB", law)
        self.assertIn("1 GB", law)
        self.assertIn("strictly **below 1,024 UTF-8 bytes**", law)
        self.assertIn("No global fourth source-piece limit exists", law)
        # The 2026-10-22 text stays available solely as append-only history.
        self.assertIn("source-piece efficiency rule (16,384 B)", law)

    def test_navigation_points_to_the_single_ceiling_law(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("scoped technical ceilings in `02-legislation.md`", agents)
        self.assertIn("scoped technical ceilings in `02-legislation.md`", readme)


if __name__ == "__main__":
    unittest.main()
