# Assignment 2: word2vec derivatives and a dependency parser

| | |
| --- | --- |
| Kind | Assignment |
| Priority | Core |
| Plan week | 05–08 |
| Status | In Progress |

Winter 2025 source. Plan for 18–24 active hours across Weeks 05–08; unattended training is additional. The detailed weekly budget is in [ROADMAP](../../ROADMAP.md).

## Why this is in the course

This is the assignment that decides whether the course feels like a sequence of diagrams or like something you can derive. Part 1 is the naive-softmax gradient. Part 2 is Adam and dropout as ideas you will meet again. Part 3 is a feedforward parser in PyTorch.

## Done when

The written gradient is yours, the parser trains, and reviews/checkpoint-after-a2.md is answered closed-book.

## Resources

- [Winter 2025 handout](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2.pdf)
- [Winter 2025 starter zip](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2.zip)
- [LaTeX template](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2_tex.zip)
- Lecture 3: `lectures/03-backprop-and-neural-nets`
- Lecture 4: `lectures/04-dependency-parsing`

Unzip into assignments/a2-word2vec-and-dependency/work/ (gitignored). Study notes go in summary.md. The handout stays on the course site. Ask concept and debugging questions in qa.md. A finished solution does not get written into this repo.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [parts-1-2-reference.md](parts-1-2-reference.md) — worked answers requested for personal review in this private repository.

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Prerequisites and milestones

L01–04, calculus/shape checks, and the PyTorch tutorial.

- [ ] Part 1: independently attempt the naive-softmax mathematical problems (Week 05).
- [ ] Part 2: independently reason about Adam and dropout (Week 05).
- [ ] Part 3: build/test parser transitions and the neural parser; train and analyze errors (Weeks 06–08).
- [ ] Record actual checks and results; complete the foundation checkpoint and request A2 sign-off.

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
