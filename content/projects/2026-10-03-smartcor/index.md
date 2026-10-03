---
title: smartcor
summary: R and Python packages that select correlation methods for mixed variable types and explain the choice, with estimates and statistical inference.
author: Harshvardhan
date: '2026-10-03'
slug: smartcor
tags:
- R
- Python
- statistics
- research
github: https://github.com/harshvardhaniimi/smartcor
website: https://harshvardhaniimi.github.io/smartcor/
websiteLabel: Documentation
projectLinks:
- label: R package
  url: https://github.com/harshvardhaniimi/smartcor/tree/master/packages/smartcor
- label: Python / PyPI
  url: https://pypi.org/project/pysmartcor/
- label: arXiv paper
  url: https://arxiv.org/abs/2607.22285
---

A correlation matrix is easy to calculate. Choosing a suitable method for each pair of variables takes more care, especially when a dataset mixes continuous, count, binary, ordinal, and categorical variables.

smartcor detects variable types, selects a suitable correlation or association method, and reports the estimate, confidence interval, p-value, and reasoning behind the choice. It also identifies alternative methods. The project has two implementations: **smartcor for R** and **pysmartcor for Python**.

I developed the project with Pritam Ranjan. Our accompanying paper, *smartcor: Intelligent Correlation Method Selection for Mixed Variable Types*, explains the method-selection framework.

- [R package source](https://github.com/harshvardhaniimi/smartcor/tree/master/packages/smartcor)
- [Python package on PyPI](https://pypi.org/project/pysmartcor/)
- [Documentation and vignettes](https://harshvardhaniimi.github.io/smartcor/)
- [Paper on arXiv:2607.22285](https://arxiv.org/abs/2607.22285)

Install the Python package with:

```bash
pip install pysmartcor
```
