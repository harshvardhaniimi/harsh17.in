---
title: Can a Machine Tell Pokémon Types Apart?
subtitle: A hands-on, no-prerequisites introduction to machine learning
summary: A hands-on workshop introducing machine learning by building classifiers that guess a Pokémon's type from the colours in its image.
author: Harshvardhan
date: '2026-04-21T12:00:00Z'
event: SBA Workshop (MODA & BAA)
location: American University of Sharjah
slug: pokemon-workshop
tags:
- academia
- ai
- machine-learning
- python
- tools
---
A gentle, hands-on introduction to machine learning that I ran for the School of Business Administration, organised by the student clubs MODA and BAA. No prior coding or machine-learning background was required. We build small classifiers that look at a Pokémon's image and guess whether it is **Fire**, **Water**, or **Grass** type, using only the colours in the picture.

Along the way we cover how a computer "sees" an image as a grid of RGB values, how to turn each image into just three numbers (the average red, green, and blue), two model families (Random Forests and Logistic Regression), evaluation with accuracy and confusion matrices, and hyperparameter tuning with cross-validation. The two takeaways cut against the usual hype: tuning is useful but not magic, and picking the right model family often matters more than tuning it. An optional bonus section covers PCA.

Everything is in the repository below. The notebook runs end-to-end in Google Colab with no local setup, and it downloads the data itself.

### Links

- [GitHub repository](https://github.com/harshvardhaniimi/pokemon-workshop)
- [Notebook (Google Colab)](https://colab.research.google.com/github/harshvardhaniimi/pokemon-workshop/blob/main/Pokemon_Workshop.ipynb)
- [Slides](/docs/pokemon-workshop/slides.pdf)
