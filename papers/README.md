# Paper reading plan

All entries are **Not Started**. These are reading assignments, not learner summaries.
Required scope means the named sections; full-paper deep reads and extra experiments
are optional. Estimated times exclude later reassessment. See [ROADMAP](../ROADMAP.md)
for the weekly time budget and [COURSE_MAP](../COURSE_MAP.md) for source verification.

The proposed lightweight structure is this index plus one `<paper-slug>.md` created
only when reading begins. No empty per-paper files or prewritten achievements are needed.

| Paper / authors and year | Week | Priority | Focus and reason to read | Estimated time |
| --- | --- | --- | --- | --- |
| [Mikolov et al., 2013: Distributed Representations of Words and Phrases](https://arxiv.org/abs/1310.4546) | 03 | Required | Negative sampling and subsampling; compare objective and computational cost. | 1 h |
| [Bahdanau, Cho, Bengio, 2014/ICLR 2015: Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | 10 | Required | Introduction and alignment/model sections; connect soft alignment to recurrent translation. | 1 h |
| [Vaswani et al., 2017: Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 14 | Required | Architecture and selected comparisons; explain what removes recurrence and what the experiments establish. | 1.5 h |
| [Devlin et al., 2018/NAACL 2019: BERT](https://arxiv.org/abs/1810.04805) | 15 | Required | Pretraining method and ablation discussion; distinguish bidirectionality and masked targets. | 1 h |
| [Ouyang et al., 2022: Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | 19 | Required | Method and evaluation setup; identify supervision, comparison models, and limits. | 1 h |
| [Rafailov et al., 2023: Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | 19, 24 | Required | Method overview first, derivation/assumptions later; connect preference data to policy ratios. | 2.5 h total |
| [Hu et al., 2021/ICLR 2022: LoRA](https://arxiv.org/abs/2106.09685) | 20 | Required | Method and primary comparisons; separate trainable parameter count from total memory. | 1.25 h |
| [Liang et al., 2022: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | 21 | Required | Evaluation framework and limitations; understand the choice of scenarios and metrics. | 1 h |
| [Lewis et al., 2020: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 22 | Required | Method and key experiments; identify what retrieval contributes and where errors remain. | 1.5 h |
| [Yao et al., 2022/ICLR 2023: ReAct](https://arxiv.org/abs/2210.03629) | 23 | Required | Method and one experiment; connect reasoning/action traces with measurable task success. | 1 h |
| [Mikolov et al., 2013: Efficient Estimation of Word Representations](https://arxiv.org/abs/1301.3781) | 02–03 or buffer | Recommended | Read the original architecture/objective motivation after the lecture. | 1 h |
| [Pennington et al., 2014: GloVe](https://aclanthology.org/D14-1162/) | 03 or buffer | Recommended | Compare a global count-based objective with predictive embeddings. | 1.5 h |
| [Lambert et al., 2024: RewardBench](https://arxiv.org/abs/2403.13787) | 24 or buffer | Recommended | Examine reward-model benchmark design and limits of aggregate scores. | 1 h |

## Reading workflow and note fields

Before reading, discuss why the paper matters, its prerequisites, the problem, and
the specific sections to focus on. During reading, track notation, assumptions,
derivations, architecture, experiment controls, and evidence. Attempt key equations
before asking for a worked derivation.

After reading, explain the problem, central idea, novelty, mechanism, evidence,
limitations, and relationship to current NLP. The assistant asks follow-ups, waits,
and records demonstrated understanding separately from explanations it supplies.

A note created at that point contains: title, authors, year/version, verified link,
related lecture, priority, reading status and actual reading extent; the learner's
own summary; equations attempted; contributions; experiment/limitations analysis;
questions and assistant feedback; remaining gaps; assessment evidence/status; and
any explicit sign-off. Leave the learner-summary field unfilled until the learner
provides it. Cite exact sections or figures when discussing results.
