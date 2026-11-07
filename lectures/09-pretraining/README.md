# Pretraining

| | |
| --- | --- |
| Kind | Lecture |
| Priority | Core |
| Plan week | 15 |
| Status | Not Started |

Week 15: compare pretraining objectives and explore model interfaces. The verified recording is Winter 2023; A4 starts in Week 16.

## Why this is in the course

Word2vec trained a vector and stopped. Pretraining trains a whole network on a huge amount of text, then that network is reused. The objective you choose (masked versus next-word) decides what the network is good at.

## Done when

You can contrast masked LM and causal LM with a one-line example of each, and say which one Assignment 4 is closer to.

## Resources

- [Winter 2023 slides matching the recording](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/slides/cs224n-2023-lecture9-pretraining.pdf)

- [Winter 2023 recording, local L09 — 1:18:46](https://www.youtube.com/watch?v=DGfCRXuNA2w)
- [Spring 2024 comparison slides (not the recording year)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture09-pretraining-updated.pdf)
- [Winter 2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture09-pretraining.pdf)
- [BERT](https://arxiv.org/pdf/1810.04805.pdf)
- [The Illustrated BERT, ELMo, and co.](http://jalammar.github.io/illustrated-bert/)
- [Jurafsky and Martin, masked language models](https://web.stanford.edu/~jurafsky/slp3/9.pdf)

The 2025 site does not link a long note for this lecture. The video and the 2025 slides are the source. The papers above are the ones worth reading, not the whole schedule list.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Study gate

**Prerequisites:** L08 attention, masks, and Transformer blocks.

Use the [roadmap](../../ROADMAP.md) for the minimal reading set and time budget, and
the [course map](../../COURSE_MAP.md) for source years. The existing concept checklist
in [summary.md](summary.md) is a target, not evidence of understanding.

- [ ] Required materials studied, with learner confirmation.
- [ ] Learner recall and questions recorded separately from assistant explanations.
- [ ] Relevant practice attempted; targeted assessment and gaps documented.
- [ ] Explicit user sign-off recorded in [progress](../../PROGRESS.md).
