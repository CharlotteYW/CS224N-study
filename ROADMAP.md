# CS224N self-paced roadmap

Plan revised 2026-11-03 (availability/progress confirmed 2026-11-02). The learner confirmed **8–10 hours/week** and no additional
lectures/assignments beyond the saved NumPy record. This is a plan, not achievement.
Actual status and approvals live in [PROGRESS.md](PROGRESS.md).

## Scope and pace

Use **Winter 2025 coursework**, the **Spring 2024 public video collection with
explicit 2023 substitutions**, and selected **Winter 2026** updates. See
[COURSE_MAP.md](COURSE_MAP.md) for verified links, provenance, mismatches, and limitations.

The core plan has **28 active weeks × 9 hours = 252 planned active hours**. Allow
**2–4 buffer weeks** for prerequisites, debugging, travel, or longer experiments:
roughly **7–8 months**, without fixed calendar deadlines. Pause the week counter
when its prerequisites are unmet. Review the estimate after A1 and A2. Full completion
of the default GPT-2 project may need **4–8 additional weeks**, to be re-estimated at
the proposal; the 28-week plan budgets a deliberately small custom project instead.
Unattended training time is tracked separately. No purchase or cloud run is scheduled.

**Required** means the weekly tasks below, including the specified portions of papers.
**Recommended** material repairs gaps or expands context; it replaces spare practice
time or goes into a buffer week. **Optional** deep dives never gate core sign-off.
Do not read every resource linked in an old lecture README. The minimal weekly set
below is the assignment. A stated reading time is a planning estimate, not a claim
that a paper has been read. Full paper deep reads beyond the named sections are optional.

Core outcomes: independently reason about representations, gradients, recurrent
models and attention; understand pretraining and post-training; critique research
evidence; complete official coursework independently; and execute a small reproducible
NLP investigation. Systems connections remain brief and complementary to ai-infra-lab.

## Weekly working agreement

At the start of each week, read progress and unresolved QA before choosing sessions.
Split the nine hours across, for example, two 2-hour concept sessions, one 3-hour
coding block, and two 1-hour recall/review sessions. Adjust to actual availability.

Each week ends only after: named materials studied with user confirmation; dated
learner notes and questions recorded; exercises attempted with evidence; the named
assignment/project milestone reviewed; an interactive assessment conducted; gaps
repaired or explicitly accepted; and the user's `SIGN OFF: Week NN`. Lecture and
assignment sign-offs are separate. Every week's approval is **pending** initially.
Checkboxes and evidence are maintained in PROGRESS, not inferred from this document.

Video rows include exact recording year, runtime, and slides. Budget allows pauses;
supplements without a public recording explicitly use slides. If a source cannot be
opened when study starts, mark the task blocked or choose an explicit substitute.
Do not count an unavailable recording as watched.

Assignment rows inherit the prerequisites, private deliverables, and test/assessment
requirements in their existing README. Never place final official answers in public
summaries. No submission-ready solutions are provided by the assistant. The 2025
TA code-review limits apply to coaching; A3/A4/project support is conceptual.

Assessment prompts below state learning targets, not a full exam or answer key.
Ask them interactively and wait. Review each important concept immediately after
study, about one week later, and at Weeks 8, 13, 21, and 28. Schedule actual dates from
confirmed completion rather than from an assumed start date.

## Weekly overview

| Week | Topic | Planned active hours |
| --- | --- | --- |
| 01 | Prerequisite diagnostic and word vectors | 9 |
| 02 | Word-vector geometry and A1 start | 9 |
| 03 | A1 finish and negative sampling | 9 |
| 04 | Backpropagation foundations | 9 |
| 05 | A2 mathematics and optimization | 9 |
| 06 | Dependency parsing and PyTorch | 9 |
| 07 | A2 parser implementation | 9 |
| 08 | A2 completion and foundation checkpoint | 9 |
| 09 | Language models and recurrent networks | 9 |
| 10 | Sequence-to-sequence, attention, and early project orientation | 9 |
| 11 | A3 implementation milestones | 9 |
| 12 | A3 training and decoding | 9 |
| 13 | A3 analysis and sequence-model checkpoint | 9 |
| 14 | Self-attention and Transformers | 9 |
| 15 | Pretraining objectives and model interfaces | 9 |
| 16 | A4 attention mathematics and codebase orientation | 9 |
| 17 | A4 pretraining and fine-tuning comparisons | 9 |
| 18 | A4 rotary positions and assignment assessment | 9 |
| 19 | Post-training: SFT, RLHF, and DPO | 9 |
| 20 | Efficient adaptation and training constraints | 9 |
| 21 | Evaluation and the second major checkpoint | 9 |
| 22 | Question answering, retrieval, and knowledge | 9 |
| 23 | Reasoning and agents | 9 |
| 24 | Preference research and responsible NLP | 9 |
| 25 | Project proposal and feasibility gate | 9 |
| 26 | Project baseline and milestone | 9 |
| 27 | Project comparison and error analysis | 9 |
| 28 | Project report, oral defense, and synthesis | 9 |

## Week 01: Prerequisite diagnostic and word vectors

**Goal / expected outcome:** Explain why context can define a representation and name the variables in skip-gram.

