# Learning progress

Updated 2026-11-06 (America/Los_Angeles). Evidence and learner confirmations belong
here; [ROADMAP.md](ROADMAP.md) is the plan. No new learning is implied by planning work.

## Current state

- **Current week:** Week 01, In Progress only because the earlier NumPy session is
  already recorded complete. The new prerequisite diagnostic has not occurred.
- **Next lecture:** L01 Word Vectors — Not Started.
- **Current assignment:** none active; A1 is Not Started, planned for Weeks 02–03.
- **Availability:** learner confirmed 8–10 hours/week on 2026-11-02.
- **Additional progress:** learner confirmed on 2026-11-02 that no lectures or
  assignments have been completed beyond the saved record.
- **Primary source:** Winter 2025 coursework; 2024 videos with labeled 2023
  substitutions; selected 2026 updates. See [COURSE_MAP.md](COURSE_MAP.md).
- **Actual study hours:** not reported. Do not enter zero or substitute estimates.
- **Latest formal assessment:** none under the new rubric. No new sign-offs.
- **Blockers:** none for starting L01. Historical assignment package compatibility,
  full-training runtime, and course Colab access have not been tested.

## Preserved NumPy evidence

The existing [session README](sessions/01-python-numpy/README.md) and
[summary](sessions/01-python-numpy/summary.md) say `complete`; retain that history.
The summary dated **2026-09-27** records the learner's belief that they understand
matrix operations, correct broadcast predictions, and the corrected `(3,)` result
for matrix-vector multiplication. [QA](sessions/01-python-numpy/qa.md) dated
2026-09-26 contains explanations about broadcasting and higher-rank arrays.

The saved [notebook](sessions/01-python-numpy/practice_numpy.ipynb) contains execution
counts 1–4 and outputs for the initial exercise. Its original `(3, 1)` prediction
remains visible, along with the actual `(3,)` result. Later `rule_predictions` and
`stack_predictions` are still unfilled; those cells have no saved execution evidence.
The historical summary also leaves the arrays-vs-lists explanation unchecked.

These facts do not erase the old completion claim or establish a fresh assessment.
The new tracking status for an optional retention check is **Ready for Review**;
the learner need not repeat the entire session. Existing QA explanations are not
automatically treated as independently authored learner answers. Loading the official
Colab was historically checked off but was not independently reverified in this audit.

## Unit status

Allowed statuses: Not Started → In Progress → Ready for Review → Assessed → Signed Off.
Blocked records a concrete obstacle, not a mastery score. Assessed does not mean
mastered; the rubric and gaps must be read. Optional units may stay Not Started.

| Unit | Status | Evidence / plan |
| --- | --- | --- |
| Python/NumPy session | Ready for Review | Legacy `complete` preserved; optional fresh recall, not a new sign-off |
| [L01 — Word vectors](lectures/01-word-vectors/README.md) | Not Started | Week 1; no completion evidence |
| [L02 — Word vectors, word senses, and classifiers](lectures/02-word-vectors-and-language-models/README.md) | Not Started | Week 2; no completion evidence |
| [L03 — Backpropagation and neural network basics](lectures/03-backprop-and-neural-nets/README.md) | Not Started | Week 4; no completion evidence |
| [L04 — Dependency parsing](lectures/04-dependency-parsing/README.md) | Not Started | Week 6; no completion evidence |
| [L05 — Recurrent neural networks and language models](lectures/05-recurrent-neural-networks/README.md) | Not Started | Week 9; no completion evidence |
| [L06 — Sequence-to-sequence models, attention, and machine translation](lectures/06-seq2seq-and-machine-translation/README.md) | Not Started | Week 10; no completion evidence |
| [L07 — Final projects and a first look at the project](lectures/07-final-projects/README.md) | Not Started | Week 10; revisit 25; no completion evidence |
| [L08 — Transformers](lectures/08-transformers/README.md) | Not Started | Week 14; no completion evidence |
| [L09 — Pretraining](lectures/09-pretraining/README.md) | Not Started | Week 15; no completion evidence |
| [L10 — Post-training: SFT, RLHF, and DPO](lectures/10-post-training/README.md) | Not Started | Week 19; no completion evidence |
| [L11 — Benchmarking and evaluation](lectures/11-evaluation/README.md) | Not Started | Week 21; no completion evidence |
| [L12 — Efficient neural network training](lectures/12-efficient-training/README.md) | Not Started | Week 20; no completion evidence |
| [L13 — Speech brain-computer interfaces](lectures/13-speech-bci/README.md) | Not Started | Week Optional after 24; no completion evidence |
| [L14 — Reasoning and agents](lectures/14-agents/README.md) | Not Started | Week 23; no completion evidence |
| [L15 — Life after DPO](lectures/15-life-after-dpo/README.md) | Not Started | Week 24; no completion evidence |
| [L16 — ConvNets, tree recursive networks, and constituency parsing](lectures/16-convnets-treernns/README.md) | Not Started | Week Optional after 24; no completion evidence |
| [L17 — Responsible and human-centered NLP](lectures/17-responsible-nlp/README.md) | Not Started | Week 24 (2026 replacement); no completion evidence |
| [L18 — NLP, linguistics, and philosophy](lectures/18-linguistics-philosophy/README.md) | Not Started | Week Optional after 28; no completion evidence |
| [Ls01 — Efficient adaptation: prompting and PEFT](lectures/s01-efficient-adaptation/README.md) | Not Started | Week 20; no completion evidence |
| [Ls02 — Question answering and knowledge](lectures/s02-qa-and-knowledge/README.md) | Not Started | Week 22; no completion evidence |
| [PyTorch tutorial](sessions/02-pytorch/README.md) | Not Started | Weeks 06; no completion evidence |
| [Hugging Face tutorial](sessions/03-huggingface-transformers/README.md) | Not Started | Weeks 15; no completion evidence |
| [A1 — Winter 2025](assignments/a1-word-vectors/README.md) | Not Started | Weeks 02–03; no completion evidence |
| [A2 — Winter 2025](assignments/a2-word2vec-and-dependency/README.md) | Not Started | Weeks 05–08; no completion evidence |
| [A3 — Winter 2025](assignments/a3-neural-machine-translation/README.md) | Not Started | Weeks 11–13; no completion evidence |
| [A4 — Winter 2025](assignments/a4-transformers/README.md) | Not Started | Weeks 16–18; no completion evidence |
| [Final project](project/README.md) | Not Started | Weeks 25–28; tentative idea in 10; no completion evidence |
| Foundation checkpoint | Not Started | Week 08; reviews/checkpoint-after-a2.md |
| Sequence-model checkpoint | Not Started | Week 13; record an assessment when it occurs |
| Transformer/post-training checkpoint | Not Started | Week 21; reviews/checkpoint-after-a4.md |
| Final synthesis | Not Started | Week 28; reviews/synthesis.md |

