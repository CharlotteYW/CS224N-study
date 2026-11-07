# Questions: Word vectors, word senses, and classifiers

Record a question when it comes up. After it is answered, keep the answer here, and mark whether it is still fuzzy. Fuzzy items are the start of the next session.

| Date | Question | Answer | Still fuzzy? |
| --- | --- | --- | --- |
| 2026-11-07 | What is negative sampling? | Skip-gram trains a binary discrimination objective on each observed pair and a few sampled noise pairs. The dot product goes into a sigmoid for each pair. The center row and the selected outside rows receive updates. | Understanding check pending. |
| 2026-11-07 | How many dot products are needed, and how are labels assigned? Does every word outside the sentence get label zero? | For one positive pair, full softmax scores all 100,000 vocabulary entries. With five sampled negatives, negative sampling scores six pairs. A context window over token positions yields observed positive pairs. Sampled noise pairs receive label zero for that training step. The sigmoid is the model prediction. Unselected words have no label for that step. | Learner follow-up pending. |
| 2026-11-07 | How does truncated SVD turn a word count row into a lower-dimensional embedding? | In the toy co-occurrence matrix with rows (3, 2, 0), (2, 3, 0), and (0, 0, 4), project each word row onto the first two right singular vectors. This gives the corresponding row of U_k Sigma_k. The kept directions capture the shared pet/vet pattern and the road pattern. The discarded direction measures the pet/vet difference. | Learner follow-up pending. |
| 2026-11-07 | How does GloVe use word-context counts? | GloVe fits the log of each positive count with the dot product of two low-dimensional vectors and two biases. It weights squared errors by count and skips zero-count cells. SVD truncates directions of the input matrix, while GloVe learns the vectors by optimizing its weighted objective. See [GloVe, equations 8–9](https://aclanthology.org/D14-1162.pdf). | Learner follow-up pending. |

## Open questions

- The learner restated how observed window pairs receive label one and sampled pairs receive label zero, then confirmed understanding. The compute comparison was explained by the assistant.
- Check whether the learner can identify what information the toy SVD discards.

## GloVe understanding check

- The learner correctly identified log(3) as the target for a count of three.
- The learner initially proposed zero as the target for an unseen pair. Feedback distinguished a skipped zero-count entry from the zero log target of a count-one entry.
- The learner asked whether SVD, GloVe, and skip-gram all produce word vectors. Each yields a fixed-length representation per vocabulary item. Skip-gram and GloVe use two embedding tables during training.

## Sparse coding and word senses

- Learner question: What is sparse coding in Lecture 02?
- Assistant explanation: Approximate a dense word embedding by a weighted sum of a few vectors from a shared learned dictionary. Sparsity applies to the coefficients. The lecture discusses how selected components can correspond to different senses of a word.
- Source: [Spring 2024 Lecture 02 slides, word senses section](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture02-wordvecs2.pdf).

## Trainable inputs in the neural window classifier

- Learner question: If the classifier learns W, how does it also learn the input word vectors? Does the input start as one-hot?
- Assistant explanation: The token ID or conceptual one-hot vector selects a column of the shared trainable embedding table L. The selected embeddings are concatenated into the window input x. Backpropagation sends the classification loss gradient through x into the selected columns of L when embeddings are trainable. Classifier parameters and the embedding table can be trained jointly.
- Source: [Spring 2024 Lecture 02, slides 35–38](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture02-wordvecs2.pdf#page=35).

## Lecture 02 recall before A1

- Learner recall: Skip-gram uses “bags of word,” negative sampling, and classification to update vectors. GloVe is unclear.
- Feedback: Skip-gram uses a center word to predict individual context words. With negative sampling, observed pairs and sampled noise pairs give binary training labels. CBOW predicts the center word from a combined representation of surrounding words. GloVe aggregates corpus-wide co-occurrence counts and uses the log of each nonzero count as a regression target.
- Follow-up: Identify the GloVe target for a count of ten and explain how a prediction below the target affects the update.

- Follow-up question: What do the dot product and two biases mean in GloVe?
- Assistant example: For the pair (cat, eats), the dot product of [1, 2] and [0.5, 0.3] is 1.1. The center bias 0.3 and context bias 0.1 give a predicted log count of 1.5. Each bias is a learned scalar shared across pairs involving that word in its corresponding role.