**Prerequisites:** Existing NumPy study; no lecture assumed complete. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L01: Lecture 1 - Intro and Word Vectors** (Spring 2024, 1:20:17) — [video](https://www.youtube.com/watch?v=DzpHeXVSC5I), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture01-wordvecs1.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture01-wordvecs1.pdf); focus on distributional meaning, one-hot vs dense vectors, two embedding matrices, and softmax.

**Required readings — 1.5 h:** [2025-linked lecture notes 01][notes01] introduction/objective (45 min); [Differential calculus review][calculus] chain-rule review (30 min); [NumPy broadcasting][broadcast] and [NumPy matmul][matmul] targeted refresh (15 min).

**Assignments / project — 0 h:** None yet. A1 starts after L02.

**Practice and review — 4.5 h:** Diagnose dot products, norms, conditional probability, log likelihood, partial derivatives, and chain rule. Predict two fresh NumPy shapes before running them; do not erase the old notebook mistake. Use a tiny invented vocabulary to identify center/context pairs. Keep the remaining time for prerequisite repair.

**Understanding check — 1.5 h:** Explain distributional evidence in your own words. Identify what a vocabulary softmax normalizes over; derive one scalar chain-rule example. Record unknowns rather than guessing a mastery rating.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 01`).

## Week 02: Word-vector geometry and A1 start

**Goal / expected outcome:** Compare prediction and counting methods; use similarity with appropriate skepticism.

**Prerequisites:** Week 1 prerequisites; L01 recall attempted. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L02: Lecture 2 - Word Vectors and Language Models** (Spring 2024, 1:19:12) — [video](https://www.youtube.com/watch?v=nBor4jfWetQ), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture02-wordvecs2.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture02-wordvecs2.pdf); focus on co-occurrence, cosine, evaluation, polysemy, and classifiers.

**Required readings — 1 h:** [2025-linked lecture notes 02][notes02] co-occurrence and evaluation sections (1 h). [Pennington et al., 2014: GloVe][glove] is recommended later, not extra required reading this week.

**Assignments / project — 4 h:** [Winter 2025 A1 official notebook ZIP][a1]: inspect instructions/environment, attempt the co-occurrence and low-dimensional visualization portion independently. Deliverable: local notebook attempts and a non-solution observation log.

**Practice and review — 1.5 h:** Compute cosine on small hand-written vectors; explain a failure of analogy evaluation. Recall L01 without notes.

**Understanding check — 1 h:** Why can a count-based and a predictive method yield useful vectors? What does a nearest-neighbor result fail to establish? Derive cosine similarity and identify its zero-norm edge case.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 02`).

## Week 03: A1 finish and negative sampling

**Goal / expected outcome:** Interpret embedding experiments and distinguish negative sampling from full softmax.

**Prerequisites:** L01–02 and A1 initial attempt. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video; rewatch only a weak section of L01/L02 within practice time.

**Required readings — 1.5 h:** [Mikolov et al., 2013: Distributed Representations of Words and Phrases][neg] introduction and negative-sampling/subsampling sections (1 h); re-read A1 instructions (30 min).

**Assignments / project — 4.5 h:** [Winter 2025 A1 official notebook ZIP][a1]: finish remaining vector exploration and written interpretation; rerun the notebook yourself. Keep answers private. Deliverable: recorded command/kernel, outputs, observations, and unresolved limitations.

**Practice and review — 2 h:** Outside official A1/A2, write the binary positive/negative prediction objective and compare its computation with full vocabulary normalization. Prepare a short paper recall note after reading.

**Understanding check — 1 h:** Explain an actual surprising neighbor and one bias/measurement limitation. Discuss the sampled objective without claiming it is an exact softmax probability. Assess A1 and request its sign-off separately.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 03`).

## Week 04: Backpropagation foundations

**Goal / expected outcome:** Trace gradients through a computation graph and check an independent toy derivative.

**Prerequisites:** Vector shapes, partial derivatives, probability, logarithms. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L03: Lecture 3 - Backpropagation, Neural Network** (Spring 2024, 1:13:27) — [video](https://www.youtube.com/watch?v=HnliVHU2g9U), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture03-neuralnets.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture03-neuralnets.pdf); focus on local derivatives, vector-Jacobian products, nonlinearities, loss, and gradient descent.

**Required readings — 1.5 h:** [2025-linked lecture notes 03][notes03] graph/gradient sections (1 h); [Matrix calculus notes][matrix] notation and shape conventions (30 min).

**Assignments / project — 0 h:** No official answers this week; A2 begins after the conceptual diagnostic.

**Practice and review — 4.5 h:** On an unrelated two-layer toy scalar-output model, label every shape, attempt a gradient, and compare with finite differences. Use a binary loss example separate from the official word2vec problems. Record your code/check results only after running them.

**Understanding check — 1.5 h:** Why are two linear layers still linear? Explain backward accumulation when a value has two consumers. Derive a toy chain rule and diagnose a wrong-shaped gradient.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 04`).

## Week 05: A2 mathematics and optimization

**Goal / expected outcome:** Produce your own Word2Vec derivations and explain optimizer/regularization choices.

**Prerequisites:** L01–03; independent chain-rule practice reviewed. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video; revisit L03 only for an identified gap.

**Required readings — 1 h:** [Winter 2025 A2 official handout][a2] Parts 1–2 and notation (30 min); [2025-linked lecture notes 03][notes03] targeted gradient review (30 min).

**Assignments / project — 6 h:** Winter 2025 A2 Parts 1–2: independently attempt naive-softmax derivatives and Adam/dropout reasoning. Deliverable: private working derivations plus a public list of topics attempted and questions. This release does not require the older negative-sampling coding assignment.

**Practice and review — 1 h:** Reason about a scalar optimizer step and expected activation under dropout using a separate example. Revisit an old shape error.

