# Summary: Efficient neural network training

Status: Not Started

## Why this unit exists

A transformer that fits in a lecture diagram does not fit in memory once the width, the batch, and the optimizer states are real. This lecture is the systems constraint behind 'just fine-tune the model'.

## Concepts you must be able to explain

- Where memory goes: weights, gradients, optimizer state, activations
- Mixed precision as a way to store fewer bits, and what it does not change about the algorithm
- Sharding and ZeRO-style ideas: not every device holds every state
- Why this is a different problem from LoRA, which is the next unit

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

## Explain without notes

- [ ] Where memory goes: weights, gradients, optimizer state, activations
- [ ] Mixed precision as a way to store fewer bits, and what it does not change about the algorithm
- [ ] Sharding and ZeRO-style ideas: not every device holds every state
- [ ] Why this is a different problem from LoRA, which is the next unit

- [ ] You can say which of weights, gradients, and Adam state dominate memory for a large fine-tune, at the level of 'there are two or three copies'.
