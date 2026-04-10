---
title: Aspect Ratio (Merck Inc.)
subtitle: Where Data Science Met Freedom
summary: My experience of working as an analyst for Merck Inc. at Aspect Ratio, Pune
author: Harshvardhan
date: '2021-07-15'
tags:
- economics
- india
slug: aspect-ratio
---
[![](images/Screen%20Recording%202022-03-16%20at%2010.28.44%20AM.gif)](https://www.aspectratioai.com/)

At Aspect Ratio, I developed a pipeline for predictive modelling of Merck's HPV vaccine. I had to find the crucial variables in the analysis. There are many methods to find them: identify significant variables in simple [linear regression](https://en.wikipedia.org/wiki/Linear_regression) or use feature selection methods such as [Principal Components Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) and Fisher's [Linear Discriminant](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). The goal was to determine what factors drove vaccine coverage in US counties and states and where to promote it.

We didn't implement the project during my short tenure. The vaccine [GARDASIL 9](https://www.merckvaccines.com/gardasil9/) is now available for sale across the US.

During the time, I realised we made a lot of calls to the central insurance database of patients provided by Merck and other insurance companies. Most of them used SQL for this; however some were fans of [dbplyr](https://dbplyr.tidyverse.org/) and Python connectors. The database was massive, and each programmer wrote their functions to collect information. In the long term, it resulted in inconsistencies in code and thus results.

I created an R Shiny app to write standardised SQL codes to solve this. It took user inputs on what information was needed and presented SQL queries in text form that could be copied and pasted into their favourite SQL tool.

Aspect Ratio and Merck were terrific companies to work with. My manager, [Sneha Apte](https://www.linkedin.com/in/sneha-apte-86b17324/?originalSubdomain=in), was considerate of project timelines and a strong proponent of independence in work. I worked with R almost entirely (Merck is a [donor](https://www.r-project.org/foundation/donors.html) in the R-Project). Sneha and many others in our team worked with Python. However, that was never a problem. The team and our analysis were truly platform-agnostic.

We also had little exchange sessions on new cool tools and ideas every month. A team member who had created something unique, a tutorial about a topic in R or Python, or sometimes just discussions on making slides or presenting. Overall, a wonderful experience.