**Understanding check — 1 h:** Explain the shape convention used in your derivation, what accumulates across examples, and why training/evaluation behavior differs. Discuss reasoning without having the assistant write official answers.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 05`).

## Week 06: Dependency parsing and PyTorch

**Goal / expected outcome:** Explain a transition parser and construct an independent miniature training loop.

**Prerequisites:** L03 and A2 mathematical attempts; tensor shapes. **Estimated effort:** 9 hours.

**Lecture videos — 2.5 h:** **L04: Lecture 4 - Dependency Parsing** (Spring 2024, 1:18:57) — [video](https://www.youtube.com/watch?v=KVKvde-_MYc), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture04-dep-parsing.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture04-dep-parsing.pdf); focus on stack, buffer, transitions, features, and action prediction. Also [PyTorch tutorial, Drew Kaul, 2023, 47:01](https://www.youtube.com/watch?v=Uv0AIRr3ptg).

**Required readings — 1.5 h:** [2025-linked lecture notes 04][notes04] transition parsing (45 min); [PyTorch autograd tutorial][autograd] (30 min); [PyTorch MPS notes][mps] device checks (15 min).

**Assignments / project — 2 h:** [Winter 2025 A2 official handout][a2] Part 3: read requirements and attempt transition-system milestones independently. Inspect starter requirements before changing the local environment.

**Practice and review — 2 h:** In sessions/02-pytorch, build an unrelated tiny classifier, run one optimizer step, and explain zero_grad/backward/step. Trace a fresh short sentence through a legal sequence of parser actions.

**Understanding check — 1 h:** What does the parser predict at one step? Which line creates gradients versus changes parameters? Explain every tensor dimension. Assess the tutorial when evidence exists.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 06`).

## Week 07: A2 parser implementation

**Goal / expected outcome:** Implement and test your parser independently and interpret training behavior.

**Prerequisites:** Parsing states, PyTorch tutorial, A2 Parts 1–2 attempts. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 A2 official handout][a2] Part 3 requirements/test instructions (30 min).

**Assignments / project — 7 h:** Complete parser coding milestones, run supplied checks locally, and begin training. Deliverables: private implementation, actual test commands/results, configuration and first learning curve. A1/A2 code review may identify issues but must not fill TODOs.

**Practice and review — 0.5 h:** Trace an erroneous action on an invented parser state and separate a data issue from a model issue.

**Understanding check — 1 h:** Explain feature lookup, action logits, loss, and the optimizer path in your own code. A passing test is evidence of behavior, not by itself of understanding.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 07`).

## Week 08: A2 completion and foundation checkpoint

**Goal / expected outcome:** Connect embeddings, derivatives, optimization, and parsing without notes.

**Prerequisites:** A2 attempted; training/test evidence available or a documented blocker. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** Revisit only the weakest section of [Winter 2025 A2 official handout][a2] or [2025-linked lecture notes 03][notes03] (30 min).

**Assignments / project — 5.5 h:** Finish remaining written/coding work, training, and parser error analysis. Deliverable: evidence checklist, limitations, and learner explanation. Request A2 sign-off only after assessment.

**Practice and review — 1 h:** Revisit the independent gradient check and one batched shape example; explain a parser error without rewriting its implementation.

**Understanding check — 2 h:** Use [checkpoint-after-a2](reviews/checkpoint-after-a2.md) interactively, not as an answer dump. Reassess weak concepts, record evidence per rubric dimension, and obtain separate Week 08 approval.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 08`).

## Week 09: Language models and recurrent networks

**Goal / expected outcome:** Factor a sequence probability and explain backpropagation through time.

**Prerequisites:** A2 checkpoint gaps repaired or explicitly accepted; chain rule. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L05: Lecture 5 - Recurrent Neural Networks** (Spring 2024, 1:18:52) — [video](https://www.youtube.com/watch?v=fyc0Jzr74y4), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture05-rnnlm.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture05-rnnlm.pdf); focus on next-token distributions, recurrence, shared weights, BPTT, and gradient products.

**Required readings — 1 h:** [2025-linked lecture notes 05][notes05] basic LM/RNN sections (1 h). Recommended repair: [Jurafsky and Martin, Speech and Language Processing (August 2026 contents)][book] chapter 3, N-gram Language Models (45 min outside core budget).

**Assignments / project — 0 h:** None. A3 starts after attention and sequence-to-sequence prerequisites.

**Practice and review — 5 h:** Build a tiny independent character RNN or trace a short recurrence in NumPy. Inspect one gradient product, compare cross-entropy with perplexity, and restate vanishing gradients the next day.

**Understanding check — 1.5 h:** Derive sequence log likelihood and explain why the same parameter receives contributions from multiple time steps. Distinguish exploding from vanishing gradients.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 09`).

## Week 10: Sequence-to-sequence, attention, and early project orientation

**Goal / expected outcome:** Draw a complete attentive encoder-decoder and explain all axes before A3.

**Prerequisites:** RNN recurrence, BPTT, and conditional likelihood. **Estimated effort:** 9 hours.

**Lecture videos — 3 h:** **L06: Lecture 6 - Sequence to Sequence Models** (Spring 2024, 1:17:09) — [video](https://www.youtube.com/watch?v=Ba6Fn1-Jsfw), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture06-fancy-rnn.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture06-fancy-rnn.pdf); also **L07: Lecture 7 - Attention, Final Projects and LLM Intro** (Spring 2024, 1:17:44) — [video](https://www.youtube.com/watch?v=J7ruSOIzhrE), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture07-final-project.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture07-final-project.pdf). L07 includes attention, so watch it before NMT. Focus on gating, alignment, decoding, and a testable project question.

**Required readings — 1.5 h:** [2025-linked lecture notes 06][notes06] gated/attention sections (30 min); [Bahdanau, Cho, Bengio, 2014/ICLR 2015: Neural Machine Translation by Jointly Learning to Align and Translate][bahdanau] introduction and alignment/model sections (1 h).

**Assignments / project — 0.5 h:** [Winter 2025 A3 official handout][a3]: read scope and environment requirements only (30 min); no official coding yet.

**Practice and review — 3 h:** Hand-compute a tiny attention weighted sum, trace teacher forcing vs inference, and annotate an encoder-decoder diagram. Record one tentative NLP research question in project/proposal.md, labeled tentative.

**Understanding check — 1 h:** Over which positions do attention weights sum to one? How does the decoder obtain its query? Derive the weighted context and distinguish gating from attention.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 10`).

