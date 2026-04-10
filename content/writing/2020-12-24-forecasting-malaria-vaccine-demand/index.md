---
title: Forecasting Malaria Vaccine Demand
subtitle: Some interesting insights from my research work on forecasting demand of
  Malaria vaccines
summary: Summary of my research work on forecasting coverage for Malaria vaccines
author: Harshvardhan
date: '2020-12-24'
slug: []
tags:
- data-science
- government
- r
---
<script src="{{< blogdown/postref >}}index_files/twitter-widget/widgets.js"></script>

**For preprint of the actual paper, [click here](https://arxiv.org/pdf/2012.11124.pdf).**

Malaria is a mosquito-borne disease caused by a Plasmodium, a malarial parasite. Although Malaria is not life-threatening by its nature, it can cause severe illness and prove fatal if left untreated.

In February 2019, a new Malaria vaccine, RTS, S — known by the trade name Mos-Quirix — was approved for human trials in Ghana, Malawi and Kenya, coordinated by WHO. The study is expected to get over by December 2022. However, several pharmaceutical majors have begun showing interest in the vaccine’s mass production in the last few months.

The companies want to estimate the coverage ratio — defined as the vaccinated population count divided by the total population. This research aimed to forecast the same for all 78 affected countries using the Dynamic Gaussian Process Model.

## Model

A vaccine’s coverage in a country or geography depends on several factors: how effective is the vaccine? How many people are scared of not taking the vaccines? How many doses it has? Is the disease contagious?

Each country will have specific characteristics which are difficult to quantify. Therefore, the best approach is to select countries with “similar” features instead of only one model. We decided to work with the Human Development Index for grouping countries in this work.

<figure>
<img src="images/Screenshot%202021-06-17%20at%2010.44.52%20PM.png" alt="HDI heatmap of world" />
<figcaption aria-hidden="true">HDI heatmap of world</figcaption>
</figure>

### Variables in Modelling

Dependent variable (`Y`) was the time-series coverage ratio of Malaria vaccine for the next T years. `X1` to `X6` were independent variables.

- Y = time-series of coverage ratios for the next T years
- X1 = Dosage number. The value is k, if k doses of the vaccine have already been given. Multiple dosages result in lower coverage.
- X2 = Dosage time. The number of months after birth when the first dosage is taken; 0 represents ‘at birth’. Typically, vaccines given at birth have higher coverage as there’s no need to return to the hospital.
- X3 = Efficacy. The ability of the vaccine to actually prevent the disease. Higher efficacy creates stronger motivation for vaccination.
- X4 = Incidence per lakh. It is more likely that the parents will give their children the vaccine if the disease’s occurrence is high. When incidences are high, the population is more careful about prevention.
- X5 = Communicability. Fear of contagion drives vaccination.
- X6 = Years active. As time passes, coverage naturally grows.

## Implementation

The training data was too big to fit a full svdGP model on a standard laptop. We implemented the localized model (i.e., lasvdGP) developed by [Zhang et al. (2018)](https://rdrr.io/cran/DynamicGP/) for the model fitting. The localized model considers only observations that “closely resemble” itself for modelling instead of considering all points.

Of the ten countries in each group, not all are used for modelling. Instead, selected few for each variable and observation are used. This “closeness” is decided based on clustering within the country group.

We executed all the methods with [the DynamicGP](https://rdrr.io/cran/DynamicGP/) package in R.

## Results

From what was known, we considered that the first dose of vaccine (X1 = 0) was given to a six-month infant (X2 = 6). Malaria is known to be non-communicable (X5 = 0). We assumed the average incidence value as 60% (X4 = 60) and the vaccine’s efficacy at 70% (X3 = 70).

We forcasted the coverage for the next 38 years using these assumptions and inputs. The choice of 38 years was arbitrary; the simulation could handle more periods—however, the more extended the time considered, the lesser the measure’s reliability.

Here is the vaccine coverage at two crucial time points: soon after the launch and at the end of the simulation (38 years after launch).

<figure>
<img src="images/Screenshot%202021-06-17%20at%2011.04.25%20PM.png" alt="Vaccine coverage at t=0 and t=38" />
<figcaption aria-hidden="true">Vaccine coverage at t=0 and t=38</figcaption>
</figure>

Vaccine coverage through the years is as follows:

<figure>
<img src="images/Screenshot%202021-06-17%20at%2011.22.23%20PM.png" alt="vaccine coverage ratio over the years" />
<figcaption aria-hidden="true">vaccine coverage ratio over the years</figcaption>
</figure>

## What’s Even More Interesting

As evident from the figure, some countries start with higher coverage ratios and lead thirty years down the line. Some groups, like group 8, remain low for the entire duration. Group 9 and 10 catch up quickly with groups 1 and 2.

Countries that score low on HDI get all the attention, NGOs and ilk. They receive higher external funding and support.

Countries that score high on HDI have established infrastructure and facilities to roll out the programs quickly. The countries in groups three to eight are less better off, with eight being the worst.

There are also trends in seasonality. The coverage ratios show spikes at the end of every decade from the launch year. This could be due to ‘anniversary’ coverage news and attention. Also, the agencies responsible for vaccinating might be pushing themselves to complete their 10-year targets.

**However, a more in-depth study is necessary to make any definitive conclusions.**

<blockquote class="twitter-tweet" data-width="550" data-lang="en" data-dnt="true" data-theme="light"><p lang="hi" dir="ltr">हर साल मलेरिया लाखों जानें लेता है। मलेरिया की वैक्सीन अभी तीन देशों में फील्ड ट्रायल पर है। हमारा मॉडल कहता है की वो दिन अब दूर नहीं जब हम मलेरिया को टाटा - बाय बाय बोलेंगे!<a href="https://twitter.com/rpbreakingnews?ref_src=twsrc%5Etfw">@rpbreakingnews</a> में प्रोफेसर प्रीतम रंजन और मेरे रिसर्च का बयां। <a href="https://twitter.com/IIM_I?ref_src=twsrc%5Etfw">@IIM_I</a> <a href="https://t.co/7m7sKDFUJj">pic.twitter.com/7m7sKDFUJj</a></p>&mdash; Harshvardhan (@harshbutjust) <a href="https://twitter.com/harshbutjust/status/1567357305787744256?ref_src=twsrc%5Etfw">September 7, 2022</a></blockquote>

![](images/WhatsApp%20Image%202022-09-06%20at%2010.41.08%20PM.jpeg)
