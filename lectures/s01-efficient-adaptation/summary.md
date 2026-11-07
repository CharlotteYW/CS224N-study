# Summary: Efficient adaptation: prompting and PEFT

Status: Not Started

## Why this unit exists

Most people do not full-fine-tune a large model. They prompt it, or they train a small set of extra weights. That is the practical counterpart of Assignment 4.

## Concepts you must be able to explain

- Few-shot prompting as conditioning, not as training
- Why a prompt can fail even when the task is 'in' the pretraining data
- Parameter-efficient fine-tuning: most weights stay frozen
- LoRA: a low-rank update added to a weight matrix, and what 'low rank' is buying
- The difference between saving memory during training (Lecture 12) and training fewer new parameters (this lecture)

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

## Explain without notes

- [ ] Few-shot prompting as conditioning, not as training
- [ ] Why a prompt can fail even when the task is 'in' the pretraining data
- [ ] Parameter-efficient fine-tuning: most weights stay frozen
- [ ] LoRA: a low-rank update added to a weight matrix, and what 'low rank' is buying
- [ ] The difference between saving memory during training (Lecture 12) and training fewer new parameters (this lecture)

- [ ] You can explain LoRA as an update of the form BA added to a frozen weight, and say what you would do if you cannot afford a full fine-tune.
