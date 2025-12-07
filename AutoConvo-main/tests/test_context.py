import unittest
from src.context_tracker import ContextTracker

class TestContextTracker(unittest.TestCase):
    def test_context_resolution(self):
        tracker = ContextTracker()
        tracker.update("get_contact_info", {"name": "Pranjal"})
        resolved = tracker.resolve("Call him")
        self.assertIn("Pranjal", resolved)

if __name__ == "__main__":
    unittest.main()
