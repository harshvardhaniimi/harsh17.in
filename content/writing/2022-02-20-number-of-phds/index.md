---
title: Number of PhDs by Field
summary: An Incomplete Data Exploration
subtitle: An Incomplete Data Exploration
author: Harshvardhan
date: '2022-02-20'
slug: number-of-phds
tags:
- data-science
- economics
- r
draft: false
cover:
  image: og.png
  hidden: true
---
<script src="{{< blogdown/postref >}}index_files/htmlwidgets/htmlwidgets.js"></script>
<link href="{{< blogdown/postref >}}index_files/datatables-css/datatables-crosstalk.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/datatables-binding/datatables.js"></script>
<script src="{{< blogdown/postref >}}index_files/jquery/jquery-3.6.0.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/dt-core/js/jquery.dataTables.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/crosstalk/css/crosstalk.min.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/crosstalk/js/crosstalk.min.js"></script>
<script src="{{< blogdown/postref >}}index_files/htmlwidgets/htmlwidgets.js"></script>
<link href="{{< blogdown/postref >}}index_files/datatables-css/datatables-crosstalk.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/datatables-binding/datatables.js"></script>
<script src="{{< blogdown/postref >}}index_files/jquery/jquery-3.6.0.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/dt-core/js/jquery.dataTables.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/crosstalk/css/crosstalk.min.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/crosstalk/js/crosstalk.min.js"></script>
<script src="{{< blogdown/postref >}}index_files/htmlwidgets/htmlwidgets.js"></script>
<link href="{{< blogdown/postref >}}index_files/datatables-css/datatables-crosstalk.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/datatables-binding/datatables.js"></script>
<script src="{{< blogdown/postref >}}index_files/jquery/jquery-3.6.0.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/dt-core/js/jquery.dataTables.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/crosstalk/css/crosstalk.min.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/crosstalk/js/crosstalk.min.js"></script>
<script src="{{< blogdown/postref >}}index_files/htmlwidgets/htmlwidgets.js"></script>
<link href="{{< blogdown/postref >}}index_files/datatables-css/datatables-crosstalk.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/datatables-binding/datatables.js"></script>
<script src="{{< blogdown/postref >}}index_files/jquery/jquery-3.6.0.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="{{< blogdown/postref >}}index_files/dt-core/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/dt-core/js/jquery.dataTables.min.js"></script>
<link href="{{< blogdown/postref >}}index_files/crosstalk/css/crosstalk.min.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/crosstalk/js/crosstalk.min.js"></script>

Yesterday I was talking to one of my friends about his plans post PhD. “I want to go for pure sciences and abstract mathematics, but there are hardly any positions in academia on these topics.”, he said. It got me into thinking how many PhD students graduate every year and if the demand (in academia or in industry) is less than that. But I didn’t even know how many PhDs are awarded each year, let alone employed.

While searching for a dataset for my Text Mining class project, I discovered this dataset on number of PhDs by field. So, let’s explore!

``` r
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──

    ## ✓ ggplot2 3.3.5          ✓ purrr   0.3.4     
    ## ✓ tibble  3.1.6          ✓ dplyr   1.0.8.9000
    ## ✓ tidyr   1.2.0          ✓ stringr 1.4.0     
    ## ✓ readr   2.1.2          ✓ forcats 0.5.1

    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(garlic)
library(DT)
theme_set(theme_linedraw())
```

