Title: Reproducible Reporting
Author: Ingmar Visser
Date: 2014-10-30 12:00
Slug: reproducible-reporting

## Why reproducible reporting?

>You are running an experiment when a conference deadline comes along; you quickly put together an abstract with 'preliminary findings' showing this or that effect. When preparing the talk for the conference, typically months later, you find a different p-value, F-value, t-value or whatever your favorite statistic was; it may still be significant or as expected, but different regardless; this nags you.

>You are preparing a manuscript with multiple experiments, a dozen or so tables and figures and many statistical results such as t-tests, ANOVA's et cetera. During manuscript preparation you decide on using another exclusion criterion for your response time data as well as your participants, all for good reasons. Then, the new semester starts and you are overloaded with teaching duties, and you are only able to start working on your manuscript weeks later. Did you already update figure 5 with the new exclusion criteria? Did you already re-run the t-test on page 17 concerning the response times? 

Unfortunately, I myself and many others are familiar with such experiences of not being able to reproduce results. Here, reproducibility refers *not* to the aspect of experimental results being reproducible. Reproducibility of experimental results has been written about frequently (see [discussion here](http://osc.centerforopenscience.org/2014/08/07/talk-about-replication/)), and serious effort is now put into testing the reproducibility of common results (eg in the [reproducibililty project](https://osf.io/ezcuj/wiki/home/)), as well as improving standards when it comes to experimentation (eg by pre-registration, see [discussion here](http://osc.centerforopenscience.org/2014/02/27/data-trawling/)). Rather, this post focuses on reproducibility of preparing the data, statistical analyses, producing figures and tables, and reporting of results in a journal manuscript. 

During my own training as a psychologist, not much attention was given in the curriculum to standards of bookkeeping, lab-journals, and reporting of results. Standards that are in place focus on the stylistic aspects of reporting, such as that the F in reporting an F-value should be italicized, rather than upright. The APA reporting guidelines concern mostly matters of form and style, such as the exquisitely detailed guidelines for producing references. While such uniformity of manuscripts in form and style are highly relevant when it comes to printing material in journals, those guidelines have not much to say about the contents of what is reported and about how to maintain the reproducibility of analyses.  

## What is reproducible reporting? 

When it comes to reproducible reporting, the goal is to have a workflow from (raw) data files to (pre-)print manuscript in such a way that every step along the way is reproducible, by others, including your future self -- for example, by others who have an interest in the results for the purposes of replication or quality control. It may be useful to have someone particular in mind such as [Jelte Wicherts](http://wicherts.socsci.uva.nl/) or [Uri Simonsohn](http://opim.wharton.upenn.edu/~uws/), both famous for tracking down errors (and worse) in published research -- hence, the goal is to make your work, say, Wicherts-proof. Typically, there are at least three phases involved in (re-)producing reports from data: 

1. transforming raw data files to a format that admits statistical analysis

2. making figures and tables, and producing analytical results from the data

3. putting it all together into a report, either a journal manuscript, a presentation for a conference, or a website

To accomplish reproducibility in reporting, the following are important desiderata for our toolchain: 

1. **Scripting** Using a scripting language (as opposed a point-and-click interface) for the statistical analyses, such as [R](http://www.r-project.org/), has the important advantage that analyses can easily be reproduced using the script. Popular statistical analysis packages, such as SPSS, also admit of the possibility of saving scripts of analyses. However, it is not necessary to do so, and hence one can easily omit doing so as it is not the *standard* way of operating. 

2. **One tool instead of many** R (and possibly other similar statistical packages) can be used to perform *all* the analytical steps from reading raw data files to analysing data, and producing (camera-ready) figures and tables; again, this is a major advantage over using a combination of text-file editors (to reformat raw data), a spreadsheet program, to clean the raw data, SPSS or otherwise to do the analyses, and a graphical program to produce figures. 

3. **High quality output in multiple formats** A toolchain to produce scientific output should produce high quality output, preferably suitable for immediate publication; that is, it should produce camera-ready copy. It should also produce outputs in different formats, that is, analysis scripts and text should be re-usable to produce either journal manuscripts, web pages or conference presentations. Other important requirements are i) portability (anyone using your source, in plain text format, should be able to reproduce your manuscript, whether they are working on Mac, Linux, Windows or otherwise), ii) flexibility (seamless integration of references and production of the reference list, automatic table of contents, indexing), iii) scalability (the tool should work similarly for small journal manuscripts and multi-volume books), iv) the separation of form and content (scientific reporting should be concerned with content, formatting issues should be left to journals, website maintainers et cetera). 

4. **Maintain a single source** Possibly the most important requirement for reproducible reporting is that the three phases of getting from raw data to pre-print manuscript are kept in a single file; data preprocessing, data analysis, and the text making up a manuscript should be tightly coupled in a single place. A workflow that only comprises a single file and where analytical results are automatically inserted into the text of a manuscript prevents common errors such as forgetting to update tables and figures (did I update this figure with the new exclusion criteria or not?), and, most importantly, simply making typing errors in copying results (the latter is arguably quite a common source of errors and hard to detect, especially so when the results are in favour of your hypotheses). 