## Week 11: A3 implementation milestones

**Goal / expected outcome:** Independently translate an NMT architecture into a working model.

**Prerequisites:** L05–07, PyTorch, attention diagram, A3 environment inspection. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 1 h:** [Winter 2025 A3 official handout][a3] model specification and written requirements (30 min); [Stanford CS231n convolution notes][conv] 1-D/local-filter intuition and shape calculations (30 min).

**Assignments / project — 6.5 h:** Winter 2025 A3: attempt embedding/convolution, encoder, decoder, and attention milestones. Run the handout sanity checks as each part becomes ready. Deliverable: private code and user-reported results. The assistant supplies conceptual guidance without inspecting solution code.

**Practice and review — 0.5 h:** Draw a separate padded batch and determine valid attention positions. Identify convolution input/output axes on an unrelated sequence.

**Understanding check — 1 h:** Explain bidirectional states, padding masks, decoder initialization, and one potential dimension mismatch from memory. Keep official written answers private.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 11`).

## Week 12: A3 training and decoding

**Goal / expected outcome:** Connect learning curves to decoded behavior and distinguish implementation from modeling failures.

**Prerequisites:** A3 sanity checks attempted; device/runtime decision made. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 A3 official handout][a3] training, decoding, and evaluation instructions (30 min).

**Assignments / project — 7 h:** Finish implementation, run local short diagnostics, then the full training/evaluation procedure if feasible. Deliverables: configuration, command, hardware, active vs elapsed compute time, observed metric, and selected failures. Historical GPU timing is not a Mac estimate.

**Practice and review — 0.5 h:** Explain beam search vs greedy search on a fresh tiny probability tree. Avoid test-set tuning.

**Understanding check — 1 h:** What would make loss improve while translations remain poor? Explain teacher forcing and inference mismatch. A reduced run must be labeled reduced, not full A3 completion.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 12`).

## Week 13: A3 analysis and sequence-model checkpoint

**Goal / expected outcome:** Critique NMT output and explain recurrent attention independently.

**Prerequisites:** Training/evaluation evidence or explicit compute limitation. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 A3 official handout][a3] analysis/metric sections (30 min).

**Assignments / project — 5.5 h:** Finish the written analysis independently, review all required artifacts/tests, and document reproducibility. Public summary contains reflections and metrics, not official answers. Prepare A3 completion assessment.

**Practice and review — 1 h:** Compare an RNN context bottleneck with attention; trace information and gradients through one step. Return to Week 9 recall.

**Understanding check — 2 h:** Explain BLEU limitations, padding, decoding, and a real observed failure. Derive the general attention weighted sum. Assess A3 orally within code-review limits and request explicit sign-off.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 13`).

## Week 14: Self-attention and Transformers

**Goal / expected outcome:** Derive scaled dot-product attention and track a full Transformer block.

**Prerequisites:** Sequence attention and matrix calculus understood sufficiently to proceed. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L08: Lecture 8 - Self-Attention and Transformers** (Winter 2023, 1:17:04) — [video](https://www.youtube.com/watch?v=LWMzyfvuehA), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/slides/cs224n-2023-lecture08-transformers.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture08-transformers.pdf); this is a 2023 recording. Focus on Q/K/V, scaling, heads, masks, positions, residuals, and normalization.

**Required readings — 2 h:** [Vaswani et al., 2017: Attention Is All You Need][attention] sections 1–3 and selected experimental comparisons (1.5 h); [2025-linked lecture notes 08][notes08] shapes/masking (30 min).

**Assignments / project — 0 h:** No official A4 solutions yet; its requirements will be introduced after pretraining.

**Practice and review — 4 h:** On an unrelated small input, compute masked attention and explain all dimensions. Build an independent tiny block only if it does not reproduce official TODOs; compare a causal and an unmasked computation.

**Understanding check — 1.5 h:** Derive softmax(QK^T/sqrt(d_k)+mask)V, specify the softmax axis, and explain permutation behavior without positions. Contrast self-attention and encoder-decoder attention.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 14`).

## Week 15: Pretraining objectives and model interfaces

**Goal / expected outcome:** Compare causal and masked objectives, inspect tokenizer outputs, and distinguish pretraining from adaptation.

