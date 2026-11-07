# Recurrent neural networks and language models

| | |
| --- | --- |
| Kind | Lecture |
| Priority | Core |
| Plan week | 9 |
| Status | Not Started |

Week 09: study the lecture and implement or trace a tiny independent recurrence. Recall vanishing gradients the next day.

## Why this is in the course

Language is ordered. A language model is a distribution over the next word. An RNN is the first architecture in the course that carries a hidden state through that order, and the first one that breaks when the sequence gets long.

## Done when

You can explain vanishing gradients without the slides, including why a product of many small derivatives shrinks.

## Resources

- [Spring 2024 recording, local L05 — 1:18:52](https://www.youtube.com/watch?v=fyc0Jzr74y4)
- [Spring 2024 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture05-rnnlm.pdf)
- [Winter 2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture05-rnnlm.pdf)
- [Notes for lectures 5 and 6](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes05-LM_RNN.pdf)
- [Jurafsky and Martin, n-gram language models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [Karpathy on RNNs](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Understanding LSTM networks (preview for Lecture 6)](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

The 2024 Tuesday lecture compresses the RNN story. The 2025 site splits basic RNNs (its lecture 5) from LSTM/GRU and attention (its lecture 6). Watch the 2024 Lecture 5 video, and read the shared notes through the basic RNN sections. Save LSTM and attention for the next unit.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Study gate

**Prerequisites:** A2 foundation checkpoint and chain rule through shared parameters.

Use the [roadmap](../../ROADMAP.md) for the minimal reading set and time budget, and
the [course map](../../COURSE_MAP.md) for source years. The existing concept checklist
in [summary.md](summary.md) is a target, not evidence of understanding.

- [ ] Required materials studied, with learner confirmation.
- [ ] Learner recall and questions recorded separately from assistant explanations.
- [ ] Relevant practice attempted; targeted assessment and gaps documented.
- [ ] Explicit user sign-off recorded in [progress](../../PROGRESS.md).
