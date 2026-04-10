---
title: Comparing two BIG data frames in Pandas
subtitle: I needed to compare two data frames with over five million rows. I asked
  ChatGPT for help. I ended up learning about SHA-256 and hashes.
summary: I needed to compare two data frames with over five million rows. I asked
  ChatGPT for help. I ended up learning about SHA-256 and hashes.
author: Harshvardhan
date: '2023-05-06'
slug: pandas-compare-df
tags:
- ai
- tools
---
Recently, I ran into a situation where I need to compare two huge `pandas` data frames. When `df` has five million rows and 100 columns, `all.equal` function is not a good option. I had to do something creative.

A straightforward solution was to break down the entire data frame into multiple smaller manageable chunks, and then do element-by-element comparison. With five million rows, this would take me around ten tries, depending on some other factors like runtime memory, etc. But, there must be a better method.

Beginning as a brainstorming activity, I decided to ask ChatGPT for ideas. Rest of this blog is our conversations. Keep reading to learn about "hash collisons", SHA-256 encryption that powers the internet of today.

If you're interested my thoughts and not this Python chat, jump to [How does ChatGPT work?].

#### how to compare if two data frames are same in pandas? tell me an efficient way as my file sizes are huge

Comparing two large DataFrames in pandas for equality can be computationally expensive. However, you can use a few techniques to make this comparison more efficient. Here's an approach that you can follow:

First, compare basic DataFrame properties like shape, columns, and dtypes. If they don't match, the DataFrames are not the same. If the basic properties match, perform a hash-based comparison for faster results. Here's a code snippet implementing this approach:

``` python
import pandas as pd
import hashlib

def hash_dataframe(df):
    return hashlib.sha256(pd.util.hash_pandas_object(df, index=True).values).hexdigest()

def are_dataframes_equal(df1, df2):
    # Check shape, columns, and dtypes
    if df1.shape != df2.shape or (df1.columns != df2.columns).any() or (df1.dtypes != df2.dtypes).any():
        return False

    # Compare hashes
    return hash_dataframe(df1) == hash_dataframe(df2)

# Load your DataFrames
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Check if DataFrames are the same
result = are_dataframes_equal(df1, df2)
print("DataFrames are equal:", result)
```

This approach first checks basic properties and then compares the hashes of the DataFrames, which is more efficient than element-wise comparison, especially for large DataFrames. Note that this method assumes your DataFrames have a deterministic order. If the row order is not guaranteed, you may want to sort the DataFrames by a unique index before hashing.

> This got me interested in hashing, so I asked.

### What is hashing?

Hashing is a process that takes an input (in our case, the DataFrame) and produces a fixed-length string (usually a sequence of numbers and letters), which is the output called the "hash" or "digest". A good hash function has the following properties:

1.  It is deterministic, meaning that the same input will always produce the same hash.
2.  It is fast to compute the hash for any given input.
3.  It is infeasible to regenerate the original input data from the hash, making it a one-way function.
4.  A small change to the input data should produce such a drastic change in the hash that the new hash appears uncorrelated to the old hash.
5.  It is unlikely that two different inputs will produce the same hash (called a collision).

In the context of comparing DataFrames, we use a hash function to create a unique representation of the entire DataFrame. By comparing the hashes of two DataFrames, we can quickly determine if they are the same or not. If the hashes are the same, it is very likely (though not 100% guaranteed) that the DataFrames are the same.

In the provided code snippet, we use the `hashlib.sha256()` hash function from the Python standard library, which implements the SHA-256 algorithm. This is a widely-used cryptographic hash function that produces a 256-bit (32-byte) hash.

The `pd.util.hash_pandas_object()` function from pandas is used to create a hashable representation of the DataFrame. It computes the hash for each row and returns a Series of hashes. We then hash this Series of hashes using SHA-256 to get a single hash that represents the entire DataFrame. This allows us to efficiently compare large DataFrames by just comparing their hashes.

