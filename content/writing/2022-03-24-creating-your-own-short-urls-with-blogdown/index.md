---
title: Creating your own short URLs with blogdown
subtitle: bit.ly, but personalised
summary: Here's how to make your short URLs using Hugo + Blogdown
author: Harshvardhan
date: '2022-03-24'
slug: creating-your-own-short-urls-with-blogdown
tags:
- r
- tools
---
A few days ago I shared my personal Zoom room link to a few people: <https://www.harsh17.in/zoom>. The neatness of this in comparison to something like <https://zoom.us/j/99672273048?pwd=eXV5R2pBR0FqNlBUWmtLdCt6THl3dz09> was amazing. It had two immediate effects:

1.  Sharing Zoom link wasn't a tedious task anymore. I could type it anywhere from my memory.
2.  People started taking my Zoom calls more seriously. I'd like to believe it was due to my content but the short URL certainly had an effect.

How did I do it?

[Blogdown](https://bookdown.org/yihui/blogdown/).

R is amazing and can easily be extended to new functionalities. Blogdown is an R package for creating personal websites.

You can create your own set of URL redirects in Blogdown. Instead of typing long URLs, you can create your own custom short URLs of the form `yourwebsite.com/shorturl`.

## Step 1

Go to your folder `/static/` located in your personal website folder. It may or may not have any content already. If you do not have that folder, create one right beside other folders such as `content`, `layout` and `themes`.

![](images/Screen%20Shot%202022-03-24%20at%203.43.02%20PM.png)

> Personal website directory. Create a folder `static` here if you don't have it already.

## Step 2

Open your text editor (Notepad in Windows and TextEdit in MacOS) and create a new file named `_redirects` with **no extension**. Your computer will tell you add an extension, ignore the warning and go ahead.

![](images/Screen%20Shot%202022-03-24%20at%203.28.32%20PM.png)

## Step 3

Write your URLs there. Start with the short URL and then long URL with at least two tab spaces. See my example below.

![](images/Screen%20Shot%202022-03-24%20at%203.28.59%20PM.png)

> Remember to leave appropriate space (at least two tabs) between the short and long URLs. Handle '`/`' properly.

You can have comments starting with `#`.

That's all!

Commit your edits to Github and give it two minutes to deploy via Netlify. Try your short URL and it should work.

# Some Tips

Create short URLs for articles or website you frequently share or visit. For example, I have created short URLs for my social media profiles because twitter.com would take me to the home page instead of profile page.

Create a short URL for your Zoom room link. This one is a no-brainer.

Create short URLs for content you share often. I frequently share link to my [Newsletter](https://www.harsh17.in/next) and my article on [IPM admissions](https://www.harsh17.in/ipm). So, I created their short URLs that I can type as I go.

# Troubleshooting

Here are some tips in case you run into some troubles.

-   Make sure you leave at least two tab spaces between short URL and long URL.

-   `/` matter. See that you are using the right short URL with or without `/` at the end.

-   Commit to Github and wait for results. Netlify takes a few minutes to deploy your new site.

If you still have troubles, write to me at [hello\@harsh17.in](mailto:hello@harsh17.in) and we can resolve it together.
