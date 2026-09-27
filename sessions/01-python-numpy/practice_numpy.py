"""Practice for NumPy shape, broadcasting, and vectorized operations.

Use the course environment:

    source .venv/bin/activate
    python sessions/01-python-numpy/practice_numpy.py

Fill in `predicted_shapes` before you run the check. Each value is a tuple
of ints, the shape you expect, written before you look at the printed array.
"""

import numpy as np

words = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.2, 0.3, 0.9],
    ]
)
query = np.array([0.2, -0.1, 0.5])
bias = np.array([10.0, 20.0, 30.0])
column = np.array([[1.0], [2.0], [3.0]])
row = np.array([10.0, 20.0])

# Replace each None with the shape you predict, for example (3,) or (3, 2).
predicted_shapes = {
    "words": None,
    "query": None,
    "words @ query": None,
    "words + bias": None,
    "column + row": None,
}


def actual_shapes():
    return {
        "words": words.shape,
        "query": query.shape,
        "words @ query": (words @ query).shape,
        "words + bias": (words + bias).shape,
        "column + row": (column + row).shape,
    }


def main():
    print("words\n", words)
    print("query", query)
    print("words @ query", words @ query)
    print("words + bias\n", words + bias)
    print("column + row\n", column + row)

    print("\nShape check")
    for name, actual in actual_shapes().items():
        guessed = predicted_shapes[name]
        if guessed is None:
            print(f"  {name}: actual {actual}  (fill in your prediction)")
        elif tuple(guessed) == tuple(actual):
            print(f"  {name}: {actual}  correct")
        else:
            print(f"  {name}: you said {guessed}, actual {actual}")


if __name__ == "__main__":
    main()
