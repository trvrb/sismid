# Wright-Fisher population dynamics

### Wright-Fisher model

![](images/wright_fisher.png)

There are *N* individuals in the population. Every generation, each individual has a Poisson number of offspring (looking forwards in time), or picks one random parent individual (looking backwards time). Generations are discrete and non-overlapping.

 * [Visualization of Wright-Fisher ancestry](http://bedford.io/projects/ancestry/)

### Wright-Fisher model with mutation and genetic drift

 * [iPython notebook](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-genetic-drift.ipynb)

 * [Visualization of Wright-Fisher haplotype dynamics](http://bedford.io/projects/haplotypes/)

### *Exercise: effects of population size and mutation rate on observed haplotype dynamics*

We'll go into this further in the next section, but a very important parameter is *&theta;*, which is equal to 2<i>N&mu;</i>, where *N* is equal to the population size and *&mu;* is equal to mutations per generation. If there are 100 sites and a per-site per-gen mutation rate of 0.0001, then *&mu;* = 0.01. If there are 50 individuals in the population, then *&theta;* = 2<i>N&mu;</i> = 1.

This exercise can be completed by running the supplied Python script [`mutation-genetic-drift.py`](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-genetic-drift.py). To run the script with population size of 50, per-site per-gen mutation rate of 0.0001, 100 sites and 500 generations, input:

```
python mutation-genetic-drift.py --pop_size 50 --mutation_rate 0.0001 --seq_length 100 --generations 500
```

Again, these parameters give *&theta;* = 1.

1. **Keeping the above parameters as baseline, adjust population size up and down to vary *&theta;* between ~0.2 and ~5. What happens to diversity, divergence and haplotype dynamics?**
2. **Keeping the above parameters as baseline, adjust mutation rate up and down to vary *&theta;* between ~0.2 and ~5. Again, what happens to diversity, divergence and haplotype dynamics?**

You might try increasing `generations` to something greater than 500 to get a better feel for equilibrium divergence and diversity, say `--generations 2500`. In this case, it may be easier to not plot the haplotype trajectories. This can be done with `--no_hap`, like so:

```
python mutation-genetic-drift.py --pop_size 50 --mutation_rate 0.0001 --seq_length 100 --generations 2500 --no_hap
```

### Neutral expectations for population summary statistics

* [Notes](summary-statistics.md)

### Wright-Fisher model with mutation, genetic drift and selection

 * [iPython notebook](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-genetic-drift-selection.ipynb)