**Prerequisites:** L08 and attention recall; train/validation/test separation. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L09: Lecture 9 - Pretraining** (Winter 2023, 1:18:46) — [video](https://www.youtube.com/watch?v=DGfCRXuNA2w), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/slides/cs224n-2023-lecture9-pretraining.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture09-pretraining.pdf); this is a 2023 recording. Focus on contextual representations, objectives, transfer, and data.

**Required readings — 2 h:** [Devlin et al., 2018/NAACL 2019: BERT][bert] abstract, model/pretraining section, and ablation discussion (1 h); [Winter 2025 slides for local 09][slides09] (30 min); [Hugging Face quicktour][hf] (30 min).

**Assignments / project — 1 h:** [Winter 2025 A4 official handout][a4]: inspect scope and environment; identify its architecture/objectives and planned experiments. No expectation that Hugging Face is an A4 dependency.

**Practice and review — 3.5 h:** Run a small public checkpoint or tiny initialized model through the official quicktour; report IDs, masks, outputs, device and exact checkpoint. Write a separate causal-vs-masked toy batch. Recommended within spare time: [Winter 2026 pretraining slides][pre26] or [Winter 2026 guest-julie-tokenization-multilinguality slides][token26] (45–60 min each, replacing optional work).

**Understanding check — 1 h:** Which tokens contribute to each objective? Explain what changes during fine-tuning and what remains unknown about training data. Assess sessions/03-huggingface-transformers when evidenced.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 15`).

## Week 16: A4 attention mathematics and codebase orientation

**Goal / expected outcome:** Attempt official attention reasoning independently and understand the research codebase.

**Prerequisites:** L08–09; pretraining objectives; PyTorch. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 A4 official handout][a4] attention and initial programming instructions (30 min).

**Assignments / project — 7 h:** Winter 2025 A4: attempt attention mathematical questions and first programming milestones independently. Deliverable: private work, a learner-drawn dataflow, and actual small-test results. Assistant support stays at conceptual/debugging-strategy level.

**Practice and review — 0.5 h:** Recall attention scaling and masks on a fresh toy example; distinguish general theory from the official problem answer.

**Understanding check — 1 h:** Explain the model objective, batch construction, and output shapes without code inspection. Identify a test that would discriminate two possible failure causes.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 16`).

## Week 17: A4 pretraining and fine-tuning comparisons

**Goal / expected outcome:** Measure what pretraining changes under a controlled evaluation.

**Prerequisites:** A4 initial milestones; small-run checks; compute plan. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 A4 official handout][a4] experiment protocol (30 min).

**Assignments / project — 7 h:** Run required baseline, pretraining, and fine-tuning experiments as specified in the 2025 handout. Record configuration, data split, hardware, commands, and metrics. Keep official outputs in ignored work/.

**Practice and review — 0.5 h:** Identify confounds in a comparison where both training data and model size change. Retrieve the Week 15 objective from memory.

**Understanding check — 1 h:** What evidence would support a pretraining benefit? Why is a memorized fact not guaranteed to be correct or current? Explain uncertainty in your own results.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 17`).

## Week 18: A4 rotary positions and assignment assessment

**Goal / expected outcome:** Explain positional choices and complete the required controlled comparisons.

**Prerequisites:** A4 experiments attempted; positional encoding foundations. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 A4 official handout][a4] remaining rotary-position and analysis requirements (30 min).

**Assignments / project — 5.5 h:** Finish RoPE-related written/programming milestones and remaining runs independently; review all requirements and actual tests. Deliverable: private complete work or precisely documented gaps, plus a safe learning summary.

**Practice and review — 1 h:** Use a separate 2-D rotation example to explain relative angle intuition. Review attention and objective shapes.

**Understanding check — 2 h:** Assess A4 understanding and request sign-off if eligible. Defer the existing broader [after-A4 checkpoint](reviews/checkpoint-after-a4.md) to Week 21 because it also asks about post-training and evaluation.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 18`).

## Week 19: Post-training: SFT, RLHF, and DPO

**Goal / expected outcome:** Explain what supervision each stage needs and what preference optimization does not guarantee.

**Prerequisites:** Pretraining, likelihood, gradients, and basic probability. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L10: Lecture 10 - Post-training by Archit Sharma** (Spring 2024, 1:19:42) — [video](https://www.youtube.com/watch?v=35X6zlhoCy4), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture10-prompting-rlhf.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture10-instruction-tunining-rlhf.pdf); focus on demonstrations, reward modeling, KL regularization, and preference learning.

**Required readings — 2 h:** [Ouyang et al., 2022: Training language models to follow instructions with human feedback][instruct] method and evaluation setup (1 h); [Rafailov et al., 2023: Direct Preference Optimization][dpo] introduction and method overview (1 h).

**Assignments / project — 0 h:** No new official assignment. Keep preference exercises separate from course work.

**Practice and review — 4 h:** Draw the SFT/reward/RL pipeline and DPO alternative. On invented preference pairs, identify chosen/rejected likelihood terms and reference-policy roles. Work toward the DPO derivation; save detailed assumptions for Week 24.

**Understanding check — 1.5 h:** What changes between pretraining and SFT? What does DPO avoid in the typical RLHF pipeline? Why can preference improvements coexist with factual errors?

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 19`).

## Week 20: Efficient adaptation and training constraints

**Goal / expected outcome:** Explain low-rank updates and estimate memory without turning this into an infrastructure course.

**Prerequisites:** Transformer parameters, gradients, and post-training. **Estimated effort:** 9 hours.

**Lecture videos — 1.25 h:** **L12: Lecture 12 - Efficient Training, Shikhar Murty** (Spring 2024, 1:02:32) — [video](https://www.youtube.com/watch?v=UVX7SYGCKkA), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture12-training-shikhar.pdf); focus on parameters, gradients, optimizer state, and activations. S01 is slide-led; no matching public 2025 video is verified.

**Required readings — 2.75 h:** [Winter 2025 slides for local s01][slidess01] (1 h); [Hu et al., 2021/ICLR 2022: LoRA][lora] method and main comparisons (1.25 h); [PyTorch MPS notes][mps] and selected review (30 min).

**Assignments / project — 0 h:** None. Full-model fine-tuning and low-rank experiments here are independent practice.

**Practice and review — 4 h:** Count trainable parameters in W + BA; implement or hand-trace a tiny unrelated low-rank update and confirm which parameters receive gradients. Estimate memory components and state dtype assumptions. Detailed distributed-training work belongs in ai-infra-lab.

**Understanding check — 1 h:** Derive r(d_in+d_out) trainable adapter parameters and compare with d_in*d_out. Why does freezing weights not remove activation storage? Explain prompting vs parameter updates.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 20`).

