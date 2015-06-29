# Description

**Short course taught by [Sarah Cobey](http://cobeylab.uchicago.edu/) and [Trevor Bedford](http://bedford.io/) for [SISMID 2015](https://depts.washington.edu/sismid/general.html).**

This module provides an introduction to modeling antigenically diverse pathogen populations. The first part of the course will introduce multistrain compartmental models and potential mechanisms of competition. These simple models will be contrasted with models with more complex assumptions (e.g., multiple forms of immunity and spatial structure). We will review how to statistically fit multistrain models to longitudinal data from individuals and time series data from populations. The second part of the course will show how, using the coalescent as a neutral expectation, evolutionary pressures can be quantified using sequence data. We will detail bioinformatic methods to build phylogenies, quantify selective pressures and estimate pathogen population structure. Methods to measure pathogen phenotypic similarity and antigenic evolution, such as antigenic cartography, will be introduced. Assumes material from Module 2 (Mathematical Models of Infectious Diseases). Material from Module 14 (Evolutionary Dynamics and Molecular Epidemiology of Viruses) would be helpful, but not required.

# Outline

## Day 1: Competitive dynamics

### [Introduction to immune-mediated competition](competition/) 

* The dangers of intuition
* The biological basis of antigenic diversity: innate, cellular, and humoral responses
* Antigenically variable pathogens

### [Mechanistic multistrain models](models/)
* Statistical, compartmental, and agent-based models
* The many forms of competition
* Analytic solutions
* Numerical integration
* *Exercise 1: Simulate from a mechanistic model with independent and competing strains. Create a bifurcation diagram, varying the strength of competition.*

### [Fitting mechanistic models](fitting/)
* Deterministic skeletons
* Nonlinear least squared and maximum likelihood with population data
* *Exercise 2: Inference of a SIR model*
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

### [Flu and its evolution](flu/)

### [Wright-Fisher Dynamics](wright-fisher/)

* Introduction to Wright-Fisher model
* Wright-Fisher with mutation and genetic drift
* *Exercise 1: Effects of mutation and population size on population dynamics*
* Neutral expectations for population summary statistics
* Wright-Fisher with mutation, genetic drift and selection
* *Exercise 2: Effects of positive and negative selection on population dynamics*
* Analysis of influenza sequence data

## Day 3: Immunity

### Serology (Trevor)

* Cartography
* Original antigenic sin

### B cells (Sarah)

 * ???