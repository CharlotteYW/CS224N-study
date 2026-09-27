# CS224N study journal

Personal study notes for Stanford CS 224N, Natural Language Processing with Deep Learning. This repository records what I can explain after each lecture and assignment. It does not host Stanford's handouts, starter code, or solution writeups.

## Sources

Watch [Spring 2024 on YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D) (Christopher Manning and guest lecturers). That is the public video series.

Read and do the work from [Winter 2025](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/). Use its slides and the notes that site links for the first half of the course. Several of those note PDFs were written in 2019 or 2023 and kept because the derivations did not change. The 2025 slides are the updated lecture. From pretraining onward, the 2025 site is slides rather than a long note, so the 2024 video carries the explanation.

Do the Winter 2025 assignments once. They cover the same four skills as 2024: word vectors, word2vec derivatives plus a dependency parser, neural machine translation, and transformer fine-tuning. The default project to follow is the 2025 minimal GPT-2, not the 2024 minimal BERT discussed in the video.

Two Winter 2025 lectures are not separate 2024 videos, and they are still required:

- [Efficient adaptation](lectures/s01-efficient-adaptation/README.md) (prompting and LoRA)
- [Question answering and knowledge](lectures/s02-qa-and-knowledge/README.md) (retrieval and RAG)

Guest lectures on speech BCIs, TreeRNNs, responsible NLP, and linguistics stay in the tree as enrichment. They wait until Assignments 2–4 are finished.

## How a study step works

1. The instructor names the next session and the learning target for that sitting: which week, which folder, what to open, and what you must be able to explain when you return. The target comes from that unit's "Done when" line and its concept list.
2. Watch the video or do the session, with the 2025 slides or notes open.
3. Come back and say what you understood. The instructor turns that into the unit's `summary.md`: your own words, dated, checked against the concept list. A sentence copied from a slide does not count.
4. Ask questions in the chat. The instructor answers, then writes a short version of your question and that answer into `qa.md`. The **Still fuzzy?** column is `yes` when the idea is not solid yet, and `no` when you can restate it.
5. Update the status row below. Use `not started`, `in progress`, `notes drafted`, or `complete`.
6. Commit the note changes and push to GitHub, then name the next session and its learning target.

Concept checklists in each summary are the target, written before studying. The notes underneath them get filled in after the session, with the instructor's help.

## Pace

Fourteen weeks, about 8–10 hours a week. Three sittings: one lecture, one second lecture or tutorial, one coding block. Assignments 2, 3, and 4 are allowed to slip a week. If a week is interrupted, finish that derivation or training run in the next week. Transformers are not allowed to start while attention is still a diagram you cannot redraw.

- **Week 1.** Environment, the prerequisite check below, the Python session, Lecture 1.
- **Week 2.** Lecture 2 and Assignment 1.
- **Week 3.** Lecture 3. Start only the written derivative part of Assignment 2.
- **Week 4.** Lecture 4, the PyTorch session, finish Assignment 2, then the closed-book checkpoint.
- **Week 5.** Lecture 5. Restate vanishing gradients the next day without slides.
- **Week 6.** Lecture 6. Draw encoder, decoder, and attention before opening Assignment 3.
- **Week 7.** Assignment 3. Start the training run early.
- **Week 8.** Lecture 7 (short), Lecture 8, Hugging Face session. Rewrite scaled dot-product attention from memory.
- **Week 9.** Lecture 9 and start Assignment 4. If this week is short, spill into Week 10 rather than skim pretraining.
- **Week 10.** Lecture 10 and continue Assignment 4.
- **Week 11.** Lecture 11, Lecture 12, the PEFT supplement, finish Assignment 4, second checkpoint.
- **Week 12.** Question answering and knowledge, Lecture 14, Lecture 15.
- **Week 13.** Enrichment lectures only if the core is solid. Write the project proposal.
- **Week 14.** First running slice of the project, and the synthesis review.

```text
prereq check -> word vectors and A1 -> backprop, parsing, and A2
             -> RNNs, attention, and A3 -> transformers, pretraining, and A4
             -> evaluation, PEFT, retrieval -> GPT-2 or a concrete custom project
```

## Prerequisite self-check

Do this in week 1, before Lecture 3. If an item fails, pause and repair it. Nielsen's *Neural Networks and Deep Learning*, chapters 1–2, plus the calculus PDFs linked from Lecture 3, are the repair material.

- Dot product, cosine, and a matrix-vector product, including the shape of the result
- A partial derivative and the chain rule on a scalar function of two variables
- Softmax and cross-entropy at the formula level
- NumPy: shape, broadcasting, and a vectorized operation you did not write as a Python loop

## Environment

```bash
bash scripts/setup_venv.sh
source .venv/bin/activate
```

The environment is Python 3 with NumPy, PyTorch, JupyterLab, and Matplotlib. It is for lectures, small experiments, and later assignment work on this machine. Download each assignment zip into that assignment's `work/` directory when you reach it. Those directories are gitignored.

