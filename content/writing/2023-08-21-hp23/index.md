---
title: ML Forecasting at HP Inc.
summary: Creating ML demand forecast for print products at HP Inc. using LightGBM
  and pushing it to production for wide adoption.
subtitle: Creating ML demand forecast for print products at HP Inc. using LightGBM
  and pushing it to production for wide adoption.
author: Harshvardhan
date: '2023-08-21'
slug: hp23
tags:
- forecasting
- python
- tools
cover:
  image: og.png
  relative: true
  hidden: true
---
(This is a formal write-up of my internship work. Read [this blog](hp-blog-2023/) for a chirpy review of my internship!)

During my 15-month internship at HP Inc., I was actively engaged in implementing and optimizing machine learning forecasting models for over 18,000 products within HP Print. 

Working with the SPaM team in supply chain modeling and machine learning, my responsibilities ranged from:
- Enhancing existing processes and understanding the codebase in my [early days](/hp22/).
- Advancing to more complex tasks such as leveling up machine learning components, integrating them into production, and pioneering SKU-level forecasting within the organization.
- Engaging in ML improvements like encoding categorical variables and feature engineering, which significantly boosted the model's accuracy.
- Building an ETL pipeline to include channel partner inventory, sell-in, and sell-through volume, facilitating smoother data processing.

## Tools Used
My work involved a multitude of tools and frameworks, vital to the execution of tasks, including:
- **Python and Pandas**: Primary language for modeling with LightGBM.
- **SQL**: Used in pipelines for data extraction and loading.
- **Tableau**: Dashboard for sharing results widely with all planners and forecasters.
- **Terminal**: Employed for various command-line operations. Learnt about symbolic links in particular, in addition to use of grep, find, move and more.
* **LightGBM**: A tree-based model used for forecasting.
* **MLFlow**: To track all our experiments, proving indispensable in managing numerous trials.

## Impacts
My contributions led to notable impacts within the organization:
- The development of the first-ever SKU-level forecast with ML for Print at HP.
- Improved accuracy and efficiency of the forecasting model by introducing innovative changes.
- Created new pathways for new data by building an ETL pipeline, allowing for more effective demand forecasting.
- Successfully loaded the forecast into the Integrated Business Planning (IBP) tool, aiding planners across 18,000 SKUs and 45 geographies.
- I embraced the culture of innovation at HP, adhering to principles such as "Fail Fast" and actively participating in "Coding is Cool" sessions.

This experience has been an invaluable part of my professional growth, and I look forward to continuing my collaboration with the team while prioritizing my research in the coming year.
