# PyTorch tutorial

| | |
| --- | --- |
| Kind | Session |
| Priority | Core |
| Plan week | 4 |
| Status | not started |

About 2 hours, before the Assignment 2 parser.

## Why this is in the course

From Assignment 2 on, the course expects you to express a model as tensors, a module, and a training loop. This session is that toolbox.

## Done when

You can write a tiny module, run one optimizer step, and say which line computed the gradient.

## Resources

- [Winter 2025 PyTorch Colab](https://colab.research.google.com/drive/1Pz8b_h-W9zIBk1p2e6v-YFYThG1NkYeS?usp=sharing)
- Local environment: `scripts/setup_venv.sh`
- [PyTorch docs](https://pytorch.org/docs/stable/index.html)

On this Mac, check torch.backends.mps.is_available() after setup. Assignments 3 and 4 were written for a GPU. MPS can run small experiments. A long training run may still want Colab or another GPU.

Full reading lists for the quarter are on the [Winter 2025 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/index.html#schedule) and the [Spring 2024 site](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/).

## Files in this folder

- [summary.md](summary.md) — concept targets, then your notes after you study
- [qa.md](qa.md) — questions from the study sessions
