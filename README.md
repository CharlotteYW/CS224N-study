# CS224N study journal

Personal study of Stanford CS224N: Natural Language Processing with Deep Learning.
The aim is independent understanding, mathematical reasoning, and practical NLP
skills. All repository content is English; conversations may be English or Chinese.

## Start here

- [Progress and next action](PROGRESS.md): actual evidence, gaps, reviews, and sign-offs.
- [Roadmap](ROADMAP.md): 28 active weeks at about 9 hours/week, plus flexible buffers.
- [Course map](COURSE_MAP.md): verified sources, video years, assignment versions,
  source mismatches, and compute/access limitations.
- [Agent instructions](AGENTS.md) and [session handoff](SESSION_HANDOFF.md): continuity.
- [Papers](papers/README.md) and [assessments](assessments/README.md): reading plan and
  evidence-based understanding checks, created as study proceeds.

The learner confirmed 8–10 hours/week and no completed lectures/assignments beyond
the saved NumPy session. That session's existing `complete` record is preserved.
The next lecture is **L01 Word Vectors**; no new mastery or sign-off is assumed.

## Course sources

Primary coursework and all four assignments are [Winter 2025](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/).
Videos come from the [official public collection](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D):
mostly Spring 2024, with explicitly labeled 2023 Transformers/Pretraining recordings.
There is no verified 2024 Lecture 17 recording in that playlist. Selected
[Winter 2026](https://web.stanford.edu/class/cs224n/) slides update later topics.

Local lecture numbers follow the original folder structure; they do not universally
match 2025 or 2026 lecture numbers. Winter 2025 A3 is NMT and A4 is Transformers;
Winter 2026 A3/A4 instead cover Transformers/evaluation. Do not mix their starters.
The course map also records reused older notes and mutable textbook chapter numbers.

## How a study step works

1. Read progress, then receive a small session plan with exact sources and outcomes.
2. Study independently and ask questions while working.
3. Explain what you learned before the assistant writes a summary. Separate learner
   statements from assistant explanations and corrections in summary/QA.
4. Attempt problems independently; keep official solutions private. Use conceptual
   guidance and permitted review rather than AI-written assignment answers.
5. Complete an interactive assessment and address or explicitly accept remaining gaps.
6. Approve a milestone explicitly, for example `SIGN OFF: Lecture 01` or
   `SIGN OFF: Week 01`. Only then record the sign-off and prepare the next milestone.

Use Not Started, In Progress, Blocked, Ready for Review, Assessed, and Signed Off.
Plans and checklists do not establish mastery. Actual hours come from learner reports.
Git commits, pushes, and publication require an explicit request; they are not an
automatic part of a learning session.

## Repository organization

- [Lectures](lectures/README.md): source links, concept targets, learner summaries, QA.
- [Assignments](assignments/README.md): Winter 2025 milestones and coaching boundaries.
- [Tutorial sessions](sessions/README.md): NumPy, PyTorch, and Hugging Face.
- [Project](project/README.md): proposal, milestone, report, and defense.
- [Reviews](reviews/synthesis.md): checkpoints and cumulative synthesis.

The revised plan replaces the former 14-week schedule. A small custom project is
budgeted for Weeks 25–28, with a tentative idea in Week 10. The full Winter 2025 GPT-2
project remains an option with more time; a partial run is not full completion.

## Environment and private work

Use the existing `.venv` for ordinary local study:

```bash
source .venv/bin/activate
jupyter lab
```

For a fresh setup only, `bash scripts/setup_venv.sh` creates the environment from
requirements.txt. Inspect assignment-specific requirements before installing old
packages; isolate incompatible dependencies when necessary. The environment was not
reinstalled or benchmarked during curriculum setup. Check actual MPS operator support
before long runs; 64 GB unified memory does not guarantee CUDA compatibility.

Official handouts, starter zips, solution code, written answers, data, and checkpoints
stay in ignored `assignments/*/work/` or `project/work/`. Public summaries record
learning reflections, experiment metadata, and limitations rather than official
answers. No course solutions or copyrighted source materials are published here.
