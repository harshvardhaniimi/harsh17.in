---
title: 'IndiaPIN: R Data Package'
subtitle: 'R Package for All India PIN Codes Directory with Latitude and Longitude
  Details (Updated: December 2021)'
summary: 'R Package for All India PIN Codes Directory with Latitude and Longitude
  Details (Updated: December 2021)'
author: Harshvardhan
date: '2022-01-11'
slug: IndiaPIN
tags:
- r
- tools
github: https://github.com/harshvardhaniimi/IndiaPIN
---
<link href="{{< blogdown/postref >}}index_files/htmltools-fill/fill.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/htmlwidgets/htmlwidgets.js"></script>

<script src="{{< blogdown/postref >}}index_files/jquery/jquery-3.6.0.min.js"></script>

<link href="{{< blogdown/postref >}}index_files/leaflet/leaflet.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/leaflet/leaflet.js"></script>

<link href="{{< blogdown/postref >}}index_files/leafletfix/leafletfix.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/proj4/proj4.min.js"></script>

<script src="{{< blogdown/postref >}}index_files/Proj4Leaflet/proj4leaflet.js"></script>

<link href="{{< blogdown/postref >}}index_files/rstudio_leaflet/rstudio_leaflet.css" rel="stylesheet" />
<script src="{{< blogdown/postref >}}index_files/leaflet-binding/leaflet.js"></script>

`IndiaPIN` contains geographic details about 19,300 PIN codes in India. Some PIN codes had more than one offices. Only the first office of that PIN code area has been retained in those cases. (Updated: December 2021.)

![](images/indiapin_tweet.png)

## Variables

1.  **Circle:** (chr) Name of the Postal Circle
2.  **Region:** (chr) Name of the Postal Region
3.  **Division:** (chr) Name of the Postal Division
4.  **Office:** (chr) Name of Postal Office
5.  **PIN:** (int) Six-digit PIN Code
6.  **District:** (chr) Name of the District
7.  **State:** (chr) Name of the State
8.  **Latitude:** (dbl) Latitude
9.  **Longitude:** (dbl) Longitude

### Data Source

Department of Posts, Ministry of Communications, Government of India. URL: <https://www.indiapost.gov.in/vas/pages/findpincode.aspx>. Wrangled for this package by Harshvardhan (<https://harsh17.in/>).

------------------------------------------------------------------------

## Installation

``` r
# install `devtools` if not already installed
if (!require("IndiaPIN")) 
    devtools::install_github("harshvardhaniimi/IndiaPIN")
```

    ## Loading required package: IndiaPIN

    ## Warning in library(package, lib.loc = lib.loc, character.only = TRUE,
    ## logical.return = TRUE, : there is no package called 'IndiaPIN'

    ## Using github PAT from envvar GITHUB_PAT. Use `gitcreds::gitcreds_set()` and unset GITHUB_PAT in .Renviron (or elsewhere) if you want to use the more secure git credential store instead.

    ## Downloading GitHub repo harshvardhaniimi/IndiaPIN@HEAD

    ## cli  (3.6.4 -> 3.6.5) [CRAN]
    ## utf8 (1.2.4 -> 1.2.5) [CRAN]

    ## Installing 2 packages: cli, utf8

    ## 
    ## The downloaded binary packages are in
    ## 	/var/folders/jw/3b0w1v0s3f990hs35ngj6jl40000gn/T//RtmpAZzBDV/downloaded_packages
    ## ── R CMD build ─────────────────────────────────────────────────────────────────
    ## * checking for file ‘/private/var/folders/jw/3b0w1v0s3f990hs35ngj6jl40000gn/T/RtmpAZzBDV/remotesd7c37e2d063/harshvardhaniimi-IndiaPIN-da43b49/DESCRIPTION’ ... OK
    ## * preparing ‘IndiaPIN’:
    ## * checking DESCRIPTION meta-information ... OK
    ## * checking for LF line-endings in source and make files and shell scripts
    ## * checking for empty or unneeded directories
    ## * building ‘IndiaPIN_0.0.1.tar.gz’

``` r
# Tidyverse
library(tidyverse)
```

    ## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ## ✔ dplyr     1.1.4     ✔ readr     2.1.5
    ## ✔ forcats   1.0.0     ✔ stringr   1.5.1
    ## ✔ ggplot2   3.5.2     ✔ tibble    3.2.1
    ## ✔ lubridate 1.9.4     ✔ tidyr     1.3.1
    ## ✔ purrr     1.0.4

    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()
    ## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

``` r
# load IndiaPIN
library(IndiaPIN)
data(IndiaPIN)
```

## Example

### Data and Variables

