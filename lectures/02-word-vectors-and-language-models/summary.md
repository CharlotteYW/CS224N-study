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

## Explain without notes

- [ ] Negative sampling as the practical replacement for the full softmax (independent practice in Week 03; Winter 2025 A2 uses naive softmax)
- [ ] Co-occurrence counts, and the idea behind GloVe: fit vectors to statistics you can count
- [ ] Cosine similarity
- [ ] Intrinsic evaluation (analogy, similarity) versus extrinsic evaluation (a real task)
- [ ] Why one vector per word type smears distinct senses together
- [ ] A window classifier and softmax as the step from embeddings into neural networks

- [ ] Co-occurrence, analogy, and cosine similarity are in your own words, and Assignment 1 is underway.
