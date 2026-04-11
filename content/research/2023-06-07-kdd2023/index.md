---
title: End-to-End Inventory Prediction and Contract Allocation for Guaranteed Delivery
  Advertising
summary: We proposed a novel end-to-end approach, the Neural Lagrangian Selling (NLS)
  model, to improve Guaranteed Delivery (GD) advertising by concurrently predicting
  ad impression inventory and optimizing contract allocation. The model incorporates
  a differentiable Lagrangian layer and a graph convolutional neural network to enable
  direct optimization of allocation regret and effective handling of various allocation
  targets and constraints. [🔗 PDF](https://www.harsh17.in/docs/kdd2023/E2E_Paper.pdf)
author: Harshvardhan
date: '2023-06-07'
slug: kdd2023
tags:
- academia
- machine-learning
- python
cover:
  image: og.png
  relative: true
  hidden: true
---
Recently, our research on end to end inventory prediction and contract allocation model got accepted to [KDD 2023 Conference](https://kdd.org/kdd2023/). I will be presenting the paper in Long Beach, CA between August 6-10, 2023. KDD (29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining) is the premier conference on data science. I am thrilled to share our research. The poster presentation and the talk went great. Scroll down for some pictures!

### Links

-   [Paper PDF](/docs/kdd2023/E2E_Paper.pdf)

-   [Slides](/docs/kdd2023/E2E_Slides.pdf)

-   [Poster](/docs/kdd2023/E2E_Poster.pdf)

-   [Video](https://www.youtube.com/watch?v=Ghh8qRZDFJw)

### Abstract

Guaranteed Delivery (GD) advertising plays an essential part in e-commerce marketing, where the ad publisher signs contracts with advertisers in advance by promising delivery of advertising impressions to fulfill targeting requirements for advertisers. Previous research on GD advertising mainly focused on online serving yet overlooked the importance of contract allocation at the GD selling stage.

Traditional GD selling approaches consider impression inventory prediction and contract allocation as two separate stages.

However, such a two-stage optimization often leads to inferior contract allocation performance. In this paper, our goal is to reduce this performance gap with a novel end-to-end approach. Specifically, we propose the Neural Lagrangian Selling (NLS) model to jointly predict the impression inventory and optimize the contract allocation of advertising impressions with a unified learning objective.

To this end, we first develop a differentiable Lagrangian layer to backpropagate the allocation problem through the neural network and allow direct optimization of the allocation regret. Then, for effective optimization with various allocation targets and constraints, we design a graph convolutional neural network to extract predictive features from the bipartite allocation graph. Extensive experiments show that our approach can improve GD selling performance compared with existing two-stage approaches.

Particularly, our optimization layer can outperform the baseline solvers in both computational efficiency and solution quality.

To the best of our knowledge, this is the first study to apply the end-to-end prediction and optimization approach for industrial GD selling problems. Our work has implications for general prediction and allocation problems as well.

### Pictures

![](images/IMG_9533.png)![](images/IMG_9459.png)![](images/IMG_9455.png)

### Citation

Wuyang Mao, Chuanren Liu, Yundu Huang, Zhonglin Zu, M Harshvardhan, Liang Wang, and Bo Zheng. 2023. End-to-End Inventory Prediction and Contract Allocation for Guaranteed Delivery Advertising. In *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '23)*, August 6--10, 2023, Long Beach, CA, USA.

I sincerely thank [Prof ChuanRen Liu](https://datamining.utk.edu/) for his guidance on this project and the opportunity to contribute meaningfully.