``` r
IndiaPIN
```

    ## # A tibble: 18,169 × 9
    ## # Groups:   PIN [18,169]
    ##    Circle        Region Division Office    PIN District State Latitude Longitude
    ##    <chr>         <chr>  <chr>    <chr>   <int> <chr>    <chr>    <dbl>     <dbl>
    ##  1 Andhra Prade… Kurno… Hindupu… Pedda… 515631 ANANTAP… ANDH…     14.6      77.9
    ##  2 Andhra Prade… Kurno… Hindupu… Obula… 515581 ANANTAP… ANDH…     14.2      78.3
    ##  3 Andhra Prade… Kurno… Hindupu… Gurra… 515571 ANANTAP… ANDH…     13.9      78.2
    ##  4 Andhra Prade… Kurno… Hindupu… Halli… 515311 ANANTAP… ANDH…     13.8      77.0
    ##  5 Andhra Prade… Kurno… Hindupu… Tamma… 515281 ANANTAP… ANDH…     14.1      77.0
    ##  6 Andhra Prade… Kurno… Hindupu… Bussa… 515241 ANANTAP… ANDH…     14.0      77.7
    ##  7 Andhra Prade… Vijay… Tadepal… Kavul… 534176 WEST GO… ANDH…     16.6      80.6
    ##  8 Bihar Circle  East … Bhagalp… Kathr… 813105 BANKA    BIHAR     84.5      24.2
    ##  9 Bihar Circle  East … Bhagalp… Kasri… 813203 BHAGALP… BIHAR     87.3      25.3
    ## 10 Bihar Circle  East … Bhagalp… Akida… 853202 BHAGALP… BIHAR     25.4      84.3
    ## # ℹ 18,159 more rows

### Number of PIN codes by State/UT

``` r
IndiaPIN %>% 
  group_by(State) %>% 
  summarise(Count = n()) %>% 
  arrange(desc(Count)) %>% 
  print(n = 40)
```

    ## # A tibble: 35 × 2
    ##    State                                        Count
    ##    <chr>                                        <int>
    ##  1 TAMIL NADU                                    2032
    ##  2 UTTAR PRADESH                                 1581
    ##  3 MAHARASHTRA                                   1466
    ##  4 KERALA                                        1425
    ##  5 KARNATAKA                                     1188
    ##  6 WEST BENGAL                                   1125
    ##  7 ANDHRA PRADESH                                1071
    ##  8 GUJARAT                                       1007
    ##  9 RAJASTHAN                                      986
    ## 10 ODISHA                                         933
    ## 11 BIHAR                                          853
    ## 12 MADHYA PRADESH                                 760
    ## 13 ASSAM                                          571
    ## 14 PUNJAB                                         531
    ## 15 TELANGANA                                      482
    ## 16 HIMACHAL PRADESH                               436
    ## 17 JHARKHAND                                      360
    ## 18 HARYANA                                        310
    ## 19 UTTARAKHAND                                    300
    ## 20 CHHATTISGARH                                   240
    ## 21 JAMMU AND KASHMIR                              195
    ## 22 DELHI                                           97
    ## 23 GOA                                             88
    ## 24 CHANDIGARH                                      25
    ## 25 PUDUCHERRY                                      22
    ## 26 SIKKIM                                          19
    ## 27 MEGHALAYA                                       16
    ## 28 TRIPURA                                         10
    ## 29 MIZORAM                                          9
    ## 30 THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU     8
    ## 31 LAKSHADWEEP                                      7
    ## 32 ARUNACHAL PRADESH                                5
    ## 33 NAGALAND                                         5
    ## 34 ANDAMAN AND NICOBAR ISLANDS                      4
    ## 35 LADAKH                                           2

### PIN Code Locations on Map

I will use `leaflet` package to plot randomly selected 50 PIN codes. I am adding the Region and Circle name in the popup.

``` r
library(leaflet)
library(tidyverse)
library(IndiaPIN)

data("IndiaPIN")

set.seed(4)
index = sample(nrow(IndiaPIN), 50)
data = IndiaPIN::IndiaPIN[index,]

l1 = data$Longitude
l2 = data$Latitude
pop = paste(data$Region, data$Circle, sep = ", ")

m = leaflet() %>% 
   addTiles() %>% 
   addMarkers(lng=l1, lat=l2, popup = pop)

m
```

