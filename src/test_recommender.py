import unittest
from recommender import cosine_common, predict_user_knn


class TestCollaborativeFiltering(unittest.TestCase):
    def test_cosine_identical(self):
        self.assertAlmostEqual(cosine_common({"m1": 4, "m2": 2}, {"m1": 4, "m2": 2}), 1.0)

    def test_cosine_no_common(self):
        self.assertEqual(cosine_common({"a": 5}, {"b": 5}), 0.0)

    def test_prediction(self):
        data = {"u1": {"m1": 5}, "u2": {"m1": 5, "m2": 4}}
        result, _ = predict_user_knn(data, "u1", "m2", 1)
        self.assertAlmostEqual(result, 4.0)


if __name__ == "__main__":
    unittest.main()
