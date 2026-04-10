---
title: Street Maps (of Some Cities)
subtitle: Some beautiful street maps
summary: Over the last few days, I dabbled with maps in R. Two days ago, I made a
  map of all the cities I've visited. Today, I thought to make street maps of some
  of them (and other cool cities).
author: Harshvardhan
date: '2022-05-28'
slug: city-maps
tags:
- r
---
Over the last few days, I dabbled with maps in R. Two days ago, I made a map of all the cities I've visited. Today, I thought to make street maps of some of them (and other cool cities).

The dark grey lines are highways and roadways, light grey lines are other streets and blue is water.

# Jhumri Tilaiya, India



<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-2-1.png" width="672" />

# Indore, India

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-3-1.png" width="672" />

# Riga, Latvia

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-4-1.png" width="672" />

# Knoxville, United States

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-5-1.png" width="672" />

# New Delhi, India

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-6-1.png" width="672" />

# Sydney, Australia

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-7-1.png" width="672" />

# New York, United States

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-8-1.png" width="672" />

# Boston, United States

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-9-1.png" width="672" />

# London, United Kingdom

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-10-1.png" width="672" />

------------------------------------------------------------------------

The function to generate these is not complicated. For a detailed tutorial, [see this tutorial](https://ggplot2tutor.com/tutorials/streetmaps?utm_source=pocket_mylist). Here's the function that I used.


```r
library(tidyverse)
library(osmdata)

city_mapper = function(city)
{
   lts = getbb(city)
   
   streets = getbb(city)%>%
      opq()%>%
      add_osm_feature(key = "highway", 
                      value = c("motorway", "primary", 
                                "secondary", "tertiary")) %>%
      osmdata_sf()
   
   small_streets = getbb(city)%>%
      opq()%>%
      add_osm_feature(key = "highway", 
                      value = c("residential", "living_street",
                                "unclassified",
                                "service", "footway")) %>%
      osmdata_sf()
   
   river = getbb(city)%>%
      opq()%>%
      add_osm_feature(key = "waterway", value = "river") %>%
      osmdata_sf()
   
   p = ggplot() +
      geom_sf(data = streets$osm_lines,
              inherit.aes = FALSE,
              color = "#282828", #3C280D
              size = .5,
              alpha = .7) +
      geom_sf(data = small_streets$osm_lines,
              inherit.aes = FALSE,
              color = "#909090", #795C34
              size = .4,
              alpha = .4) +
      geom_sf(data = river$osm_lines,
              inherit.aes = FALSE,
              color = "#03026F",
              size = .7,
              alpha = .8) +
      coord_sf(xlim = c(lts[1], lts[3]), 
               ylim = c(lts[2], lts[4]),
               expand = FALSE) +
      theme_void() +
      labs(caption = "Learn more: harsh17.in/city-maps")
   
   return(p)
   
}
```
