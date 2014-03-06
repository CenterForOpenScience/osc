Title: Confidence Intervals for Effect Sizes from Noncentral Distributions
Author: Russ Clay
Date: 2014-03-06 12:00
Slug: confidence intervals
Status: draft

<sup>(Thanks to Shauna Gordon-McKeon, Fred Hasselman, Daniël Lakens, Sean Mackinnon, and Sheila Miguez for their contributions and feedback to this post.)</sup>

_I recently took on the task of calculating a confidence interval around an effect size stemming from a noncentral statistical distribution (the F-distribution to be precise).  This was new to me, and as I am of the view that such statistical procedures would add value to the work being done in the social and behavioral sciences, but that they are not common in practice at the present time, potentially due to lack of awareness, I wanted to pass along some of the things that I found._  

In an effort to estimate the replicability of psychological science, an important first step is to determine the criteria for declaring a given replication attempt as successful.  Lacking clear consensus around this criteria, the OpenScience group determined that rather than settling on a single set of criteria by which the replicability of psychological research would be assessed, multiple methods would be employed, all which provide a measure of valuable insight regarding the reproducibility of published findings in psychology (OpenScience Collaboration, 2012).  One such method is to examine the confidence interval around the original target effect and to see if this confidence interval overlaps with the confidence interval from the replication effect.  However, estimating the confidence interval around many effects in social science research requires the use of  non-central probability distributions, and most mainstream statistical packages (e.g. SAS, SPSS) do not provide off the shelf capabilities for deriving confidence intervals from these distributions (Kelley, 2007).  

Most of us probably picture common statistical distributions such as the t-distribution, the F-distribution, and the χ2 distribution as being two dimensional, with the x-axis representing the value of the test statistic and the y-axis representing the probability of obtaining such a value.  When first learning to conduct these statistical tests, such visual representations likely provided a helpful way to convey the concept that more extreme values of the test statistic were less likely.  In the realm of null hypothesis statistical testing (NHST), this provides a tool for visualizing how extreme the test statistic would need to be before we would be willing to reject a null hypothesis.  However, it is important to remember that these distributions vary along a third parameter as well: the noncentrality parameter.  The distribution that we use to determine the cut-off points for rejecting a null hypothesis is a special, central case of the distribution when the noncentrality parameter is zero.  This special-case distribution gives the probabilities of test statistic values when the null hypothesis is true (i.e., when the population effect is zero).  As the noncentrality parameter changes (i.e., when we assume that an effect does exist), the shape of the distribution which defines the probabilities of obtaining various values of the parameter in our statistical tests changes as well.  The following figure (copied from the Wikipedia page for the noncentral t-distribution) might help provide a sense of how the shape of the t-distribution changes as the noncentrality parameter varies.  

<img src="/images/CIs.png" alt="non-central T distribution" align="center" style="padding-right: 20px;" width="360px" />  
<sup>Figure by <a href="http://en.wikipedia.org/wiki/File:Nc_student_t_pdf.svg">Skbkekas</a>, licensed <a href="http://creativecommons.org/licenses/by/3.0/deed.en">CC BY 3.0.</a></sup>

The first two plots (orange and purple) illustrate the different shapes of the distribution under the assumption that the true population parameter (the difference in means) is zero.  The value of v indicates the degrees of freedom used to determine the probabilities under the curve.  The difference between these first two curves stems from the fact that the purple curve has more degrees of freedom (a larger sample), and thus there will be a higher probability of observing values near the mean.  These distributions are central (and symmetrical), and as such, values of x that are equally higher or lower than the mean are equally probable.  The second two plots (blue and green) illustrate the shapes of the distribution under the assumption that the true population parameter is two.  Notice that both of these curves are positively skewed, and that this skewness is particularly pronounced in the blue curve as it is based on fewer degrees of freedom (smaller sample size).  The important thing to note is that for these plots, values of x that are equally higher or lower than the mean are NOT equally probable.  Observing a value of x = 4 under the assumption that the true value of x is two is considerably more probable than observing a value of x = 0.  Because of this, a confidence interval around an effect that is anything other than zero will be asymmetrical and will require a bit of work to calculate.  

