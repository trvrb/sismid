# Exercise: effects of population size and mutation rate on population dynamics

We'll go into this further in the next section, but a very important parameter is *&theta;*, which is equal to 2<i>N&mu;</i>, where *N* is equal to the population size and *&mu;* is equal to mutations per generation. If there are 100 sites and a per-site per-gen mutation rate of 0.000025, then *&mu;* = 0.0025. If there are 200 individuals in the population, then *&theta;* = 2<i>N&mu;</i> = 1.

This exercise can be completed by running the supplied Python script [`mutation-drift.py`](mutation-drift.py). To run the script with population size of 200, per-site per-gen mutation rate of 0.000025, 100 sites and 1000 generations, input:

```
python mutation-drift.py --pop_size 200 --mutation_rate 0.000025
```

This will output the file `fig_mutation_drift.png` that can be examined locally. Again, these parameters give *&theta;* = 1.

> (1) Keeping the above parameters as baseline, adjust population size up and down to vary *&theta;* between ~0.2 and ~5. What happens to diversity, divergence and haplotype dynamics?

> (2) Keeping the above parameters as baseline, adjust mutation rate up and down to vary *&theta;* between ~0.2 and ~5. Again, what happens to diversity, divergence and haplotype dynamics?

> (3) Adjust *N* and *&mu;* up and down, while keeping *&theta;* = 1, to explore high *N* / low *&mu;* and low  *N* / high *&mu;* scenarios. What happens to diversity, divergence and haplotype dynamics?

You might try increasing `generations` to something greater than 1000 to get a better feel for equilibrium divergence and diversity, say `--generations 2500`. In this case, it may be easier to not plot the haplotype trajectories. This can be done with `--summary`, like so:

```
python mutation-drift.py --pop_size 200 --mutation_rate 0.000025 --generations 2500 --summary
```

--------------------------------------------

Alternatively, if you don't have a working local Python install, you can run the `mutation-drift.ipynb` notebook or the `mutation-drift.py` script online with MyBinder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/trvrb/sismid/HEAD)
