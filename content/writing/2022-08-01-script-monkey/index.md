---
title: Script monkey! 🐒
subtitle: Recently, I learnt a neat trick during my internship at HP.
summary: Use a Script Monkey in your codebase at all locations where you need to change
  things manually. All that involves is writing an extra comment saying 'Script Monkey'.
  Later on, search for all monkeys in the script and make the changes. Simple.
author: Harshvardhan
date: '2022-08-01'
slug: script-monkey
tags:
- python
- r
- tools
---
Recently, I learned a neat trick during my internship at HP.

Sometimes you only need a few changes in the existing script before rerunning it all. For example, while working on a periodically executed project, we needed to run the same set of Jupiter notebooks every month. The code didn't change, barring a few parameters.

Usually, I recommend keeping the parameters at the beginning, so you notice what you need to change readily. But sometimes, you cannot avoid changes midway through the script.

How do you identify all the changes you need manually before hitting "restart kernel and run all" (in Jupyter Notebooks) or "Source" (in RStudio)?

# Hi Monkey 🐵

Use a Script Monkey in your codebase at all locations where you need to change things manually. All that involves is writing an additional comment saying "Script Monkey". Later, search for all monkeys in the script and make the changes. Simple.


```python
# Script monkey: Add current month and lag
df = pd.DataFrame(month = ['2022-02', '2022-03', '2022-03'], 
                  lag = [1, 2, 3])
```

Adding a small comment with #Script Monkey will save you hours looking through the codes. Just Cmd + F (⌘ + F in Mac or Ctrl + F in Windows) for "monkey", and you will know what to keep track of!

# Beyond Scripts

Scripts are only the beginning. Later on, you might need to modify more things. In that case, use Data Monkey, Tuning Monkey, Timing Monkey -- and more!

## Data Monkey 🐵

In data analytics or machine learning projects, data modifications are inevitable as new data streams in or data structures evolve.


```python
# Data monkey: Update data source
data = pd.read_csv('new_data_source.csv')

# Data monkey: Add new features
data['new_feature'] = data['existing_feature1'] * data['existing_feature2']
```

Utilize "Data Monkey" comments to mark places where data sources or features may need updates. A quick search for "Data Monkey" will guide you to all data-related modifications at once.

## Tuning Monkey 🐵

Parameter tuning is crucial for optimizing model performance.


```python
# Tuning monkey: Update hyperparameters
model = RandomForestClassifier(n_estimators=100, max_depth=5)
```

By marking parameter tuning sections with "Tuning Monkey," you can swiftly locate and adjust model parameters, streamlining the tuning process.

## Timing Monkey 🐵

Project timelines often shift, impacting deadlines and schedules.


```r
# Timing monkey: Update project month
project_month = '2023-11-01'
```

Employ "Timing Monkey" comments to highlight date or time-sensitive code segments, aiding in keeping project timelines accurate and up-to-date.

Each Monkey variant simplifies managing different project elements, helping maintain a clean, organized, and efficient workflow.

[Monkey will find its way to you.](https://www.instagram.com/reel/CO8WNMDnjLnKt9Pscy4_74xykrDqwZXAtrG2zw0/)[^1]

[^1]: Featured image credit: <a href='https://www.freepik.com/vectors/cute-monkey'>Cute monkey vector created by catalyststuff - www.freepik.com</a>
