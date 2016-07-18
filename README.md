# Description

**Short course taught by [Sarah Cobey](http://cobeylab.uchicago.edu/) and [Trevor Bedford](http://bedford.io/) for [SISMID 2015](http://sismid.uw.edu).**

This module provides an introduction to modeling antigenically diverse pathogen populations. The first part of the course will introduce multistrain compartmental models and potential mechanisms of competition. These simple models will be contrasted with models with more complex assumptions (e.g., multiple forms of immunity and spatial structure). We will review how to statistically fit multistrain models to longitudinal data from individuals and time series data from populations. The second part of the course will show how, using the coalescent as a neutral expectation, evolutionary pressures can be quantified using sequence data. We will detail bioinformatic methods to build phylogenies, quantify selective pressures and estimate pathogen population structure. Methods to measure pathogen phenotypic similarity and antigenic evolution, such as antigenic cartography, will be introduced. Assumes material from Module 2 (Mathematical Models of Infectious Diseases). Material from Module 14 (Evolutionary Dynamics and Molecular Epidemiology of Viruses) would be helpful, but not required.

# Outline

## Day 1

### [Pathogen diversity](pathogens/)

* Antigenically (and otherwise) variable pathogens
* *Exercise: Assigning study groups and picking pathogens*

### [Immunity and Immune-mediated competition](immunity/) 

* The biological basis of antigenic diversity: innate, cellular, and humoral responses

### [Serology](serology/)

* Serological binding and neutralization data
* Antigenic cartography
* *Exercise: Antigenic map*
* Original antigenic sin
* *Exercise: Serological data for chosen pathogens*

### [Multistrain models](models/)

* Statistical, compartmental, and agent-based models
* The many forms of competition
* Analytic solutions
* Numerical integration
* *Exercise: Dynamics of a multistrain SIR system*

## Day 2

### [Timeseries analysis](timeseries/)

* Maximum likelihood
* *Exercise: Inference for a multistrain SIR model*
* Bayesian approaches
* When to trust a model
* Tips & tricks: insights from natural experiments
* State-space reconstruction
* *Exercise: Attractor reconstruction and convergent cross-mapping*
* *Exercise: Timeseries data for chosen pathogens*

### [The coalescent and phylogenetics](sequences/)

* Introduction to Kingman's coalescent
* Effective population size and demographic inference
* *Exercise: Skyline plots*
* Effects of selection on tree topology
* Introduction to phylogenetic inference
* *Exercise: Parsimony reconstruction*
* Maximum likelihood and Bayesian methods
* *Exercise: Bayes' rule*

### [Selection and wright-Fisher Dynamics](selection/)

* Introduction to Wright-Fisher model
* Wright-Fisher with mutation and genetic drift
* *Exercise: Effects of mutation and population size on population dynamics*
* Wright-Fisher with mutation, genetic drift and selection
* *Exercise: Effects of positive and negative selection on population dynamics*
* Tests of selection
* *Exercise: Genetic data for chosen pathogens*

### [Forecasting](forecasting/)

* TBD

## Day 3

### [Synthesis](synthesis/)

* Group presentations on specific pathogens

### [B cell selection and evolution](bcells/)

* VDJ recombination and somatic hypermutation
* Clonal dynamics and repertoire diversity
* Unsolved problems and vaccine design
