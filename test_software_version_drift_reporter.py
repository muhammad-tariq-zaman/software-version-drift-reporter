import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import drift

def inst(h, s, v):
    return {"host": h, "software": s, "version": v}
def base(s, v):
    return {"software": s, "baseline_version": v}

class TestDrift(unittest.TestCase):
    def test_drift_detected(self):
        self.assertEqual(len(drift([inst("H1", "App", "1.0")], [base("App", "2.0")])), 1)
    def test_matching_clean(self):
        self.assertEqual(drift([inst("H1", "App", "2.0")], [base("App", "2.0")]), [])
    def test_unknown_software_ignored(self):
        self.assertEqual(drift([inst("H1", "Other", "9.9")], [base("App", "2.0")]), [])
    def test_fields(self):
        self.assertEqual(drift([inst("H1", "App", "1.0")], [base("App", "2.0")])[0], ("H1", "App", "1.0", "2.0"))
