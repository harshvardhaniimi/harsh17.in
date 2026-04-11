---
title: 'Dynamic GP: Application to Malaria Vaccine Coverage Prediction'
summary: We applied a dynamic Gaussian process model to predict coverage for novel
  Malaria vaccines in 78 countries. Using publicly available WHO data on coverage
  of nine vaccines, we developed localised models for countries grouped using the
  human development index (HDI). We deployed convolutions of standard GP models with
  weights determined using singular value decomposition of time-series response matrix.
  [🔗 PDF](https://www.harsh17.in/docs/malaria_paper.pdf)
author: Harshvardhan
date: '2020-12-20'
slug: dynamic-gp-application-to-malaria-vaccine-coverage-prediction
tags:
- academia
- economics
- r
cover:
  image: og.png
  relative: true
  hidden: true
---
We applied a dynamic Gaussian process model to predict coverage for novel Malaria vaccines in 78 countries. Using publicly available WHO data on coverage of nine vaccines, we developed localised models for countries grouped using the human development index (HDI). We deployed convolutions of standard GP models with weights determined using singular value decomposition of time-series response matrix.

### Abstract

Gaussian process (GP) based statistical surrogates are popular, inexpensive substitutes for emulating the outputs of expensive computer models that simulate real-world phenomena or complex systems. Here, we discuss the evolution of dynamic GP model — a computationally efficient statistical surrogate for a computer simulator with time series outputs. The main idea is to use a convolution of standard GP models, where the weights are guided by a singular value decomposition (SVD) of the response matrix over the time component. The dynamic GP model also adopts a localized modeling approach for building a statistical model for large datasets. In this chapter, we use several popular test function based computer simulators to illustrate the evolution of dynamic GP models. We also use this model for predicting the coverage of Malaria vaccine worldwide. Malaria is still affecting more than eighty countries concentrated in the tropical belt. In 2019 alone, it was the cause of more than 435,000 deaths worldwide. The malice is easy to cure if diagnosed in time, but the common symptoms make it difficult. We focus on a recently discovered reliable vaccine called Mos-Quirix (RTS,S) which is currently going under human trials. With the help of publicly available data on dosages, efficacy, disease incidence and communicability of other vaccines obtained from the World Health Organisation, we predict vaccine coverage for 78 Malaria-prone countries.

### Citation

Ranjan, P. and Harshvardhan, M. (2022). "The Evolution of Dynamic Gaussian Process Model with
Applications to Malaria Vaccine Coverage Prediction". In D.D. Hanagal, R.V. Latpatel & G. Chandra
(Eds.), Applied Statistical Methods: ISGES 2020. *Springer*. Singapore.

### Links
- PDF: https://www.harsh17.in/docs/malaria_paper.pdf
- arXiv: https://arxiv.org/abs/2012.11124
- Google Books: https://www.google.co.in/books/edition/Applied_Statistical_Methods/h1-vzgEACAAJ?hl=en
- Blog: https://www.harsh17.in/forecasting-malaria-vaccine-demand/
- Springer: https://link.springer.com/book/9789811679322