> Although GPT doesn't say this explicitly, SHA-256 also powers most encryption algorithms today, including protecting apps we love: Whatsapp, Email, Financial Transactions, and my digital garden. Whenever you head "256-bit encryption", it's probably this. I had no clue data frames could be converted to hashes so easily.
>
> Also, "hash collison" sounds like a term straight from [The Hitchhiker's Guide to the Galaxy](https://www.goodreads.com/book/show/386162.The_Hitchhiker_s_Guide_to_the_Galaxy).[^1]

[^1]: As I was telling Greeshma, this book is the epitome of Sci-Fi. It was my first space adventure book and it delivers. If you haven't already, read it. And then [watch the movie](https://www.rottentomatoes.com/m/hitchhikers_guide_to_the_galaxy). Not the other way around.

#### What is the probability that the data frames are not the same if they have the same hash?

The probability of two different DataFrames having the same hash (a hash collision) is extremely low but not impossible. The probability depends on the hash function used and the size of its output (the number of bits in the hash). In the provided code snippet, we use the SHA-256 hash function, which produces a 256-bit (32-byte) hash.

For a well-designed hash function like SHA-256, the probability of a hash collision is roughly 1 in 2\^(number of bits in the hash). In this case, since there are 256 bits in the hash, the probability of a collision is about 1 in 2\^256, which is approximately 1.1579209 x 10\^(-77).

This probability is incredibly small, so small that it is practically negligible in most use cases. To put this into perspective, it is far less likely than winning the lottery multiple times in a row or being struck by lightning multiple times.

However, it's essential to understand that while the probability is extremely low, it's not zero. In applications where it is absolutely critical to detect every difference, you might want to perform an element-wise comparison as a final step after the hash comparison. But in most cases, hash comparison should be more than sufficient to determine if two DataFrames are the same.

#### Let's say I got false. How do I identify the difference between data frames?

If the comparison returns `False`, indicating that the DataFrames are not the same, you can use the `compare()` function in pandas to identify the differences between the two DataFrames. The `compare()` function is available in pandas version 1.1.0 and later.

Here's an example of how to use the compare() function:

``` python
import pandas as pd

# Load your DataFrames
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Compare DataFrames and find differences
df_diff = df1.compare(df2)

# Save the differences to a CSV file
df_diff.to_csv('differences.csv')

# Print the differences
print(df_diff)
```

The `compare()` function returns a new DataFrame showing the differences between the two input DataFrames. The output DataFrame will have a MultiIndex with two levels of columns. The first level corresponds to the original column names, and the second level contains two labels: "self" for the values in the first DataFrame (`df1`) and "other" for the values in the second DataFrame (`df2`).

If you want to display only the rows with differences, you can use the following code snippet:

``` python
rows_with_diff = df_diff.dropna(how='all').stack().reset_index()
rows_with_diff.columns = ['index', 'column', 'df1', 'df2']
print(rows_with_diff)
```

This will output a DataFrame with the index, column, and the different values for each DataFrame, making it easier to identify the differences.

------------------------------------------------------------------------

## How does ChatGPT work?

Last week, some of us researchers at the [University of Tennessee](https://www.harsh17.in/gpt/), wrote up an essay explaining the basics of GPT models. It is for people who are like, "what the heck is this thing and how is it so good?".

-   ChatGPT and similar LLMs are powerful AI generative models based on deep neural networks with multiple layers of transformer blocks, trained on diverse text sources and fine-tuned for specific tasks.
-   ChatGPT can conduct human-like conversations, solve problems, and provide information related to a user's question but may provide inaccurate information, misinterpret context, and perpetuate biases.
-   LLMs, like ChatGPT, have limitations as they are only as reliable and accurate as the data they have been trained on, and can produce irrelevant or misleading responses due to misinterpretation or hallucination.
-   Using ChatGPT at face value can hinder creativity, critical thinking, and problem-solving skills, and users should critically evaluate its output and consider its limitations.

Check it out and share your thoughts!

------------------------------------------------------------------------

### AI is developing fast. Light-speed fast.

GPT models have been making huge strides. In February 2023, Meta launched LLaMA, a relatively small but capable language model, which was soon leaked to the public. The following month saw rapid innovations and developments, including minification efforts, fine-tuning on a laptop, the release of Alpaca, and the creation of GPT4All. By the end of March, open-source GPT-3 models were available, and multimodal training could be achieved in one hour. The open-source language model ecosystem continued to expand and become more accessible for users.

In April, the Koala dialogue model was launched, and it was shown that real humans couldn't consistently tell the difference between it and ChatGPT. Why Berkeley's Koala is critical? It was only trained on public data sources, including some cleverly collected data sources. Some scourged through [Sharegpt.com](https://sharegpt.com/) to find only good responses, and use them in training dataset. This improvement in underlying data more than translated to actual responses.

Open Assistant then released a model and dataset for Alignment via RLHF, which made reinforcement learning from human feedback more accessible to smaller experimenters. As a [Google researcher wrote](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither), the landscape of language models evolved rapidly, with the community no longer dependent on LLaMA and open-source solutions becoming increasingly sophisticated and competitive.

When I started my [brain dump on AI](https://www.harsh17.in/ai/) about a year ago, I hadn't imagined things would accelerate this fast. Few months ago when I tried to (not) make [predictions about AI](https://www.harsh17.in/ai2/), I still hadn't imagined this trail. But I like where it's headed. Fast development usually means greater accessibility. In my mind, we should be far less concerned about "AI Takeoff" than unequal access to AI. The future is already here -- it's just not evenly distributed.[^2]

[^2]: [William Gibson riffs on writing and the future \| (ted.com)](https://ideas.ted.com/william-gibson-riffs-on-writing-and-the-future/)

![](images/Screenshot%202023-05-09%20at%202.09.22%20AM.png)