<div class="leaflet html-widget html-fill-item" id="htmlwidget-1" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-1">{"x":{"options":{"crs":{"crsClass":"L.CRS.EPSG3857","code":null,"proj4def":null,"projectedBounds":null,"options":{}}},"calls":[{"method":"addTiles","args":["https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",null,null,{"minZoom":0,"maxZoom":18,"tileSize":256,"subdomains":"abc","errorTileUrl":"","tms":false,"noWrap":false,"zoomOffset":0,"zoomReverse":false,"opacity":1,"zIndex":1,"detectRetina":false,"attribution":"&copy; <a href=\"https://openstreetmap.org/copyright/\">OpenStreetMap<\/a>,  <a href=\"https://opendatacommons.org/licenses/odbl/\">ODbL<\/a>"}]},{"method":"addMarkers","args":[[15.59,20.8123078,26.4418889,26.49,13.98,26.08,14.896666,9.685375000000001,10.799571,19.0160278,26.198944,23.394827,19.3638871,20.872131,20.2362451,17.75097222,31.32,13.0786433,26.8522,11.67014,15.6618661,8.26,20.8148633,25.57391667,21.2305298,25.3471,10.3,21.475104,17.7041944,29.7208611,31.2101,24.5439167,13.801001,21.783465,26.1095277,17.5476,10.94,10.642185,20.3850278,27.9834271,22.38,24.585445,23.45038,28.9,28.62,14.55,25.393,8.7256944,9.890644,19.08258],[73.34,86.31015480000001,80.3425833,88.58,75.73999999999999,89.61,74.10785180000001,76.99091199999999,76.642318,72.84586109999999,74.143584,79.01925,78.792953,71.40767200000001,82.59031779999999,78.90016667,74.76000000000001,76.4548795,84.78225,78.11459499999999,77.0748349,77.17,86.62437660000001,91.88486111,72.86389,74.6408,78.06999999999999,79.79325,83.29649999999999,75.90252769999999,77.4003,81.3015833,78.925532,70.930808,84.2933611,74.03735,79.25,76.544826,78.119,78.3998642,69.04000000000001,73.712479,73.17921200000001,78.45999999999999,78.77,75.06999999999999,87.193966,78.2025556,76.783423,72.882228],null,null,null,{"interactive":true,"draggable":false,"keyboard":true,"title":"","alt":"","zIndexOffset":0,"opacity":1,"riseOnHover":false,"riseOffset":250},["Vadodara Region, Gujarat Circle","DivReportingCircle, Odisha Circle","Kanpur Region, Uttar Pradesh Circle","North Bengal Region, West Bengal Circle","South Karnataka Region, Karnataka Circle","North Bengal Region, West Bengal Circle","North Karnataka Region, Karnataka Circle","Kochi Region, Kerala Circle","Calicut Region, Kerala Circle","Mumbai Region, Maharashtra Circle","Muzaffarpur Region, Bihar Circle","Jabalpur Region, Madhya Pradesh Circle","Hyderabad Region, Telangana Circle","Rajkot Region, Gujarat Circle","Berhampur Region, Odisha Circle","Hyderabad City Region, Telangana Circle","Punjab West Region, Punjab Circle","South Karnataka Region, Karnataka Circle","Muzaffarpur Region, Bihar Circle","Western Region, Coimbatore, Tamilnadu Circle","North Karnataka Region, Karnataka Circle","Southern Region, Madurai, Tamilnadu Circle","DivReportingCircle, Odisha Circle","Shillong HQ Region, North Eastern Circle","Vadodara Region, Gujarat Circle","Ajmer Region, Rajasthan Circle","Southern Region, Madurai, Tamilnadu Circle","Nagpur Region, Maharashtra Circle","Visakhapatnam Region, Andhra Pradesh Circle","DivReportingCircle, Haryana Circle","DivReportingCircle, Himachal Pradesh Circle","Jabalpur Region, Madhya Pradesh Circle","Jabalpur Region, Madhya Pradesh Circle","Rajkot Region, Gujarat Circle","Muzaffarpur Region, Bihar Circle","Pune Region, Maharashtra Circle","Central Region, Trichirapalli, Tamilnadu Circle","Calicut Region, Kerala Circle","Nagpur Region, Maharashtra Circle","Agra Region, Uttar Pradesh Circle","Rajkot Region, Gujarat Circle","DivReportingCircle, Chattisgarh Circle","Ahmedabad HQ Region, Gujarat Circle","Bareilly Region, Uttar Pradesh Circle","Bareilly Region, Uttar Pradesh Circle","South Karnataka Region, Karnataka Circle","East Region, Bhagalpur, Bihar Circle","Southern Region, Madurai, Tamilnadu Circle","Kochi Region, Kerala Circle","Mumbai Region, Maharashtra Circle"],null,null,null,null,{"interactive":false,"permanent":false,"direction":"auto","opacity":1,"offset":[0,0],"textsize":"10px","textOnly":false,"className":"","sticky":true},null]}],"limits":{"lat":[8.26,31.32],"lng":[69.04000000000001,91.88486111]}},"evals":[],"jsHooks":[]}</script>

Also see this [Stackoverflow thread](https://stackoverflow.com/questions/31336898/how-to-save-leaflet-in-r-map-as-png-or-jpg-file) to understand how to save the plots.

See [Github](https://github.com/harshvardhaniimi/IndiaPIN) for source code.
