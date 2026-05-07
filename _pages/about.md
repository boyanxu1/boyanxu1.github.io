---
permalink: /
title: "Boyan Xu"
excerpt: "Researcher in Text-to-SQL, Large Language Models, Sentiment Analysis, and Machine Learning"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a researcher at Guangdong University of Technology, working in the [**Data Mining & Information Retrieval Laboratory**](https://dmir.gdut.edu.cn/) under the supervision of [**Prof. Ruichu Cai**](https://ruichucai.github.io/). My research focuses on **Text-to-SQL**, **Large Language Models** and **Affective Computing**. My work aims to bridge the gap between natural language processing and database management, enhancing human-computer interaction.

My research interests include:

- **Text-to-SQL:** Developing models that translate natural language queries into SQL statements, facilitating intuitive database interactions.
- **Large Language Models:** Exploring the capabilities and applications of large-scale language models in various NLP tasks.
- **Affective Computing:** Analyzing and interpreting human emotions and opinions through computational methods.

I am always keen to collaborate with motivated students and industry partners on Text‑to‑SQL agents, causal LLMs and ABSA. Drop me an email with your CV and a short statement of interest.


# 🔥 News
- *2026.04*: &nbsp;🎉🎉 4 papers(2 main and 2 findings) under my supervision have been accepted by ACL 2026.
- *2025.12*: &nbsp;🎉🎉 We introduce a new benchmark for Indonesian Multimodal Emotion Recognition, accompanying OmniMER.
- *2025.11*: &nbsp;🎉🎉 DSQ-SQL ranks 3rd on the Spider 2.0-Lite leaderboard and has been open-sourced.
- *2025.08*: &nbsp;🎉🎉 GenLink have been accepted by EMNLP 2025 Main.
- *2025.01*: &nbsp;🎉🎉 3 papers under my supervision have been accepted by NAACL 2025.
- *2025.01*: &nbsp;🎉🎉 Chat2DB have been accepted by ICDE 2025 Demo track.
- *2024.11*: &nbsp;🎉🎉 2 papers under my supervision have been accepted by COLING 2025.
- *2024.07*: &nbsp;🎉🎉 I am the problem setter for the **2024 Third International Algorithm Case Competition (IACC)**, hosted by Pazhou Lab. The challenge I designed focuses on **"Generating Database Query Commands Based on Large Language Models"**. The competition is currently underway with a total prize pool of 500,000 RMB. ([Learn more](https://iacc.pazhoulab-huangpu.com/contestdetail?id=668de12c7ff47da8cc88c0ce&award=500,000+%E7%BB%8F%E8%B4%B9%E6%94%AF%E6%8C%81))
- *2024.05*: &nbsp;🎉🎉 The paper I supervised, "S2GSL: Incorporating Segment to Syntactic Enhanced Graph Structure Learning for Aspect-based Sentiment Analysis" has been accepted by ACL 2024 Main.
- *2023.04*: &nbsp;🎉🎉 My leader launched **Chat2DB**, a conversational AI product designed to access private databases or tabular data. With **Chat2DB**, users don't need to learn technical principles or use specialized tools. By simply uploading their data or database and describing their requirements in the chatbox, they can receive results within seconds.

# 📝 Publications 
†Corresponding Author, *Equal Contribution

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026(Main)</div><img src='images/2026_ACL_MMERROR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MMErroR: A Benchmark for Erroneous Reasoning in Vision-Language Models](https://arxiv.org/pdf/2601.03331)

Yang Shi*, Yifeng Xie*, Minzhe Guo, Liangsi Lu, Mingxuan Huang, Jingchao Wang, Zhihong Zhu, **Boyan Xu†**, Zhiqi Huang

* We introduce MMErroR, a multi-modal benchmark for process-level error diagnosis in vision-language models, comprising 1,997 curated samples across 24 subdomains and four reasoning error types, revealing that even the strongest evaluated VLM achieves only 66.65% accuracy in fine-grained error-type classification. 

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026(Main)</div><img src='images/2026_ACL_ROSESQL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Rose-SQL: Role-State Evolution Guided Structured Reasoning for Multi-Turn Text-to-SQL](https://arxiv.org/pdf/2605.03720)

Le Zhou, Feng Yao, Fengcai Qiao, Bo Xu, Fangyuan Wang, **Boyan Xu†**

* We propose Rose-SQL, a training-free framework that adapts small-scale reasoning models to multi-turn Text-to-SQL through Role-State evolution, using gain dependency analysis, structural isomorphism checks, and augmented hierarchical reasoning to track dialogue changes and guide SQL generation, achieving state-of-the-art performance on SParC and CoSQL without task-specific fine-tuning.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026(Findings)</div><img src='images/2026_ACL_SAMNER.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition](https://arxiv.org/pdf/2605.03706)

Ruichu Cai, Juntao Gan, Miao Mai, Zhifeng Hao, **Boyan Xu†**

* We propose SAM-NER, a three-stage zero-shot NER framework that mitigates semantic drift through semantic archetype mediation, combining cooperative entity discovery, universal archetype projection, and definition-guided calibration to achieve state-of-the-art cross-domain performance on CrossNER without relying on external knowledge bases. 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026(Findings)</div><img src='images/2026_ACL_SERE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification](https://arxiv.org/pdf/2605.03701)

Zhifeng Hao, Zhongjie Chen, Junhao Lu, Shengyin Yu, Guimin Hu, Keli Zhang, Ruichu Cai, **Boyan Xu†**

* We propose SERE, a structural example retrieval framework that enhances LLMs for event causality identification by jointly leveraging conceptual path similarity, syntactic tree similarity, and causal pattern filtering to retrieve structurally aligned demonstrations, mitigating causal hallucination and improving performance across multiple ECI datasets. 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025(Main)</div><img src='images/2025_EMNLP_Genlink.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GenLink: Generation-Driven Schema-Linking via Multi-Model Learning for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.1518.pdf)

Zhifeng Hao, Junqi Huang, Shaobin Shi, Ruichu Cai, **Boyan Xu†**

* We propose GenLink, a generation-driven schema-linking framework that integrates multiple small language models to infer implicit schema links through SQL generation and self-consistency, achieving strong cross-domain Text-to-SQL performance on BIRD and Spider with execution accuracies of 67.34%, 89.7%, and 87.8%. 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICDE 2025(Demo)</div><img src='images/2025_ICDE_CHAT2DB.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Chat2DB: Chatting to the Database with Interactive Agent Assisted Language Models](https://ieeexplore.ieee.org/abstract/document/11113201/)

**Boyan Xu** *, **Yuyuan Cai** *, Shaobin Shi, Zhifeng Hao, Ruichu Cai 

* We propose Chat2DB, an interactive conversational database system that enhances Text-to-SQL parsers through agent-assisted question-schema linking and adaptive retraining, enabling users to collaboratively refine schema selection, improve SQL generation accuracy, and query domain-specific databases through natural language. 

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2025(Main)</div><img src='images/2025_NAACL_IRRA.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Handling Missing Entities in Zero-Shot Named Entity Recognition: Integrated Recall and Retrieval Augmentation](https://aclanthology.org/2025.naacl-long.540.pdf)

Ruichu Cai, Junhao Lu, Zhongjie Chen, **Boyan Xu†**, Zhifeng Hao

-  We introduce IRRA, a novel two-stage framework that first uses recall-augmented entity extraction on perturbed data to boost recall and then applies retrieval-augmented generation for type correction, achieving state-of-the-art zero-shot cross-domain NER performance.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2025(Main)</div><img src='images/2025_NAACL_TRACKSQL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Track-SQL: Enhancing Generative Language Models with Dual-Extractive Modules for Schema and Context Tracking in Multi-turn Text-to-SQL](https://aclanthology.org/2025.naacl-long.536.pdf)

Bingfeng chen, Shaobin Shi, yongqi luo, **Boyan Xu†**, Ruichu Cai, Zhifeng Hao

-  We propose Track-SQL, a dual-extractive framework that augments generative LMs with a semantic-enhanced schema extractor and a schema-aware context extractor to track schema and context changes in multi-turn Text-to-SQL, achieving state-of-the-art results on SparC and CoSQL with execution accuracy gains of 7.1% and 9.55%.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2025(Findings)</div><img src='images/2025_NAACL_S2IT.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[S^2IT: Stepwise Syntax Integration Tuning for Large Language Models in Aspect Sentiment Quad Prediction](https://aclanthology.org/2025.findings-naacl.379.pdf)

Bingfeng chen, Chenjie Qiu, Yifeng Xie, **Boyan Xu†**, Ruichu Cai, Zhifeng Hao

-  We propose S^2IT, a novel Stepwise Syntax Integration Tuning framework that progressively incorporates global and local syntactic structure knowledge into LLMs to significantly enhance performance on Aspect Sentiment Quad Prediction.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">COLING 2025(Oral)</div><img src='images/2025_COLING_DRECI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Dr.ECI: Infusing Large Language Models with Causal Knowledge for Decomposed Reasoning in Event Causality Identification](https://aclanthology.org/2025.coling-main.628.pdf)

Ruichu Cai, Shengyin Yu, Jiahao Zhang, Wei Chen, **Boyan Xu†**, Keli Zhang

-  We propose Dr.ECI, a multi-agent decomposed reasoning framework for Event Causality Identification that employs specialized discovery agents (Causal Explorer, Mediator Detector) and reasoning agents (Direct and Indirect Reasoners) to capture implicit, indirect, and generalized causal structures, achieving state-of-the-art performance.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">COLING 2025(Oral)</div><img src='images/2025_COLING_CACA.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[CACA: Context-Aware Cross-Attention Network for Extractive Aspect Sentiment Quad Prediction](https://aclanthology.org/2025.coling-main.635.pdf)

Bingfeng Chen, Haoran Xu, Yongqi Luo, **Boyan Xu†**, Ruichu Cai, Zhifeng Hao

-  We propose CACA, an extractive ASQP framework that employs a Context-Aware Cross-Attention Network—alternating updates of explicit and implicit representations—and contrastive learning to align aspects and opinions for implicit term prediction, achieving superior results on three benchmarks.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024(Main)</div><img src='images/2024_ACL_S2GSL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


[S^2GSL: Incorporating Segment to Syntactic Enhanced Graph Structure Learning for Aspect-based Sentiment Analysis](https://arxiv.org/abs/2406.02902)

Bingfeng Chen, Qihan Ouyang, Yongqi Luo, **Boyan Xu†**, Ruichu Cai, Zhifeng Hao (ACL 2024 Main)

-  We introduce S^2GSL, a novel graph-structure learning framework for ABSA that combines segment-aware semantic graph learning with syntax-based latent graph learning—and a self-adaptive aggregation network to filter irrelevant contexts and fuse diverse structures—achieving superior results on four benchmarks.

</div>
</div>

- [Hierarchical Action Learning for Weakly-Supervised Action Segmentation](https://arxiv.org/pdf/2602.24275), Junxian Huang, Ruichu Cai, Hao Zhu, Juntao Fang, **Boyan Xu**, Weilin Chen, Zijian Li, Shenghua Gao (CVPR 2026)
- [What Gets Activated: Uncovering Domain and Driver Experts in MoE Language Models](https://arxiv.org/pdf/2601.10159), Guimin Hu, Meng Li, Qiwei Peng, Lijie Hu, **Boyan Xu**, Ruichu Cai (Preprints)
- [ENTRA: Entropy-Based Redundancy Avoidance in Large Language Model Reasoning](https://arxiv.org/pdf/2601.07123), Ruichu Cai, Haopeng Du, Qingwen Lin, Yutong Chen, Zijian Li, **Boyan Xu†** (Preprints)
- [CMCTS: A Constrained Monte Carlo Tree Search framework for mathematical reasoning in large language model](https://arxiv.org/pdf/2502.11169), Qingwen Lin, **Boyan Xu**, Guimin Hu, Zijian Li, Zhifeng Hao, Keli Zhang, Ruichu Cai (Applied Intelligence)
- [OmniMER: Indonesian Multimodal Emotion Recognition via Auxiliary-Enhanced LLM Adaptation](https://arxiv.org/pdf/2512.19379), **Xueming Yan** *, **Boyan Xu** * Yaochu Jin, Lixian Xiao, Wenlong Ye, Runyang Cai, Zeqi Zheng, Jingfa Liu, Aimin Yang (Preprints)
- [Text-to-SQL as Dual-State Reasoning: Integrating Adaptive Context and Progressive Generation](https://arxiv.org/pdf/2511.21402), Zhifeng Hao, Qibin Song, Ruichu Cai, **Boyan Xu†** (Preprints)
- [Causal View of Time Series Imputation: Some Identification Results on Missing Mechanism](https://arxiv.org/pdf/2505.07180), Ruichu Cai, Kaitao Zheng, Zijian Li, Junxian Huang, Zhengming Chen, **Boyan Xu**, Zhifeng Hao (IJCAI 2025)
- [Causal-aware Large Language Models: Enhancing Decision-Making through Learning, Adapting and Acting](https://arxiv.org/abs/2505.24710), Wei Chen, Jiahao Zhang, Haipeng Zhu, **Boyan Xu**, Zhifeng Hao, Keli Zhang, Junjian Ye, Ruichu Cai (IJCAI 2025)
- PEFT Innovations in Text-to-SQL: Adapter and Prefix Tuning Methods with Structural Awareness, Zhifeng Hao, Yuyuan Cai, Shaobin Shi, **Boyan Xu†**, Ruichu Cai (IJCNN 2025)
- [TP-UNet: Temporal Prompt Guided UNet for Medical Image Segmentation](https://arxiv.org/pdf/2411.11305), Ranmin Wang, Limin Zhuang, Hongkun Chen, **Boyan Xu†**, Ruichu Cai (Preprint)
- [SDGNN: Structure-aware Dual Graph Neural Network for Code Summarization](https://link.springer.com/article/10.1007/s13042-024-02471-2), Zhifeng Hao, Zonghao Lin, Shengqiang Zhang, **Boyan Xu†**, Ruichu Cai (JMLC)
- [From Large to Tiny: Distilling and Refining Mathematical Expertise for Math Word Problems with Weakly Supervision](https://arxiv.org/pdf/2403.14390), Qingwen Lin, **Boyan Xu**, Zhengting Huang, Ruichu Cai (ICIC 2024)
- [SADGA: Structure-aware dual graph aggregation network for text-to-sql](https://proceedings.neurips.cc/paper_files/paper/2021/file/3f1656d9668dffcf8119e3ecff873558-Paper.pdf), Ruichu Cai, Jinjie Yuan, **Boyan Xu†**, Zhifeng Hao (NeurIPS 2021)
- [Causal mechanism transfer network for time series domain adaptation in mechanical systems](https://dl.acm.org/doi/abs/10.1145/3445033), Zijian Li, Ruichu Cai, Hong Wei Ng, Marianne Winslett, Tom ZJ Fu, **Boyan Xu**, Xiaoyan Yang, Zhenjie Zhang (TIST)
- [Semi-supervised disentangled framework for transferable named entity recognition](https://arxiv.org/pdf/2012.11805), Zhifeng Hao, Di Lv, Zijian Li, Ruichu Cai, Wen Wen, **Boyan Xu** (Neural Networks)
- [Meta Multi-Task Learning for Speech Emotion Recognition](http://www.interspeech2020.org/uploadfile/pdf/Wed-3-8-8.pdf), Ruichu Cai, Kaibin Guo, **Boyan Xu†**, Xiaoyan Yang, Zhenjie Zhang (Interspeech 2020)
- [TAG: Type auxiliary guiding for code comment generation](https://aclanthology.org/2020.acl-main.27.pdf), Ruichu Cai, Zhihao Liang, **Boyan Xu†**, Zijian Li, Yuixing Hao, Yao Chen (ACL 2020)
- [Disentanglement Challenge: From Regularization to Reconstruction](https://openreview.net/pdf?id=r1griYFhiB), **Jie Qiao** *, **Zijian Li** *, **Boyan Xu** *, Ruichu Cai, Kun Zhang, NeurIPS 2019 Workshop Disentanglement Challenge
- [An encoder-decoder framework translating natural language to database queries](https://www.ijcai.org/proceedings/2018/0553.pdf), Ruichu Cai, **Boyan Xu**, Xiaoyan Yang, Zhenjie Zhang, Zijian Li, Zhihao Liang (IJCAI 2018)
- [Data driven chiller plant energy optimization with domain knowledge](https://arxiv.org/abs/1812.00679), Hoang Dung Vu, Kok Soon Chai, Bryan Keating, Nurislam Tursynbek, **Boyan Xu**, Kaige Yang, Xiaoyan Yang, Zhenjie Zhang (CIKM 2017)
