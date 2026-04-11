---
title: The Map of Tiny Perfect Things
summary: A crowd-sourced map of meaningful places — cafes, parks, museums, and other tiny perfect things — built with Dea Bardhoshi.
author: Harshvardhan
date: '2026-04-11'
slug: mtpt
tags:
- tools
- travel
- coffee
github: https://github.com/harshvardhaniimi/map-of-tiny-perfect-things
website: https://mtpt.netlify.app/
cover:
  image: og.png
  hidden: true
---

This project started with two things: [Dea](https://deabardhoshi.com/)'s journal and my obsession with [Knoxville cafes](/best-cafes-in-knoxville/).

Dea keeps an intricate journal of places she's visited --- not just names and addresses, but what made them worth remembering. The kind of notes you'd text a close friend, not write in a Yelp review. I first learn about them when I was exploring cafes in Portland, OR with her in 2022.

I, on the other hand, had spent a year cataloguing every cafe in Knoxville worth sitting in, complete with notes on wifi quality and whether they'd judge you for staying four hours. Between the two of us, we had a dataset of places that mattered to us. And an itch to build something with it.

So we built [The Map of Tiny Perfect Things](https://mtpt.netlify.app/).

![The Map of Tiny Perfect Things](/images/mtpt-home.png)

## What It Is

An interactive map of places that feel memorable --- not just highly rated. Currently, we have Cafes, Restaurants and more. We have about 230 places across 17 cities and 2 countries (United States and India). About a third of them are creator picks --- places Dea or I can personally vouch for. The rest come our or our friends’ general suggestions.

We also made possible for anyone to submit a place through the [submission form](https://mtpt.netlify.app/submit) --- no login, no account needed. We review submissions before they go live. There's also a [feature request form](https://mtpt.netlify.app/feature) if you want to suggest improvements.

## The Chat

We added a chat interface at [`/chat`](https://mtpt.netlify.app/chat) where you can ask natural language questions like "best coffee in Knoxville" or "somewhere quiet to read in San Francisco." It searches through our dataset and returns recommendations. The retrieval is backed by a Netlify Function calling OpenAI's API, but if the model call fails, it falls back to plain retrieval-based recommendations.

![Ask Ava - Our Chatbot](/images/ask-ava.png)

I'll be honest --- I don't fully understand every piece of the technology stack here. The app is React + Leaflet for the map, Netlify Functions for the backend, OpenAI for the chat. A lot of the recent development work is courtesy [Claude Code](https://claude.ai/claude-code). We'd been stuck on some things for months and then one afternoon it all just... worked.

## Data Collection

This is the part that's still not steady. We have an automated pipeline --- a GitHub Action runs every six hours, pulls new submissions from Netlify Forms, geocodes them, and opens a PR to merge into the master dataset. It works. But the *submissions* themselves are sporadic. Getting people to submit places is harder than building the infrastructure to receive them.

We're working on it. If you have a place that matters to you, [submit it](https://mtpt.netlify.app/submit).

![Add a Place to MTPT](/images/mtpt-home.png)

## The Name

Yes, it's from the [movie](https://en.wikipedia.org/wiki/The_Map_of_Tiny_Perfect_Things). The idea of noticing small, perfect moments in ordinary places felt exactly right for what we were trying to do. We're not mapping the best-reviewed restaurants in a city. We're mapping the places where something clicked.

Hope you guys like it.
