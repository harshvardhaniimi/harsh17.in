---
title: Score and Fisher's Information
subtitle: Intuitive Understanding and Mathematical Notions
summary: Intuitive Understanding and Mathematical Notions
author: Harshvardhan
date: '2022-02-13'
slug: score-and-fisher-s-information
tags:
- data-science
header-includes:
- \usepackage{amsmath}
bibliography: references.bib
cover:
  image: og.png
  relative: true
  hidden: true
---
## Likelihood

Likelihood is a measure of how probable a parameter is, given our data. It is calculated as the joint probability of the observed data as a function of parameters for a given statistical model. Since joint probabilities are usually products, it is much easier to deal with log-likelihood which is a sum of probabilities.

Note that, likelihood is not the PDF of parameters. In maximum likelihood estimation, the likelihood function (i.e. the joint probability) is maximised to obtain a specific value of parameter. This value is “most likely” to be the true but unknown parameter. Generally, true parameter is denoted as `\(\theta\)` and it’s estimate is denoted as `\(\hat{\theta}\)`.

## Score

Score is a derivative of log-likelihood function with respect to the parameter. It is usually evaluated at a particular value of the parameter.

$$
s(\theta) = \frac{\partial \log \mathcal{L}(\theta)}{\partial \theta}
$$

This differentiation will lead to a `\(1 \times m\)` vector. This vector indicates the sensitivity of the likelihood. Under certain regularity conditions[^1], we can prove that the expected value of `\(s(\theta)\)` is zero when evaluated at the true `\(\theta\)`.

$$
E \left[ \frac{\partial}{\partial \theta} \log f(X; \theta) \bigg\rvert \theta \right] \\
= \int_\mathbb{R} \frac{\frac{\partial}{\partial \theta} f(x; \theta)}{f(x;\theta)}
f(x;\theta) dx \\
= \frac{\partial}{\partial \theta} \int_{\mathbb{R}} f(x;\theta) dx \\
= \frac{\partial}{\partial \theta} 1 \\
= 0.
$$

## Fisher’s Information

Fisher’s information is a way to measure how much information is contained in a known random variable `\(X\)` about the unknown population parameter `\(\theta\)` that is supposed to model `\(X\)`. It is calculated as the variance of the score.[^2]

Imagine you want to estimate how good an estimate is given all our knowledge about it. Fisher’s information describes the probability `\(f(x)\)`, given a known value of `\(\theta\)`. If `\(f(x)\)` is sharply peaked at a value of `\(X\)`, it indicates we have a good estimate of the true `\(X\)`. If `\(f(x)\)` is more evenly spread, we know little about the true value. Consequently we would need many more samples to accurately know what the value should be. Theoretically, we would need to know the entire population.

This intuitive understanding tells us that there would be some way to know how much information we have or how much information we need. Thus, there has to be a measure of variance with respect to `\(\theta\)`.

Therefore, Fisher’s information is defined as the variance of the score, `\(s(\theta)\)`.

$$
I(\theta) = E \left[ \left(\frac{\partial}{\partial \theta} \log f(X; \theta \right)^2 \bigg\rvert \theta\right].
$$

For a continuous PDF, this can be evaluated as the following.

$$
I(\theta) = \int_\mathbb{R} \left( \frac{\partial}{\partial \theta} \log f(x;\theta) \right)^2 f(x;\theta) dx.
$$

Since this is variance and has a square term, `\(I(\theta)\)` is always non-negative.

Sometimes, it is also denoted as the following.

$$
I(\theta) = -E \left[ \frac{\partial^2}{\partial \theta^2} \log f(X; \theta) \bigg\rvert \theta \right],
$$

as

$$
\frac{\partial^2}{\partial \theta^2} \log f(X; \theta) = \frac{\frac{\partial^2}{\partial \theta^2} f(X; \theta)}{f(X; \theta)} - \left( \frac{\frac{\partial}{\partial \theta} f(X; \theta)}{f(X; \theta)} \right)^2 \\
= \frac{\frac{\partial^2}{\partial \theta^2} f(X; \theta)}{f(X; \theta)} - \left( \frac{\partial}{\partial \theta} \log f(X; \theta) \right)^2.
$$

Also note that

$$
E \left[ \frac{\frac{\partial^2}{\partial \theta^2} f(X; \theta)}{f(X; \theta)} \bigg\rvert \theta \right] = \frac{\partial^2}{\partial \theta^2} \int_\mathbb{R} f(x; \theta) dx = 0,
$$

as proved earlier in Score. Putting this result in the last equation, we obtain the expected result.

## Cramer-Rao Bound

Cramer-Rao bound is a related concept. It states that the inverse of Fisher information is a lower bound on the variance of any unbiased estimator `\(\theta\)`. That is,

$$
V (\hat{\theta}) \geq \frac{1}{I(\theta)}.
$$

[^1]: To estimate the population parameter using maximum likelihood approach, we need to assume certain conditions about our probability density and likelihood functions. Continuity assumption is easily satisfied in real life but compactness isn’t as parameter space is often unbounded. Even when it is bounded, the bounds are usually unknown. For more details, see [this](https://en.wikipedia.org/wiki/Likelihood_function#Regularity_conditions).

[^2]: All that follows is a correct but strong simplification of the complex concepts. For more mathematical notions, check [Wikipedia](https://en.wikipedia.org/wiki/Fisher_information) and [Ly et al. (2017)](https://arxiv.org/pdf/1705.01064.pdf).
