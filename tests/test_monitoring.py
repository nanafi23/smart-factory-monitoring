import tempfile
import unittest
from pathlib import Path
from database import Database
from monitoring import get_status, health_score

class MonitoringTests(unittest.TestCase):
    def test_threshold_boundaries_and_vibration_override(self):
        for temp,vib,expected in [(75,80,'NORMAL'),(76,10,'WARNING'),
            (90,80,'WARNING'),(91,10,'CRITICAL'),(50,81,'CRITICAL')]:
            with self.subTest(temp=temp,vib=vib):
                self.assertEqual(get_status(temp,vib),expected)

    def test_score_bounds_and_load_direction(self):
        self.assertGreater(health_score(50,10),health_score(90,80))
        self.assertEqual(health_score(1000,1000),0)
        self.assertEqual(health_score(-100,-100),100)

    def test_persistence_and_history_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'test.db'
            db=Database(path)
            db.insert_reading(60,20,'NORMAL',64)
            db.insert_reading(100,90,'CRITICAL',23)
            db.close()
            db=Database(path)
            try:
                rows=db.fetch_all()
                self.assertEqual(len(rows),2)
                self.assertEqual(rows[0][1:],(100,90,'CRITICAL',23))
            finally:
                db.close()
