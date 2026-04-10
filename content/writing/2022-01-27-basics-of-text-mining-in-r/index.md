---
title: Basics of Text Mining in R
subtitle: Thinking of Text as List of Words
summary: Thinking of Text as List of Words
author: Harshvardhan
date: '2022-01-27'
slug: basics-of-text-mining-in-r
tags:
- machine-learning
- ml
- r
---
Text in R can be represented in several ways but generally it is a character vector (strings). Reading a text file would mean most of the content would either be in a single long character file, or broken into several variables and observations as a data frame like comma separated files (CSV). In this blog tutorial, I will download a Jane Austen's book and perform some basic analysis to understand how these text functions work.

# Packages

The common packages for text mining in R are `stringr`, `tidytext`, `tidyverse` and `quanteda`. I will also use `gutenbergr` to download the book for analysis.


```r
library(stringr)
library(tidyverse)
```

```
## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──
```

```
## ✔ ggplot2 3.3.6.9000     ✔ purrr   0.3.4     
## ✔ tibble  3.1.7          ✔ dplyr   1.0.9     
## ✔ tidyr   1.2.0          ✔ forcats 0.5.1     
## ✔ readr   2.1.2
```

```
## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
```

```r
library(tidytext)
library(quanteda)
```

```
## Package version: 3.2.1
## Unicode version: 14.0
## ICU version: 70.1
```

```
## Parallel computing: 8 of 8 threads used.
```

```
## See https://quanteda.io for tutorials and examples.
```

```r
library(gutenbergr)

# changing default ggplot theme to minimal
theme_set(theme_minimal())
```

# Downloading the Book

Once I have the required functions in my namespace, I can download the book using `gutenberg_download()`. `gutenberg_works()` gives a list of works that can be downloaded. (`gutenberg_metadata` will give a list of all books in Project Gutenberg, but we only need the ones that can be downloaded.)


```r
gutenberg_works(title == "Persuasion")
```

```
## # A tibble: 1 × 8
##   gutenberg_id title    author gutenberg_autho… language gutenberg_books… rights
##          <int> <chr>    <chr>             <int> <chr>    <chr>            <chr> 
## 1          105 Persuas… Auste…               68 en       <NA>             Publi…
## # … with 1 more variable: has_text <lgl>
```

I am looking for **Persuasion**, Jane Austen's last book. R tells me the rights to the book are public and it has text, so works for my purpose. Downloading the book requires its `gutenberg_id,` which is 105 for **Persuasion**, as seen in previous output.


```r
book = gutenberg_download(105)
```

```
## Determining mirror for Project Gutenberg from http://www.gutenberg.org/robot/harvest
```

```
## Using mirror http://aleph.gutenberg.org
```

```
## Warning in .f(.x[[i]], ...): Could not download a book at http://
## aleph.gutenberg.org/1/0/105/105.zip
```

```
## Warning: Unknown or uninitialised column: `text`.
```

I can download more than one books at a time and many other fancy things. Check `gutenbergr`'s [vignette](https://docs.ropensci.org/gutenbergr/) for more information.

# Exploring the Book

Let's see what we have in `book`.


```r
book
```

```
## # A tibble: 0 × 2
## # … with 2 variables: gutenberg_id <int>, text <chr>
```

The `book` object has two variables: `gutenberg_id` and `text`. Unless you are downloading multiple books, `text` is the only useful variable.

