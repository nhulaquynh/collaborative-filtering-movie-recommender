"""Educational collaborative filtering: cosine similarities on co-rated entries.
This is a small reproducible demo, not a validated recommender benchmark.
"""
import argparse
import csv
import math
from collections import defaultdict


def read_ratings(path):
    ratings = defaultdict(dict)
    with open(path, encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            value = float(row["rating"])
            if not 1 <= value <= 5:
                raise ValueError("Rating must be in [1,5]")
            ratings[row["user"]][row["item"]] = value
    return dict(ratings)


def cosine_common(left, right):
    common = left.keys() & right.keys()
    if not common:
        return 0.0
    dot = sum(left[i] * right[i] for i in common)
    norma = math.sqrt(sum(left[i] ** 2 for i in common))
    normb = math.sqrt(sum(right[i] ** 2 for i in common))
    return dot / (norma * normb) if norma * normb else 0.0


def predict_user_knn(ratings, user, item, k=2):
    if user not in ratings:
        raise ValueError("Unknown user")
    if item in ratings[user]:
        return ratings[user][item], []
    neighbors = []
    for other, other_ratings in ratings.items():
        if other != user and item in other_ratings:
            weight = cosine_common(ratings[user], other_ratings)
            if weight > 0:
                neighbors.append((weight, other, other_ratings[item]))
    neighbors.sort(reverse=True)
    neighbors = neighbors[:k]
    if not neighbors:
        return None, []
    score = sum(weight * value for weight, _, value in neighbors) / sum(weight for weight, _, _ in neighbors)
    return max(1., min(5., score)), neighbors


def main():
    p = argparse.ArgumentParser(description="Educational User-KNN movie predictor")
    p.add_argument("--input", default="data/ratings.csv")
    p.add_argument("--user", default="u1")
    p.add_argument("--item", default="m4")
    p.add_argument("--k", type=int, default=2)
    args = p.parse_args()
    if args.k < 1:
        p.error("k must be >= 1")
    ratings = read_ratings(args.input)
    score, neighbors = predict_user_knn(ratings, args.user, args.item, args.k)
    print(f"User: {args.user}, item: {args.item}, k={args.k}")
    print("Prediction:", f"{score:.4f}" if score is not None else "Not enough neighbors")
    for similarity, user, rating in neighbors:
        print(f"neighbor={user}; similarity={similarity:.4f}; rating={rating:.1f}")


if __name__ == "__main__":
    main()
