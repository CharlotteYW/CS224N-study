# Summary: Sequence-to-sequence models, attention, and machine translation

Status: not started

## Why this unit exists

Translation is two sequences of different lengths. The encoder compresses the source. The decoder produces the target. Attention is how the decoder looks back, and it is the idea the transformer will keep after it throws the recurrence away.

## Concepts you must be able to explain

- LSTM and GRU as gated ways to keep a signal alive across many steps (2025 lecture 6 / the shared notes)
- Encoder-decoder: one sequence in, another sequence out
- Attention weights as a learned soft alignment over encoder states
- Query, key, and value in this RNN setting, before self-attention
- Subword vocabularies as the way an open vocabulary fits in a fixed softmax
- BLEU: what it counts, and why a high BLEU is not the same as a good translation

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

## Explain without notes

- [ ] LSTM and GRU as gated ways to keep a signal alive across many steps (2025 lecture 6 / the shared notes)
- [ ] Encoder-decoder: one sequence in, another sequence out
- [ ] Attention weights as a learned soft alignment over encoder states
- [ ] Query, key, and value in this RNN setting, before self-attention
- [ ] Subword vocabularies as the way an open vocabulary fits in a fixed softmax
- [ ] BLEU: what it counts, and why a high BLEU is not the same as a good translation

- [ ] You can draw encoder, decoder, and attention weights for one decoding step, and say what the weights are a distribution over.