``` r
# Loading dataset from their repository
phds = readr::read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-02-19/phd_by_field.csv")
```

    ## Rows: 3370 Columns: 5
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (3): broad_field, major_field, field
    ## dbl (2): year, n_phds
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
phds
```

    ## # A tibble: 3,370 × 5
    ##    broad_field   major_field                                 field   year n_phds
    ##    <chr>         <chr>                                       <chr>  <dbl>  <dbl>
    ##  1 Life sciences Agricultural sciences and natural resources Agric…  2008    111
    ##  2 Life sciences Agricultural sciences and natural resources Agric…  2008     28
    ##  3 Life sciences Agricultural sciences and natural resources Agric…  2008      3
    ##  4 Life sciences Agricultural sciences and natural resources Agron…  2008     68
    ##  5 Life sciences Agricultural sciences and natural resources Anima…  2008     41
    ##  6 Life sciences Agricultural sciences and natural resources Anima…  2008     18
    ##  7 Life sciences Agricultural sciences and natural resources Anima…  2008     77
    ##  8 Life sciences Agricultural sciences and natural resources Envir…  2008    182
    ##  9 Life sciences Agricultural sciences and natural resources Fishi…  2008     52
    ## 10 Life sciences Agricultural sciences and natural resources Food …  2008     96
    ## # … with 3,360 more rows

There are many records by fields — in three levels of granularity.There are 337 fields and we have records for each of them between 2008 to 2017. Let’s see how many people are from which field.

``` r
phds %>%
   group_by(broad_field) %>%
   summarise(n_phds = sum(n_phds, na.rm = T)) %>%
   arrange(desc(n_phds)) %>%
   datatable(colnames = c("Broad Field", "Number of PhDs"),
             rownames = FALSE,
             caption = "Number of PhDs by their broad fields. Life sciences lead the way.") %>%
   formatRound("n_phds", digits = 0)
```

<div id="htmlwidget-1" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-1">{"x":{"filter":"none","vertical":false,"caption":"<caption>Number of PhDs by their broad fields. Life sciences lead the way.<\/caption>","data":[["Life sciences","Psychology and social sciences","Humanities and arts","Education","Mathematics and computer sciences","Other","Engineering"],[205703,119116,53045,52639,35481,28855,18139]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th>Broad Field<\/th>\n      <th>Number of PhDs<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"columnDefs":[{"targets":1,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"className":"dt-right","targets":1}],"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render"],"jsHooks":[]}</script>

**Life sciences** has most number of graduates. **Engineering** has least number of graduates — even less than mysterious **Other**. Surprisingly social sciences, humanities and eucation are higher than mathematics and computer science. And they lead by a margin. The number of graduates in “humanities and social science” subjects is four times the number of PhDs in in “hard sciences” like engineering and maths. No wonder there is such a shortage of people in the tech world.

Life sciences as such a broad encompassing field. Let’s explore what is covered in life sciences.

``` r
phds %>%
   filter(broad_field == "Life sciences") %>%
   group_by(major_field) %>%
   summarise(n_phds = sum(n_phds, na.rm = T)) %>%
   arrange(desc(n_phds)) %>%
   datatable(colnames = c("Major Field", "Number of PhDs"),
             rownames = FALSE,
             caption = "Number of PhDs by their major fields. Biology, excluding health sciences, leads the way.") %>%
   formatRound("n_phds", digits = 0)
```

<div id="htmlwidget-2" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-2">{"x":{"filter":"none","vertical":false,"caption":"<caption>Number of PhDs by their major fields. Biology, excluding health sciences, leads the way.<\/caption>","data":[["Biological and biomedical sciences","Physics and astronomy","Chemistry","Health sciences","Geosciences, atmospheric sciences, and ocean sciences","Agricultural sciences and natural resources"],[85637,41176,25015,20882,19868,13125]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th>Major Field<\/th>\n      <th>Number of PhDs<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"columnDefs":[{"targets":1,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"className":"dt-right","targets":1}],"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render"],"jsHooks":[]}</script>

Biological and biomedical sciences has the most number of graduates. Let me explore engineering too. There are so few PhDs in geosciences. With climate change becoming another major issue, I wonder why the field isn’t picking up fast.

Let’s see the fields in engineering.

``` r
phds %>% 
  filter(broad_field == "Engineering") %>% 
  group_by(major_field) %>% 
  summarise(n_phds = sum(n_phds, na.rm = T)) %>% 
  arrange(desc(n_phds))
```

    ## # A tibble: 1 × 2
    ##   major_field       n_phds
    ##   <chr>              <dbl>
    ## 1 Other engineering  18139

Oh, so no information. The information is nested in another column, I guess. I’ll have to group by field.

``` r
phds %>% 
  filter(broad_field == "Engineering") %>% 
  group_by(field) %>% 
  summarise(n_phds = sum(n_phds, na.rm = T)) %>% 
  arrange(desc(n_phds)) %>% 
   datatable(colnames = c("Field", "Number of PhDs")) %>% 
   formatRound("n_phds", digits = 0)
```

<div id="htmlwidget-3" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-3">{"x":{"filter":"none","vertical":false,"data":[["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"],["Computer engineering","Environmental, environmental health engineeringl","Engineering, other","Nuclear engineering","Operations research (engineering)","Systems engineering","Petroleum engineering","Structural engineering","Agricultural engineering","Polymer, plastics engineering","Engineering mechanics","Robotics","Transportation and highway engineering","Engineering science","Engineering, general","Engineering management, administration","Geotechnical and geoenvironmental engineering","Engineering physics","Ocean engineering","Metallurgical engineering","Communications engineering","Mining and mineral engineering","Ceramic sciences engineering"],[4030,2001,1488,1166,985,924,760,743,674,658,644,566,556,497,467,430,396,287,271,244,231,83,38]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th> <\/th>\n      <th>Field<\/th>\n      <th>Number of PhDs<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"columnDefs":[{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"className":"dt-right","targets":2},{"orderable":false,"targets":0}],"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render"],"jsHooks":[]}</script>

Computer engineering PhDs are most popular; twice as much as next in the list. Environmental engineering is the second most popular. That’s impressive. Let’s visualise the counts.

``` r
phds %>% 
  filter(broad_field == "Engineering") %>% 
  group_by(field) %>% 
  summarise(n_phds = sum(n_phds, na.rm = T)) %>% 
  ggplot(aes(reorder(field, n_phds), n_phds)) +
  geom_col() +
  coord_flip() +
  labs(y = "Number of PhDs", x = "Field (Engineering only)")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-7-1.png" width="672" />

The data gives me opportunity to see how it grew up with the rise in popoularity of computer engineering. I’ve heard numerous time that its popularity has increased over the years.

``` r
# ggrepel for text labels
library(ggrepel)

phds %>%
   filter(broad_field == "Engineering") %>%
   mutate(label = if_else(year == max(year), field, NA_character_)) %>%
   ggplot(aes(x = year, y = n_phds, colour = field)) +
   geom_line() +
   scale_x_continuous(breaks = seq(from = 2008, to = 2017, by = 1)) +
   geom_label_repel(aes(label = label),
                    nudge_x = 1,
                    na.rm = TRUE) +
   labs(x = "Year", y = "Number of PhDs") +
   theme(legend.position = "none")
```

    ## Warning: Removed 20 row(s) containing missing values (geom_path).

    ## Warning: ggrepel: 10 unlabeled data points (too many overlaps). Consider
    ## increasing max.overlaps

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-8-1.png" width="672" />

``` r
phds_top_engineering = phds %>% 
  filter(broad_field == "Engineering") %>% 
  group_by(field) %>% 
  summarise(n_phds = sum(n_phds)) %>% 
  filter(n_phds > 100) %>% 
  slice_max(order_by = n_phds, n = 6)

phds_top_engineering
```

    ## # A tibble: 6 × 2
    ##   field                                            n_phds
    ##   <chr>                                             <dbl>
    ## 1 Computer engineering                               4030
    ## 2 Environmental, environmental health engineeringl   2001
    ## 3 Engineering, other                                 1488
    ## 4 Nuclear engineering                                1166
    ## 5 Operations research (engineering)                   985
    ## 6 Systems engineering                                 924

