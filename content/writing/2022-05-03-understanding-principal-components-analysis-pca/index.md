---
title: Understanding Principal Components Analysis (PCA)
author: Harshvardhan
date: '2022-05-03'
slug: understanding-principal-components-analysis-pca
tags:
- data-science
draft: true
cover:
  image: og.png
  relative: true
  hidden: true
---
Principal Components Analysis is a technique to reduce the dimensions of data while accounting for linear variability. Consider a simple equation:

$$
y = x_0 \beta_0 + x_1\beta_1 + \epsilon.
$$

As our textbooks would've instructed us, the variables `\(x_0\)` and `\(x_1\)` are independent variable and `\(y\)` is the dependent variable. In a natural experiment, we provide a treatment and observe the variable measures. There is little distinction between `\(x\)` and `\(y\)` until the researcher manually assigns predictors and response.

Principal component analysis utilises this "hidden" linear relationship between the independent variables to fit a line or a hyper plane that minimises the overall error. Sounds gibberish? Bear with me.

# Thought Bubble

Imagine there are lots of small fishes floating around in a sea. The shark is hungry and she wants food. Their positions are as in the picture below. Pardon my art skills.

![](images/Screen%20Shot%202022-05-03%20at%204.13.49%20PM.png)

The red and green shark will both have enough to eat. However, it is the indigo shark which will have the highest kills. Why? Look at their positions! In fact, the blue shark is following the first *principal component* of the school of small fishes. PCA gives a linear estimate of the line that explains the maximum variability. The fishes are coming down diagonally and that is the direction with the maximum variability.

Consider we have data about 500 people on their ten different behaviour parameters. If we want to reduce the number of dimensions to a smaller set, we can look for the "direction" that has the maximum variability.

# Example

The best way to learn an algorithm is to practice it by hand. Consider this data:



