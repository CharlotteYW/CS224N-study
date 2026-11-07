# Efficient neural network training

| | |
| --- | --- |
| Kind | Lecture |
| Priority | Core |
| Plan week | 20 |
| Status | Not Started |

Week 20: pair this 62:32 lecture with S01 PEFT. Keep the systems discussion focused on understanding training constraints.

## Why this is in the course

A transformer that fits in a lecture diagram does not fit in memory once the width, the batch, and the optimizer states are real. This lecture is the systems constraint behind 'just fine-tune the model'.

## Done when

You can say which of weights, gradients, and Adam state dominate memory for a large fine-tune, with explicit dtype assumptions and a separate accounting for activations.

## Resources

- [Spring 2024 recording, local L12 — 1:02:32](https://www.youtube.com/watch?v=UVX7SYGCKkA)
- [Spring 2024 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture12-training-shikhar.pdf)
- [Mixed precision training](https://arxiv.org/abs/1710.03740)
- [ZeRO](https://arxiv.org/abs/1910.02054)

Winter 2025 does not repeat this as its own numbered lecture. It folds the adaptation half (LoRA, prompting) into its lecture 11, which is lectures/s01-efficient-adaptation in this repo. Watch this 2024 video for the training-systems half.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Study gate

**Prerequisites:** Transformer parameters, gradients, optimizer state; L10.

Use the [roadmap](../../ROADMAP.md) for the minimal reading set and time budget, and
the [course map](../../COURSE_MAP.md) for source years. The existing concept checklist
in [summary.md](summary.md) is a target, not evidence of understanding.

- [ ] Required materials studied, with learner confirmation.
- [ ] Learner recall and questions recorded separately from assistant explanations.
- [ ] Relevant practice attempted; targeted assessment and gaps documented.
- [ ] Explicit user sign-off recorded in [progress](../../PROGRESS.md).
