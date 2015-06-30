# Wright-Fisher population dynamics

### Wright-Fisher model

![](images/wright_fisher.png)

There are *N* individuals in the population. Every generation, each individual has a Poisson number of offspring (looking forwards in time), or picks one random parent individual (looking backwards time). Generations are discrete and non-overlapping.

 * [Visualization of Wright-Fisher ancestry](http://bedford.io/projects/ancestry/)

### Wright-Fisher model with mutation and genetic drift

 * [iPython notebook](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-genetic-drift.ipynb)
 * [Python script](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-genetic-drift.py)

Run script with:

	python mutation-genetic-drift.py --pop_size 100 --mutation_rate 0.002 --generations 200

 * [Visualization of Wright-Fisher haplotype dynamics](http://bedford.io/projects/haplotypes/)

### [Neutral expectations for population summary statistics](summary-statistics.md)

### Wright-Fisher model with mutation, genetic drift and selection

 * [iPython notebook](https://github.com/trvrb/sismid/blob/master/wright-fisher/mutation-genetic-drift-selection.ipynb)
