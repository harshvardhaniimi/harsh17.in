---
title: Notes on STATA
subtitle: Some nitty-gritties that economists remember but I don't
summary: Some nitty-gritties that economists remember but I don't
author: Harshvardhan
date: '2022-02-16'
slug: notes-on-stata
tags:
- data-science
- economics
cover:
  image: og.png
  relative: true
  hidden: true
---
#### Conventions through this page

`x` is the name of the variable.

------------------------------------------------------------------------

### Set Working Directory

``` r
cd "/directory/"
```

### Use a Dataset

``` r
use data.dta, clear
```

### Clear all items from memory

``` r
clear all
```

See [documentation](https://www.stata.com/manuals13/dclear.pdf) for details.

### Display all items

``` r
list
```

### Display first element only (useful for a scalar)

``` r
di x
```

### Setting number of observations

``` r
qui set obs 30
```

`qui` says this command is executed quietly, i.e. with no output.

### Summary of a variable

``` r
summarize x
```

This will number of observations, mean, standard deviation, minimum and maximum.

### Describe

``` r
describe x
```

This will tell us the type of variable it is.

# Functions

Functions in Stata are called Programs. See [documentation](https://www.stata.com/manuals13/rsimulate.pdf).

Below is a sample program named `onesample` that generates 30 uniform random numbers and calculates their mean. We do need to specify `rclass` to specify the kind of return for the function. Other options is `eclass`.

`drop _all` is different from `drop all` ; the former drops all observations and the latter looks for a variable named `all` and deletes that.

``` r
program onesample, rclass
    drop _all
    qui set obs 30
    gen x = runiform()
    summ x
    return scalar mean = r(mean)
end
```

# Monte Carlo Simulation

If the function is defined as above, we can use the following codes to perform Monte Carlo simulation.

``` r
* Simulate it 10000 times
simulate xbar = r(mean), seed(0) reps(10000): onesample
```

# Visualisation

### Histogram

``` r
hist x, width(0.1) title("Histogram of x")
```

See [documentation](https://www.stata.com/manuals/rhistogram.pdf) for details.
