# Assignment 3: neural machine translation

| | |
| --- | --- |
| Kind | Assignment |
| Priority | Core |
| Plan week | 11–13 |
| Status | Not Started |

Winter 2025 source. Plan for 20–26 active hours across Weeks 11–13; unattended training is additional. The detailed weekly budget is in [ROADMAP](../../ROADMAP.md).

## Why this is in the course

You implement an encoder-decoder with attention, then you look at what it actually does to sentences. The written half is there so a BLEU number does not replace an error analysis.

## Done when

A training run finishes, the official written analysis is completed privately and summary.md records safe learning reflections, and you can point at one attention pattern and say whether it is sensible.

## Resources

- [Winter 2025 handout](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a3.pdf)
- [Winter 2025 starter zip](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a3.zip)
- [LaTeX template](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a3_tex.zip)
- Lecture 5: `lectures/05-recurrent-neural-networks`
- Lecture 6: `lectures/06-seq2seq-and-machine-translation`

Unzip into assignments/a3-neural-machine-translation/work/ (gitignored). The 2025 handout expects a GPU-class run. Use Colab or another GPU if MPS is too slow. Record the command, the hardware, and the BLEU you observed in summary.md. Do not commit the code or the checkpoint.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions

## Prerequisites and milestones

L05–07, gated RNNs, attention, PyTorch, and a small convolution/shape primer.

- [ ] Read the complete 2025 architecture and environment requirements; attempt encoder/decoder/attention milestones.
- [ ] Run the official sanity checks and short local diagnostics; record only actual results.
- [ ] Train/decode/evaluate as instructed; record hardware, commands, active time, compute time, and metrics.
- [ ] Independently finish written NMT analysis, explain failures and limitations, then assess and request A3 sign-off.

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
