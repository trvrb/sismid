# Exercise: effects of positive and negative selection on population dynamics

Here, we'll keep *N* and *&mu;* fixed and keep *&theta;* = 1, but include a small fraction of selectively advantageous mutations.

This exercise can be completed by running the supplied Python script [`mutation-drift-selection.py`](mutation-drift-selection.py). To run the script with default population size of 200, per-site per-gen mutation rate of 0.000025, 100 sites and 1000 generations, but with a chance of 0.01 for a mutation to have a fitness effect of 1.5:

```
python mutation-drift-selection.py
```

Again, you might try increasing `generations` to something greater than 1000 to get a better feel for equilibrium divergence and diversity, say `--generations 2500`. In this case, it may be easier to not plot the haplotype trajectories, using `--summary`, like so:

```
python mutation-drift-selection.py --generations 2500 --summary
```

> (1) Can you recognize "selective sweeps" in these dynamics where a new advantage mutation appears and rapidly increases to fixation?

> (2) What do sweeps do to diversity and divergence relative to the neutral scenario?

--------------------------------------------

Alternatively, if you don't have a working local Python install, you can run the `mutation-drift-selection.ipynb` notebook or the `mutation-drift-selection.py` script online with MyBinder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/trvrb/sismid/HEAD)
