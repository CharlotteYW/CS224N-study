# Questions: Backpropagation and neural network basics

Record a question when it comes up. After it is answered, keep the answer here, and mark whether it is still fuzzy. Fuzzy items are the start of the next session.

| Date | Question | Answer | Still fuzzy? |
| --- | --- | --- | --- |
| | | | |

## Open questions

- None yet.

## Forward, backward, and the optimizer

- Learner explanation: Forward uses matrix multiplication and ends with cross-entropy. Backward uses gradient descent.
- Assistant feedback: For the classification example, forward computes layer outputs using affine transformations and nonlinear activations, then cross-entropy. Backpropagation computes parameter gradients by applying the chain rule. Gradient descent then uses those gradients to update the parameters.
- Understanding check: Given a weight, its computed gradient, and a learning rate, explain the update and identify which step computed the gradient.