Also note that there are 8,328 rows in the dataset. However, this text is not in `tidytext` [format](https://www.tidytextmining.com/tidytext.html), where each row identifies a token and each column is a variable. (An easy way to remember the format is to repeat out loud "**One Token Per Document Per Row**" as often as you can.)

To convert it into `tidytext` format, I will use `unnest_tokens()` function from `tidytext` package.


```r
book %>% 
  unnest_tokens(word, text)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: gutenberg_id <int>, word <chr>
```

`unnest_tokens` used here has two parameters: what you want to convert *into* and what you want to convert. First we have the output column name that will be created as the text is unnested into it (`word`, in this case), and then the input column that the text comes from (`text`, in this case).

The function also did some other operations in the background. It removed all the punctuation marks from the text. It also converted everything to lower case (which can be toggled OFF by using `to_lower = FALSE` in `unnest_tokens`. The function also has an argument `token` to specify what kind of text is it. `words` is the default option that worked for our case. Other options are `characters`, `character_shingles`, `ngrams`, `skip_ngrams`, `sentences`, `lines`, `paragraphs`, `regex`, `tweets` and `ptb`.

# Exploring Words

We can look for several manipulations for insights about the words. Such as, how many four letter words did she use? Less than four letter words? Longer than ten letter words?


```r
book = book %>% 
  unnest_tokens(word, text)

# Four Letter Words
book %>% 
  filter(str_length(word) == 4)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: gutenberg_id <int>, word <chr>
```

```r
# Less than four letter words
book %>% 
  filter(str_length(word) < 4)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: gutenberg_id <int>, word <chr>
```

```r
# More than ten letters
book %>% 
  filter(str_length(word) > 10)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: gutenberg_id <int>, word <chr>
```

We see that there are 15,505 words that have exactly four letters. 37,908 have less than four letters (that includes numbers such as 1). There are 1,636 words that have more than ten letters in them.

# Words that Start or End with ...

We can also find words that start or end with a particular string. For example, I wonder how often does Jane Austen use V4 form of the verb --- ending in "ing"? We can use `str_ends()` from `stringr` package.


```r
book %>% 
  filter(str_ends(word, "ing"))
```

```
## # A tibble: 0 × 2
## # … with 2 variables: gutenberg_id <int>, word <chr>
```

She uses 2,638 words that end with "ing". I'm curious, what are their frequencies? I only need to add the `count()` at the end.


```r
book %>% 
  filter(str_ends(word, "ing")) %>% 
  count(word, sort = T)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <chr>, n <int>
```

"Being" and "nothing" are the most often used (no pun intended). What about words that start with "h"? I can use `str_starts()` from `stringr` package for this.


```r
book %>% 
  filter(str_starts(word, "h")) %>% 
  count(word, sort = T)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <chr>, n <int>
```

They're mostly pronouns. How many times does "gh" appear in her texts and in which words? (If I recall correctly, "gh" is probably one of the most common letter-pair in English.)


```r
book %>% 
  filter(str_detect(word, fixed("gh"))) %>% 
  count(word, sort = T)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <chr>, n <int>
```

I did this using `str_detect()` function from `stringr`. This function usually looks for regular expressions. Since there was a fix string that I was looking for (`gh`), I used `fixed()` to tell R exactly what I was looking for. It will not make pattern matches but only exact fixed matches. I'm very naive in handling regular expressions but the starting guide could be Hadley Wickham's R for Data Science chapter on [Strings](https://r4ds.had.co.nz/strings.html).

I can also look for words that start with a certain letter(s) and end with certain letter(s). How? Just add another condition in the `filter()` statement. Let's look for words Jane used that start and end with "t".


```r
book %>% 
  filter(str_starts(word, "t") & str_ends(word, "t")) %>% 
  count(word, sort = T)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <chr>, n <int>
```

The most common such word is "that", followed by "thought".

# Frequency Distribution Plots

We saw how adding `count(word, sort = T)` created the frequency distribution. We can also visualise the counts.

## Frequency Table


```r
book %>% 
  count(word, sort = T) %>%
  head(20) %>% 
  mutate(word = reorder(word, n))
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <fct>, n <int>
```

## Frequency Plot

I will have to reorder the counts for creating the plot as `count()` only counts and doesn't change the order of the tibble.


```r
book %>% 
  count(word, sort = T) %>%
  head(20) %>% 
  mutate(word = reorder(word, n)) %>% 
  ggplot(aes(x = n, y = word)) +
  geom_col() +
  xlab("Count") +
  ylab("Word")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-13-1.png" width="672" />

# Finding Hapaxes

Hapaxes are words that occur only once in the text. Nothing complicated; I will first count the occurrences and then filter when the `count` is 1.


```r
book %>% 
  count(word, sort = T) %>% 
  filter(n == 1)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <chr>, n <int>
```

These are all numbers. What about words?


```r
book %>% 
  count(word, sort = T) %>% 
  filter(n == 1) %>% 
  filter(!str_detect(word, "[0-9]"))
```

```
## # A tibble: 0 × 2
## # … with 2 variables: word <chr>, n <int>
```

I have used regular expression here to identify all the words that didn't have any numerals.

# Distribution of Word Lengths

Some writers have a habit of writing long words. What were the longest words used by Jane and how often did she use them?


```r
book %>% 
  mutate(length = str_length(word)) %>% 
  count(length, sort = T)
```

```
## # A tibble: 0 × 2
## # … with 2 variables: length <int>, n <int>
```

Three letter words are most commonly used, followed by four letter and two letter ones. I have first calculated the length of words using `mutate()` and `str_length()`.

I can also plot them.


```r
book %>% 
  mutate(length = str_length(word)) %>% 
  count(length, sort = T) %>% 
  mutate(length = reorder(length, n)) %>% 
  ggplot(aes(x = length, y = n)) +
  geom_col() +
  xlab("Length of Word") +
  ylab("Count")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-17-1.png" width="672" />

That was all! See you in next week when I try some harder text analysis tools.

------------------------------------------------------------------------

P.S. I have used the words "word(s)" and "token(s)" quite liberally. They are not always the same. As `token` argument in `unnest_token` informs, there are *many* options besides words that can be tokens.
