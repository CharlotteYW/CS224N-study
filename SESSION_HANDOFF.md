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
- Week 01 includes that legacy work, but L01 and the new diagnostic are Not Started.
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

**Next:** offer the [L01 first sitting](lectures/01-word-vectors/README.md), about two
hours. Begin with one small diagnostic, for example: given `X.shape == (4, 3)` and
`q.shape == (3,)`, predict `(X @ q).shape` and explain why. Wait for the learner's
answer before feedback. Then provide the verified L01 video/slides and focus questions.
Do not mark the lecture watched or begin an assessment record until evidence exists.
