"""Equivalence classes: ordinary, boundary, empty, and invalid score inputs."""
import unittest
from grade_summary import summarize


class GradeSummaryTest(unittest.TestCase):
    def test_ordinary_scores(self):
        result = summarize([50, 60, 70, 80])
        self.assertEqual(result["count"], 4)
        self.assertEqual(result["average"], 65)
        self.assertEqual(result["passed"], 3)

    def test_boundaries(self):
        result = summarize([0, 59.99, 60, 100])
        self.assertEqual(result["passed"], 2)
        self.assertAlmostEqual(result["average"], 54.9975)

    def test_single_score(self):
        self.assertEqual(summarize([75])["average"], 75)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            summarize([])

    def test_invalid_values(self):
        for score in [-1, 101, float("inf"), float("nan")]:
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    summarize([score])


if __name__ == "__main__":
    unittest.main()
