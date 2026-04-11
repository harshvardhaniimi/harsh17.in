---
title: 50 Statistics Terms Indeed Got Wrong
subtitle: Was this article written by a noob?
summary: Was this article written by a noob?
author: Harshvardhan
date: '2022-04-10'
slug: 50-statistics-terms-indeed-got-wrong
tags:
- data-science
draft: true
cover:
  image: og.png
  relative: true
  hidden: true
---
> **50 Statistics Terms To Know (With Definitions)**
>
> Indeed Editorial Team, July 8 2021
>
> Link: <https://www.indeed.com/career-advice/career-development/list-of-statistics-terms>

Many people get statistics wrong these days. Sometimes even [senior data scientists](https://twitter.com/tunguz/status/1501574682520080390?s=20&t=gIgoYH1CYElCc4a8771Xyg), which is just sad. Sometimes, they I wonder [if they know what they're talking about](https://twitter.com/tunguz/status/1501903467475914754?s=20&t=gIgoYH1CYElCc4a8771Xyg).

I get it; it's not easy. But at least Google it. Or even ask --- statisticians love to correct wrong assumptions. Make some effort to learn.

Today, I will present the first few definitions and explain why they are misleading. Here's the [archive version](https://archive.ph/Tn2BF) in case the original link doesn't work.

> # **1. Alternative hypothesis**
>
> An alternative hypothesis is also known as the null hypothesis. The null hypothesis is the opposite claim of the thesis. If the data you collect demonstrates that your original hypothesis was correct, then you can reject the alternative hypothesis.

Alternative hypothesis is NOT null hypothesis. Null hypothesis is a representation of the *status quo* of beliefs. Mathematically, it denotes that two possibilities are the same. Usually, it is the thesis. Alternative hypothesis is... *drumrolls...* the opposite of null hypothesis.

> # **2. Analysis of covariance**
>
> An analysis of covariance refers to a technique that evaluates if a dependent variable produces equal results across numerous independent variable situations. It specifically looks at the differences between the mean values of dependent variables that relate to each other.

This definition is partly true. Analysis of covariance (ANCOVA) measures the impact of independent categorical variables (like sex) on dependent variable (like income) while controlling for other continuous variables that might have an impact (like intellectual abilities). It breaks down the variance of dependent variable ($y_{ij}$) into variance explained by covariates (continuous variables, `\(x_{ij}\)`) and categorical variable's variance ($\tau_i$).

$$
y_{ij} = \mu + \tau_i + A(x_{ij} - \bar{x}) + e_{ij},
$$

where `\(\mu\)` is the "grand mean", `\(A\)` is the slope of the regression line and `\(e_{ij}\)` is the residual variance.

> # **3. Analysis of variance**
>
> An analysis of variance is a method of evaluating the differences between variables in a study. It also includes a two-way study, which is a way to split variability into two parts, including systematic and random factors.

I do not understand this definition well enough to say whether it is right or wrong. Can ANOVA tell me difference between two variables? Yes. But so can t-test, F-test or any mean difference test. What does two-way study mean?

ANOVA is a generalization of t-test beyond two variables. It is used to compare means between two or more variables, testing if they are equal. It does that by comparing the variances between the groups.

> # **4. Average**
>
> The average refers to the mean of data. You can calculate the average by adding up the total of the data and dividing it by the number of data points.

This is correct. The technically correct term for this is arithmetic average. There are other kinds of means such as geometric mean and harmonic mean.

> # **5. Bell curve**
>
> The bell curve, which is also referred to as the normal distribution, displays the mean, median and mode of the data you collect. It usually follows the shape of a bell with a slope on each side.

Although bell curve typically refers to the normal distribution, it is not the only bell curve. Almost all unimodal symmetric distributions would be bell curve. Most distributions will have mean, median and mode as well. All curves will have a slope at all points where the differential exists. In common parlance, bell curve is the normal distribution. No less and certainly no more.

> # **6. Beta level**
>
> A beta level refers to the probability of accepting the null or alternative hypothesis. The beta level also means that the hypothesis is incorrect.

This. Is. Just. Wrong. Statistical power of hypothesis test is the probability that we correctly reject the null hypothesis when the alternative hypothesis is true. It is often represented as `\(1 - \beta\)` where `\(\beta\)` is the probability of making Type-II error.

|                                          | Reject Null Hypothesis ($H_0$) | Fail to Reject Null ($H_0$) |
|--------------------------|------------------------|----------------------|
| **Null hypothesis (**$H_0$**) is true**  | Type - I Error, `\(\alpha\)`       | Good call                   |
| **Null hypothesis (**$H_0$**) is false** | Good call                      | Type - II Error, `\(\beta\)`    |

> # **7. Binomial test**
>
> You can use a binomial test when you are studying a hypothesis with two potential outcomes and you believe one has a higher probability of being true. Its theory is based on probability calculations and the study of small samples.

This is largely correct. It is not based on study of small samples, rather it is valid for small samples.

> # **8. Breakdown point**
>
> The breakdown point is a point in which an estimator is no longer useful. A lower breakdown point means the information may not be useful, whereas a higher number means there is less chance of resistance.

Breakdown point is the proportion of arbitrary large observations that an estimator can handle before giving incorrect arbitrary large results. For example, the mean given by

$$
\bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n}
$$

