# Assignment 4: self-supervised learning and fine-tuning transformers

| | |
| --- | --- |
| Kind | Assignment |
| Priority | Core |
| Plan week | 16–18; broader checkpoint 21 |
| Status | Not Started |

Winter 2025 source. Plan for 20–26 active hours across Weeks 16–18, plus unattended training. The broader checkpoint is in Week 21. See [ROADMAP](../../ROADMAP.md) for the weekly budget.

## Why this is in the course

The official handout is titled Self-Attention, Transformers, and Pretraining. It combines mathematical attention reasoning, a research codebase, pretraining/fine-tuning experiments, and rotary position encodings.

## Done when

All required mathematical/programming/experiment work is independently complete, actual checks and limitations are recorded, and the learner explains the results. The broader checkpoint follows in Week 21 after post-training and evaluation.

## Resources

- [Winter 2025 handout](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a4.pdf)
- [Winter 2025 starter zip](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a4.zip)
- [LaTeX template](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a4_tex.zip)
- [Colab run script](https://colab.research.google.com/drive/1vp_6RYYqMhjVIzt2MRhuWnBBmz4BJ30j?usp=sharing)
- Lecture 8: `lectures/08-transformers`
- Lecture 9: `lectures/09-pretraining`
- Related tutorial: `sessions/03-huggingface-transformers` (not an assumed A4 dependency)

Unzip into assignments/a4-transformers/work/ (gitignored). L10 is not a prerequisite for this assignment. It is required before the broader Week 21 review.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Prerequisites and milestones

L08–09, attention/masks/positions, pretraining objectives, and PyTorch. Hugging Face is useful tutorial practice, not an assumed starter dependency.

- [ ] Attempt the mathematical attention questions independently; inspect the 2025 codebase and environment.
- [ ] Implement required pretraining/fine-tuning milestones; run the specified comparisons independently.
- [ ] Finish rotary-position requirements, remaining experiments, and written analysis; retain actual test/metric evidence.
- [ ] Explain architecture, objectives, and results; assess and request A4 sign-off. Complete the wider review after L10/L11 in Week 21.

## Evidence and coaching boundary

Keep official written answers, starter code, implementations, and submission artifacts
in this folder's ignored `work/` directory. Public summary/QA records concepts,
learner questions, allowed hints, mistakes/corrections, and non-solution reflections.
Record tests only when actually run, including command, runner, outcome, and limits.
For completion, satisfy all official required tasks, explain your reasoning, document
remaining limitations, complete an assessment, and explicitly sign off.

Follow the [2025 policy](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/):
no AI-generated final answers or completed TODOs. A1/A2 review may identify issues
without solving them; A3/A4 support follows the course's TA code-inspection limit and
uses conceptual questions, unrelated examples, and debugging strategies. Access to
Gradescope, course credits, or cloud resources is not assumed. A reduced experiment
must be labeled reduced and does not establish full official completion.
