# A2 Part 3 self-study guide

This reference follows the Winter 2025 parser assignment. The trace and
attachment examples use new sentences. The learner chose to review the design
and examples and defer implementation and training.

[Winter 2025 A2 handout](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2.pdf#page=5)

| Question | What it asks | What to learn |
| --- | --- | --- |
| 3(a) | Trace a given dependency tree through the parser actions. | A stack, a buffer, and an arc list are enough to describe each intermediate state. |
| 3(b) | Count the actions for a sentence of length n. | Each token enters the stack once and leaves it once. |
| 3(c) | Implement the state and the three transitions. | A legal action changes the state in a specific way. An arc removes its dependent, so finish that dependent's children first. |
| 3(d) | Parse several unfinished sentences in a minibatch. | Batch the classifier calls while each sentence keeps its own state and can finish at a different time. |
| 3(e) | Derive local gradients, implement the classifier, train it, and report UAS. | A supervised classifier chooses one action at a time. A sequence of actions produces a tree. |
| 3(f) | Diagnose four bad attachments and identify the intended heads. | Classify an error by the kind of phrase or modifier attached to the wrong head. |
| 3(g) | Explain why POS tags help. | Tags let the model reuse grammatical patterns across different words. |

## Worked trace and action count

For “Cats chase birds,” suppose the intended heads give the arcs
`chase → Cats`, `chase → birds`, and `ROOT → chase`. The stack top
is on the right and the buffer front is on the left.

| Action | Stack after action | Buffer after action | New arc |
| --- | --- | --- | --- |
| Start | ROOT | Cats, chase, birds | |
| SHIFT | ROOT, Cats | chase, birds | |
| SHIFT | ROOT, Cats, chase | birds | |
| LEFT-ARC | ROOT, chase | birds | chase → Cats |
| SHIFT | ROOT, chase, birds | empty | |
| RIGHT-ARC | ROOT, chase | empty | chase → birds |
| RIGHT-ARC | ROOT | empty | ROOT → chase |

SHIFT moves one buffer token to the stack. LEFT-ARC takes the top item as
head and removes the item just below it. RIGHT-ARC takes the item just below
the top as head and removes the top. Use the head and dependent indices to
distinguish repeated word forms in a sentence.

There are n SHIFTs because each input token leaves the buffer once. There
are n arc actions because each input token is popped once and ROOT stays.
The trace therefore takes 2n actions, including the final root attachment.

For batched decoding, keep an ordered list of states for the original
sentences. Take a minibatch from the unfinished states, predict one legal
action per state, apply each action, and remove finished states from the
unfinished list. Read the arc lists from the original ordered states at the
end. This batches inference. A training minibatch instead groups labeled
states to compute a gradient and one optimizer update.

## Classifier, gradients, and evaluation

Select features from the current stack, buffer, and partial arcs. If a state
provides m feature IDs and each embedding has d coordinates, gather the m
rows and concatenate them into an md-dimensional vector x. For a batch of B
states, the gathered tensor has shape (B, m, d), the flattened input has
shape (B, md), and the network produces logits of shape (B, 3).

The hidden layer computes z = xW + b1 and h = ReLU(z). One input coordinate
x_j affects hidden coordinate h_i with derivative W[j, i] when z_i is
positive and 0 when z_i is negative. At the output, softmax cross-entropy
gives a logit gradient of p_i minus the indicator that i is the gold
action. For example, if the scores yield [0.2, 0.6, 0.2] and the middle
action is correct, the gradient is [0.2, -0.4, 0.2].

During training, gather the embeddings, compute hidden activations, apply
dropout, and compute the logits. Feed these logits to cross-entropy,
backpropagate, and take an optimizer step. The assignment asks learners to
build the embedding lookup and affine layers explicitly. During decoding,
restrict action selection to legal moves. One attachment error can change
the next state and affect later predictions.

UAS counts tokens whose predicted head matches the reference head, ignoring
relation labels under the evaluation's token selection. For example, four
correct heads among five scored tokens yield 80% UAS. Example scores here
are illustrative. Assignment training and its sanity checks are pending.

## Worked attachment examples

The arrows below use head → dependent. Each example states the intended
reading so the choice of head can be checked.

| Error type | Example and intended reading | Incorrect arc | Correct arc |
| --- | --- | --- | --- |
| Prepositional phrase | “Maya sliced the bread with a knife.” The knife is her instrument. | bread → knife | sliced → knife |
| Verb phrase | “Hearing the bell, Maya closed the door.” The opening phrase describes the circumstances of closing the door. | door → Hearing | closed → Hearing |
| Modifier | “The soup was extremely salty.” The adverb gives the degree of saltiness. | soup → extremely | salty → extremely |
| Coordination | “We packed apples and pears.” The two fruits are coordinated objects. | packed → pears | apples → pears |

For POS features, compare “They read books” with “They repair bicycles.”
The words differ, but the verb followed by a noun provides a reusable clue
for an object attachment. Word identities still add information about the
specific head and the intended meaning.
