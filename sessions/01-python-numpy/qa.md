# Questions: Python and NumPy review

Record a question when it comes up. After it is answered, keep the answer here, and mark whether it is still fuzzy. Fuzzy items are the start of the next session.

| Date | Question | Answer | Still fuzzy? |
| --- | --- | --- | --- |
| 2026-09-26 | How do NumPy shape, broadcasting, and a vectorized operation work, compared with writing a Python loop? | An array's shape is the size of each axis: a vector is `(dim,)`, a matrix of word vectors is `(words, dim)`, a batch is `(batch, words, dim)`. A vectorized operation such as `words @ query` does the loop inside NumPy and returns one score per row. Broadcasting lines axes up from the right and stretches any axis of length 1, so `words + bias` with shapes `(3, 3)` and `(3,)` is still `(3, 3)`. Predict that result shape before running the code. | yes |

## Open questions

- Predict the five shapes in `sessions/01-python-numpy/practice_numpy.py` before running the check. Still fuzzy until those predictions match.
