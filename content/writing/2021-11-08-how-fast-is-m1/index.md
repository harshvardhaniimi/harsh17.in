---
title: How fast is M1?
subtitle: Comparing Apple M1 processor with Other Systems in R
summary: Comparing Apple M1 processor with Other Systems in R
author: Harshvardhan
date: '2021-11-08'
slug: how-fast-is-m1
tags:
- r
draft: false
---
I upgraded my laptop to MacBook Air (2020) with the infamous M1 processor a few days ago. I went after the most powerful machine in the category, one with 16 gigabytes of RAM and one terabyte of storage --- I didn't want to regret my choices anytime soon. M1 has been [praised](https://www.tomsguide.com/news/intel-alder-lake-chips-beat-apple-m1-max-for-speed-but-thats-only-half-the-story) for its [performance](https://www.cpubenchmark.net/cpu.php?cpu=Apple+M1+8+Core+3200+MHz&id=4104) time and again by multiple different agencies. M1 Macs are probably the only products that Apple has promoted less than it should.

> M1 is *smooth*.
>
> -   Sreyan Chaterjee, my friend who recommended me to upgrade

Since I got my new machine principally for helping me with computations, I wanted to test how good it was with R compared to other devices.

Someone on [Reddit](https://www.reddit.com/r/rstats/comments/k9z0xn/comment/gf8oyoq/?utm_source=share&utm_medium=web2x&context=3) had tried this with an old version of R built on Rosetta, but now that the [native M1 version](https://mac.r-project.org) was out, I wanted to get my hands dirty and test it. RStudio doesn't yet have a native app for M1 ([yet](https://community.rstudio.com/t/rstudio-on-macbook-air-m1/113848)), but the [v1.4](https://blog.rstudio.com/2021/06/09/rstudio-v1-4-update-whats-new/) allows to take full benefits of M1's processing power as the components interacting with R are built natively.

I wrote a small script performing singular value decomposition of a matrix, reconstructing it and noted the time it took for various machines. This experiment isn't scientific by any means, but I hoped I could get my answers.

``` r
library(lhs)

e = numeric()

n = 500
k = 30
nsim = 500

t1 = Sys.time()
for (i in 1:nsim)
{
  set.seed(i)
  x = maximinLHS(n,k)
  s = svd(x)
  x.new = s$u %*% diag(s$d) %*% t(s$v)
  e[i] = sum((x - x.new)^2)
}

t2 = Sys.time()
tt = t2 - t1

plot(e)
abline(h = mean(e), col = "red")

cat("Total time: ", tt)
cat("\nMean error: ", mean(e))
```

The code is pretty straightforward. I construct 500 matrices of size 500x30. Each of them is randomly designed using Latin Hypercube Samples. Then, I decompose them using the singular value decomposition method and then reconstruct it likewise. Finally, I create a plot of error and time taken. The plot of errors look the same on all machines due to the use of same seed.

![Errors in matrix decomposition and reconstruction via singular value decomposition.](https://www.harsh17.in/how-fast-is-m1/images/Rplot01.png "Errors in Matrix Reconstruction")

### Testing on MacBook Air (2020)

This machine had 1 TB of SSD storage, 16 GB of RAM and Apple M1 processor. It took **5.6 minutes** to run the entire code block.

### Testing on MacBook Pro (2019) #1

This machine had 1 TB of SSD storage, 16 GB of RAM and 2.6 GHz 6-core Intel Core i7. It took **9.2 minutes** to run the entire code block.

### Testing on MacBook Pro (2019) #2

This machine had 1 TB of SSD storage , 16 GB of RAM and 2.3 GHz 8-core Intel Core i9. It took **9.7 minutes** to run the entire code block.

### Testing on Microsoft Surface Pro (5th Gen)

This machine had 512 GB of SSD storage, 16 GB of RAM and 1.9 GHz Intel Core i7. It took **12.4 minutes** to run the entire code block.

## Conclusion

It was amazing to see how better was M1. Because all had the same memory (16 GB), I could technically say I was controlling for it to check how much would run time vary just by the processor and operating system change.

Note that RStudio on M1 is still running with Rosetta and giving almost twice as good a performance. I am very excited about all I can do in the days to come.

### Holy moly 😂

[![Parody of Intel CEO Hitler reacts to Apple Silicon M1 launch by Zeeshan Ali Zeeshan Ali. Youtube.](https://www.harsh17.in/how-fast-is-m1/images/hitler.png "Intel CEO Hitler Reacts to Apple Silicon M1")](https://www.youtube.com/watch?v=7syCGv-0VwQ)