## Week 21: Evaluation and the second major checkpoint

**Goal / expected outcome:** Design an evaluation that measures a specific capability and exposes failure modes.

**Prerequisites:** A4, L10, PEFT, experiment design. **Estimated effort:** 9 hours.

**Lecture videos — 1.5 h:** **L11: Lecture 11 - Benchmarking by Yann Dubois** (Spring 2024, 1:24:24) — [video](https://www.youtube.com/watch?v=TO0CqzqiArM), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture11-evaluation-yann.pdf), [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture12-evaluation-final.pdf); focus on metric choice, human/model judges, contamination, and distribution shift.

**Required readings — 2 h:** [Liang et al., 2022: Holistic Evaluation of Language Models][helm] evaluation framework and limitations (1 h); [Winter 2026 evaluation slides][eval26] comparison with [Winter 2025 slides for local 11][slides11] (1 h).

**Assignments / project — 0 h:** No 2026 A4 completion is claimed. Its API setup is not required for this path.

**Practice and review — 3.5 h:** Independent exercise: use a small local model or saved predictions to compare exact match with a documented human rubric on 20–50 examples. Freeze examples before evaluating; log disagreements and uncertainty. Do not build a production benchmark service.

**Understanding check — 2 h:** Use [checkpoint-after-a4](reviews/checkpoint-after-a4.md) interactively, including post-training. Explain one metric failure and a contamination risk. Record remaining gaps and phase sign-off.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 21`).

## Week 22: Question answering, retrieval, and knowledge

**Goal / expected outcome:** Separate retrieval failures from generation failures and explain parametric vs external knowledge.

**Prerequisites:** Vector similarity, Transformer conditioning, evaluation. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** S02 is slide-led. No matching public 2025 recording is verified; video budget is zero.

**Required readings — 3 h:** [Winter 2025 slides for local s02][slidess02] (1.5 h); [Lewis et al., 2020: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks][rag] introduction, method, and key experiments (1.5 h).

**Assignments / project — 0 h:** None. This is an independent miniature retrieval experiment.

**Practice and review — 4.5 h:** Create a tiny fixed passage collection and questions. Compare retrieval alone, closed-book answers, and context-conditioned answers using the Week 21 evaluation discipline. A simple baseline is sufficient; annotate where each failure occurred.

**Understanding check — 1.5 h:** Write the retrieval-conditioned prediction idea and explain the difference between retrieving evidence and proving an answer. Which update needs retraining, and which only changes the collection?

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 22`).

## Week 23: Reasoning and agents

**Goal / expected outcome:** Explain a tool loop, reason about failure propagation, and distinguish reasoning claims from evidence.

**Prerequisites:** Post-training, retrieval, and evaluation. **Estimated effort:** 9 hours.

**Lecture videos — 1.25 h:** **L14: Lecture 14 - Reasoning and Agents by Shikhar Murty** (Spring 2024, 1:03:42) — [video](https://www.youtube.com/watch?v=I0tj4Y7xaOQ), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture14-agents-shikhar-updated.pdf); focus on actions, observations, control flow, and evaluation.

**Required readings — 2.75 h:** [Yao et al., 2022/ICLR 2023: ReAct][react] method and one experiment (1 h); [Winter 2026 rag-agents slides][agent26] selected changes (45 min); [Winter 2026 reasoning-part1 slides][reason26] selected reasoning/evaluation themes (1 h).

**Assignments / project — 0 h:** None. Optional 2026 Reasoning 2 belongs in a buffer week, not an extra required assignment.

**Practice and review — 4 h:** Trace a toy agent with a deterministic calculator or mocked retrieval tool; perturb an observation and inspect failure handling. Compare fixed compute budgets and distinguish a useful trace from evidence that the trace faithfully explains the model.

**Understanding check — 1 h:** What changes when an LM can act? How do you measure success beyond fluent output? Explain one compounding error and a controlled experiment that could detect it.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 23`).

## Week 24: Preference research and responsible NLP

**Goal / expected outcome:** Critique preference-learning assumptions and connect model evaluation with affected users.

**Prerequisites:** L10, evaluation, and Week 19 DPO overview. **Estimated effort:** 9 hours.

**Lecture videos — 1.25 h:** **L15: Lecture 15 - After DPO by Nathan Lambert** (Spring 2024, 1:08:57) — [video](https://www.youtube.com/watch?v=dnF463_Ar9I), [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture15-life-after-dpo-lambert.pdf); historical 2024 perspective, not a statement of the 2026 frontier. Local L17 has no verified public recording.

**Required readings — 2.75 h:** [Rafailov et al., 2023: Direct Preference Optimization][dpo] objective derivation and assumptions (1.5 h); [Winter 2026 impact-on-humanity slides][risk26] selected social-impact sections (1.25 h). [Lambert et al., 2024: RewardBench][reward] is recommended, 1 h outside core budget.

**Assignments / project — 0 h:** None. Select one project risk to investigate explicitly.

**Practice and review — 3.5 h:** Attempt the DPO objective derivation from a KL-regularized preference framework, documenting assumptions and weak steps. Draft a project evaluation slice for an underserved group or known failure mode. Keep empirical claims tied to the paper/year.

**Understanding check — 1.5 h:** Which assumptions connect preference probabilities to policy ratios? What evidence could falsify a claimed improvement? Explain a tradeoff in your planned project and whose outcomes the metric omits.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 24`).

