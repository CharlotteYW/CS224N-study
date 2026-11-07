# Sequence-to-sequence models, attention, and machine translation

| | |
| --- | --- |
| Kind | Lecture |
| Priority | Core |
| Plan week | 10 |
| Status | Not Started |

Week 10: study this lecture and the attention portion of L07 before beginning A3 in Week 11.

## Why this is in the course

Translation is two sequences of different lengths. The encoder compresses the source. The decoder produces the target. Attention is how the decoder looks back, and it is the idea the transformer will keep after it throws the recurrence away.

## Done when

You can draw encoder, decoder, and attention weights for one decoding step, and say what the weights are a distribution over.

## Resources

- [Spring 2024 recording, local L06 — 1:17:09](https://www.youtube.com/watch?v=Ba6Fn1-Jsfw)
- [Spring 2024 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture06-fancy-rnn.pdf)
- [Winter 2025 slides (advanced RNNs and attention)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture06-fancy-rnn.pdf)
- [Notes for lectures 5 and 6](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes05-LM_RNN.pdf)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf)
- [Bahdanau attention](https://arxiv.org/pdf/1409.0473.pdf)
- [Attention and augmented RNNs](https://distill.pub/2016/augmented-rnns/)
- [Colah, Understanding LSTM networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

Year mismatch to keep straight: the 2024 video for this slot is sequence-to-sequence and machine translation. The 2025 lecture of the same number is advanced RNNs and attention, and the slide filename on both sites is fancy-rnn. Watch the 2024 video for the translation system. Read the 2025 slides and the shared notes for LSTM/GRU and the attention equations. Assignment 3 needs both.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Study gate

**Prerequisites:** L05 RNNs and backpropagation through time.

Use the [roadmap](../../ROADMAP.md) for the minimal reading set and time budget, and
the [course map](../../COURSE_MAP.md) for source years. The existing concept checklist
in [summary.md](summary.md) is a target, not evidence of understanding.

- [ ] Required materials studied, with learner confirmation.
- [ ] Learner recall and questions recorded separately from assistant explanations.
- [ ] Relevant practice attempted; targeted assessment and gaps documented.
- [ ] Explicit user sign-off recorded in [progress](../../PROGRESS.md).
