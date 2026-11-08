# Summary: Word vectors, word senses, and classifiers

Status: In Progress

## Why this unit exists

Lecture 1 builds vectors by prediction. This lecture asks whether counting co-occurrence works as well, how to tell a good vector space from a bad one, and how a classifier on those vectors becomes a neural net.

## Concepts you must be able to explain

- Negative sampling as the practical replacement for the full softmax (independent practice in Week 03; Winter 2025 A2 uses naive softmax)
- Co-occurrence counts, and the idea behind GloVe: fit vectors to statistics you can count
- Cosine similarity
- Intrinsic evaluation (analogy, similarity) versus extrinsic evaluation (a real task)
- Why one vector per word type smears distinct senses together
- A window classifier and softmax as the step from embeddings into neural networks

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

### Guided recall before A1

- The learner correctly restated that observed context-window pairs receive positive labels and sampled noise pairs receive negative labels. Feedback clarified the prediction direction in skip-gram and CBOW.
- In the GloVe example, the learner identified the log-count target for a count of three and confirmed that the embedding vectors and biases are learned. Feedback distinguished a skipped zero-count cell from a zero target for a count of one.
- Assistant walkthroughs covered truncated SVD as projection, sparse coding for word senses, and how a classifier backpropagates into a trainable embedding table. Independent derivations were not demonstrated in this session.
- The learner requested to proceed to A1. Assigned reading confirmation and formal lecture sign-off remain pending.

## Assistant reference before A1

| Method | Training signal | Parameters or factors | How the vectors are obtained |
| --- | --- | --- | --- |
| Skip-gram | Given a center token, score one observed context token per positive pair. | Center table V and output context table U. | Compute a prediction loss and update the tables by gradient descent. |
| CBOW | Combine the surrounding token vectors and predict the center token. | Input context table and output center table. | Update the output rows and backpropagate through the context combination into the input rows. |
| GloVe | Fit the log of each positive corpus-wide co-occurrence count. | Center and context embedding tables plus a scalar bias per word in each role. | Minimize weighted squared error with gradient-based optimization. |
| Truncated SVD | Approximate the word-context count matrix with a chosen rank. | Singular vectors and singular values computed from the matrix. | Factor the matrix and keep its top directions. One word representation is the corresponding row of the projected matrix. |

### Small parameter updates

All prediction examples below use a learning rate of 0.1 and evaluate gradients
using the old parameters. The Word2Vec examples use negative sampling. For a
score s and binary label y, the score gradient is sigmoid(s) minus y. With full
softmax the gradient is the predicted class probability minus its target
indicator, and the calculation includes the entire output vocabulary.

- **Skip-gram.** Use `cat` as the center, `eats` as the observed context, and
  `car` as a sampled negative. Let the one-dimensional values be
  v_cat = 1, u_eats = 0, and u_car = 1. The scores are 0 and 1. Their gradients
  are -0.5 and about 0.731. The updated values are u_eats = 0.05,
  u_car = 0.927, and v_cat = 0.927. The input update combines both score paths.
- **CBOW.** Use `the` and `eats` to predict center token `cat`. Their input
  embeddings are 0.5 and 1.5, so the average is 1. Let the output embeddings
  for target `cat` and sampled negative `car` be 0 and 1. The same output
  gradients as above give updated output embeddings of 0.05 and 0.927.
  The average receives a gradient of about 0.731. Each input embedding receives
  half, so they become about 0.463 and 1.463.
- **GloVe.** For a count of 10, let the center and context vectors be [1, 2]
  and [0.5, 0.3], with respective biases 0.3 and 0.1. The prediction is 1.5
  and the target is log(10), about 2.303. With the paper's weighting function,
  f(10) = (10/100)^0.75, the gradient with respect to the prediction is
  2 f(10) (1.5 - log(10)), about -0.285. Each bias has this gradient.
  The center vector gradient is this scalar times the context vector and
  vice versa. One step moves the center bias to about 0.329 and the first
  center coordinate to about 1.014. Zero counts are skipped.
- **SVD.** For the toy rows [3, 2, 0], [2, 3, 0], and [0, 0, 4],
  keep the directions [1, 1, 0]/sqrt(2) and [0, 0, 1]. The first word's
  vector becomes [5/sqrt(2), 0]. This is a projection using the
  factorization, with no per-word SGD update in the example.

The input embedding table in a supervised window classifier is another way
to learn word representations. If that table is trainable, the task loss
updates the embeddings selected by the window as well as the classifier
weights. Sparse coding instead re-expresses embeddings that already exist.

Sources: [Lecture 02 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture02-wordvecs2.pdf),
[Word2Vec negative sampling](https://proceedings.neurips.cc/paper_files/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf),
and [GloVe equations 8–9](https://aclanthology.org/D14-1162.pdf).

## Explain without notes

- [ ] Negative sampling as the practical replacement for the full softmax (independent practice in Week 03; Winter 2025 A2 uses naive softmax)
- [ ] Co-occurrence counts, and the idea behind GloVe: fit vectors to statistics you can count
- [ ] Cosine similarity
- [ ] Intrinsic evaluation (analogy, similarity) versus extrinsic evaluation (a real task)
- [ ] Why one vector per word type smears distinct senses together
- [ ] A window classifier and softmax as the step from embeddings into neural networks

- [ ] Co-occurrence, analogy, and cosine similarity are in your own words, and Assignment 1 is underway.
