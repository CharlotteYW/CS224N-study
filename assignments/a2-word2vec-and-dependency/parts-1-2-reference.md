# A2 Parts 1–2 self-study reference

Winter 2025. Worked notes for personal review. See the [official handout](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2.pdf) for the question numbering.

## 1. Word2Vec with full softmax

Use the handout's column convention. With vocabulary size $N$ and embedding size $d$, the outside matrix $U=[u_1,\ldots,u_N]$ has shape $(d,N)$, and the center vector $v_c$ has shape $(d,1)$. The scores are $z=U^\top v_c$, the predictions are $\hat y=\operatorname{softmax}(z)$, and $y$ is one-hot at the observed outside word $o$.

### 1(a). Cross-entropy

$$-\sum_w y_w\log\hat y_w=-\log\hat y_o.$$

Only $y_o=1$ contributes. The loss is the negative log probability assigned to the observed word.

### 1(b). Center vector gradient

**(i)** Expand the loss as $J=-z_o+\log\sum_j e^{z_j}$. The two terms give

$$\frac{\partial J}{\partial z_w}=-y_w+\frac{e^{z_w}}{\sum_j e^{z_j}}=\hat y_w-y_w.$$

Since $z_w=u_w^\top v_c$ has derivative $u_w$ with respect to $v_c$, sum over the score paths:

$$\nabla_{v_c}J=\sum_w(\hat y_w-y_w)u_w=U(\hat y-y).$$

The final expression has shape $(d,1)$.

**(ii)** The gradient is zero exactly when $U(\hat y-y)=0$, or equivalently $U\hat y=Uy=u_o$. This means the prediction-weighted average of outside vectors coincides with the observed outside vector. Equality of the probability vectors is sufficient, while a nontrivial null space of $U$ can allow different probability vectors with the same average.

**(iii)** The update is $v_c \leftarrow v_c+\eta u_o-\eta\sum_w\hat y_w u_w$. The first term moves the center toward the observed outside vector. The second moves it away from the current predicted average, so outside words assigned more probability contribute more to that correction. The two terms act together.

### 1(c). What L2 normalization can erase

If $u_x=\alpha u_y$ with $\alpha>0$ and $u_y\ne0$, the two normalized vectors are identical. Normalizing each word before adding the vectors can erase useful magnitude differences. For example, suppose one coordinate expresses sentiment, two interchangeable positive terms contribute $+3$ and $+1$, and the other words together contribute $-2$. The raw phrase scores are $+1$ and $-1$. After normalization the two positive terms contribute equally, so the classifier can no longer distinguish those phrases via that term.

Normalization is harmless for this distinction if vector length carries no useful information and the task depends on direction. For example, if all word vectors have the same positive norm and the decision is the sign of a linear score on their sum with zero intercept, normalizing scales the whole sum by one positive constant and leaves the sign unchanged.

### 1(d). Matrix layout

$$\nabla_U J=[\nabla_{u_1}J\;\;\nabla_{u_2}J\;\;\cdots\;\;\nabla_{u_N}J].$$

Each column has the shape of its corresponding outside vector.

### 1(e). Outside vector gradients

Only score $z_w$ depends directly on $u_w$, with derivative $v_c$. The chain rule gives

$$
\nabla_{u_w}J=(\hat y_w-y_w)v_c
=
\begin{cases}
(\hat y_o-1)v_c & w=o,\\
\hat y_w v_c & w\ne o.
\end{cases}
$$

For review, stacking the columns gives the outer product $\nabla_U J=v_c(\hat y-y)^\top$, with shape $(d,N)$. Gradient descent adds a multiple of $v_c$ to the observed outside vector and subtracts probability-weighted multiples from the other vectors.

**Tiny check.** If the logits are $[0,\log 2,0]$ and the middle word is observed, then $\hat y=[1/4,1/2,1/4]^\top$. The score gradients are $[1/4,-1/2,1/4]^\top$. Multiply each scalar by $v_c$ to get the corresponding column gradient.

## 2. Adam and dropout

### 2(a)(i). Momentum

The exponential moving average $m$ blends the newest minibatch gradient with recent gradients. An isolated fluctuation has less effect than it would in a plain SGD step, while a direction that repeats across minibatches persists in the average. This can reduce zigzagging and make progress along persistent directions steadier.

### 2(a)(ii). Adaptive scaling

Adam maintains a separate moving average of squared gradients for each parameter coordinate. For the same numerator magnitude $|m_i|$, a coordinate with smaller recent squared gradients has a smaller denominator $\sqrt{v_i}$ and receives a larger update. Conversely, coordinates with large recent squared gradients receive more scaling down. This helps when different coordinates have different gradient scales. The actual update size depends on both numerator and denominator.

### 2(b)(i). Dropout scale

For a fixed activation $h_i$, the mask has expectation $\mathbb{E}[d_i]=1-p_{\mathrm{drop}}$. Therefore,

$$\mathbb{E}[\gamma d_i h_i]=\gamma(1-p_{\mathrm{drop}})h_i.$$

Matching this to $h_i$ gives $\gamma=1/(1-p_{\mathrm{drop}})$ for $0\le p_{\mathrm{drop}}<1$. For example, with $h_i=4$ and $p_{\mathrm{drop}}=0.25$, the activation is zero a quarter of the time and $16/3$ otherwise. The mean is still $4$.

### 2(b)(ii). Training and evaluation

During training, random masks expose the model to different subsets of activations. This regularizes the model by discouraging reliance on a particular set of units. During standard evaluation, keep all units active for deterministic predictions. With the training-time scale above, evaluation uses the unmasked activations directly.
