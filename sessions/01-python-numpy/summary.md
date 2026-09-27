# Summary: Python and NumPy review

Status: complete

## Why this unit exists

Every assignment is Python. The failure mode this session prevents is writing correct math as a slow Python loop, or losing a dimension in a NumPy shape.

## Concepts you must be able to explain

- NumPy arrays versus Python lists, and why the difference matters for a corpus
- Shapes: what a vector, a matrix, and a batch look like
- Broadcasting, and the bugs it hides
- Vectorized computation instead of iterating tokens in pure Python

## My study notes

### 2026-09-27

I think I have understood NumPy's matrix operations.

The broadcast predictions `words + bias` as `(3, 3)` and `column + row` as `(3, 2)` were right. `words @ query` is `(3,)`, not `(3, 1)`. `+` and `-` stretch an axis of length 1. `@` multiplies on the shared inner axis and does not stretch that axis. Axes to the left of the matrix are a batch.

## Explain without notes

- [ ] NumPy arrays versus Python lists, and why the difference matters for a corpus
- [x] Shapes: what a vector, a matrix, and a batch look like
- [x] Broadcasting, and the bugs it hides
- [x] Vectorized computation instead of iterating tokens in pure Python

- [x] You can predict the shape of a broadcasted operation before you run it, and you can load the course Colab.
