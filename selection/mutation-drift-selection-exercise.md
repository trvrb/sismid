# Exercise: effects of positive and negative selection on population dynamics

Here, we'll keep *N* and *&mu;* fixed and keep *&theta;* = 2, but vary the fitness effects of mutations.

This exercise can be completed by running the supplied Python script [`mutation-drift-selection.py`](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-drift-selection.py). To run the script with default population size of 100, per-site per-gen mutation rate of 0.0001, 100 sites and 500 generations, but with one mutation in every 20 having a fitness effect of 1.1, input:

```
python mutation-drift-selection.py --fitness_effect 1.1 --fitness_chance 0.1 --generations 500
```

Again, you might try increasing `generations` to something greater than 500 to get a better feel for equilibrium divergence and diversity, say `--generations 2500`. In this case, it may be easier to not plot the haplotype trajectories, using `--summary`, like so:

```
python mutation-drift-selection.py --fitness_effect 1.1 --fitness_chance 0.1 --generations 2500 --summary
```

> (1) Let's start by examining constant negative selection. Set `--fitness_chance 1.0` and vary `fitness_effect` between 0.8 and 1.0. What happens to diversity, divergence and haplotype dynamics? 

> (2) Let's now examine constant positive selection. Set `--fitness_chance 1.0` and vary `fitness_effect` between 1.0 and 1.2. What happens to diversity, divergence and haplotype dynamics? Do alleles fix faster with positive selection?

> (3) What are the effects of occasional mutations of large selective effect? Set parameters `--fitness_chance 0.01` and `--fitness_effect 2.0`. What happens to diversity, divergence and haplotype dynamics? Can you see selective sweeps in action?
