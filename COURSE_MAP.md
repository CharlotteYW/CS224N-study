# Course map and source audit

Sources audited 2026-11-02; map finalized 2026-11-03 (America/Los_Angeles). This map identifies sources, not completed study.

## Curriculum decision

- **Primary offering and all four assignments: Winter 2025.** This retains a coherent
  sequence from embeddings through parsing, RNN translation, and Transformer pretraining.
- **Primary public video collection: Spring 2024**, with **Winter 2023** recordings
  for Transformers and Pretraining. Always use the individual links below.
- **Selected Winter 2026 updates:** pretraining, evaluation, agents/RAG, reasoning,
  tokenization/multilinguality, and social impacts. These are supplements, not a change
  to assignment numbering. No public Winter 2026 recording is assumed.
- **Final project:** a scoped custom NLP experiment using the Winter 2025 project
  guidance, or the complete Winter 2025 GPT-2 default project with additional time.
  The default project discussed in the 2024 video is BERT, not GPT-2.

This recommendation preserves the repository's existing course choices and the NMT
foundation the learner wants. It is a self-study curriculum, not a claim of Stanford
enrollment or completion of Winter 2026 coursework. The current course explicitly
requires current assignments for enrolled students; old work would not earn credit.

## Authoritative sources and verification limits

- [Winter 2025 schedule and policy](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/)
- [Spring 2024 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/)
- [Winter 2023 schedule](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/)
- [Winter 2026 schedule and policy](https://web.stanford.edu/class/cs224n/)
- [Official public playlist linked by Winter 2026](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D)

The official HTML schedules were fetched and inspected. Video URLs, titles, years,
and durations were read from the live playlist metadata; videos were **not watched**
and playback was not tested. YouTube's separate oEmbed endpoint returned Unauthorized.
PDF/starter links were checked for HTTP reachability; that does not certify that every
page has been read or that a starter environment runs. Selected assignment handouts
were inspected for scope. Colab links are verified as official schedule links only;
notebook access and execution remain unverified. Both 2025 and 2026 describe their
current recordings as restricted to enrolled students on Canvas.

## What the repository actually contained

- Lecture directories 01–18 follow the **2024 topic order**, not the 2025/2026 order.
- Slides and all assignment links primarily target **Winter 2025**. `s01` and `s02`
  correspond to its lectures 11 and 13.
- The NumPy session is recorded complete, with dated notes and saved notebook outputs.
  All other units are recorded not started; their summaries are learning targets.
- There were no central agent instructions, course map, progress record, handoff,
  paper index, or assessment log. These are now lightweight navigation/state files.
- The previous 14-week schedule had little room for assignment debugging or a finished
  project. The revised plan has 28 active weeks and optional buffer weeks.

No existing directory has been renamed or deleted. Existing learner notes and notebook
answers/outputs are preserved. A legacy completion claim is not a new formal sign-off.

## Video and lecture directory mapping

Directory IDs below are stable local IDs. Times are playlist runtimes at 1x; budget
extra time to pause. `Lxx` in ROADMAP means the local ID, not an official year-specific number.

| Local folder / topic | Public recording: actual year, title, duration | Primary material / official 2025 match | Study week |
| --- | --- | --- | --- |
| [lectures/01-word-vectors](lectures/01-word-vectors/README.md) | 2024: [Lecture 1 - Intro and Word Vectors](https://www.youtube.com/watch?v=DzpHeXVSC5I) (1:20:17) | 2025 L1: Word Vectors; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture01-wordvecs1.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture01-wordvecs1.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n_winter2023_lecture1_notes_draft.pdf) | 1 |
| [lectures/02-word-vectors-and-language-models](lectures/02-word-vectors-and-language-models/README.md) | 2024: [Lecture 2 - Word Vectors and Language Models](https://www.youtube.com/watch?v=nBor4jfWetQ) (1:19:12) | 2025 L2: Word Vectors and Language Models; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture02-wordvecs2.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture02-wordvecs2.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes02-wordvecs2.pdf) | 2 |
| [lectures/03-backprop-and-neural-nets](lectures/03-backprop-and-neural-nets/README.md) | 2024: [Lecture 3 - Backpropagation, Neural Network](https://www.youtube.com/watch?v=HnliVHU2g9U) (1:13:27) | 2025 L3: Backpropagation and Neural Network Basics; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture03-neuralnets.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture03-neuralnets.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes03-neuralnets.pdf) | 4 |
| [lectures/04-dependency-parsing](lectures/04-dependency-parsing/README.md) | 2024: [Lecture 4 - Dependency Parsing](https://www.youtube.com/watch?v=KVKvde-_MYc) (1:18:57) | 2025 L4: Dependency Parsing; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture04-dep-parsing.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture04-dep-parsing.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes04-dependencyparsing.pdf) | 6 |
| [lectures/05-recurrent-neural-networks](lectures/05-recurrent-neural-networks/README.md) | 2024: [Lecture 5 - Recurrent Neural Networks](https://www.youtube.com/watch?v=fyc0Jzr74y4) (1:18:52) | 2025 L5: Basic Sequence Models to RNNs; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture05-rnnlm.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture05-rnnlm.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes05-LM_RNN.pdf) | 9 |
| [lectures/06-seq2seq-and-machine-translation](lectures/06-seq2seq-and-machine-translation/README.md) | 2024: [Lecture 6 - Sequence to Sequence Models](https://www.youtube.com/watch?v=Ba6Fn1-Jsfw) (1:17:09) | 2025 L6: Advanced Variants of RNNs, Attention; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture06-fancy-rnn.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture06-fancy-rnn.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-2019-notes05-LM_RNN.pdf) | 10 |
| [lectures/07-final-projects](lectures/07-final-projects/README.md) | 2024: [Lecture 7 - Attention, Final Projects and LLM Intro](https://www.youtube.com/watch?v=J7ruSOIzhrE) (1:17:44) | 2025 L7: Final Projects: Custom and Default; Practical Tips; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture07-final-project.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture07-final-project.pdf) | 10; revisit 25 |
| [lectures/08-transformers](lectures/08-transformers/README.md) | 2023: [Lecture 8 - Self-Attention and Transformers](https://www.youtube.com/watch?v=LWMzyfvuehA) (1:17:04) | 2025 L8: Transformers; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture08-transformers.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/slides/cs224n-2023-lecture08-transformers.pdf); [notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/readings/cs224n-self-attention-transformers-2023_draft.pdf) | 14 |
| [lectures/09-pretraining](lectures/09-pretraining/README.md) | 2023: [Lecture 9 - Pretraining](https://www.youtube.com/watch?v=DGfCRXuNA2w) (1:18:46) | 2025 L9: Pretraining; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture09-pretraining.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/slides/cs224n-2023-lecture9-pretraining.pdf) | 15 |
| [lectures/10-post-training](lectures/10-post-training/README.md) | 2024: [Lecture 10 - Post-training by Archit Sharma](https://www.youtube.com/watch?v=35X6zlhoCy4) (1:19:42) | 2025 L10: Post-training (RLHF, SFT, DPO); [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture10-instruction-tunining-rlhf.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture10-prompting-rlhf.pdf) | 19 |
| [lectures/11-evaluation](lectures/11-evaluation/README.md) | 2024: [Lecture 11 - Benchmarking by Yann Dubois](https://www.youtube.com/watch?v=TO0CqzqiArM) (1:24:24) | 2025 L12: Benchmarking and Evaluation; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture12-evaluation-final.pdf); [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture11-evaluation-yann.pdf) | 21 |
| [lectures/12-efficient-training](lectures/12-efficient-training/README.md) | 2024: [Lecture 12 - Efficient Training, Shikhar Murty](https://www.youtube.com/watch?v=UVX7SYGCKkA) (1:02:32) | 2024 supplement; no separate 2025 core equivalent; [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture12-training-shikhar.pdf) | 20 |
| [lectures/13-speech-bci](lectures/13-speech-bci/README.md) | 2024: [Lecture 13 - Brain-Computer Interfaces, Chaofei Fan](https://www.youtube.com/watch?v=tfVgHsKpRC8) (1:12:49) | 2024 optional guest lecture; [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture13-speech-bci.pdf) | Optional after 24 |
| [lectures/14-agents](lectures/14-agents/README.md) | 2024: [Lecture 14 - Reasoning and Agents by Shikhar Murty](https://www.youtube.com/watch?v=I0tj4Y7xaOQ) (1:03:42) | 2024 supplement; not 2025 L14; [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture14-agents-shikhar-updated.pdf) | 23 |
| [lectures/15-life-after-dpo](lectures/15-life-after-dpo/README.md) | 2024: [Lecture 15 - After DPO by Nathan Lambert](https://www.youtube.com/watch?v=dnF463_Ar9I) (1:08:57) | 2024 historical supplement; not a 2025 scheduled lecture; [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture15-life-after-dpo-lambert.pdf) | 24 |
| [lectures/16-convnets-treernns](lectures/16-convnets-treernns/README.md) | 2024: [Lecture 16 - ConvNets and TreeRNNs](https://www.youtube.com/watch?v=S8d-7v3f5MQ) (1:11:56) | 2024 optional historical models; [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture16-CNN-TreeRNN.pdf) | Optional after 24 |
| [lectures/17-responsible-nlp](lectures/17-responsible-nlp/README.md) | No matching public recording verified; study slides | 2024 responsible NLP slot; use 2026 L16 replacement; [legacy deck; match unverified](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-2024-lecture17-human-centered-nlp.pdf); [2026 social impacts slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture16-impact-on-humanity.pdf) | 24 (2026 replacement) |
| [lectures/18-linguistics-philosophy](lectures/18-linguistics-philosophy/README.md) | 2024: [Lecture 18 - NLP, Linguistics, Philosophy](https://www.youtube.com/watch?v=NxH0Y78xcF4) (1:16:27) | 2024 optional closing lecture; [video-year slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/cs224n-spr2024-lecture18-nlp-linguistics-philosophy.pdf) | Optional after 28 |
| [lectures/s01-efficient-adaptation](lectures/s01-efficient-adaptation/README.md) | No matching public recording verified; study slides | 2025 L11: Efficient Adaptation (Prompting + PEFT); [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture11-adapatation.pdf) | 20 |
| [lectures/s02-qa-and-knowledge](lectures/s02-qa-and-knowledge/README.md) | No matching public recording verified; study slides | 2025 L13: Question Answering and Knowledge; [2025 slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-lecture13-QA.pdf) | 22 |

### Important mismatches and coverage gaps

1. Playlist position is not lecture number. A 2023 Natural Language Generation video
   appears between Pretraining and the 2024 Post-training recording. It is optional,
   not the 2024 evaluation lecture. The playlist also appends 2023 multimodality,
   interpretability, and tutorial videos.
2. No 2024 Lecture 17 recording appears in the inspected playlist. The previously
   linked human-centered slide file is reachable, but the 2024 schedule lists Adina
   Williams's Responsible NLP lecture without a slide link. Do not claim that file
   matches her talk. The required Week 24 replacement is the explicitly labeled
   2026 Social and Broader Impacts of NLP deck.
3. The 2024 L7 recording includes **attention**, as its title indicates. Study it
   before A3; it is not merely a project orientation to skip until Transformers.
4. The 2025 notes reuse 2019 and 2023 drafts. Their file years are provenance, not
   new assignments. L5/L6 intentionally share notes; read different sections.
5. 2025 L11 is PEFT; L12 is evaluation; L13 is QA. These differ from local 11–13.
   The 2025 guest sequence (Rush, Min, Yao, Huang, Brown, then Open Questions) is not
   represented by the similarly numbered 2024 folders. No unavailable guest video
   is invented. Interpretability is a recommended extension below; other guest
   material can be added by topic when public resources are available.
6. Post-training L10 and Life after DPO L15 overlap intentionally: foundation first,
   later critical reading. Efficient training and PEFT are distinct; systems depth
   remains in `ai-infra-lab`.
7. The old A2 summary incorrectly assigned negative-sampling derivations to A2.
   Winter 2025 A2 uses naive-softmax derivatives; negative sampling is independent
   practice. A4 includes attention, pretraining, and rotary positions, not merely
   a Hugging Face fine-tuning tutorial. A3 also uses a convolutional layer; include
   a small convolution primer rather than requiring all of optional L16.
8. Live *Speech and Language Processing* chapter numbers changed. At the inspected
   August 2026 edition, Dependency Parsing is chapter 20 (old link 19 now means
   constituency), Transformers and Pretraining is 7 (old 9 now means masked LMs),
   and Masked Language Models is 9 (old 11 now means IR/RAG). Verify topic titles
   through the [current contents](https://web.stanford.edu/~jurafsky/slp3/) each time.
9. The old `transformersbook.com` URL returned 404; use official Hugging Face docs.
   The Stanford GloVe PDF host was unreachable; use the ACL Anthology version.
   The optional Karpathy Medium backprop article returned 403: unverified/inaccessible
   in this audit. The required course notes cover that material.

## Assignment versions and local routing

All required handouts and code come from the **2025 archive**, even where a topic
also appears in 2026. Do not merge starters or tests between years.

| Local assignment | Winter 2025 required work | Winter 2026 comparison | Plan |
| --- | --- | --- | --- |
| [A1](assignments/a1-word-vectors/README.md) | Word-vector exploration; [official notebook ZIP](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a1.zip). Instructions are in the notebook. The old HTML preview is a supplementary preview, not the authoritative 2025 version. | Word vectors; separate release. | Weeks 2–3; 8–12 active hours |
| [A2](assignments/a2-word2vec-and-dependency/README.md) | [Word2Vec and Dependency Parsing](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a2.pdf): naive-softmax derivatives, Adam/dropout, neural parser. | Foundations/derivatives/parsing; use its handout only if explicitly changing the course plan. | Weeks 5–8; 18–24 active hours |
| [A3](assignments/a3-neural-machine-translation/README.md) | [Neural Machine Translation](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a3.pdf): recurrent encoder-decoder, attention, analysis. | [Self-Attention and Transformers](https://web.stanford.edu/class/cs224n/assignments_w26/a3.pdf). **Not NMT.** | Weeks 11–13; 20–26 active hours plus training |
| [A4](assignments/a4-transformers/README.md) | [Self-Attention, Transformers, and Pretraining](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/assignments_w25/a4.pdf): mathematical attention questions, pretraining/fine-tuning, RoPE, analysis. | [LLM Evals](https://web.stanford.edu/class/cs224n/assignments_w26/a4.pdf): API benchmarks, model judges, red-teaming. This file's first-page header says 2025, but the 2026 schedule/path and later page headers identify the 2026 release. | Weeks 16–18; 20–26 active hours plus training |

The 2026 evaluation assignment refers to course-provided model/API access and credits;
public availability of a PDF does not establish that an independent learner can run
it. Week 21 instead uses a clearly separate local evaluation exercise. It does not
count as completing 2026 A4.

The [2025 policy](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/)
allows AI collaboration but prohibits soliciting/copying answers and substantial AI
completion. It restricts TA code inspection for A3/A4 and projects. The companion
uses conceptual/debugging-strategy support for those units. No official solution is
generated or published. Assignment tests and remote grading access are not assumed.

## Winter 2026 update routing

These are topic mappings, not equivalent lecture numbers or additional assignments.

| 2026 lecture | Local home | Priority and use |
| --- | --- | --- |
| L1 History of NLP; L2 Word Vectors; L3 Backpropagation | local 01–03 | Optional historical/update reading; core foundation uses 2025 |
| L4 Language Models and RNNs; L5 Transformers; L6 Projects | local 05–08 | Covered by primary path; local 04 parsing and 06 NMT remain required |
| L7 Pretraining | local 09 | Recommended update in Week 15: [slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture07-pretraining.pdf) |
| L8 Post-training; L9 Efficient Adaptation | local 10 and s01 | Optional updated [post-training](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture08-posttraining.pdf) and [PEFT](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture09-peft.pdf) decks |
| L10 Agents, Tool Use, and RAG | local s02 and 14 | Required selected update in Week 23: [slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture10-rag-agents.pdf) |
| L11 Benchmarking and Evaluation | local 11 | Required comparison in Week 21: [slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture11-evaluation.pdf) |
| L12 Reasoning 1; L13 Reasoning 2 | local 14 | Required selected update Week 23: [part 1](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture12-reasoning-part1.pdf); part 2 recommended |
| L14 Tokenization and Multilinguality | local 09 | Recommended Week 15 or buffer: [slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture14-guest-julie-tokenization-multilinguality.pdf) |
| L15 Interpretability | local 11 | Recommended older public substitute below; 2026 public recording/slides not verified |
| L16 Social and Broader Impacts of NLP (Risks) | local 17 | Required Week 24: [slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture16-impact-on-humanity.pdf) |
| L17 Multimodality | local 13 QA for cross-modal comparisons | Optional older public substitute below; not equivalent to speech BCI |
| L18 Tinker and LoRA Without Regret | local s01 | Optional guest topic; public 2026 recording/slides not verified |
| L19 Open Questions in NLP 2026 | reviews/synthesis.md | Recommended Week 28: [slides](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture19-open-questions.pdf) |

## Tutorials and optional public extensions

Tutorial recordings below are **2023**, even though the playlist containing them is
labeled Spring 2024. Use current library documentation alongside historical videos.

| Unit | Verified public recording | Role |
| --- | --- | --- |
| Python/NumPy | [Manasi Sharma, 47:14](https://www.youtube.com/watch?v=8j4wpU98Q74) | Optional refresher; preserve completed session |
| PyTorch | [Drew Kaul, 47:01](https://www.youtube.com/watch?v=Uv0AIRr3ptg) | Required Week 6 with current autograd docs |
| Hugging Face | [Eric Frankel, 47:57](https://www.youtube.com/watch?v=b80by3Xk_A8) | Recommended Week 15; current quicktour is required |
| Natural Language Generation | [2023 L11, 1:18:25](https://www.youtube.com/watch?v=N9L32bFieEY) | Recommended after Week 15; decoding beyond the core budget |
| Model Interpretability & Editing | [Been Kim, 2023 L19, 1:11:42](https://www.youtube.com/watch?v=cd3pRpEtjLs) | Recommended after Week 21; compare with [2025 guest slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/slides_w25/cs224n-2025-guest-lecture-interpretability.pdf) |
| Multimodal Deep Learning | [Douwe Kiela, 2023 L16, 1:18:23](https://www.youtube.com/watch?v=5vfIT5LOkR0) | Optional after Week 24 |

## Compute and environment

Use the existing `.venv` for ordinary practice; it was not modified in this audit.
Do not assume that this modern Python environment satisfies old assignment pins.
At each assignment start inspect the official requirements and run a small user-led
smoke check before installing packages or scheduling long training. MPS support must
be checked for the actual operations; 64 GB unified memory is not CUDA compatibility.

The 2025 A3 handout estimates about two GPU hours; A4 describes two pretraining runs
of roughly an hour each on its reference GPU setup. These are **historical handout
estimates**, not Mac benchmarks or promised runtimes. Count active study separately
from unattended compute. Start with CPU/MPS diagnostics; request a compute decision
only if full runs are impractical. No cloud credits, account access, spend, or automatic
reminders have been arranged.
