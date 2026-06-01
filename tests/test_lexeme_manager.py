import json
import tempfile
import unittest
from pathlib import Path

from core.lexeme_manager import LexemeManager


class TestLexemeManager(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.registry_path = Path(self.tmp_dir.name) / "registry.json"
        self.registry_path.write_text(
            json.dumps(
                {
                    "primal": {
                        "endpoint": "primal_bbs",
                        "status": "active",
                        "aliases": ["primal_bbs", "primalBBS"],
                    }
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_resolve_primary(self):
        manager = LexemeManager(self.registry_path)
        record = manager.resolve("primal")
        self.assertIsNotNone(record)
        self.assertEqual(record["lexeme"], "primal")

    def test_resolve_alias(self):
        manager = LexemeManager(self.registry_path)
        record = manager.resolve("primalBBS")
        self.assertIsNotNone(record)
        self.assertEqual(record["endpoint"], "primal_bbs")

    def test_resolve_alias_with_underscore(self):
        manager = LexemeManager(self.registry_path)
        record = manager.resolve("primal_bbs")
        self.assertIsNotNone(record)
        self.assertEqual(record["lexeme"], "primal")

    def test_unknown_lexeme(self):
        manager = LexemeManager(self.registry_path)
        self.assertIsNone(manager.resolve("unknown"))


if __name__ == "__main__":
    unittest.main()