Assignments 3 and 4 were written to train on a GPU. Apple MPS is checked by the setup script and is appropriate for small runs. Use the course Colab links in those assignment folders if a local run is too slow.

## What does not get committed

Stanford PDFs, starter zips, datasets, checkpoints, and your solution code stay on disk under `assignments/*/work/` and `project/work/`. The remote is the study journal: summaries, questions, the tracker, and the project writeup notes.

## Status tracker

Rows follow the study order. Lecture 13 and the other enrichment lectures sit in week 13, after the week 12 core.

| Unit | Kind | Priority | Week | Status | Summary | QA |
| --- | --- | --- | --- | --- | --- | --- |
| [sessions/01-python-numpy](sessions/01-python-numpy/README.md) | Session | Core | 1 | not started | — | — |
| [lectures/01-word-vectors](lectures/01-word-vectors/README.md) | Lecture | Core | 1 | not started | — | — |
| [lectures/02-word-vectors-and-language-models](lectures/02-word-vectors-and-language-models/README.md) | Lecture | Core | 2 | not started | — | — |
| [assignments/a1-word-vectors](assignments/a1-word-vectors/README.md) | Assignment | Core | 2 | not started | — | — |
| [lectures/03-backprop-and-neural-nets](lectures/03-backprop-and-neural-nets/README.md) | Lecture | Core | 3 | not started | — | — |
| [lectures/04-dependency-parsing](lectures/04-dependency-parsing/README.md) | Lecture | Core | 4 | not started | — | — |
| [sessions/02-pytorch](sessions/02-pytorch/README.md) | Session | Core | 4 | not started | — | — |
| [assignments/a2-word2vec-and-dependency](assignments/a2-word2vec-and-dependency/README.md) | Assignment | Core | 3–4 | not started | — | — |
| [lectures/05-recurrent-neural-networks](lectures/05-recurrent-neural-networks/README.md) | Lecture | Core | 5 | not started | — | — |
| [lectures/06-seq2seq-and-machine-translation](lectures/06-seq2seq-and-machine-translation/README.md) | Lecture | Core | 6 | not started | — | — |
| [assignments/a3-neural-machine-translation](assignments/a3-neural-machine-translation/README.md) | Assignment | Core | 7 | not started | — | — |
| [lectures/07-final-projects](lectures/07-final-projects/README.md) | Lecture | Core | 8 | not started | — | — |
| [lectures/08-transformers](lectures/08-transformers/README.md) | Lecture | Core | 8 | not started | — | — |
| [sessions/03-huggingface-transformers](sessions/03-huggingface-transformers/README.md) | Session | Core | 8 | not started | — | — |
| [lectures/09-pretraining](lectures/09-pretraining/README.md) | Lecture | Core | 9 | not started | — | — |
| [lectures/10-post-training](lectures/10-post-training/README.md) | Lecture | Core | 10 | not started | — | — |
| [assignments/a4-transformers](assignments/a4-transformers/README.md) | Assignment | Core | 9–11 | not started | — | — |
| [lectures/11-evaluation](lectures/11-evaluation/README.md) | Lecture | Core | 11 | not started | — | — |
| [lectures/12-efficient-training](lectures/12-efficient-training/README.md) | Lecture | Core | 11 | not started | — | — |
| [lectures/s01-efficient-adaptation](lectures/s01-efficient-adaptation/README.md) | Supplement | Core supplement | 11 | not started | — | — |
| [lectures/s02-qa-and-knowledge](lectures/s02-qa-and-knowledge/README.md) | Supplement | Core supplement | 12 | not started | — | — |
| [lectures/14-agents](lectures/14-agents/README.md) | Lecture | Core | 12 | not started | — | — |
| [lectures/15-life-after-dpo](lectures/15-life-after-dpo/README.md) | Lecture | Core | 12 | not started | — | — |
| [lectures/13-speech-bci](lectures/13-speech-bci/README.md) | Lecture | Enrichment | 13 | not started | — | — |
| [lectures/16-convnets-treernns](lectures/16-convnets-treernns/README.md) | Lecture | Enrichment | 13 | not started | — | — |
| [lectures/17-responsible-nlp](lectures/17-responsible-nlp/README.md) | Lecture | Enrichment | 13 | not started | — | — |
| [lectures/18-linguistics-philosophy](lectures/18-linguistics-philosophy/README.md) | Lecture | Enrichment | 13 | not started | — | — |
| [project](project/README.md) | Project | Core | 13–14 | not started | — | — |
| [reviews/checkpoint-after-a2.md](reviews/checkpoint-after-a2.md) | Review | Core | 4 | not started | — | — |
| [reviews/checkpoint-after-a4.md](reviews/checkpoint-after-a4.md) | Review | Core | 11 | not started | — | — |
| [reviews/synthesis.md](reviews/synthesis.md) | Review | Core | 14 | not started | — | — |
