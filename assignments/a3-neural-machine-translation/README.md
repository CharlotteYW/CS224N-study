# Assignment 3: neural machine translation

| | |
| --- | --- |
| Kind | Assignment |
| Priority | Core |
| Plan week | 7 |
| Status | not started |

A full week, and start the training run before the writeup is polished. The model is larger than Assignment 2 and the run is the long part.

## Why this is in the course

You implement an encoder-decoder with attention, then you look at what it actually does to sentences. The written half is there so a BLEU number does not replace an error analysis.

## Done when

A training run finishes, the written analysis is in your own words in summary.md, and you can point at one attention pattern and say whether it is sensible.

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
