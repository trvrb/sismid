## Introduction

H3N2 influenza undergoes frequent antigenic drift in which a new variant emerges and takes over the viral population.
Here, we will investigate phylogenetic and coalescent patterns of variant emergence and spread.
This tutorial walks through how to use [BEAST](http://beast.bio.ed.ac.uk/) and associated software to infer spatiotemporal dynamics from viral sequence data.

## Required software

* [BEAST](http://beast.bio.ed.ac.uk/) is used to infer evolutionary dynamics from sequence data. Download [here](http://tree.bio.ed.ac.uk/software/beast/).
* [BEAGLE](http://beast.bio.ed.ac.uk/BEAGLE) is a helper library that allows faster and more advanced functions to be run in BEAST. For this practical, it is not necessary to install CUDA drivers (step 2 in the BEAGLE installation). Download [here](https://github.com/beagle-dev/beagle-lib).
* [Tracer](http://tree.bio.ed.ac.uk/software/tracer/) is used to analyze parameter estimates from BEAST.
* [FigTree](http://tree.bio.ed.ac.uk/software/figtree/) is used to analyze phylogeny estimates from BEAST.

## Contents

1. [Compile sequence data](data.md)
2. [Prepare BEAST analysis](beauti.md)
3. [Run BEAST analysis](beast.md)
4. [Examine MCMC output](tracer.md)
5. [Examine tree output](figtree.md)
6. [Analyze vaccine strain choice](vaccine.md)

### Next section

* [Compile sequence data](data.md)