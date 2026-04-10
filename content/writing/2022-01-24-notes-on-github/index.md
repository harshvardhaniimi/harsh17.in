---
title: Notes on Github
subtitle: Tricks of trade I learnt along the way
summary: Tricks of trade I learnt along the way
author: Harshvardhan
date: '2022-01-24'
slug: notes-on-github
tags:
- r
cover:
  image: og.png
  hidden: true
---
------------------------------------------------------------------------

# RStudio

Using Github is the popular method of version control in RStudio. I have struggled with managing Github with RStudio. In this section, I will put together pieces from different sources to fix your issues or get started with it.

## Starting a New Project

### Step 1: Create a Github Repository

Go to github.com and create a new repository. Copy it's link.

![Creating a new repository in Github](images/Screen%20Shot%202022-02-19%20at%2011.19.01%20PM.png)

It could be private or public depending on your whims. Public repositories are public --- other users can see and fork it. Forking is a fancy term for copying to their Github. Private repositories are seen only to you. I'd also recommend to add a README file. Project description goes here. Once you create your repository, copy the link to it. Not SSH link but link visible in your browser.

### Step 2: Create a New R Project

In RStudio, head over to File -\> New Project. In that, select the option for version control (git). Paste the link to your newly created repository.

![Choosing version control, Git and pasting link to your repository.](images/Screen%20Shot%202022-02-19%20at%2011.23.05%20PM.png)

Once you do that, the newly created project will be synced with Github repository. You can make changes and then "commit" to your online repository.

### Step 3: Commit Changes!

The last step is to create files that you want.

![Creating a dummy R Markdown file for demonstration](images/Screen%20Shot%202022-02-19%20at%2011.40.18%20PM.png)

Finally, commit the changes.

![Top right "Git" pane in RStudio](images/Screen%20Shot%202022-02-19%20at%2011.29.32%20PM.png)

In the top right corner of RStudio, tick all the changes you want to commit. Then add a message to the "commit message" box in the top right corner. This message is a record of what changes you did. (My advice is to use this to explain your intent rather than explain the changes. Changes are trivial to trace thanks to Git, but "why" is easy to forget.)

You'll have the results available (almost) immediately.

![I haven't used very informative commit messages for this. Beg your pardon for that.](images/Screen%20Shot%202022-02-19%20at%2011.45.29%20PM.png)

# Handling Passwords

If you are starting a project, jump to this. If you had a project that used password for commits (discontinued today, Aug 13 2021), jump to the first article. If it still does not resolve your issues, try the next three in that order.

-   [Simplest Guide on Github with R](https://gist.github.com/Z3tt/3dab3535007acf108391649766409421) This literally solves more than 80 per cent of my problems.

## Undo git commit in RStudio for more than 100 mb files

Every once in a while, you will end up trying to upload something in your local files that you do not want to commit to Github repository. How do you release that commit from R Studio? Github has a hard limit of 100 mb per file and I occasionally fail trying to upload it. Analysis paralysis.

![](images/Screen%20Shot%202022-01-24%20at%205.55.28%20PM.png)

### TL;DR

1.  Ensure you only have commits that you want to delete in the Git pane. Then go to Git tab.
2.  Click on <i class="fas fa-cog"></i> (machine-like icon) and select "Shell...".
3.  In Shell, type: `git reset HEAD~`.
4.  Keep hitting the statement as many times as you have commits.
5.  Voila.

### Full Steps

First, ensure you have only the changes you do not want to commit. If I try commiting with `.key` file, it will fail as it's larger than 100 mb.

![](images/Screen%20Shot%202022-01-24%20at%205.45.58%20PM.png)

I want to commit the last two changes (something about this blog post), so I will commit it and push changes to the [repository](https://github.com/harshvardhaniimi/personal-website). Then, I will go the <i class="fas fa-cog"></i> (machine-like icon) and click on "Shell...".

Now, I will paste in the Terminal window the magic spell: `git reset HEAD~`.

# Python

Use `nbdime` for diffing and merging Jupyter notebooks. Github desktop app is soon going to use it as default diff-tool for Jupyter notebooks.[^1]

[^1]: It annoys me that `.ipynb` is not plain text. Making it a plain text file would make it much easier to handle. Plus, we won't require an additional tool like JupyterLab/JupyterHub for viewing or editing. Why didn't they make it a plaintext file? I might be technically wrong on this one but one benefit might be plugins but they can easily be delivered as notebook extensions like in RStudio visual editor.

If you have a better suggestion on how to handle Python notebooks in Github, I'm [all ears](mailto:hello@harsh17.in).

## Some additional resources

-   <https://rfortherestofus.com/2021/02/how-to-use-git-github-with-r/>

-   <https://happygitwithr.com/https-pat.html#store-pat>

-   <https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/>
