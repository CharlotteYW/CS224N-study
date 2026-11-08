# Summary: Backpropagation and neural network basics

Status: In Progress

## Why this unit exists

This is the gate for the rest of the course. Later lectures name architectures. This lecture is why training changes the parameters.

## Concepts you must be able to explain

- A network as a computation graph of local functions
- The chain rule, applied from the loss backward
- Shapes: which dimension a derivative travels along
- Why a nonlinearity is what makes a stack of layers more than one linear map
- Cross-entropy loss as the training signal for a classifier
- Gradient descent, and what a learning rate is doing

## My study notes

Write these after you watch, read, or solve. Date each entry. Use your own words. A sentence copied from a slide is not a note.

## Assistant quick reference

Forward computes and saves intermediate values. Backward applies the chain rule
to compute gradients. The optimizer uses those gradients to update parameters.

For a toy binary classifier, use x = 2 and y = 1. Start with w1 = 1, b1 = 0,
w2 = 0.5, and b2 = -1. Forward gives z1 = 2, ReLU(z1) = 2, z2 = 0,
sigmoid(z2) = 0.5, and binary cross-entropy = log(2). Backward starts
with dL/dz2 = p - y = -0.5. The gradients for w2, b2, w1, and b1 are
-1, -0.5, -0.5, and -0.25, respectively. One SGD step at learning rate
0.1 gives w2 = 0.6, b2 = -0.95, w1 = 1.05, and b1 = 0.025.
The assistant verified the four gradients with central finite differences.

When one value feeds multiple paths, add their contributions. For example,
L = h^2 + 3h gives dL/dh = 2h + 3. At h = 2, the two paths contribute
4 and 3, giving a total of 7.

### Matrix mini-batch example

Use two samples as rows of X = [[1, 1], [2, 2]] and class IDs [0, 1].
Both weight matrices start as the 2-by-2 identity and both biases are zero.
ReLU leaves the first layer outputs unchanged. The final logits in each row
are tied, so each predicted distribution is [0.5, 0.5] and the mean
cross-entropy is log(2).

With a mean batch loss, the logit gradient is (P - Y) / 2, where Y contains
the one-hot labels. Its two rows are [-0.25, 0.25] and [0.25, -0.25].
Multiplying by the transpose of the hidden activations gives the output
weight gradient [[0.25, -0.25], [0.25, -0.25]]. The output bias gradient
is the sum of the rows, [0, 0]. The hidden gradient is the logit gradient
times the transpose of the second weight matrix. Both hidden units are
active, so the first weight gradient is the same as the second in this
specific example.

In a standard mini-batch loop, clear the old gradients, compute one forward
pass and one batch loss, backpropagate, then call the optimizer step once.
Backward computes gradients. The optimizer step applies the update.
Gradient accumulation can deliberately combine several batches before a step.

## Explain without notes

- [ ] A network as a computation graph of local functions
- [ ] The chain rule, applied from the loss backward
- [ ] Shapes: which dimension a derivative travels along
- [ ] Why a nonlinearity is what makes a stack of layers more than one linear map
- [ ] Cross-entropy loss as the training signal for a classifier
- [ ] Gradient descent, and what a learning rate is doing

- [ ] A small gradient is derived on paper and written into the study notes. The result matches a finite-difference check or a worked example you trust.
