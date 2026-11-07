# Questions: Word vectors

Record a question when it comes up. After it is answered, keep the answer here, and mark whether it is still fuzzy. Fuzzy items are the start of the next session.

| Date | Question | Answer | Still fuzzy? |
| --- | --- | --- | --- |
| | | | |

## Open questions

- None yet.

## Latest study discussion

- Learner question: What do the trainable skip-gram parameters look like for a tiny vocabulary, and how do we differentiate the loss?
- Assistant explanation: Two embedding tables, one for each role. With full softmax, the score gradient is predicted probability minus target indicator. Apply the dot-product chain rule to the active center row and each outside row.
- Learner derivation and understanding check pending.

## Gensim demo outputs reported by the learner

- The five nearest neighbors of `bank` were `banks` (0.806), `banking` (0.753), `credit` (0.704), `investment` (0.694), and `financial` (0.678).
- Cosine similarity for `cat` / `dog` was 0.87980753 and for `cat` / `car` was 0.31097826.
- Learner interpretation: The words are close because the study material is financial.
- Feedback: The neighbors indicate the financial sense of `bank`. The demo loads pretrained GloVe vectors trained on Wikipedia 2014 and Gigaword 5. The relevant link is how often words occur in similar contexts in that corpus. The displayed neighbors provide evidence about the representation, and the corpus is identified separately by the [Stanford GloVe release](https://nlp.stanford.edu/projects/glove/).
- Follow-up: Predict how the nearest neighbors might change if the vectors were trained on a corpus dominated by descriptions of rivers.
- Learner prediction: `river` would be a plausible neighbor in a river-heavy corpus. The explanation for the predicted change is pending.