can become arbitrary large (and thus incorrectly represent the distribution of `\(x_i\)`) by changing any of the `\(x_i\)`. Thus, breakdown point of `\(\bar{x}\)` is zero ($\lim_{n \to \infty} \frac{1}{n}$).

> # **9. Causation**
>
> Causation is a direct relationship between two variables. Two variables have a direct relationship if a change in one value causes a change in the other variable.

This is a really confusing way to say if I hit the accelerator and the car moves, it is the accelerator that moves the car.

> # **10. Coefficient**
>
> A coefficient measures a variable by using a multiplier. When conducting research and computing equations, the coefficient is often a numerical value that multiplies by a variable, giving you a coefficient of the variable. If a variable does not have a number, the coefficient is always one.

Let's say you have a algebraic expression like `\(ax + b\)`. `\(a\)` and `\(b\)` are coefficients; the constant terms in the expression. They're most common in regression in statistics.

> # **11. Confidence intervals**
>
> A confidence interval measures the level of uncertainty of a collection of data. It is also the level of probability that data will fall into a set of pre-assigned values.

Confidence intervals give us a probabilistic range (after accounting for uncertainty) of an unknown parameter. It does not measure uncertainty in data collection. If I say my 95% confidence interval is `\((I_1, I_2)\)` and I collect 100 samples of my data, 95 out of 100 times my parameter of interest would be between `\(I_1\)` and `\(I_2\)`.

> # **12. Correlation coefficient**
>
> The correlation coefficient describes the level of correlation or dependence between two variables. This value is a number between negative one and positive one and can suggest when two variables may have an identifiable relationship.

Correlation measures *linear* relationship between two variables. Many mistake it to represent dependency but [correlation doesn't imply causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation). Further, there could be quadratic relationship between variables that correlation simply misses out.

Consider `\(y = x^2\)`. As you can see in the figure below, the correlation is (almost) zero but there is clear quadratic relationship between `\(x\)` and `\(y\)`. Here's an interesting website with many examples of [spurious correlation](https://www.tylervigen.com/spurious-correlations) --- where is no relationship but correlation is significant.


```r
x = seq(-1, 1, length.out = 100)
y = x^2
cor(x, y)
```

```
## [1] 2.754455e-16
```

```r
plot(x, y, type = "l", xlab = "x", ylab = "y = x^2")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-1-1.png" width="672" />

> # **13. Cronbach's alpha coefficient**
>
> Cronbach's alpha coefficient is a measurement of internal consistency. It shows the nature of the relationship between multiple variables in a subset of data. Additionally, Cronbach's alpha coefficient remains consistent in the number of items it measures and can increase when the average correlation between items increases.

Honestly, I don't know much about this. From the [University of Virginia Libraries](https://data.library.virginia.edu/using-and-interpreting-cronbachs-alpha/):

> Cronbach's alpha is a measure used to assess the reliability, or internal consistency, of a set of scale or test items. In other words, the reliability of any given measurement refers to the extent to which it is a consistent measure of a concept, and Cronbach's alpha is one way of measuring the strength of that consistency.

> # **14. Dependent variable**
>
> A dependent variable is a value that depends on another variable to exhibit change. When computing in statistical analysis, you can use dependent variables to make conclusions about causes of events, changes and other translations in statistical research.

This is a good intuitive explanation of dependent variable. In the model `\(Y = f(X) + \epsilon\)`, `\(Y\)` is the dependent variable and `\(X\)` is the independent variable.

> # **15. Descriptive statistic**
>
> Descriptive statistics are the results that describe the data of your study. This may include the mean or median of the data as well as any other information that describes a trend among the population.

Descriptive statistics describe the data sample we have. Usually it includes summary statistics like mean, median, standard deviation, mode, skewness, kurtosis, range and many others. The give us the "feel" of what we're dealing with.

> # **16. Effect size**
>
> The effect size is a way to quantify significant differences between two populations or sets of data. Effect size considers the size of the population rather than focusing solely on the data you collect.

Effect size is **not** a way to quantify differences between two populations. Statistical tests are used for that purpose.

Assume that you ask 500 people in Tennessee, US about their opinions on free speech. Then you ask 10 people in Massachusetts, US about their opinions on free speech. You find that they agree --- but is it because you asked only 10 people in MA and 500 in TN? This is called the effect size of the sample size, which is kind of effect size. There are more than fifty types of effect size. See [Wikipedia](https://en.wikipedia.org/wiki/Effect_size#Types) for more details.

> # **17. F-test**
>
> An F-test is any test that uses F-distribution. F-distribution refers to the process of comparing different models of statistics to determine which model works best for the specific study.

F-test uses the F-distribution. Here's how F-distribution looks; it's just a probability distribution.
