# Word vectors

| | |
| --- | --- |
| Kind | Lecture |
| Priority | Core |
| Plan week | 1 |
| Status | Not Started |

About 3 hours for the lecture, selected notes, and recall, within Week 01. The first sitting is about 2 hours; read remaining notes in the next sitting.

## Why this is in the course

The course starts by replacing a word-as-symbol with a word-as-vector. Everything later (contextual states, attention, transformers) is a more careful version of this move.

## Done when

You can state the distributional hypothesis and say what skip-gram is optimizing, without the slides.

## Resources

- [Spring 2024 recording, local L01 — 1:20:17](https://www.youtube.com/watch?v=DzpHeXVSC5I)
- [Spring 2024 slides (match the video)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture01-wordvecs1.pdf)
- [Winter 2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture01-wordvecs1.pdf)
- [Winter 2025 notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n_winter2023_lecture1_notes_draft.pdf)
- [word2vec paper](https://arxiv.org/pdf/1301.3781.pdf)
- [Negative sampling paper](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)

The notes PDF was drafted for an earlier offering and kept on the 2025 site because the word2vec math is the same. Read it with the 2025 slides.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Study gate

**Prerequisites:** Dot products, shapes, elementary conditional probability, logs, and a basic chain rule.

Use the [roadmap](../../ROADMAP.md) for the minimal reading set and time budget, and
the [course map](../../COURSE_MAP.md) for source years. The existing concept checklist
in [summary.md](summary.md) is a target, not evidence of understanding.

- [ ] Required materials studied, with learner confirmation.
- [ ] Learner recall and questions recorded separately from assistant explanations.
- [ ] Relevant practice attempted; targeted assessment and gaps documented.
- [ ] Explicit user sign-off recorded in [progress](../../PROGRESS.md).

## First sitting: about 2 hours

Spend 10 minutes on a prerequisite diagnostic, watch the 80:17 recording with about
15 minutes for pauses, then spend 15 minutes on recall. Read the required notes in
the next sitting if needed.

Focus on distributional meaning, one-hot vs dense representations, center/outside
embeddings, conditional softmax, and gradient updates. While watching, consider:

1. What information about a word does its context provide?
2. What does skip-gram predict, and what is it conditioned on?
3. What does the softmax denominator normalize over?

Afterward, report the extent watched, your actual study time, and a short explanation
in your own words. The assistant will assess that explanation before any sign-off.

## Week 01: concrete study sessions

Goal: explain distributional meaning and the skip-gram prediction task, identify the
quantities in its objective, and resolve any prerequisite gaps. Plan for **9 hours**
across the sessions below. This is a flexible study week, not a calendar deadline.

| Session | Time | What to do | Evidence to bring back |
| --- | --- | --- | --- |
| 1. Diagnostic and lecture | 2 h | Briefly check shapes/dot products, then watch the Spring 2024 L01 video above with its matching slides. Pause on unclear notation. | Extent watched, actual time, a five-sentence explanation, and 2–3 questions. |
| 2. Minimal readings | 1.5 h | Read the 2025-linked L01 notes' introduction/objective sections (45 min), the differential calculus review's chain-rule material (30 min), and targeted NumPy broadcasting/matmul documentation (15 min). Links are in Week 01 of ROADMAP. | Your definitions of center word, outside word, embedding vector, and conditional probability; mark unclear symbols. |
| 3. Math practice | 2 h | On small invented examples, calculate a dot product and norm, normalize three scores with softmax, take the negative log probability of one outcome, and attempt a scalar chain-rule derivative. Use the time to repair gaps. | Your attempted calculations and reasoning, including mistakes/questions; no need for polished prose. |
| 4. NumPy and context practice | 2 h | Predict two fresh array-operation shapes before execution. Make a tiny corpus of 2–3 sentences, choose a context-window size, and enumerate center/outside pairs. Connect a matrix-vector product to one score per vocabulary item. | Predictions vs actual outputs, the context pairs, and an explanation of the score shapes. Reuse the existing NumPy notebook or chat; a new notebook is unnecessary. |
| 5. Recall and assessment | 1.5 h | Return for an interactive explanation/derivation check; repair the specific gaps it reveals and update learner notes/QA. | Assessment feedback, remaining gaps, reported study hours, and explicit sign-off only when ready. |

The original word2vec and negative-sampling papers are later/recommended reading;
they are not extra required Week 01 work. A1 starts in Week 02. Finish early if the
practice goals are demonstrated; report actual time rather than filling nine hours.

By the end, explain the distributional hypothesis, dense vs one-hot representations,
the two embedding roles, what skip-gram predicts, what softmax normalizes, and how a
gradient update changes a parameter. Attempt the objective/chain-rule reasoning and
document any unresolved parts. Completion requires the assessment plus your separate
`SIGN OFF: Lecture 01` and `SIGN OFF: Week 01` confirmations.
