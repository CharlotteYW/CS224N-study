# Questions: Python and NumPy review

Record a question when it comes up. After it is answered, keep the answer here, and mark whether it is still fuzzy. Fuzzy items are the start of the next session.

| Date | Question | Answer | Still fuzzy? |
| --- | --- | --- | --- |
| 2026-09-26 | How do NumPy shape, broadcasting, and a vectorized operation work, compared with writing a Python loop? | An array's shape is the size of each axis: a vector is `(dim,)`, a matrix of word vectors is `(words, dim)`, a batch is `(batch, words, dim)`. A vectorized operation such as `words @ query` does the loop inside NumPy and returns one score per row. Broadcasting lines axes up from the right and stretches any axis of length 1, so `words + bias` with shapes `(3, 3)` and `(3,)` is still `(3, 3)`. | no |
| 2026-09-26 | Why is `words @ query` shape `(3,)` and not `(3, 1)`? What is the general rule when the shapes are not the same? | `(3,)` is a 1-D array, not a column. `@` multiplies along a shared inner axis and drops that axis. It does not stretch a mismatch, and it does not add an axis, so `(3, 3) @ (3,)` is `(3,)`. A column result `(3, 1)` happens only if the query is already shaped `(3, 1)`. `+`, `-`, `*`, and `/` are the operations that broadcast: pad missing axes with 1 on the left, then stretch any axis of length 1. | yes |
| 2026-09-26 | Do the shape rules change for 3-D, 4-D, and higher arrays? | No. Axes to the left of the matrix are a batch. For `@`, multiply the last two axes with the matrix rule, and broadcast only the batch axes. A 1-D operand is still not given an extra axis in the result. For `+` and `*`, keep aligning from the right and stretching axes of length 1, however many axes there are. | yes |

## Open questions

- Apply the stack rule at the bottom of `practice_numpy.ipynb` to the six higher-rank shapes. Still fuzzy until a batch axis is separated from the matrix axes before predicting.
