---
title: Is the world population going to collapse?
subtitle: Is the sale of baby diapers 👶 increasing faster than adult diapers 🧓?
author: Harshvardhan
date: '2022-11-10'
slug: population-collapse
tags:
- data-science
---
<script src="{{< blogdown/postref >}}index_files/twitter-widget/widgets.js"></script>
<script src="{{< blogdown/postref >}}index_files/core-js/shim.min.js"></script>
<script src="{{< blogdown/postref >}}index_files/react/react.min.js"></script>
<script src="{{< blogdown/postref >}}index_files/react/react-dom.min.js"></script>
<script src="{{< blogdown/postref >}}index_files/reactwidget/react-tools.js"></script>
<script src="{{< blogdown/postref >}}index_files/htmlwidgets/htmlwidgets.js"></script>
<script src="{{< blogdown/postref >}}index_files/reactable-binding/reactable.js"></script>

![](images/Screenshot%202022-11-10%20at%208.32.15%20PM.png)

Population collapse is a theory that says if the growth rates continue to decline the way they are decreasing right now, we would reach population zero. It is a stage where the population neither grows, nor declines. That is, the number of births plus in-migrants equals the number of deaths plus out-migrants. While this may sound cheerful, you may not have considered the pitfalls yet. The smaller size of working adults would result in lower taxes and thus lower funds for welfare. The welfare that old and young desperately need.

While I had learnt about the concept of population collapse in my population studies class. Until YouTube showed me this video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_U2kR6TOQcY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>

