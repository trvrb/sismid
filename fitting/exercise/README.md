### Exercise

You saw earlier that depending on the parameters, you could expect annual, biennial, or more complex dynamics from two interacting strains--or from a single strain with seasonal forcing.
The differences in these dynamics and the uncertainties of our parameter estimates make it essential to fit models rather than rely on correlations and other (often incorrect) rules of thumb.

One of the most powerful methods for analyzing time series is a [sequential Monte Carlo](https://en.wikipedia.org/wiki/Particle_filter) (a.k.a. particle filtering) method, multiple iterated filtering for partial observed Markov Processes (MIF for [POMP](http://kingaa.github.io/pomp/)). 
It's powerful because it incorporates both process noise and sampling error. 
Links to tutorials on pomp are in the Additional Resources, and the developers (Ed Ionides and Aaron King) teach an entire SISMID course on the method, which this brief exercise won't replace!
Pomp is one of the best methods for fitting stochastic nonlinear models, although it's still often difficult to use in practice--it's computationally intense, and complex models may not converge in the time scale we care about.

Instead, we'll briefly practice fitting our model using a simple error function (instead of calculating likelihoods) and simple optimization routines for minimizing the error.
The main motivation for these choices is to give you a sense in a short time period of where optimizers can get stuck, and which parameters and dynamical regimes are most challenging to fit.
These methods are available in the [scipy.optimize](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html) package.
Once you understand their performance, it might be fun to try to improve on the fits to the same data set using pomp or other methods on your own.

For this exercise, we'll initially fit by minimizing squared differences using a [Nelder-Mead simplex search](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method).
Nelder-Mead is a "derivative-free" method that picks *n*+1 parameter combinations to form the vertices of a simplex, evaluates the error (or likelihood) at each point, and updates the worst-scoring point. The description below, directly from [Bolker 2007](http://ms.mcmaster.ca/~bolker/emdbook/)), describes the simplex's subsequent movement:

- attempt to move in the best direction by reflecting the worst point in the simplex through the opposite face;
- if the fit at the new point is better than the best other point in the simplex, double the length of the jump in that direction;
- if this jump was bad -- the height at the new point is worse than the second-worst point in the simplex --then try a point that's only half as far out as the initial try;
- if this second try, closer to the original, is also bad, then contract the simplex around the current best  point.

Most fitting methods in use are more complex, efficient, and flexible than the Nelder-Mead simplex. [See it in action.](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method#/media/File:Nelder_Mead2.gif)

> (1) Referencing your bifurcation diagrams, pick parameters in an area associated with stable dynamics: moving a little to the left or the right of each parameter doesn't appear to change dynamics too much. (Of course, because we've considered only a few "slices" by varying one parameter at a time, we can't be really sure how stable each area is yet.) Update the parameters in [`fitting.py`](https://github.com/trvrb/sismid/blob/master/fitting/exercise/fitting.py) with these values, and generate sample observations. Now assume we don't know the true value of one of the parameters (ideally one you have examined in a bifurcation diagram). Guess that its true value is 10-20% higher or lower than its actual value, and try to fit.  

> (2) Now try again, starting from a slightly different location.

> (3) If your fits have been pretty good so far, start from a very different point, ideally one corresponding to different dynamics. 

> (4) Assume you have incorrectly estimated the duration of infection, but you do not know you've made a mistake. Change its value in `error_function`, but do not fit it. Repeat a successful optimization from step 1. How are your results affected?

> (5) Try fitting two parameters simultaneously.

> (Optional) Change the error function so that you the maximize the likelihood (i.e., minimize the negative log-likelihood).


