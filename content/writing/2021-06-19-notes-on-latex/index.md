---
title: Notes on LaTeX
subtitle: Typesetting isn't that easy
summary: Typesetting isn't that easy
author: Harshvardhan
date: '2021-06-19'
tags:
- tools
slug: latex
cover:
  image: og.png
  hidden: true
---
## Write Markdown in LaTeX for Notes

I often write my "chain of thought" in documents before writing the full page.
I used to use verbatim environment for this.
Now, I've found an alternative --- Markdown directly!

First, make sure you import `listings` and `xcolor` packages.

```latex
\usepackage{listings}
\usepackage{xcolor}
```

Then, create a custom environment:

```latex
\lstdefinestyle{markdownstyle}{
    basicstyle=\ttfamily\footnotesize,
    breaklines=true,
    moredelim=[is][\textbf]{**}{**},
    moredelim=[is][\textit]{*}{*},
    moredelim=[is][\textcolor{blue}]{`}{`},
    frame=single,
    backgroundcolor=\color{gray!10},
}

\lstnewenvironment{markdown}{
    \lstset{style=markdownstyle}
}{}
```

Now, whenever you want to write notes, you can put them in "markdown" environment.

```latex
\begin{markdown}
Significance of research and prior work

Include
- Discussion on novelty compared to previous work
- Why is it a hard problem?
\end{markdown}
```

## Cosmetics

-   **Bold math symbols:** Use the command `\mathbf{}` to write bold faced symbols like matrix variables.

-   **Margins:** The easiest way is to add `\usepackage[margin=0.5in]{geometry}` in the preamble.

-   **Outer quotes:** Latex doesn't understand " as outer quotes. By default, you have to use \`\`. Here is a way out.

``` latex
\usepackage [autostyle, english = american]{csquotes}
\MakeOuterQuote{"}
```

-   **Some handy commands:** `\hfill, \vfill, \hskip, \vskip, \hspace, \vspace`.
    Just Google to know their usage.
    They're needed for extra spaces here and there in Latex documents.

-   **Horizontal Line:** `\hrulefill` for all non-tabular environments.

## Images

-   **Inserting Images:** Use \usepackage{graphicx,graphics} in preamble. Then, add image with the following code block.

``` latex
\begin{figure}
  \centering
    \includegraphics[width=5in]{example.png}
    \caption{An example of fitting \texttt{GP} model in 1-d function with seven data points.}
    \label{fig:example}
\end{figure}
```

## Tables

-   **Inserting Table:** Use [Table Generator](https://www.tablesgenerator.com) online.
    Create the schema and then fill in the content.

-   [Resize](https://tex.stackexchange.com/a/10864/159263) Latex Tables to Column-width or Text-width using `resizebox`:

    ```latex
    \usepackage{graphics}
    % ...

    \begin{table}
    \centering
    \resizebox{\columnwidth}{!}{%
    \begin{tabular}{r|lll}
    \multicolumn{1}{r}{}
    & \multicolumn{1}{l}{Heading 1}
    & \multicolumn{1}{l}{Heading 2}
    & \multicolumn{1}{l}{Heading 3} \\ \cline{2-4}
    Row 1 & Cell 1,1 & Cell 1,2 & Cell 1,3 \\
    Row 2 & Cell 2,1 & Cell 2,2 & Cell 2,3
    \end{tabular}%
    }
    \end{table}
    ```

## Exact Math Symbols

-   **argmin and argmax:** Use this in preamble:

``` latex
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
```

Then, `\underset{x} \argmax f(x)` or `\underset{x} \argmax f(x)`.
This might not be very right according to this thread, but okay -- it serves the purpose.
If you find something better, tell me.

-   **Sum (Sigma):** `\sum_{i = 1}^{n} x_n`

-   **Integral:** `\int_a^b f(x) \di x`

-   **Other math symbols:** [Overleaf](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols) and [Oeis Wiki](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols).

-   **Tab:** The simple tab (horizontal space) can be worked with `\quad`.

-   **Drawing any symbol:** It is difficult to find the appropriate symbol every time, so use [Detexify](http://detexify.kirelabs.org/classify.html) to identify what you need.

-   Writing algorithms in LaTeX.
    Use `algorithm` and `algorithmic`.
    See [this article](https://www.math-linux.com/latex-26/faq/latex-faq/article/how-to-write-algorithm-and-pseudocode-in-latex-usepackage-algorithm-usepackage-algorithmic) for quick review.

## Typesetting *Exactly*

-   To place pictures exactly in a slide, use tikz package. Exact coordinates by cm:

``` latex
\begin{tikzpicture}[remember picture,overlay]
%% (x coord, y coord) -> (0 cm, 6.5 cm)
  \node[anchor=south west,inner sep=0pt] at ($(current page.south west)+(0cm,6.5cm)$) {
     {picture.png}
  };
\end{tikzpicture}
```

The best part is that it also works for exact text placements.

## Referencing and Cross-referencing

-   **Bibliography and References:** Understand that in most academic writings they are different and Latex considers references as default. To add them, add following lines at the end of file, just before `\end{document}`.

``` latex
    \bibliographystyle{apalike}
    \bibliography{bibfile}
```

Don't forget to add `\usepackage{natbib}` in the preamble.
Note that bibfile.bib contains all bibliographies.
If you can't get the BibTeX citations right, use Google Scholar.

-   **Citations Generator:** Use this tool online to generate citations: <https://truben.no/latex/bibtex/>.

## Meta

-   **New Commands:** Outline format is `\newcommand{newname}{definition}`.
    See [this](https://www.overleaf.com/learn/latex/Commands) and [this](https://en.wikibooks.org/wiki/LaTeX/Macros#New_commands) for more details.

-   **Style File (`.sty`):** Basically, they're instructions that can be used to redefine the preexisting values in the document.
    See my Github for two examples that I've created - one for homework assignments and other for IIM Indore's official presentation.

## Templates

-   [Overleaf Gallery](https://www.overleaf.com/gallery/) is the best.
    Otherwise, you can find some repositories on Google.

-   [**By Me**](https://www.harsh17.in/latex-templates/)**:** If you are searching for reports or presentations, or are an IIM Indore student looking for presentations, check my templates.