Because the shape (and thus the degree of symmetry) of many statistical distributions depends on the size of the effect that is present in the population, we need a noncentrality parameter to aid in determining the shape of the distribution and the boundaries of any confidence interval of the population effect.  As mentioned previously, these complexities do not arise as often as we might expect in everyday research because when we use these distributions in the context of null-hypothesis statistical testing (NHST), we can assume a special, ‘centralized’ case of the distributions that occurs when the true population effect of interest is zero (the typical null hypothesis).  However, confidence intervals can provide different information than what can be obtained through NHST.  When testing a null hypothesis, what we glean from our statistics is the probability of obtaining the effect observed in our sample if the true population effect is zero.  The p-value represents this probability, and is derived from a probability curve with a noncentrality parameter of zero.  As mentioned above, these special cases of statistical distributions such as the t, F, and χ2 are ‘central’ distributions.  On the other hand, when we wish to construct a confidence interval of a population effect, we are no longer in the NHST world, and we no longer operate under the assumption of ‘no effect’.  In fact, when we build a confidence interval, we are not necessarily making assumptions at all about the existence or non-existence of an effect.  Instead, when we build a confidence interval, we want a range of values that is likely to contain the true population effect with some degree of confidence.  To be crystal clear, when we construct a 95% confidence interval around a test statistic, what we are saying is that if we repeatedly tested random samples of the same size from the target population under identical conditions, the true population parameter will be bounded by the 95% confidence interval derived from these samples 95% of the time.  

From a practical standpoint, a confidence interval can tell us everything that NHST can, and then some.  If the 95% confidence interval of a given effect contains the value of zero, then there is a good chance that there is a negligible effect in the relationship you are testing.  In this case, as a researcher, the conclusion that you would reach is conceptually similar to declaring that you are not willing to reject a null hypothesis of zero effect on the grounds that there is greater than a 5% chance that the effect is actually zero.  However, a confidence interval allows the researcher to say a bit more about the potential size of a population effect as well as the degree of variability that exists in it’s estimate, whereas NHST only permits the researcher to state, with a specified level of confidence, the likelihood that an effect exists at all.  

Why, then, is NHST the overwhelming choice of statisticians in the social sciences?  The likely answer has to do with the idea of non-centrality stated above.  When we build a confidence interval around an effect size, we generally do not build the confidence interval around an effect of zero.  Instead, we build the confidence interval around the effect that we find in our sample.  As such, we are unable to build the confidence interval using the symmetrical, special case instances of many of our statistical distributions.  We have to build it using an asymmetrical distribution that has a shape (a degree of non-centrality) that depends on the effect that we found in our sample.  This gets messy, complicated, and requires a lot of computation.  As such, the calculation of these confidence intervals was not practical until it became commonplace for researchers to have at their disposal the computational power available in modern computing systems.  However, research in the social sciences has been around much longer than your everyday, affordable, quad-core laptop, and because building confidence intervals around effects from non-central distributions was impractical for much of the history of the social sciences, these statistical techniques were not often taught, and their lack of use is likely to be an artifact of institutional history (Steiger & Fouladi, 1997).
All of this to say that in today’s world, researchers generally have more than enough computational power at their disposal to easily and efficiently construct a confidence interval around an effect from a non-central distribution.  The barriers to these statistical techniques have been largely removed, and as the value of the information obtained from a confidence interval exceeds the value of the information that can be obtained from NHST, it is useful to spread the word about resources that can help in the computation of confidence intervals around common effect size metrics in the social and behavioral sciences.  

