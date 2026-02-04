import unittest
from number_guess import check_guess, calculate_score, give_hint


class TestNumberGuess(unittest.TestCase):

    def test_check_guess(self):
        self.assertEqual(check_guess(50, 70), "HIGH")
        self.assertEqual(check_guess(50, 30), "LOW")
        self.assertEqual(check_guess(50, 50), "CORRECT")

    def test_calculate_score(self):
        self.assertEqual(calculate_score(2), 100)
        self.assertEqual(calculate_score(5), 70)
        self.assertEqual(calculate_score(8), 40)
        self.assertEqual(calculate_score(15), 10)

    def test_basic_hints(self):
        self.assertEqual(give_hint(60, [58]), "Very Close!")
        self.assertEqual(give_hint(60, [52]), "Close!")

    def test_history_range_narrowing(self):
        history = [20, 80]
        self.assertEqual(
            give_hint(60, history),
            "Try between 21 and 79"
        )

    def test_multiple_constraints(self):
        history = [10, 90, 40, 70]
        self.assertEqual(
            give_hint(60, history),
            "Close!"
        )

    def test_last_guess_only_is_wrong(self):
        history = [5, 95, 10]
        self.assertEqual(
            give_hint(50, history),
            "Try between 11 and 94"
        )

    def test_close_priority(self):
        history = [10, 90, 55]
        self.assertEqual(
            give_hint(60, history),
            "Very Close!"
        )


if __name__ == "__main__":
    unittest.main()