## Week 25: Project proposal and feasibility gate

**Goal / expected outcome:** Define one testable NLP question with a baseline, fixed evaluation, and affordable experiments.

**Prerequisites:** Assignments assessed; major gaps documented; evaluation and responsible-NLP discussion. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new required video. Revisit the project portion of L07 only if needed.

**Required readings — 1.5 h:** [2025-linked proposal instructions (reused Spring 2024 document)][proposal] and [Official custom project tips][tips] (1 h); [Winter 2025 default GPT-2 project][gpt2] scope comparison (30 min).

**Assignments / project — 5.5 h:** Project: choose the scoped custom path or explicitly expand the schedule for the full 2025 GPT-2 project. Fill project/proposal.md with hypothesis, data/license, splits, baseline, one change, metric, compute cap, risks, reused code, and your contribution.

**Practice and review — 1 h:** Estimate a tiny run from measured throughput before committing to scale. Recommended custom question: does a positional-encoding choice affect length generalization in a small character LM? Use a separate corpus/implementation, not repackaged A4 answers.

**Understanding check — 1 h:** What result would disconfirm your hypothesis? How will you prevent train/test leakage and separate extra compute from a method improvement? Assess proposal feasibility before training.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 25`).

## Week 26: Project baseline and milestone

**Goal / expected outcome:** Produce a reproducible baseline and an honest milestone.

**Prerequisites:** Feasible proposal chosen and reviewed; dataset and compute plan ready. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** [Winter 2025 project milestone instructions][milestone] (30 min).

**Assignments / project — 7 h:** Project: implement the agreed baseline independently; verify split integrity, run a short diagnostic, and obtain the first measured result. Fill project/milestone.md with actual commands, data/version, hardware, elapsed vs active time, metrics, failures, and next experiment.

**Practice and review — 0.5 h:** Explain the end-to-end tensor and gradient path verbally. The assistant follows project code-inspection limits; discuss diagnostics rather than rewriting implementation.

**Understanding check — 1 h:** Can another person reproduce the baseline from your record? What failed, and what evidence distinguishes model limitations from an implementation issue?

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 26`).

## Week 27: Project comparison and error analysis

**Goal / expected outcome:** Evaluate one controlled change and judge the strength of the evidence.

**Prerequisites:** Baseline and fixed evaluation exist; milestone reviewed. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new video.

**Required readings — 0.5 h:** Re-read the methods/experiment sections of the single paper most relevant to the approved project (30 min); record the exact paper and link in the proposal.

**Assignments / project — 7 h:** Project: run one main comparison, at least one informative ablation, and repeat small runs where feasible. Aim for three seeds; if compute prevents this, report the limitation rather than imply certainty. Produce result tables and concrete error categories.

**Practice and review — 0.5 h:** Audit confounds: token count, model size, runtime, data split, and tuning budget. Decide which claim the measurements actually support.

