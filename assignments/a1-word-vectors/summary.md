# Summary: Assignment 1: exploring word vectors

Status: Signed Off for self-study

## Why this unit exists

Assignment 1 makes you touch real vectors: similarity, analogy, and the biases sitting in a space that was trained on text. It is there so Lecture 1 and 2 are not only vocabulary.

## Learning goals and completion evidence

| Part | What to practice | What to explain afterward |
| --- | --- | --- |
| 1. Count-Based Word Vectors | Build a vocabulary and a word-context count matrix from a corpus. Use truncated SVD to represent words in two dimensions, then plot selected words. | What a row and a cell count represent, why vocabulary order matters, and which relationships a two-dimensional projection preserves or obscures. |
| 2. Prediction-Based Word Vectors | Explore pretrained GloVe vectors with cosine similarity, nearest neighbors, analogies, and bias probes. Compare observations with Part 1. | Why neighbors can reveal a word sense, why antonyms can be close, how analogy arithmetic can fail, and how patterns from the training corpus can appear in the vectors. |

For the first sitting, run the setup cells and independently attempt Question 1.1.
Use its checks to confirm the vocabulary handling before moving to the count
matrix in Question 1.2. Track the checks you ran and keep a short reflection
on one result that surprised you and one limitation of your interpretation.
The notebook lives in the assignment work directory and is tracked here as a private self-study copy.
This tracked file is for concepts, observed behavior, and review questions.

## Concepts you must be able to explain

- Cosine similarity as a ranking over a vocabulary
- Analogy as vector arithmetic, and when that arithmetic is a party trick
- What a bias in an embedding looks like when you query it
- The difference between reading a claim about word2vec and checking it on vectors

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

### Part 1 completion report

The learner reported completing Part 1. They reported passing the notebook checks
for Questions 1.2 and 1.3, shared their plotting approach for 1.4, and reported
no issue with 1.5. During debugging, they distinguished document positions
from vocabulary indices, handled the exclusive right window bound, and used
word indices to plot the selected rows.

### Part 2 self-study closeout

The learner generated the GloVe plot and observed that the three size-related
words clustered more tightly in its two-dimensional projection. They identified
vector arithmetic as the main idea behind analogy questions. They reviewed
assistant reference explanations and reported understanding the assignment
concepts and being ready to close the notebook. The reference examples cover
polysemy, similarity and antonymy, successful and failed analogies, and bias.

The assistant filled the Part 2 notebook with clearly labeled self-study answers
and runnable examples. The learner did not report running those added cells or
submitting the assignment. This closes A1 for personal study. It is not a record
of independent completion or a formal assessment.

## Explain without notes

- [ ] Cosine similarity as a ranking over a vocabulary
- [ ] Analogy as vector arithmetic, and when that arithmetic is a party trick
- [ ] What a bias in an embedding looks like when you query it
- [ ] The difference between reading a claim about word2vec and checking it on vectors

- [ ] The notebook runs, and summary.md says what surprised you in the nearest neighbors, not only that the code finished.
