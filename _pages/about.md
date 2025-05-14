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

I am a researcher at Guangdong University of Technology, working in the [**Data Mining & Information Retrieval Laboratory**](https://dmir.gdut.edu.cn/) under the supervision of [**Prof. Ruichu Cai**](https://ruichucai.github.io/). My research focuses on **Text-to-SQL**, **Large Language Models** and **Sentiment Analysis**. My work aims to bridge the gap between natural language processing and database management, enhancing human-computer interaction.

My research interests include:

- **Text-to-SQL:** Developing models that translate natural language queries into SQL statements, facilitating intuitive database interactions.
- **Large Language Models:** Exploring the capabilities and applications of large-scale language models in various NLP tasks.
- **Sentiment Analysis:** Analyzing and interpreting human emotions and opinions through computational methods.

I am always keen to collaborate with motivated students and industry partners on Text‑to‑SQL agents, causal LLMs and ABSA. Drop me an email with your CV and a short statement of interest.


# 🔥 News
- *2025.01*: &nbsp;🎉🎉 3 papers under my supervision have been accepted by NAACL 2025.
- *2025.01*: &nbsp;🎉🎉 Chat2DB have been accepted by ICDE 2025 Demo track.
- *2024.11*: &nbsp;🎉🎉 2 papers under my supervision have been accepted by COLING 2025.
- *2024.07*: &nbsp;🎉🎉 I am the problem setter for the **2024 Third International Algorithm Case Competition (IACC)**, hosted by Pazhou Lab. The challenge I designed focuses on **"Generating Database Query Commands Based on Large Language Models"**. The competition is currently underway with a total prize pool of 500,000 RMB. ([Learn more](https://iacc.pazhoulab-huangpu.com/contestdetail?id=668de12c7ff47da8cc88c0ce&award=500,000+%E7%BB%8F%E8%B4%B9%E6%94%AF%E6%8C%81))
- *2024.05*: &nbsp;🎉🎉 The paper I supervised, "S2GSL: Incorporating Segment to Syntactic Enhanced Graph Structure Learning for Aspect-based Sentiment Analysis" has been accepted by ACL 2024 Main.
- *2023.04*: &nbsp;🎉🎉 My leader launched **Chat2DB**, a conversational AI product designed to access private databases or tabular data. With **Chat2DB**, users don't need to learn technical principles or use specialized tools. By simply uploading their data or database and describing their requirements in the chatbox, they can receive results within seconds.

# 📝 Publications 
†Corresponding Author, *Equal Contribution

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

- Causal View of Time Series Imputation: Some Identification Results on Missing Mechanism, Ruichu Cai, Kaitao Zheng, Zijian Li, Junxian Huang, Zhengming Chen, **Boyan Xu**, Zhifeng Hao (IJCAI 2025)
- Causal-aware Large Language Models: Enhancing Decision-Making through Learning, Adapting and Acting, Wei Chen, Jiahao Zhang, Haipeng Zhu, **Boyan Xu**, Zhifeng Hao, Keli Zhang, Junjian Ye, Ruichu Cai (IJCAI 2025)
- PEFT Innovations in Text-to-SQL: Adapter and Prefix Tuning Methods with Structural Awareness, Zhifeng Hao, Yuyuan Cai, Shaobin Shi, **Boyan Xu†**, Ruichu Cai (IJCNN 2025)
- [Leveraging Constrained Monte Carlo Tree Search to Generate Reliable Long Chain-of-Thought for Mathematical Reasoning](https://arxiv.org/abs/2502.11169), Qingwen Lin, Boyan Xu, Zijian Li, Zhifeng Hao, Keli Zhang, Ruichu Cai (Work in Progress)
- Chat2DB: Chatting to the Database with Interactive Agent Assisted Language Models，**Boyan Xu** *, **Yuyuan Cai** *, Shaobin Shi, Zhifeng Hao, Ruichu Cai (ICDE 2025 Demo) 
- [TP-UNet: Temporal Prompt Guided UNet for Medical Image Segmentation](https://arxiv.org/pdf/2411.11305), Ranmin Wang, Limin Zhuang, Hongkun Chen, **Boyan Xu†**, Ruichu Cai (Preprint)
- SDGNN: Structure-aware Dual Graph Neural Network for Code Summarization, Zhifeng Hao, Zonghao Lin, Shengqiang Zhang, **Boyan Xu†**, Ruichu Cai (JMLC)
- [From Large to Tiny: Distilling and Refining Mathematical Expertise for Math Word Problems with Weakly Supervision](https://arxiv.org/pdf/2403.14390), Qingwen Lin, **Boyan Xu**, Zhengting Huang, Ruichu Cai (ICIC 2024)
- [SADGA: Structure-aware dual graph aggregation network for text-to-sql](https://proceedings.neurips.cc/paper_files/paper/2021/file/3f1656d9668dffcf8119e3ecff873558-Paper.pdf), Ruichu Cai, Jinjie Yuan, **Boyan Xu†**, Zhifeng Hao (NeurIPS 2021)
- [Causal mechanism transfer network for time series domain adaptation in mechanical systems](https://dl.acm.org/doi/abs/10.1145/3445033), Zijian Li, Ruichu Cai, Hong Wei Ng, Marianne Winslett, Tom ZJ Fu, **Boyan Xu**, Xiaoyan Yang, Zhenjie Zhang (TIST)
- [Semi-supervised disentangled framework for transferable named entity recognition](https://arxiv.org/pdf/2012.11805), Zhifeng Hao, Di Lv, Zijian Li, Ruichu Cai, Wen Wen, **Boyan Xu** (Neural Networks)
- [Meta Multi-Task Learning for Speech Emotion Recognition](http://www.interspeech2020.org/uploadfile/pdf/Wed-3-8-8.pdf), Ruichu Cai, Kaibin Guo, **Boyan Xu†**, Xiaoyan Yang, Zhenjie Zhang (Interspeech 2020)
- [TAG: Type auxiliary guiding for code comment generation](https://aclanthology.org/2020.acl-main.27.pdf), Ruichu Cai, Zhihao Liang, **Boyan Xu†**, Zijian Li, Yuixing Hao, Yao Chen (ACL 2020)
- [Disentanglement Challenge: From Regularization to Reconstruction](https://openreview.net/pdf?id=r1griYFhiB), **Jie Qiao** *, **Zijian Li** *, **Boyan Xu** *, Ruichu Cai, Kun Zhang, NeurIPS 2019 Workshop Disentanglement Challenge
- [An encoder-decoder framework translating natural language to database queries](https://www.ijcai.org/proceedings/2018/0553.pdf), Ruichu Cai, **Boyan Xu**, Xiaoyan Yang, Zhenjie Zhang, Zijian Li, Zhihao Liang (IJCAI 2018)
- [Data driven chiller plant energy optimization with domain knowledge](https://arxiv.org/abs/1812.00679), Hoang Dung Vu, Kok Soon Chai, Bryan Keating, Nurislam Tursynbek, **Boyan Xu**, Kaige Yang, Xiaoyan Yang, Zhenjie Zhang (CIKM 2017)