One resource that I found to be particularly useful is the MBESS (Methods for the Behavioral, Educational, and Social Sciences) package for the [R statistical software platform](http://www.r-project.org/).  For those unfamiliar with R, it is a free, open-source statistical software package which can be run on Unix, Mac, and Windows platforms.  The standard R software contains basic statistics functionality, but also provides the capability for contributors to develop their own functionality (typically referred to as ‘packages’) which can be made available to the larger user community for download.   MBESS is one such package which provides ninety-seven different functions for statistical procedures that are readily applicable to statistical analysis techniques in the behavioral, educational, and social sciences.  Twenty-five of these functions involve the calculation of confidence intervals or confidence limits, mostly for statistics stemming from noncentral distributions.  

For example, I used the ci.pvaf (confidence interval of the proportion of variance accounted for) function from the MBESS package to obtain a 95% confidence interval around an η2 effect of 0.11 from a one-way between groups analysis of variance.  In order to do this, I only needed to supply the function with several relevant arguments:  

>	__F-value:__  This is the F-value from a fixed-effects ANOVA  
>	__df:__  The numerator and denominator degrees of freedom from the analysis  
>	__N:__  The sample size  
>	__Confidence Level:__  The confidence level coverage that you desire (i.e. 95%)  

No more information is required.  Based on this, the function can calculate the desired confidence interval around the effect. Here is a copy of the code that I entered and what was produced (with comments in italics to explain what is going on in each step):  

> __library(MBESS);__  

> _once you have installed the MBESS package, this command makes it available for your current session of R_  

> __ci.pvaf(F.value=4.97, df.1=2, df.2=81, N=84, conf.level=.95)__  

> _this uses the ci.pvaf function in the MBESS package to calculate the confidence interval.  I have given # the function an F-value (F.value) of 4.97, with 2 degrees of freedom between groups (df.1), and 81 # degrees of freedom within groups (df.2), a sample size (N) of 84, and have asked it to produce a 95% confidence interval (conf.level).  Executing the above command produces the following output:_  

> __$Lower.Limit.Proportion.of.Variance.Accounted.for__  
> __[1] 0.007611619__  

> __$Probability.Less.Lower.Limit__  
> __[1] 0.025__  

> __$Upper.Limit.Proportion.of.Variance.Accounted.for__  
> __[1] 0.2320935__  

> __$Probability.Greater.Upper.Limit__  
> __[1] 0.025__  

> __$Actual.Coverage__  
> __[1] 0.95__  

> _Thus, the 95% confidence interval around my η2 effect is __[0.01 - 0.23]__._  

Similar functions are available in the MBESS package for calculating confidence intervals around a contrast in a fixed-effects ANOVA, multiple correlation coefficient, squared multiple correlation coefficient, regression coefficient, reliability coefficient, RMSEA, standardized mean difference, signal-to-noise ratio, and χ2 parameters, among others.  

##### Additional Resources

* Fred Hasselman has created [a brief tutorial](http://osc.centerforopenscience.org/materials/using_R_to_compute_effect_size_CIs.html) for computing effect size confidence intervals using R.  

* For those more familiar with conducting statistics in an SPSS environment, Dr. Karl Wuensch at East Carolina University provides links to several SPSS programs on his Web Page.  [This program](http://core.ecu.edu/psyc/wuenschk/SPSS/SPSS-Programs.htm) is for calculating confidence intervals for a standardized mean difference (Cohen’s d).  

* In addition, I came across several publications that I found useful in providing background information regarding non-central distributions (a few of which are cited above).  I’m sure there are more, but I found these to be a good place to start:

> Cumming, G. (2006).  _How the noncentral t distribution got its hump._  Paper presented at the seventh International Conference on Teaching Statistics, Salvador, Bahia, Brazil.  

> Cumming, G. (2014).  _The new statistics: Why and how._  Psychological Science, 25, 7-29.  DOI: 10.1177/0956797613504966  

> Kelley, K. (2007).  _Confidence intervals for standardized effect sizes: Theory, application, and implementation._  Journal of Statistical Software, 20, 1-24.  

> Smithson, M. (2001). _Correct confidence intervals for various regression effect sizes and parameters: The importance of noncentral distributions in computing intervals._ Educational And Psychological Measurement, 61(4), 605-632. doi:10.1177/00131640121971392  

> Steiger, J. H., & Fouladi, R. T. (1997).  _Noncentrality interval estimation and the evaluation of statistical models._  In L. Harlow, S. > Mulaik, & J. Steiger (Eds.), What if there were no significance tests? (pp. 221-256).  Mahwah, NJ: Erlbaum.  

* There is also [thorough documentation of the MBESS package itself](http://cran.r-project.org/web/packages/MBESS/MBESS.pdf).

Hopefully others find this information as useful as I did!