**Understanding check — 1 h:** What changed besides the intended variable? Are differences stable enough to interpret? Explain negative results and choose the next experiment only if needed.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 27`).

## Week 28: Project report, oral defense, and synthesis

**Goal / expected outcome:** Explain the path from static embeddings to modern NLP and defend an evidence-based project conclusion.

**Prerequisites:** Project results and gaps documented; core work reviewed. **Estimated effort:** 9 hours.

**Lecture videos — 0 h:** No new required video. Optional L18 may follow the core completion review.

**Required readings — 0.5 h:** [Winter 2025 project report instructions][report] (30 min). Recommended extension: [Winter 2026 open-questions slides][open26] (45 min in buffer time).

**Assignments / project — 4.5 h:** Project: finish project/report.md, report methods/results/limitations and source attribution, and prepare a short poster-style explanation. A running demo alone is insufficient. Keep official solution details private.

**Practice and review — 1.5 h:** Fill [synthesis](reviews/synthesis.md) from recall: representations, gradient flow, sequence modeling, attention, objectives, adaptation, retrieval, evaluation. Name what you can independently derive or implement and what still needs work.

**Understanding check — 2.5 h:** Conduct an interactive oral defense and cumulative assessment. Record evidence, unresolved gaps, and the exact user sign-offs for project, Week 28, and course phase. Do not label full official GPT-2 completion for a scoped custom project.

**Completion evidence:** the deliverables above, dated learner recall in the relevant summary/QA, actual run records where applicable, and assessment feedback. **User sign-off:** pending (`SIGN OFF: Week 28`).

## Recommended and optional extensions

Choose at most one per buffer week. The core remains 252 hours.

| Priority | Resource / local home | Time | Expected evidence |
| --- | --- | --- | --- |
| Recommended | Original [word2vec][word2vec] and [GloVe][glove], local 01/02 | 1–2 h each | Contrast objectives and evaluation evidence |
| Recommended | Textbook [current contents][book]: Embeddings ch. 5, Neural Networks ch. 6, Dependency Parsing ch. 20 | 1–2 h selected chapter | Repair a named gap; chapter numbers refer to August 2026 |
| Recommended | 2023 Natural Language Generation and interpretability videos in COURSE_MAP | 2–3 h each including notes | Explain decoding tradeoffs or critique an interpretation claim |
| Recommended | 2026 pretraining/tokenization updates; Reasoning 2 via official schedule | 1–2 h each | Compare a specific change to the older recording |
| Optional | L13 Speech BCI, [resources](lectures/13-speech-bci/README.md) | 2 h | Explain sequence modeling outside text |
| Optional | L16 ConvNets/TreeRNNs, [resources](lectures/16-convnets-treernns/README.md) | 2–3 h | Compare inductive biases; A3 only requires a small convolution primer |
| Optional | L18 Linguistics/philosophy, [resources](lectures/18-linguistics-philosophy/README.md) | 2 h | State and defend one precise disagreement |
| Optional | 2023 multimodality recording in COURSE_MAP | 2–3 h | Separate modality-specific assumptions from shared objectives |
| Optional | Full [2025 GPT-2 default project][gpt2] | Add 4–8 weeks initially | All official project tasks, experiments, report, and defense; re-estimate after feasibility check |

## Next study session: L01 pre-watch briefing

**Budget:** about 2 hours, inside Week 1. Begin with a 10-minute prerequisite
diagnostic, then the **80:17** [Spring 2024 L01 recording](https://www.youtube.com/watch?v=DzpHeXVSC5I)
and its [matching slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture01-wordvecs1.pdf).
Allow 15 minutes for pauses and 15 minutes for recall. Read the required notes in the
next sitting rather than forcing everything into this session.

Prerequisites: vector dot products/shapes, elementary probability, logs, and a basic
chain rule. Focus on (1) distributional meaning, (2) sparse vs dense representations,
(3) center/outside embeddings, (4) conditional softmax and negative log likelihood,
(5) why gradients change the vectors.

While watching, consider: What information about words does context provide? What
does skip-gram predict from what? What is being normalized in the softmax? Afterward,
report what you watched, your actual study time, and a short explanation in your own
words. Then discuss gaps and begin a targeted assessment; no automatic completion.

## Resource links

These reference definitions keep recurring weekly links consistent. Verification
scope and year caveats are in COURSE_MAP. Recheck mutable documentation when used.

[calculus]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/review-differential-calculus.pdf
[matrix]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/gradient-notes.pdf
[broadcast]: https://numpy.org/doc/stable/user/basics.broadcasting.html
[matmul]: https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
[autograd]: https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html
[mps]: https://docs.pytorch.org/docs/stable/notes/mps.html
[hf]: https://huggingface.co/docs/transformers/quicktour
[neg]: https://arxiv.org/abs/1310.4546
[word2vec]: https://arxiv.org/abs/1301.3781
[glove]: https://aclanthology.org/D14-1162/
[bahdanau]: https://arxiv.org/abs/1409.0473
[attention]: https://arxiv.org/abs/1706.03762
[bert]: https://arxiv.org/abs/1810.04805
[instruct]: https://arxiv.org/abs/2203.02155
[dpo]: https://arxiv.org/abs/2305.18290
[lora]: https://arxiv.org/abs/2106.09685
[helm]: https://arxiv.org/abs/2211.09110
[rag]: https://arxiv.org/abs/2005.11401
[react]: https://arxiv.org/abs/2210.03629
[reward]: https://arxiv.org/abs/2403.13787
[conv]: https://cs231n.github.io/convolutional-networks/
[book]: https://web.stanford.edu/~jurafsky/slp3/
[proposal]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project/project-proposal-instructions-spr2024-updated.pdf
[milestone]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project_w25/CS224N_Final_Project_Milestone_Instructions__Winter_2025_.pdf
[report]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project/CS224N_Final_Project_Report_Instructions_2025.pdf
[gpt2]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project_w25/CS_224n__Default_Final_Project__Build_GPT_2.pdf
[tips]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project/custom-final-project-tips.pdf
[notes01]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n_winter2023_lecture1_notes_draft.pdf
[notes02]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes02-wordvecs2.pdf
[notes03]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes03-neuralnets.pdf
[notes04]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes04-dependencyparsing.pdf
[notes05]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes05-LM_RNN.pdf
[notes06]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes05-LM_RNN.pdf
[notes08]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-self-attention-transformers-2023_draft.pdf
[slides09]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture09-pretraining.pdf
[slides10]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture10-instruction-tunining-rlhf.pdf
[slides11]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture12-evaluation-final.pdf
[slidess01]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture11-adapatation.pdf
[slidess02]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture13-QA.pdf
[pre26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture07-pretraining.pdf
[eval26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture11-evaluation.pdf
[agent26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture10-rag-agents.pdf
[reason26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture12-reasoning-part1.pdf
[risk26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture16-impact-on-humanity.pdf
[open26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture19-open-questions.pdf
[token26]: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture14-guest-julie-tokenization-multilinguality.pdf
[a1]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a1.zip
[a2]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2.pdf
[a3]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a3.pdf
[a4]: https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a4.pdf
