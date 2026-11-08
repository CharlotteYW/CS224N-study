# Session handoff

Updated 2026-11-06 (America/Los_Angeles).

## Read first

Follow [AGENTS.md](AGENTS.md), then [PROGRESS.md](PROGRESS.md), the current unit's
README/summary/QA, and the relevant [ROADMAP](ROADMAP.md) section. Consult
[COURSE_MAP](COURSE_MAP.md) before naming a video, slide deck, or assignment year.

## Current learning state

- Learner is an experienced software/infrastructure engineer studying NLP foundations.
  Keep infrastructure connections brief; a separate ai-infra-lab covers that curriculum.
- Learner confirmed **8–10 hours/week** and **no additional lectures or assignments**
  beyond the saved NumPy record on 2026-11-02.
- NumPy's historical `complete` record and all notebook predictions/outputs are
  preserved byte-for-byte. Initial saved outputs show a matrix-vector rank mistake
  later corrected in notes. Later rule/stack predictions remain unfilled/unexecuted
  in the saved notebook. Do not erase that evidence or restart the whole session.
- The learner confirmed completing Week 01 Sessions 1–3. The earlier reference to “2” meant Session 2 readings. The learner approved closing Week 01 and requested to start L02.
  No assignment is active, no study hours were reported, and no new assessment or
  explicit milestone sign-off has occurred.

## Decisions and source findings

- Use **Winter 2025 coursework and all four assignments**. This preserves the RNN/NMT
  foundation. Use 2024 public videos, labeled 2023 substitutions, and selected 2026 slides.
- The public playlist's L08/L09 recordings are **2023**; playlist positions are not
  lecture numbers. No 2024 L17 recording was verified. Its replacement is a required
  2026 social-impact slide session, clearly labeled as such.
- L07 includes attention: study it before A3. Winter 2026 A3 is Transformers and
  A4 is LLM evaluation; do not put those starters into the existing 2025 NMT/A4 flow.
- Live textbook chapter numbers drifted; corrected dependency parsing, Transformer,
  and masked-LM links. Recheck current topic titles when using mutable sources.
- Plan: **28 active weeks at 9 hours/week (252 hours)** plus 2–4 flexible buffer weeks.
  A small custom NLP project occupies Weeks 25–28; a full official GPT-2 project
  needs a separately estimated extension. No project topic has been chosen.
- Course policy allows conceptual AI collaboration but not answer generation or
  substantial assignment completion. Use the course's TA code-inspection boundary
  for A3/A4/projects. Official answers and code stay in ignored work/ directories.
- On 2026-11-06 the learner explicitly authorized a local commit of the setup changes.
  See Git history for the resulting commit. Push/publication was not requested; no
  paid compute or reminder has been performed or scheduled.

## Work completed in this setup session

- Added AGENTS, COURSE_MAP, ROADMAP, PROGRESS, this handoff, an assessments index,
  and a lightweight papers index. No paper summaries or assessment history invented.
- Replaced the root README's obsolete 14-week plan/tracker with navigation to the
  authoritative plan and evidence files. All actual old progress was carried forward.
- Updated existing lecture/tutorial/assignment/project READMEs for source provenance,
  new week numbers, prerequisites, milestones, evidence, and sign-off requirements.
- Corrected a planning target that falsely attributed negative-sampling derivations
  to 2025 A2; corrected A4 scope and private written-answer handling for A3.
- Updated checkpoint timing and project completion criteria. Normalized not-started
  planning statuses; retained the NumPy session's original files without modification.
- No existing directory was renamed/deleted. Runtime code, notebook content,
  requirements, setup script, and .gitignore were not changed.
- On 2026-11-06 added a concrete five-session Week 01 plan to the existing L01 README
  (2 + 1.5 + 2 + 2 + 1.5 hours), with exact activities and evidence. The learner has
  not answered the diagnostic or reported new study progress.

## Verification and limitations

- Inspected tracked study documents, the saved NumPy notebook, and Git history/status.
- Fetched official 2023/2024/2025/2026 schedules; inspected assignment scope and AI
  policy. Read live playlist titles/IDs/durations; did not watch or test playback.
- HTTP reachability checks and Markdown link/reference checks were run: all local
  links and 66 reference-link uses across 101 Markdown files passed. All 12 newly
  introduced URLs in the final check returned HTTP 200. See COURSE_MAP
  for blocked optional links and the limits of verification. Colab notebook execution,
  course account access, and old package compatibility remain unverified.
- Checked all 28 weekly budgets sum to 9 hours; inspected source/year and study-order
  consistency. `git diff --check` passed. Verified all four NumPy files match HEAD.
- No model, notebook, assignment test suite, or training run was executed in this
  planning session. Reading saved outputs is not a new test execution.

## Unresolved items and exact next step

No blocker prevents starting study. Remaining questions are prerequisite readiness,
retention of NumPy shape rules, actual future study hours, and later project/compute
choices. Discuss those when relevant; do not ask for approval to repeat this setup.

**Next:** Begin Winter 2025 A1. The learner finished the Lecture 02 video, discussed negative sampling, SVD, GloVe, sparse coding, and trainable embeddings, and requested to proceed. The Lecture 02 QA and summary preserve the guided recall. Reading confirmation and formal lecture sign-off are pending.

The official A1 starter was unpacked in the ignored assignment work directory. The learner's first step is to run the setup cells and independently attempt Question 1.1. Carry the Week 01 context-similarity explanation and independent skip-gram gradient derivation into later review.

A dedicated Python 3.12 environment was prepared under the ignored A1 student directory. Import checks passed for datasets, Gensim, scikit-learn, Matplotlib, and JupyterLab. The learner will run the notebook setup cells, including the data-loading step.

The learner requested a comparison of word-vector methods before starting A1. The Lecture 02 summary now includes assistant examples for Skip-gram, CBOW, GloVe, and truncated SVD. A1 setup and Question 1.1 remain the next learner actions.

The learner reported opening the A1 notebook and requested a reviewable explanation of its goals. The tracked A1 summary now maps both parts to their learning outcomes. No notebook checks or learner solutions were reported.

The learner reported a passing A1 Question 1.2 check. Next is Question 1.3 on truncated SVD. The public QA records the debugging concepts and the learner-reported result.

The learner reported that the A1 Question 1.3 check passed. Next is Question 1.4, which maps selected words to rows of the reduced matrix and plots their two coordinates.

The learner reported completing A1 Part 1. Questions 1.2 and 1.3 checks were reported as passing. Continue at Question 2.1 and ask for an independent comparison of the GloVe and Part 1 plots.

The learner requested a worked self-study review of A1 Part 2 and stated that they will not submit the assignment. Reference examples were checked against the local GloVe model. Learner execution, assessment, and sign-off for Part 2 remain unreported.


A1 self-study closeout: The learner reported understanding the chapter and asked
to save, commit, and push the notebook before closing it. Added 13 written
references and five runnable example cells for Part 2. Notebook schema validation
and compilation of the edited code cells passed. Prior checks used the local
200-dimensional GloVe model. Existing cells and outputs outside the edits were
preserved. The learner's private GitHub repository was verified before tracking
this notebook and its referenced figure. The next planned topic is negative
sampling review in Week 03. Formal assessment and Week 02 sign-off remain open.

The learner closed the Week 03 negative-sampling review at the conceptual level and requested commit, push, and the next lesson. They deferred paper reading and gradient derivation. Start Lecture 03 backpropagation with the recording, slides, and one small computation graph.
