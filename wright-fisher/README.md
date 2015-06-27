# Wright-Fisher population dynamics

### Wright-Fisher model

There are *N* individuals in the population. Every generation, each individual has a Poisson number of offspring (looking forwards in time), or picks one random parent individual (looking backwards time). Generations are discrete and non-overlapping.

![](figures/wright-fisher.png)

 * [Visualization of Wright-Fisher ancestry](http://bedford.io/projects/ancestry/)

### 1. Wright-Fisher model with mutation and genetic drift

 * [iPython notebook](mutation-genetic-drift.ipynb)
 * [Python script](mutation-genetic-drift.py)

Run script with:

	python mutation-genetic-drift.py --pop_size 100 --mutation_rate 0.002 --generations 200

 * [Visualization of Wright-Fisher haplotype dynamics](http://bedford.io/projects/haplotypes/)

### 2. Neutral expectations for population summary statistics

### 3. Wright-Fisher model with mutation, genetic drift and selection

 * [iPython notebook](mutation-genetic-drift-selection.ipynb)
