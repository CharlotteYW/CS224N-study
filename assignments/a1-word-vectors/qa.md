# Questions: Assignment 1: exploring word vectors

Record a question when it comes up. After it is answered, keep the answer here, and mark whether it is still fuzzy. Fuzzy items are the start of the next session.

| Date | Question | Answer | Still fuzzy? |
| --- | --- | --- | --- |
| | | | |

## Open questions

- None yet.

## Part 1 implementation review

- Question 1.1: The learner corrected the order of the nested comprehension so that the document is bound before iterating its words. Test execution was not reported separately.
- Question 1.2: The learner implemented the matrix and reported a passing check after moving the vocabulary mapping before the loop, including the rightmost context position, and mapping document positions through tokens to vocabulary indices. The assistant reviewed the pasted attempts. The check was reported by the learner.
- Question 1.3: The learner reported that the notebook check passed. Feedback clarified the distinction between the notebook variable n_iters and the scikit-learn keyword n_iter. The assistant separately verified the shape change on a toy ratings matrix.
- Questions 1.4–1.5: The learner shared a plotting approach that looks up the selected rows and annotates their coordinates. They reported no issue with Question 1.5 and noticed that the reference uses crosses while their plot uses dots. Feedback explained that the marker affects appearance, while the coordinates and labels determine the plotted relationships. No separate 1.4 test result was reported.
- Question 2.1: The learner generated the plot and asked why it could differ from Part 1. Coaching identified the distinct corpora, the count rows versus pretrained embeddings, and the separate two-dimensional SVD fits. The learner will choose and interpret a difference visible in their own plots.

## Self-study review of Part 2

- The learner requested worked reference explanations for self-study and stated that they do not intend to submit the assignment. They identified vector arithmetic as the main idea behind the analogy questions.
- The assistant checked illustrative nearest-neighbor, distance, analogy, and bias queries against the locally cached 200-dimensional GloVe model using the A1 Python environment. These are assistant-run examples. They do not establish that the learner ran or completed those cells.
- The review covered shared context, approximate relation offsets, polysemy, interpretation of corpus associations, and projection-based debiasing.
