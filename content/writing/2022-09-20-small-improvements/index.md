---
title: How the government of Bihar is changing lives one girl at a time?
subtitle: Small Improvements
summary: Bihar is one of the poorest states in India. Their over all literacy rate
  is 70% but there's stark difference between girls (50%) and boys (70%). In 2007,
  the government decided to distribute bicycles to all girls for free in the hope
  to get higher school enrollment. The program was called Mukhyamantri Balika Cycle
  Yojna (Chief Minister's Programme on Cycle for Girls). The program had astonishing
  improvements.
author: Harshvardhan
date: '2022-09-20'
slug: bihar
tags:
- data-science
- economics
draft: false
cover:
  image: og.png
  hidden: true
---
In our econometrics class few months ago, [Prof Luiz](https://web.utk.edu/~llima/) showed us a video to demonstrate how difference-in-difference-in-difference works. To measure the impact of some policy (or *treatment* in economic-speak), we can compare the outcomes before and after the policy.

# Difference in Difference in Difference

Let's say McDonalds believes adding cheese to its Deluxe Chicken Sandwich[^1] would increase sales. One fine day --- April 1, 2022 --- they added cheese to their sandwich in their Knoxville store. In March 2022, they sold 10,000 units. Six months later, they measured sales again. They sold 15,000 units in October 2022. The analyst was ecstatic with the results.

[^1]: Its my go-to McD product, other than their Latte. Personally, I prefer McD's coffee over any other chain, especially Starbucks (in India). Recently, I started grinding my own coffee beans to make latte, and that's so much better than any coffee sold at Starbucks, McD or like.

However, the excitement was short. The Nashville manager turned up and said, we sold 12,000 sandwiches in March; we sold 15,000 in October. How can you say this increment of 5,000 sandwiches was because of that extra cheese? Were Nashville customers were *cheesing* anyway?

But come on, Knoxville's sales increased by 5,000 sandwiches. Nashville's sales increased by 3,000 sandwiches. Knoxville's sales increased by 2,000 more than Nashville! I have to attribute it to the extra cheese!

Assuming both the cities are similar in size, this has to be true. I know Nashville is much larger than Knoxville, but if they were similar, the effect of cheese is clear. This method of analysis is called difference in difference in difference --- a play on three differences we did just now.

# Gifting Bicycles to School Girls in Bihar

Bihar is one of the poorest states in India. Their over all literacy rate is 70% but there's stark difference between girls (50%) and boys (70%).[^2] In 2007, the government decided to distribute bicycles to all girls for free in the hope to get higher school enrollment.[^3] The program was called *Mukhyamantri Balika Cycle Yojna* (Chief Minister's Programme on Cycle for Girls).

[^2]: From [Wikipedia](https://en.wikipedia.org/wiki/Literacy_In_Bihar):

    Bihar has a total literacy rate of 69.83%. Overall Male and Female literacy rate is 70.32% and 53.57% respectively. Total Rural literacy rate is 43.9%. In rural areas of Bihar, Male and Female literacy rate is 57.1% and 29.6% respectively. Total Urban literacy rate is 71.9%. In urban areas of Bihar, Male and Female literacy rate is 79.9% and 62.6% respectively.

[^3]: There was also an option to get ₹2,000 cash to buy a bicycle. Some people preferred their own model over what the government offered.

The principal of a school surmised it perfectly:

> If the girl can ride a bicycle, she can come to school with little difficulty. She can help her family in everyday chores. She can take up economic opportunities. She can travel far for extra classes and private tuitions. Most importantly, she can dream herself as an empowered girl who can be an engineer, a doctor, anything.

Two professors: [Karthik Muralidharan](https://econweb.ucsd.edu/~kamurali/) (University of California, San Diego) and [Nishith Prakash](https://nishithprakash.com/) (University of Connecticut) were hired by the International Growth Center to study the economic impact. Their findings are best described in this video.[^4]

[^4]: It mildly offends me that the map in the picture shows Pakistan-occupied-Kashmir (PoK) is shown to be part of Pakistan and not India. With a deep breath, I will let it go.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6nG63ISt_Ek" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>

</iframe>

The researchers compared the enrollment before and after the free distribution of bicycles. The enrollment had gone up significantly!

![](images/Screen%20Shot%202022-04-29%20at%205.16.10%20PM.png)

Many could argue that the enrollment was rising anyway. There could be a myriad of reasons why the enrollment went up. There was higher economic growth, better schools, attitude change on education.

![](images/Screen%20Shot%202022-04-29%20at%205.17.24%20PM.png)

So, the researchers compared this growth with the growth in enrollment of boys. Almost all the reasons listed above would also be affecting boy's enrollment. That's where difference-in-difference comes in.

![](images/Screen%20Shot%202022-04-29%20at%205.21.00%20PM.png)

But this gross comparison also assumes that the growth rate for both girls and boys were going up at the same rate before and after. That's simply not true. Therefore, they compared the rise in enrollment with a neighbour state --- Jharkhand (my home state). Jharkhand and Bihar are very similar to each other culturally. In fact, Jharkhand was part of Bihar until 2000.

![](images/Screen%20Shot%202022-04-29%20at%205.23.41%20PM.png)

Using the difference in difference in difference approach, they found that the program was super effective. It increased the enrollment in Bihar by three times more than the enrollment in Jharkhand.

# Conclusion

This video explains two things: difference in difference approach of analysing systematic changes and the impact of having a *little more freedom* in our lives. Once the girls had the bicycles, they could travel to other places and help their parents in errands and jobs. They could go to the next city and open their bank accounts.

Atomic improvements lead to major changes.
