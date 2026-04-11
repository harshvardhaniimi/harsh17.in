---
title: The best stats you've ever seen
subtitle: 'There''s a famous saying: All models are wrong but some are useful. How
  much of statistics is wrong and how much of it is useful? Some thoughts on Hans
  Rosling''s popular talk on global economic development and optimism.'
summary: 'There''s a famous saying: All models are wrong but some are useful. How
  much of statistics is wrong and how much of it is useful? Some thoughts on Hans
  Rosling''s popular talk on global economic development and optimism.'
author: Harshvardhan
date: '2022-07-03'
slug: the-best-stats-you-ve-ever-seen
tags:
- data-science
- economics
cover:
  image: og.png
  relative: true
  hidden: true
---
Last week, I received a note from a reader of my [newsletter](https://www.getrevue.co/profile/harshbutjust/issues/what-happened-in-the-last-two-months-next-issue-37-1235976):

> Dear Harshvardhan,
>
> I would like to say in advance that I enjoy your collection of R packages in your newsletter very much.
>
> Today, I saw that you featured the talk „The best stats you've ever seen" by Hans Rosling the second time in your newsletter, but I cannot say I share your enthusiasm about it. It could have been equally titled „How to lie with statistics", as it takes quite some effort to (mis)lead the audience in a particular direction.
>
> Take the „Income Mountains": By stacking different regions on top of each other the graph hides inequalities between groups. Even more important, regions are heterogeneous. Who would put Urugay, Chile or Costa Rica in the same group as Bolivia, Haiti or Guatemala?
>
> But it gets worse when looking at the underlying transformation: Using logarithmic scale hides the long tail of rich people and thus extreme differences in income. (It is worth pointing out that the Gapminder foundation is sponsored by Bill Gates these days.)
>
> And the raw data are unfit for the purpose either: PPP as used by the World Bank -- Roslings data source -- overstates the purchasing power of the poor vis-a-vis the rich. Calculations of PPP invariably make poor people's income look greater than it is.
>
> And all of this to convey the happy message that we do not live in a two-hump world anymore. Sadly, this is not the case and I believe putting the talk into context would have been appropriate for the newsletter. Something I actually urge you to do for the next issue.
>
> Read on: <https://www.jasonhickel.org/blog/2019/3/17/two-hump-world>
>
> Best,

They were referring to Hans Rosling's talk on how our pre-conceived notions of the world are not aligned with general reality shown by data.

<iframe width="560" height="315" src="https://www.youtube.com/embed/hVimVzgtD6w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>

</iframe>

Development and growth are tricky subjects.[^1] There are complicated and do not seem to have one single answer.

[^1]: Prof Abhijit Banerjee's [lecture](https://www.youtube.com/watch?v=K2LvCx8H0OU) on The Challenge of World Poverty might be a good starting point.

In this TED talk, Rosling presents how when he started teaching as a professor of international health at the Karolinska Institute, his biggest problem was not the student's ignorance but preconceived notions. He asked his students to choose one country from the pair with higher mortality rates.

![](images/Screen%20Shot%202022-07-03%20at%202.22.35%20PM.png)

The countries with the arrow actually have higher child mortality rate. But the bigger lesson is the students performed worse than a Chimpanzee (or a coin toss) and professors performed as good/bad as a Chimpanzee.

The graph that stood out most to me was how life expectancy had varied by GDP per capita over the years. Here's an updated version of the graph. **Hit play button.**

<iframe src="//www.gapminder.org/tools/?embedded=true#%24chart-type=bubbles&amp;url=v1" style="width: 100%; height: 500px; margin: 0 0 0 0; border: 1px solid grey;" allowfullscreen>

</iframe>

But what they had written to me was about Income Mountains.

# Mountain Peaks

![](images/Screen%20Shot%202022-07-03%20at%202.39.17%20PM.png)

Rosling's point was the incomes are converging to one "hump", something that my reader and Jason Hickel disputed. Here's how the graph looks in 2020.

<iframe src="//www.gapminder.org/tools/?embedded=true#%24chart-type=mountain&amp;url=v1" style="width: 100%; height: 500px; margin: 0 0 0 0; border: 1px solid grey;" allowfullscreen>

</iframe>

But everything aside, it was great to hear some criticism of Hans Rosling's work. I read his book Factfulness which interested me in telling stories with data. I hadn't heard/seen significant criticism of his work --- which is dangerous, especially in development economy works.[^2]

[^2]: Some people say development economics is all that's left for novel economic work. No wonder many recent Nobel prize economists worked in the area of development economics.

# Stacking Regions

The stacked plots do hide the differences between the regions. Countries in the same group likely have very different economic indicators, which is one way to say the average is the average because it's the average. In the figure below, I expanded his chart to all countries.

<iframe src="//www.gapminder.org/tools/?embedded=true#$model$markers$mountain$data$filter$dimensions$geo$un_state:true;;;;&amp;encoding$selected$data$filter$markers@=ury&amp;=gtm;;;;&amp;facet_row$data$constant=none;;;;;;&amp;chart-type=mountain&amp;url=v1" style="width: 100%; height: 500px; margin: 0 0 0 0; border: 1px solid grey;" allowfullscreen>

</iframe>

One obvious peril is that smaller countries like Uruguay are now almost hidden. However, the trend still looks the same. Both Uruguay's hump and the global hump are very much aligned. Furthermore, all six countries mentioned in their email have a pretty similar distribution.

# Logarithmic Scales

Logarithmic scales are hideous. They correspond larger differences to smaller differences, making it easy to read but not easy to interpret. However, one good thing about log scales is that they supply growth numbers; they're on [relative](https://stats.stackexchange.com/questions/18844/when-and-why-should-you-take-the-log-of-a-distribution-of-numbers) changes rather than absolute change. Hans Rosling acknowledges it in the talk saying, "our concept of economy is to look at growth with percentage".

I've been fiddling with the idea in my head of what happens if countries stop growing, and I've not settled on an answer yet. It was great to see Jason Hickel (whose blog they shared) had a book on it: *Less is More: How Degrowth Will Save the World* and I will check it out.

# Purchasing Power Parity

PPP is a wrong but valuable metric. Before starting my PhD, I worked for a few months in India. According to tax returns, my pay would've put me in 0.1% of India. During my PhD, I'm graciously supported with a scholarship. Just the scholarship amount, when converted to Indian rupees using the current exchange rate of ₹78:\$1, would put me in 0.001% of India. And I'm making below US minimum wage on the scholarship.

![](images/Screen%20Shot%202022-07-03%20at%203.56.06%20PM.png)

PPP exchange rates are not the complete picture. But they are a compromise between foreign exchange rates and no exchange rate. People argue for RER, REER, NEER, PER and many others, but each has its pros and cons.

Jason presents a graph with constant dollars. While eye-opening, I don't think that's very useful.

![](images/Screen%20Shot%202022-07-03%20at%203.22.50%20PM.png)

The blog talks about issues with making the baskets as well. That is well-founded. People consume different goods in different countries, and it's tough to come up with the same basket. Some economists suggested using [time](https://www.gapminder.org/dollar-street) as a metric: consumption in a day measured in local currency.[^3] That has its shortcomings.

[^3]: The dollar street has several other visualisations: on [alcohol](https://www.gapminder.org/dollar-street?topic=alcoholic-drinks), on [pets](https://www.gapminder.org/dollar-street?topic=pets), on [toothbrushes](https://www.gapminder.org/dollar-street?topic=toothbrushes) and even [toys](https://www.gapminder.org/dollar-street?topic=toys).

The broader picture from Rosling's talk is about bringing forward the optimistic view of the world. His central argument is that economic conditions in developing countries are not as bad as they used to be. Does that mean we've reached our goal? Far from it. Bill and Melinda Gates Foundation is working on it in many cases, including by [supporting](https://www.gapminder.org/about/about-gapminder/supporters/) Gapminder.[^4]

[^4]: I don't agree Gapminder being supported by Gates Foundation is the same as being sponsored by Bill Gates. Isn't that akin to calling my \$10 donation to Wikipedia a sponsorship? Also, Gapminder has apparently [diversified](https://www.gapminder.org/about/about-gapminder/supporters/) its income sources to strengthen their economic independence. No single source of income is allowed to exceed 60% of the total annual income.

Living here in the US made me realise the importance of starting resources. An average kid in developed countries has more options than her counterpart in the developing world. This means there are more questions than answers, which is why development economics is a growing field these days.

Hopefully, we will make it so that everyone can be rich.[^5]

[^5]: If you're looking for a shortcut, there are none. Here are [some tips](https://twitter.com/naval/status/1002103360646823936?s=20&t=nj-qRNJ-9ReLDHarokx5xg) to get started on your long journey.

# Update: July 5, 2022

They responded back to my note and this blog post bringing forward another set of interesting points.

It is important to understand logarithmic transformations are not trivial. As they correctly identified --- which most readers would miss --- logarithmic scales in graphs grossly underestimate actual differences.[^6]

[^6]: They shared [this amazing website](https://mkorostoff.github.io/1-pixel-wealth/) which shows wealth in pixels. No log scales; just note the difference.

~~For example, the difference between \$1 and \$10 in this graph actually means a difference of \$3 and \$22,026. Why use logarithmic scales at all? Because incomes vary widely and log-transform brings some order. Furthermore, growth is more easily captured with log numbers. But difference of \$22,023 is much more than \$9, right?~~[^7]

[^7]: This description is wrong/incomplete. Here's how Gapminder makes income mountains: <https://www.gapminder.org/data/documentation/income-mountains-dataset/>.

> One could also ask whether relative change is actually what is of interest. It is often deemed appropriate with a reference to "diminishing returns": the logarithmic scale incorporates peoples perception about the worth of additional income, giving 1 dollar to a person with 1\$/day income is much more significant than giving to a 10\$/day person. But to quote [Jason Hickel](https://www.jasonhickel.org/blog/2019/5/15/how-not-to-measure-inequality): "Ultimately, there is a difference in perspectives at stake here. Additional dollars going to the rich are, from the perspective of the rich, diminishing in terms of marginal utility. But from the perspective of the poor they represent increasing egregiousness. To rely solely on the theory of diminishing marginal utility in discussing inequality, then, is to adopt the perspective of the rich and dress it up as neutral and objective."

If you have a hundred dollar and I give you a hundred more, you'd be ecstatic. If you have a million and I give you a hundred more, you'd be meh...

To hammer the point home, here's what they say:

> When transforming and ultimately visualizing data, we are driven by questions, make omissions, simplifications and assumptions. It is not proper to omit them afterwards as more often than not we communicate "facts" through our very own lens.

------------------------------------------------------------------------

Thanks for reading my blogpost. Thanks to the wonderful readers who take time to write back with such fervor. Such interactions motivate me to continue writing.

*Next --- Today I Learnt About R* is a free weekly newsletter on R related stories. I present five stories, four packages, three jargon, two tweets and one meme related to Data Science and R. Click [here](https://www.getrevue.co/profile/harshbutjust) to subscribe or read past editions.
