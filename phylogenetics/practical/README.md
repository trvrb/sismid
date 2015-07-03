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

1. [Compile sequence data](compile-sequence-data.md)
2. [Prepare a skyline analysis](prepare-a-skyline-analysis.md)
3. [Run the skyline analysis](run-the-skyline-analysis.md)
4. [Examine the skyline output](examine-the-skyline-output.md)
5. [Examine the skyline tree](examine-the-skyline-tree.md)
6. [Prepare a logistic growth analysis](prepare-a-logistic-growth-analysis.md)
7. [Run the logistic growth analysis](run-the-logistic-growth-analysis.md)
8. [Examine the logistic growth output](examine-the-logistic-growth-output.md)
9. [Prepare a phylogeographic analysis](prepare-a-phylogeographic-analysis.md)
10. [Run the phylogeographic analysis](run-the-phylogeographic-analysis.md)
11. [Examine the phylogeographic output](examine-the-phylogeographic-output.md)

### Next section

* [Compile sequence data](compile-sequence-data.md)