One measure of population collapse, according to [@elonmusk](https://twitter.com/elonmusk) at least, is the ratio of baby diapers sale to adult diapers sale.[^1] [Japan](https://www.wikiwand.com/en/Aging_of_Japan) is leading all the way while [China](https://www.wikiwand.com/en/Aging_of_China) is closely following it.

Sometimes it also leads to [innovative products](https://www.marketplace.org/2016/08/29/japans-changing-culture/):

> The company, she said, took into consideration that Japanese seniors, already petite by American standards, tend to become even more so with age. The average height of a Japanese woman, notes Yamanaka, is 157 centimeters (5 feet, 1 and a half inches), “however, this senior citizen, 50s and 60s, the average height is 152 centimeters, (just under five feet), five centimeters shorter,” she said.

> “So we make products which is more suitable for them — this height. For example refrigerators and washing machines designed for them to easily take things out.”

> Because of their stature, products designed elsewhere can be inconvenient for a smaller Japanese population, requiring climbing or reaching to access wet clothes in a washing machine easily.

> “In Japan, most people have backache,” Yamanaka said.

> In rural areas, many Japanese live in houses with two stories. And stairs. “And these people will clean up their house, stairs, holding up vacuum cleaners. And for them, the average weight, four kilo, was very heavy.” Almost nine pounds. So Panasonic created a lighter vacuum.

<blockquote class="twitter-tweet" data-width="550" data-lang="en" data-dnt="true" data-theme="light"><p lang="en" dir="ltr">even their fashion shows have adult diaper collections now. a collection of 170 adult diapers and smaller pads <br> was launched in Japan. Men and women walked, striking a pose to the tunes of 1980s British and American pop and rock music. <a href="https://t.co/6f5c35Q823">pic.twitter.com/6f5c35Q823</a></p>&mdash; Harshvardhan (@harshbutjust) <a href="https://twitter.com/harshbutjust/status/1589866512890093568?ref_src=twsrc%5Etfw">November 8, 2022</a></blockquote>

A few days ago, I was discussing this topic with a friend. She was concerned that her maid in New Delhi had too many children, beyond what she could support. Over population, especially if with the economically weaker section of population, can get pretty severe. However, I think this is a short-term view. I would prefer a [long-term view](https://www.wikiwand.com/en/Longtermism). If the population growth rate keeps decreasing at its current pace, we can have problems.

If you are curious about population declines, I can recommend you some good starting points.

- [Population decline, Wikipedia](https://www.wikiwand.com/en/Population_decline)

- [Zero population growth, Wikipedia](https://www.wikiwand.com/en/Zero_population_growth)

- Coleman, David, and Robert Rowthorn. “[Who’s afraid of population decline? A critical examination of its consequences.](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1728-4457.2011.00385.x)” *Population and Development Review,* 37 (2011): 217-248.

- [Ranked: The 20 Countries With the Fastest Declining Populations](https://www.visualcapitalist.com/ranked-the-20-countries-with-the-fastest-declining-populations/)

## Is the sale of baby diapers 👶 increasing faster than adult diapers 🧓?

When I decided to look at the data for this, I found mixed results. The ratio of adult diapers to baby diapers sold varies a lot between the countries.

For countries with rapidly ageing population like Japan, it is almost approaching 0.6, while for young countries like India and Bangladesh, it is much smaller. See the table below for the sales and ratio calculated for the year 2021.

<div id="htmlwidget-1" class="reactable html-widget" style="width:auto;height:auto;"></div>
<script type="application/json" data-for="htmlwidget-1">{"x":{"tag":{"name":"Reactable","attribs":{"data":{"country":["Australia","Bangladesh","Brazil","China","India","Norway","Israel","Russia","USA","Japan"],"baby":[370.3,493.9,1010,8900,5540,83.99,109.1,830,7170,1300],"adult":[211.6,116.5,160,730,1430,43.95,62.95,228.6,3560,830],"ratio":[0.57,0.24,0.16,0.08,0.26,0.52,0.58,0.28,0.5,0.64]},"columns":[{"accessor":"country","name":"Country","type":"character"},{"accessor":"baby","name":"Baby Diapers","type":"numeric","format":{"cell":{"prefix":"$","digits":0,"separators":true},"aggregated":{"prefix":"$","digits":0,"separators":true}}},{"accessor":"adult","name":"Adult Diapers","type":"numeric","format":{"cell":{"prefix":"$","digits":0,"separators":true},"aggregated":{"prefix":"$","digits":0,"separators":true}}},{"accessor":"ratio","name":"Ratio of Sales","type":"numeric"}],"defaultSortDesc":true,"defaultSorted":[{"id":"ratio","desc":true}],"defaultPageSize":10,"paginationType":"numbers","showPageInfo":true,"minRows":1,"dataKey":"dcb4ee0ed267a71e6e4b89357bd27f5c"},"children":[]},"class":"reactR_markup"},"evals":[],"jsHooks":[]}</script>

There is a confounding effect of accessibility as well. Adult diapers are not readily available in developing countries very easily. Even though they are available, people may not like wearing them because it makes them feel infantile. This stigma associated with diapers — diapers are for kids not adults — would be playing a role of their low sales in young countries, which generally also happen to be developing countries.

With this caveat in mind, let us get down to exploring these numbers as a time-series. The orange bars represent sale of baby diapers in millions of USD, while the purple bars represent sale of incontinence or adult diapers.[^2]

### Japan 🇯🇵

> The glaring example is Japan, a country ageing really fast. The sale of baby diapers is growing at 10.2%, while adult diapers are growing at 8.1% — quite close.

![](images/japan.png)

### United States of America 🇺🇸

> Both are growing, but it is clear that adult diapers is growing faster. USA’s absolute sales volume is much higher for a country of 331 million.

![](images/usa.png)

### India 🇮🇳

> India is one of the youngest countries right now. The baby diapers sale is increasing fast but adult diapers? Not so much.

![](images/india.png)

### China

> I cannot understand China’s data well. Period.

![](images/china.png)

### Russia

> I’ve no clue if sales are increasing or decreasing 🤷

![](images/russia.png)

### Data

All data is sourced from [Statista](https://www-statista-com.utk.idm.oclc.org/outlook/cmo/tissue-hygiene-paper/united-states#revenue). Thanks to the University of Tennessee, I have free access to Statista. Libraries are the best! If you need the data for all years between 2014 to 2027, let me know.

------------------------------------------------------------------------

The code to generate the plots can be found [here](https://gist.github.com/harshvardhaniimi/2d47c68f1d2e06778c3a1094b1a0acc7).

[^1]: Incontinence, if you’re being pedantic.

[^2]: Funny story: my first research project in PhD was with a company that manufactured incontinence diapers. If I had learnt about this before, I would have asked them their perspective.
