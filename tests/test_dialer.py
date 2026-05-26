import json
import tempfile
import unittest
from pathlib import Path

from core.connection_manager import ConnectionManager
from core.dialer import Dialer
from core.lexeme_manager import LexemeManager
from core.session_logger import SessionLogger


class TestDialer(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        base = Path(self.tmp_dir.name)
        registry_path = base / "registry.json"

        registry_path.write_text(
            json.dumps(
                {
                    "primal": {
                        "endpoint": "primal_bbs",
                        "status": "active",
                        "aliases": ["primal_bbs"],
                    },
                    "house": {
                        "endpoint": "house_of_confusion_bbs",
                        "status": "active",
                        "aliases": ["thehouse"],
                    },
                }
            ),
            encoding="utf-8",
        )

        lex = LexemeManager(registry_path)
        logger = SessionLogger(base / "sessions.log")
        conn = ConnectionManager(lex, logger)
        self.dialer = Dialer(lex, conn, max_history=2, connection_delay=0.0)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_autocomplete(self):
        self.assertIn("primal", self.dialer.autocomplete("pri"))

    def test_history_max_size(self):
        self.dialer.record_history("one")
        self.dialer.record_history("two")
        self.dialer.record_history("three")
        self.assertEqual(self.dialer.history, ["two", "three"])


if __name__ == "__main__":
    unittest.main()
