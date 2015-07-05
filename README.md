# Description

**Short course taught by [Sarah Cobey](http://cobeylab.uchicago.edu/) and [Trevor Bedford](http://bedford.io/) for [SISMID 2015](http://sismid.uw.edu).**

This module provides an introduction to modeling antigenically diverse pathogen populations. The first part of the course will introduce multistrain compartmental models and potential mechanisms of competition. These simple models will be contrasted with models with more complex assumptions (e.g., multiple forms of immunity and spatial structure). We will review how to statistically fit multistrain models to longitudinal data from individuals and time series data from populations. The second part of the course will show how, using the coalescent as a neutral expectation, evolutionary pressures can be quantified using sequence data. We will detail bioinformatic methods to build phylogenies, quantify selective pressures and estimate pathogen population structure. Methods to measure pathogen phenotypic similarity and antigenic evolution, such as antigenic cartography, will be introduced. Assumes material from Module 2 (Mathematical Models of Infectious Diseases). Material from Module 14 (Evolutionary Dynamics and Molecular Epidemiology of Viruses) would be helpful, but not required.

# Outline

## Day 1: Competitive dynamics

### [Immune-mediated competition](competition/) 

* The dangers of intuition
* The biological basis of antigenic diversity: innate, cellular, and humoral responses
* Antigenically variable pathogens

### [Multistrain models](models/)
* Statistical, compartmental, and agent-based models
* The many forms of competition
* Analytic solutions
* Numerical integration
* *Exercise 1: Analyzing the dynamics of a multistrain SIR system.*

### [Fitting mechanistic models](fitting/)
* Deterministic skeletons
* Nonlinear least squared and maximum likelihood with population data
* *Exercise 2: Inference for a multistrain SIR model*
* GLMs with longitudinal data
* MCMC with Stan: HPV as a case study
* Probes and arbitrary metrics
* *Exercise 3: When to trust a model.*
* Tips & tricks: insights from natural experiments

### [State-space reconstruction](ssr/)
* State space and attractors
* Prediction
* Takens theorem
* Convergent cross-mapping for causal inference
* *Exercise 4: Attractor reconstruction and convergent cross-mapping.*

## Day 2: Evolution and selection

### [Influenza](flu/)

* Introduction to influenza and its evolution

### [The coalescent](coalescent/)

* Introduction to Kingman's coalescent
* Effective population size and demographic inference
* *Exercise: Skyline plots*
* Effects of selection on tree topology

### [Phylogenetics](phylogenetics/)

* Introduction to phylogenetic inference
* *Exercise: Parsimony reconstruction*
* Maximum likelihood and Bayesian methods
* *Exercise: Bayes' rule*
* Introduction to BEAST and coalescent inference
* *Exercise: BEAST practical*
* Covers molecular clock, demographic models and discrete trait estimation

### [Wright-Fisher Dynamics](wright-fisher/)

* Introduction to Wright-Fisher model
* Wright-Fisher with mutation and genetic drift
* *Exercise: Effects of mutation and population size on population dynamics*
* Neutral expectations for population summary statistics
* Wright-Fisher with mutation, genetic drift and selection
* *Exercise: Effects of positive and negative selection on population dynamics*
* Analysis of influenza sequence data

## Day 3: Immunity

### [Serology](serology/)

* Serological binding and neutralization data
* Antigenic cartography
* *Exercise: Antigenic map*
* Original antigenic sin

### B cells (Sarah)

 * ???