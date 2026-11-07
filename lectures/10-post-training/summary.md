# Summary: Post-training: SFT, RLHF, and DPO

Status: Not Started

## Why this unit exists

A pretrained model predicts text. A model people talk to has been through a second stage that prefers some answers over others. This lecture is that second stage.

## Concepts you must be able to explain

- Supervised fine-tuning on demonstrations
- A reward model trained on preferences
- RLHF as optimizing the policy against that reward, with a penalty for drifting from the pretrained model
- DPO as a way to train on the same preferences without an explicit reward model and RL loop
- What this lecture does not claim: that the resulting model is correct, or that the preference data is unbiased

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

## Explain without notes

- [ ] Supervised fine-tuning on demonstrations
- [ ] A reward model trained on preferences
- [ ] RLHF as optimizing the policy against that reward, with a penalty for drifting from the pretrained model
- [ ] DPO as a way to train on the same preferences without an explicit reward model and RL loop
- [ ] What this lecture does not claim: that the resulting model is correct, or that the preference data is unbiased

- [ ] You can say what DPO removes relative to RLHF, and what information the preference pairs still have to provide.