## Current Week 01 checklist

- [ ] Prerequisite diagnostic attempted: shapes, calculus, probability, logarithms.
- [ ] L01 video watched, with extent confirmed by learner.
- [ ] Required L01 notes and targeted prerequisite readings studied.
- [ ] Independent toy word/context exercise and recall attempted.
- [ ] Learner explanation, assistant feedback, and gaps recorded separately.
- [ ] Interactive assessment completed and evidence linked.
- [ ] Explicit `SIGN OFF: Lecture 01` received.
- [ ] Explicit `SIGN OFF: Week 01` received.

The pre-existing NumPy session completion is documented above; it is not a checked
item for a newly administered diagnostic.

## Weekly evidence checklist

Use `[x]` only with learner confirmation or a linked artifact. M = materials;
N = learner notes/QA; P = practice; C = coursework/project milestone (or explicitly
record N/A); A = interactive assessment. User approval is a separate final column.
The row summarizes this revised plan, so the old NumPy session alone does not
complete Week 01's materials or assessment.

| Week | Status | M | N | P | C | A | User sign-off |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | In Progress | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 02 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 03 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 04 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 05 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 06 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 07 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 08 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 09 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 10 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 11 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 12 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 13 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 14 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 15 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 16 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 17 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 18 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 19 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 20 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 21 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 22 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 23 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 24 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 25 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 26 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 27 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |
| 28 | Not Started | [ ] | [ ] | [ ] | [ ] | [ ] | Pending |

## Readings and study time

All papers in [papers/README.md](papers/README.md) and all newly assigned lecture
readings are pending. No reading achievement was inferred from resource collection.

| Period | Planned active study | User-reported actual study | Unattended compute |
| --- | --- | --- | --- |
| Earlier NumPy session | Historical README estimate: about 2 h | Not reported | Not reported |
| Week 01 | 9 h | Not reported | Not reported |
| Weeks 02–28 | 9 h per week | Not reported | Not reported |

Add dated session entries only when actual time is reported; do not count this
repository setup or assistant source audit as the learner's study time.

## Assessment and knowledge gaps

No new rubric rating has been assigned. Conceptual understanding, mathematical
reasoning, implementation understanding, method comparison, and independent explanation
are **Not Yet Demonstrated under the new assessment process**. This is absence of a
new assessment, not a claim that the learner lacks these abilities.

- Retention to check: matrix-vector output rank and broadcasting of batch axes.
- Evidence gap: later notebook predictions/checks are unfinished or have no saved output.
- Evidence gap: arrays-vs-lists explanation remains unchecked in the old summary.
- Diagnostic pending: probability, logarithms, derivatives, and the chain rule.
- NLP topics have not yet been studied according to the learner's confirmation.

## Flexible review queue

| Concept | Suggested review | Evidence needed / follow-up |
| --- | --- | --- |
| NumPy shapes | Next study session (suggested 2026-11-03 or next available day), 10 min | Fresh predictions before execution; no automatic reset of legacy completion |
| L01 meaning and skip-gram | Immediately after confirmed viewing | Learner's short explanation; targeted feedback |
| L01 recall | About 7 days after confirmed completion; date not set yet | Explain objective and normalization without notes |
| Embeddings/backprop/parsing | Week 08 checkpoint | Interactive conceptual, math, implementation evidence |
| RNNs and attention | Week 13 checkpoint | Derivation and observed NMT error analysis |
| Transformers, post-training, evaluation | Week 21 checkpoint | Existing after-A4 review plus evidence-based follow-ups |
| Whole course | Week 28 | Oral project defense and synthesis |

No automatic reminders have been created. Shift reviews according to actual study,
and record exact dates once a lecture is confirmed complete.

## Sign-off history

No explicit sign-offs under this protocol. The historical NumPy `complete` status
is preserved as a legacy record, not converted into a fabricated approval command.

## Recommended next action

On 2026-11-06 the learner requested a local commit of the curriculum setup and a
clear Week 01 plan. The L01 README now breaks the week into five concrete sessions
totaling nine planned hours. No additional study, assessment, or sign-off was reported.

Start the [L01 pre-watch briefing](lectures/01-word-vectors/README.md): a short
prerequisite diagnostic, the 80:17 video, and an explanation in the learner's own
words. Total first sitting: about 2 hours. The required notes can be read in the
next sitting. Ask one diagnostic question first; do not provide a full answer key.