Fortunately, many tools are available these days that satisfy these requirements to help ensure reproducibility of each of the phases of reporting scientific results. In particular, data pre-processing and data analysis can be made reproducible using [R](http://www.r-project.org/), an open source script based statistics package, which currently has close to 6000 add-on packages to do analyses ranging from simple t-tests to multi-level irt models, and from analysing two-by-two tables to intricate Markov models for complex panel designs. 

As for the third requirement, high quality output, LaTeX is the tool of choice. LaTeX has been the de-facto standard for high-quality typesetting in the sciences since its inception in 1986 by [Leslie Lamport](http://en.wikipedia.org/wiki/Leslie_Lamport). LaTeX belongs to the family of [markup languages](http://en.wikipedia.org/wiki/Markup_language), together with HTML, Markdown, XML, et cetera; the key characteristic of markup languages is the separation of form and content. Writing in LaTeX means assigning semantic labels to parts of your text, such as *title*, *author*, *section*, et cetera. Rather than deciding that a *title* should be type-set in 12-point Times New Roman, as an author I just want to indicate what the title *is*. Journals, websites and other media can then decide what their preferred format is for *title*'s in their medium and use the source LaTeX file to produce say PDF, for a journal, or HTML, for a website, output. Separation of form and content is precisely the feature that allows this flexibility in output formats. 

The superior typographical quality of LaTeX produced output is nicely illustrated [here](http://www.zinktypografie.nl/latex.php?lang=en), showing improved hyphenation, spacing, standard use of ligatures and others. Besides typographical quality, portability, automatic indexing, producing tables of contents, citations and referencing, and scalability were built into the design of LaTeX. See [here](http://www.andy-roberts.net/writing/latex/benefits), for a -- balanced -- discussion of the benefits of LaTeX over other word-processors.

The real benefit of these tools -- R and LaTeX -- comes in when they are used in combination. Several tools are available to combine R with LaTeX in a single document and the main advantage of this combination is that all three phases scientific report production are combined in a single document, fulfilling the fourth requirement. In the following I provide some minor examples of using R/LaTeX. 


## How to get started with reproducible reporting?

The main tools required for combining statistical analyses in R with LaTeX are Sweave and knitr. Below are the main portals for getting the required -- free! open-source! -- software, as well as some references to appropriate introductory guides. 

1. Getting started with R: the [R home page](http://www.r-project.org/), for downloads of the program, add-on packages and manuals; as for the latter, [R for psychologists](http://cran.r-project.org/doc/contrib/Baron-rpsych.pdf), is particularly useful with worked examples of many standard analyses. 

2. Getting started with LaTeX: the [LaTeX-homepage](http://www.latex-project.org/) for downloads, introductory guides and much much more; here's a [cheat sheet](http://www.stdout.org/~winston/latex/latexsheet.pdf) that helps in avoiding having to read introductory material. 

3. Getting started with [Sweave](https://stat.ethz.ch/R-manual/R-devel/library/utils/doc/Sweave.pdf), or alternatively [knitr](http://yihui.name/knitr/); both provide minimal examples to produce reproducible reports. 

If using these programs through their command-line interfaces seems overwhelming to start with, [Rstudio](http://www.rstudio.com/) provides a nice graphical user interface for R, as well as having options to produce PDF's from Sweave and/or knitr files. 

Needless to say, [Google](http://google.com) is your friend for finding more examples, troubleshooting et cetera. 

### Minimal R, LaTeX and Sweave example

A minimal example of using R and LaTeX using Sweave can be downloaded here: [reproducible-reporting.zip](http://osc.centerforopenscience.org/static/reproducible-reporting.zip).

To get it working do the following:

1. Install Rstudio
2. Install LaTeX
3. Open the .Rnw file in Rstudio after unpacking and run Compile pdf

### Some Markdown examples

Similar to the combination of LaTeX, R in Sweave, [Markdown](http://en.wikipedia.org/wiki/Markdown) combines simple markup and R code to produce HTML pages as done in this blog. The examples below illustrate some of the possibilities. 

To get the flavour, start with loading some data and use 'head(sleep)' to see what's in it:
```{r}
data(sleep)
head(sleep)
```

This data gives the 'case' values for application of two types of drug and its influence on hours of sleep. The following plots the means and standard deviations of the two types of treatments:
```{r}
plot(extra~group,data=sleep)
```

This data set is the one used by Student to introduce his t-test, so it's only fitting to do such a test on these data here:
```{r}
t.test(extra~group,data=sleep,paired=TRUE)
```

---

There is much more to say about reproducibility in reporting and statistical analysis than a blog can contain. There are several recent books on the topic for further reading: 

Gandrud, C. (2013). Reproducible research with R and RStudio. CRC Press.

Stodden, V., Leisch, F., & Peng, R. D. (Eds.). (2014). Implementing Reproducible Research. CRC Press.

Xie, Yihui. Dynamic Documents with R and knitr. CRC Press, 2013.

... and an online course [here](https://www.coursera.org/course/repdata). 

There is a world to win in acceptance of reproducible research practices, and reproducible reporting should be part and parcel of that effort. Such acceptance not only requires investment on the side of scientists and authors but also on the side of journals, in that they should accept LaTeX/R formatted manuscripts. Many psychometrics and mathematical psychology journals do accept LaTeX, as well as Elsevier, who provide explicit instructions for [submitting manuscripts in LaTeX](http://www.elsevier.com/author-schemas/latex-instructions), and so does Frontiers, see [here](http://www.frontiersin.org/Journal/AuthorInfo/ManuscriptGuidelines.aspx). Change in journal policy can be brought about by (associate) editors: if you have such a position make sure that your journal subscribes to open-source, reproducible reporting standards as this will also help improve the standards of reviewing and eventually the journal itself. As a reviewer, one may request to see the data and analysis files to aid in judging adequacy of reported results. At least some jourals, such as the Journal of Statistical Software, require the source and analysis files to be part of every submission; in fact, JSS, accepts LaTeX submissions only, and this should become the standard throughout psychology and other social sciences as well. 