``` r
phds %>% 
  filter(field %in% phds_top_engineering$field) %>% 
ggplot(aes(x = year, y = n_phds, fill = field)) +
  geom_bar(stat = "identity") + 
  scale_x_continuous(labels = scales::label_number(accuracy = 1)) +
  scale_fill_manual(values = MetBrewer::met.brewer("Hokusai1", 6)) +
  facet_wrap( ~ field) +
  labs(x = "Year", y = "Number of PhDs", fill = "Field")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-9-1.png" width="672" />

Computer engineering has been ever popular. I didn’t expect that.

But wait, wasn’t there a computer science in `major_field`? What was that? It was called `Mathematics and computer sciences`.

``` r
phds %>%
   filter(broad_field == "Mathematics and computer sciences") %>%
   group_by(major_field) %>%
   summarise(n_phds = sum(n_phds, na.rm = T)) %>%
   arrange(desc(n_phds)) %>%
   datatable(colnames = c("Major Field", "Number of PhDs"),
             rownames = FALSE,
             caption = "Mathematics and computer sciences has two fields.") %>%
   formatRound("n_phds", digits = 0)
```

<div id="htmlwidget-4" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-4">{"x":{"filter":"none","vertical":false,"caption":"<caption>Mathematics and computer sciences has two fields.<\/caption>","data":[["Computer and information sciences","Mathematics and statistics"],[18395,17086]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th>Major Field<\/th>\n      <th>Number of PhDs<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"columnDefs":[{"targets":1,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"className":"dt-right","targets":1}],"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render"],"jsHooks":[]}</script>

``` r
phds %>%
   filter(broad_field == "Mathematics and computer sciences") %>%
   filter(n_phds >= 300) %>% 
   mutate(label = if_else(year == max(year), field, NA_character_)) %>%
   ggplot(aes(x = year, y = n_phds, colour = field)) +
   geom_line() +
   scale_x_continuous(breaks = seq(from = 2008, to = 2017, by = 1)) +
   geom_label_repel(aes(label = label),
                    nudge_x = 1,
                    na.rm = TRUE) +
   labs(x = "Year", y = "Number of PhDs") +
   theme(legend.position = "none")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-11-1.png" width="672" />

Computer engineering averaged around 400; computer science averaged around 1500. I think this the “computer science” in general parlance.

------------------------------------------------------------------------

**This exploration is incomplete. I couldn’t finish it in time but I’d get back to it someday.**

Today I found this wonderful visualisation on Twitter that I thought to replicate for the number of PhDs by field.

``` r
library(tweetrmd)
tweet_screenshot("https://twitter.com/jenjentro/status/1512997114896269312?t=nWQqyQa3tHQVNSHPakh2TA")
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-12-1.png" width="672" />

Her codes were available on [Github](https://github.com/jenjentro/TidyTuesday/blob/master/2022/2022-04-05/tidytues_newsorg.R).

``` r
# Loading packages
library(tidytuesdayR)
library(tidylog)
```

    ## 
    ## Attaching package: 'tidylog'

    ## The following objects are masked from 'package:dplyr':
    ## 
    ##     add_count, add_tally, anti_join, count, distinct, distinct_all,
    ##     distinct_at, distinct_if, filter, filter_all, filter_at, filter_if,
    ##     full_join, group_by, group_by_all, group_by_at, group_by_if,
    ##     inner_join, left_join, mutate, mutate_all, mutate_at, mutate_if,
    ##     relocate, rename, rename_all, rename_at, rename_if, rename_with,
    ##     right_join, sample_frac, sample_n, select, select_all, select_at,
    ##     select_if, semi_join, slice, slice_head, slice_max, slice_min,
    ##     slice_sample, slice_tail, summarise, summarise_all, summarise_at,
    ##     summarise_if, summarize, summarize_all, summarize_at, summarize_if,
    ##     tally, top_frac, top_n, transmute, transmute_all, transmute_at,
    ##     transmute_if, ungroup

    ## The following objects are masked from 'package:tidyr':
    ## 
    ##     drop_na, fill, gather, pivot_longer, pivot_wider, replace_na,
    ##     spread, uncount

    ## The following object is masked from 'package:stats':
    ## 
    ##     filter

``` r
library(showtext)
```

    ## Loading required package: sysfonts

    ## Loading required package: showtextdb
