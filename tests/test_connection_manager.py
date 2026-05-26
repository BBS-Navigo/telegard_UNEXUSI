import json
import tempfile
import unittest
from pathlib import Path

from core.connection_manager import ConnectionManager
from core.lexeme_manager import LexemeManager
from core.session_logger import SessionLogger


class TestConnectionManager(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        base = Path(self.tmp_dir.name)

        self.registry_path = base / "registry.json"
        self.log_path = base / "sessions.log"

        self.registry_path.write_text(
            json.dumps(
                {
                    "primal": {
                        "endpoint": "primal_bbs",
                        "status": "active",
                        "aliases": ["primal_bbs"],
                    }
                }
            ),
            encoding="utf-8",
        )

        self.lexemes = LexemeManager(self.registry_path)
        self.logger = SessionLogger(self.log_path)
        self.manager = ConnectionManager(self.lexemes, self.logger)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_connect_unknown_lexeme(self):
        result = self.manager.connect("does-not-exist", input_func=lambda _: "", output_func=lambda _: None)
        self.assertEqual(result["connection_status"], "failed")
        self.assertEqual(result["reason"], "unknown_lexeme")

    def test_connect_success(self):
        responses = iter(["", "3"])
        result = self.manager.connect("primal", input_func=lambda _: next(responses), output_func=lambda _: None)
        self.assertEqual(result["connection_status"], "success")
        self.assertIn("rooms_visited", result)


if __name__ == "__main__":
    unittest.main()
