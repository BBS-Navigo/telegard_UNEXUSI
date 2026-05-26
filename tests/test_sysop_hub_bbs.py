import unittest

from bbs_systems.sysop_hub_bbs import run


class TestSysopHubBbs(unittest.TestCase):
    def test_run_shadow_ops_then_exit(self):
        responses = iter(["", "1", "all systems nominal", "3"])
        outputs = []

        result = run(
            {"lexeme": "sysop"},
            input_func=lambda _: next(responses),
            output_func=outputs.append,
        )

        self.assertEqual(result["entry_state"], "shadow")
        self.assertEqual(result["signal"], "all systems nominal")
        self.assertEqual(result["exit"], "disconnect")
        self.assertIn("Sysop Switchboard", result["rooms_visited"])
        self.assertIn("Ops Board", result["rooms_visited"])
        self.assertIn("Carrier Drop", result["rooms_visited"])
        self.assertTrue(any("SYSOP HUB BBS" in line for line in outputs))


if __name__ == "__main__":
    unittest.main()
