---
title: Print Demand Forecasting with Machine Learning at HP Inc.
author: Harshvardhan
date: '2025-06-04'
slug: print-demand-forecasting-with-machine-learning-at-hp-inc
summary: HP Inc. replaced manual and statistical forecasting with a machine learning
  (LightGBM) model to improve demand prediction accuracy across 18,000+ print products.
  The model has been deployed enterprise-wide, with demonstrated business value and
  principles for scaling ML in large organizations. [🔗 PDF](https://www.harsh17.in/docs/papers/HP_Paper_IJAA_Preprint.pdf)
tags:
- academia
- economics
- forecasting
cover:
  image: og.png
  hidden: true
---
My three-year-long collaboration with HP Inc.—including an 18-month internship with their Strategic Planning and Modeling team—has culminated in a new publication in the *INFORMS Journal of Applied Analytics*.
This paper is also the primary research output from [my dissertation](https://blog.harsh17.in/phd/), co-authored with the HP team and my advisor, Dr. Charles Liu.
I’m especially grateful to Cara Curtland at HP, whose partnership was instrumental in executing this work.

## Abstract

HP Inc. manufactures and sells more than 18,000 print-related products in over 170 countries.
Accurate forecasting of the heterogeneous and dynamic demand is vital to support supply planning decisions for manufacturing, inventory management, shipment scheduling, and ultimately, customer satisfaction.
Forecasting higher or lower than actual demand results in excess or shortage that reduces profitability and impacts on-time delivery to customers.

Historically, the supply planning depended on (1) consensus demand forecasting approach, which requires manual collection and integration of information by the forecasting experts, and (2) statistical time-series forecasting models.
The consensus forecasting approach also requires frequent corrections if some uncertainties in the demand are not accounted for when releasing the forecasting results.
Traditional time-series models can work automatically without frequent correction, but their forecasting performance is unsatisfactory because of oversimplified modeling inputs and assumptions.

In this project, we document the process of using machine learning (ML) techniques across all print products at HP Inc., worldwide.
Our aim is to automate the forecasting process with high accuracy and to integrate those results into a human-in-the-loop process that merges the strengths of ML, statistical, and consensus forecasting.
Our tree-based (LightGBM) forecasting model reduced systematic errors in comparison with existing approaches, such as the consensus and statistical forecasting approaches, and was deployed as an integrated part of HP Inc.’s forecasting process.

Furthermore, our ML framework establishes strong foundation for further methodological improvements in the ML algorithm.
We report extensive empirical evidence guiding our methodology design and demonstrating the business implications of our project.
We also share several important principles we have applied to manage team-based collaboration for an enterprise-scale project and to ensure the success of our ML-based demand forecasting.

## Links

DOI: <https://doi.org/10.1287/inte.2024.0126>

PDF: [Finally-accepted Preprint](https://www.harsh17.in/docs/papers/HP_Paper_IJAA_Preprint.pdf)
