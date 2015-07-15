# Fitting mechanistic models

* [Slides](slides.html)

### Exercise

You saw earlier that depending on the parameters, you could expect annual, biennial, or more complex dynamics from two interacting strains--or from a single strain with seasonal forcing.
The differences in these dynamics and the uncertainties of our parameter estimates make it essential to fit models rather than rely on correlations and other (often incorrect) rules of thumb.

One of the most powerful methods for analyzing time series is a sequential Monte Carlo method, multiple iterated filtering for partial observed Markov Processes (MIF for POMP). 
It's powerful because it incorporates both process noise and sampling error. 
Links to tutorials on pomp are in the Additional Resources, and the developers (Ed Ionides and Aaron King) teach an entire SISMID course on the method.
Pomp is a good place to start, although it's still often difficult to use in practice--it's computationally intense, and multistrain models may not converge.

We'll practice fitting our model with a different, much simpler methods available in the [scipy.optimize](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html) package.



### Additional resources

#### Methods 
* Introductions to POMP (MIF): [Ionides et al. 2006](http://www.pnas.org/content/103/49/18438) [and 2011](http://projecteuclid.org/euclid.aos/1311600283), [Ionides Case Study: Polio in Wisconsin](http://dept.stat.lsa.umich.edu/~ionides/tutorials/polio/polio.html) and [Case Study: Dynamic Variation in Sexual Contact Rates](http://dept.stat.lsa.umich.edu/~ionides/tutorials/contacts/contacts.html), and the [pomp page](http://kingaa.github.io/pomp/)
* Various Monte Carlo tutorials:[The Clever Machine](https://theclevermachine.wordpress.com/2012/09/22/monte-carlo-approximations/)
* Particle MCMC: [Andrieu et al. 2010](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-9868.2009.00736.x/abstract;jsessionid=FBE7D26487E7F72D8935A257788DA2B3.f04t02)
* Approximate Bayesian Computation: [Toni et al. 2009](http://rsif.royalsocietypublishing.org/content/6/31/187)
* Probes: [Kendall et al. 1997](http://www.esajournals.org/doi/abs/10.1890/0012-9658%281999%29080%5B1789%3AWDPCAS%5D2.0.CO%3B2)
* Synthetic likelihood: [Wood 2010](http://www.nature.com/nature/journal/v466/n7310/full/nature09319.html)

#### Some fitted multistrain models
* Dengue
* ...