---
title: 'Up Your Blogging Game: Three Enhancements to Hugo Apero'
subtitle: Revamp Themes, Add Search Bars, Change Fonts
summary: This post provides a detailed guide to customizing the Hugo Apero template,
  focusing on changing themes, adding a search bar, and altering fonts for a truly
  personalized blogging experience.
author: Harshvardhan
date: '2023-05-20'
slug: hugo
tags:
- r
draft: false
cover:
  image: og.png
  relative: true
  hidden: true
---
[Hugo Apero](https://hugo-apero.netlify.app/) is the Blogdown template I use for this website. The template ships with great defaults, the best of all Hugo templates in my opinion. Beyond those defaults, it provides many options to modify your website in a meaningful way. In this blog, I list out three good ones.

From changing the color theme and adding a custom search bar, to customizing the fonts, each of these tweaks can significantly enrich your site's aesthetic and functionality. So buckle up as we delve into the nuances of the Hugo Apero template, and let's unlock the potential of your website!

## 1. Change your Theme

The colour theme for Hugo Apero can be changed by editing your `config.toml` or `config.yaml` file. The exact one would depend on your template version.

In your `config.yaml` file, you will find an option for `theme`. Edit it to suit your needs! There are six themes available by default.


```r
# use a built-in color theme
# one of: forest / grayscale / peach / plum /
#         poppy / sky / violet / water 
theme = "violet"
```

![Default colour themes in Hugo Apero.](images/Screenshot%202023-04-16%20at%2011.30.43%20PM.png)

[Michael McCarthy](https://github.com/mccarthy-m-g) also created [four new themes](https://github.com/hugo-apero/hugo-apero/pull/72): Earth, Paper (Grayscale alternative which I like more), Magma ("dark" mode) and Primer (another dark one based on Github's "primer" theme).[^1] As of today (April 16, 2023), I use "Earth". If you want to use any of these, you will have to do some additional work.

[^1]: This is a pull request on Apero's Github repo. At some point, I believe it will be merged into the theme. But that hasn't happened in almost a year...

Before I describe what you need to do to use them, take a look at these themes.

![](images/Screenshot%202023-04-16%20at%2011.53.16%20PM.png)

**I've found Magma and Primer (dark themes basically) to be bad at showing `kable` and `DT` tables. Just something to keep in mind.**

To identify the changes needed to your site's configuration, one can look at the [pull request](https://github.com/hugo-apero/hugo-apero/pull/72/commits). Here are the steps:

1.  First, head over to `assets/scaffold.scss` and add the theme name you want to use to the following line.


```r
{{$themes := (slice "earth" "forest" "grayscale" "paper" "peach" "plum" "poppy" "sky" "violet" "water")}}
```

2.  Then create a `theme_name.scss` file in `assets/theme/` folder. You can look at the pull request for exact content of the files. ([Earth and Paper](https://github.com/hugo-apero/hugo-apero/pull/72/commits/04735183ad6351badcaacabc86196752d899bf6b), [Magma](https://github.com/hugo-apero/hugo-apero/pull/72/commits/d0bd72003f2084357ec7af15cb1964b3c702fc33), and [Primer](https://github.com/hugo-apero/hugo-apero/pull/72/commits/909406f6c66269b33706fd735728784d861e5dd4))

3.  Go to your `config.yaml` or `config.toml` file and change the theme name as described earlier. (Whether is "=" or ":" would depend on whether is `yaml` or `toml`.)


```r
    theme: "sky"
```

## 2. Add a Search Bar

Another simple addition is to add a custom search bar in your site. Having a search tab on a website is useful because it allows users to quickly and easily find the information they are looking for. It also helps users who may not be familiar with the website's organization or navigation, allowing them to quickly locate information without having to spend time browsing through different pages.

It is super simple to do in Hugo Apero.

1.  Head over to `cse.google.com`. Create a new search engine by clicking "Add".

    ![](images/Screenshot%202023-05-05%20at%203.22.29%20PM.png)

2.  Give your custom search engine a cool name. Add you website's URL in "What to Search". Would you like to include images for search and use safe-search? Choose appropriately.

3.  Following this, you will get a public URL for your custom search engine. It would be something like "<https://cse.google.com/cse?cx=7d9698c281e7d2001>".

4.  I've added my search box to About page. To do that, you can head over to `/content/about/_index.md`. Then in the `outro` section, add the following HTML code.


```r
    outro: |
      <i class="fas fa-mug-hot pr2"></i>If my blog has helped you, you can [buy me a coffee](https://www.buymeacoffee.com/harsh17)!
      <script async src="https://cse.google.com/your_search_url"></script>
      <div class="gcse-search"></div>
```

Make sure that `show_outro` is set to `true`. Enjoy your new search engine!

## 3. Changing Fonts

This subsection largely follows the [official documentation](https://hugo-apero-docs.netlify.app/learn/fonts/). There are six fonts included out of the box. You can choose them in `config.toml` or `config.yaml`.


```r
  textFontFamily = "courier"
  headingFontFamily = "baskerville"
```

You like it spicy? Me too. Let's play with some nontraditional fonts from Google Fonts.[^2] We will be using this [Webapp](https://gwfh.mranftl.com/fonts) to get the files in the right format.

[^2]: I'm truly grateful to Google for making such a huge database of fonts freely available. Like seriously...

1.  First, decide which fonts you want for your heading and text. This is likely going to take a lot of trials but to understand the process, you can choose any from [Google Fonts site](https://fonts.google.com/).
2.  Once you know which font you want, search it's name in the [Webapp](https://gwfh.mranftl.com/fonts). The app will show you the **custom CSS** as well as prepare the ZIP file.![](images/Screenshot%202023-05-05%20at%203.41.19%20PM.png)
3.  Create a `static/fonts` folder and add the font files (that you got from **Download files** option) to that folder.
4.  Finally, head back to `config.toml` or `config.yaml` and edit the font name.


```r
  customtextFontFamily = ""
  customheadingFontFamily = "Nanum Myeongjo"
```

Push the commits to Github and enjoy your new fonts! If you're not sure which fonts to choose, my advice is experiment, experiment and experiment. Jonathan Hoefler, who created fonts for Apple, Obama's Change campaign, and more, did an episode on typeface design: ["Abstract: The Art of Design" (Netflix)](https://jonathanhoefler.com/documentary).[^3] The linked site is an introduction to typeface fundamentals.

[^3]: Hat tip to Dea for the recommendation.

## And that's a wrap!

In this post, we have traversed a number of essential changes that can truly enhance your Hugo Apero site, ensuring it stands out. From switching up the theme and adding a custom search bar, to refining the fonts, these tips serve to unlock the potential that resides in the Blogdown template.

Experimenting is key -- so go ahead and try out various themes, search bars, and fonts until you find the perfect fit. Remember, your website is a reflection of you, so don't be afraid to show off your style!
