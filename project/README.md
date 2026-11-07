# Final project

| | |
| --- | --- |
| Kind | Project |
| Priority | Core |
| Plan week | 25–28; tentative idea in 10 |
| Status | Not Started |

Week 10 records a tentative idea; Weeks 25–28 cover a scoped custom NLP experiment: proposal, baseline, controlled comparison, and report/defense. Budget about 36 active hours. A full 2025 default GPT-2 project may need 4–8 additional weeks, re-estimated at proposal time.

## Why this is in the course

The project is where the pieces meet: a transformer, a training objective, an evaluation, and a writeup that says what you changed. The official 2025 default project is a minimal GPT-2 with downstream tasks. The recommended self-study path is a small custom experiment with a concrete question and affordable compute; choose the path at the proposal gate.

## Done when

The approved scope has a reproducible baseline, controlled comparison, error/limitations analysis, completed report, oral defense, and explicit learner sign-off. A first running slice is a milestone, not project completion.

## Resources

- [Winter 2025 default project handout](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project_w25/CS_224n__Default_Final_Project__Build_GPT_2.pdf)
- [Proposal instructions (format reference)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project/project-proposal-instructions-spr2024-updated.pdf)
- [Milestone instructions](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project_w25/CS224N_Final_Project_Milestone_Instructions__Winter_2025_.pdf)
- [Report instructions](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/project/CS224N_Final_Project_Report_Instructions_2025.pdf)
- Lecture 7: `lectures/07-final-projects`
- Lecture 8: `lectures/08-transformers`

Code lives in project/work/ and is gitignored. proposal.md, milestone.md, and report.md in this folder are your study writeups, not copies of the Stanford templates. The 2024 video's default project was a minimal BERT. If choosing the official default path, follow the complete 2025 GPT-2 handout; otherwise clearly label the custom project.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Milestones and safeguards

- [ ] Week 25: proposal states a falsifiable question, data/license and splits,
  baseline, one change, metric, compute cap, risks, and source attribution.
- [ ] Week 26: baseline runs; milestone records actual commands, hardware, metrics,
  failures, active study time, and unattended compute time.
- [ ] Week 27: controlled comparison and ablation; repeat small runs where feasible
  and document uncertainty if replication is limited.
- [ ] Week 28: report, poster-style explanation, oral defense, and course synthesis.
- [ ] Explicit project sign-off after assessment, with any accepted gaps recorded.

The assistant follows the course's project code-inspection limit: conceptual support,
experiment design, and debugging strategy, without inspecting or rewriting solution
code. The learner independently implements and explains their contribution. A custom
project is not the official default project, and a reduced run is not its completion.
