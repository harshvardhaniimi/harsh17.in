---
title: Let’s say you’re copying a folder to a folder
subtitle: What should the progress bar show? How to measure 10% work done?
summary: What should the progress bar show? How to measure 10% work done?
author: Harshvardhan
date: '2022-03-10'
slug: lets-say-you-re-copying-a-folder-to-a-folder
tags:
- data-science
- r
cover:
  image: og.png
  hidden: true
---
Imagine a folder A whose content is to be copied to a folder B. A has five subfolders, each with 1, 2, 3, 4 and 5 files, respectively. For simplicity, consider the case that each file is of equal size. When copying the files from A to B, how would you measure the progress?

Total number of files is 1 + 2 + 3 + 4 + 5 = 15. One way to measure progress is in the intervals of 1/15. The progress bar would evenly progress in multiples of 0.06.

Another way is to consider the folder and its files to be divided as 1, 1/2 x 2, 1/3 x 3, 1/4 x 4, 1/5 x 5. In that case, when the first folder is done, the progress would be 20%. Then it'll progress to 30%, 40%, 45%, 50%, 55%, 60%, and so on. The slowly decreasing rate of progress would be incredibly frustrating to watch. Most computer programs prefer the first version but the second alternative is possible.

This example might sound trivial and unreal, but it is incredible how often it turns up in real practical problems --- including cooking and supply chain statistics.

My roommate Tagg has a unique way of making ramen noodles. He would bring the water to boil, pour the ramen in, leave it for less than a minute and put many seasonings on top. My other roommate Jack pours most of the water out and then lets it sit with the seasoning to soak in the spices. Tommy and Jake boil it with the herb and dry every drop of water. They like raw ramen noodles.

Which one's better? I can't say definitely. (Although I like Tagg's method, [this NY Times recipe](https://cooking.nytimes.com/recipes/1016583-perfect-instant-ramen) is the best.)

# Devils in The Details

I am working on a research project with a hygiene products company based in North Carolina. It's facing returns, sometimes up to 15% of its sales. Prof Sean and I were trying to find why. We found opportunities to streamline distribution using their data for sales, transportation, and claims.

This problem of choosing the "how" to calculate the metric turned up in something I thought was super simple. The company gave sales, transportation and products datasets. See the following examples. Of course, they're not real, but they give you a good idea.

![](images/Screen%20Shot%202022-03-10%20at%203.39.36%20PM.png)

![](images/Screen%20Shot%202022-03-10%20at%203.40.30%20PM.png)

![](images/Screen%20Shot%202022-03-10%20at%203.41.01%20PM.png)

> These datasets have random values and aren't real. But they give you a taste of what the company provided us.

# Deciding on the metrics is way more complicated than I initially thought.

Consider you want to estimate how many complete pallet orders were shipped from a location. Where do you start? Well, each item was in a carton which was in a pallet. So maybe, that's a reasonable starting point.

We want to estimate the *proportion of orders from a location in full pallets*. There are at least two methods to find it.

First, I find the number of full pallets for every row since each row (in the Sales sheet) is an order-item combination. Group all the entries by an order number; then, you can find what proportion of cases were sent in full pallets. But that is for every order, and we wanted to get metrics by location. So, you can aggregate the results again by (City, State) and calculate the average proportion of total pallet cases.

Or, the other method is to group by (City, State) without first grouping by order number. This would disregard which items were part of which order --- breaking 1-to-1 matches. Some orders would be higher volume than others. There's no reason they should be the same unless all items were the same.

This situation of defining the right metric turns up in so many different ways. How we aggregate things together matters because the end product depends not only on raw materials but the method as well. Simple things aren't as intuitive as one might think. Ultimately, we have to use the metric that the company likes to use.

# **A general note on metrics**

-   If people have to perform calculations on your metrics to generate insights, they're not good metrics.

-   Specify what your metric represents *and* what it doesn't represent. You'll avoid situations where your metric is misused.

-   Always consider what the company or client thinks about your metrics and their businesses. If they disagree with your formulation, your metric will be just another number.

-   There is more variability than what a statistical model can capture. Listen to managers; they've more knowledge about their businesses than you'd ever have.

[![](https://imgs.xkcd.com/comics/standards.png)](https://xkcd.com/927/)
