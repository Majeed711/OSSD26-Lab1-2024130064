"""Small, dependency-free score statistics CLI used for Lab1 Git practice."""
import argparse
import math

DEFAULT_TITLE = "成绩统计 - B1 + C4"


def summarize(scores):
    """Return summary statistics for finite scores in the interval [0, 100]."""
    values = [float(score) for score in scores]
    if not values:
        raise ValueError("at least one score is required")
    if any(not math.isfinite(value) or not 0 <= value <= 100 for value in values):
        raise ValueError("scores must be finite numbers between 0 and 100")
    return {"count": len(values), "average": sum(values) / len(values),
            "passed": sum(value >= 60 for value in values),
            "minimum": min(values), "maximum": max(values)}


def main():
    parser = argparse.ArgumentParser(description=DEFAULT_TITLE)
    parser.add_argument("scores", nargs="+", type=float)
    args = parser.parse_args()
    try:
        result = summarize(args.scores)
    except ValueError as error:
        parser.error(str(error))
    print(DEFAULT_TITLE)
    for name, value in result.items():
        print(f"{name}: {value:.2f}" if isinstance(value, float) else f"{name}: {value}")


if __name__ == "__main__":
    main()
