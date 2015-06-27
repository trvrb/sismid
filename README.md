### Short course taught by [Sarah Cobey](http://cobeylab.uchicago.edu/) and [Trevor Bedford](http://bedford.io/) for [SISMID 2015](https://depts.washington.edu/sismid/general.html).

# Description

This module provides an introduction to modeling antigenically diverse pathogen populations. The first part of the course will introduce multistrain compartmental models and potential mechanisms of competition. These simple models will be contrasted with models with more complex assumptions (e.g., multiple forms of immunity and spatial structure). We will review how to statistically fit multistrain models to longitudinal data from individuals and time series data from populations. The second part of the course will show how, using the coalescent as a neutral expectation, evolutionary pressures can be quantified using sequence data. We will detail bioinformatic methods to build phylogenies, quantify selective pressures and estimate pathogen population structure. Methods to measure pathogen phenotypic similarity and antigenic evolution, such as antigenic cartography, will be introduced. Assumes material from Module 2 (Mathematical Models of Infectious Diseases). Material from Module 14 (Evolutionary Dynamics and Molecular Epidemiology of Viruses) would be helpful, but not required.

# Outline

## Day 1: Competitive dynamics

### Strain dynamics are evolutionary dynamics

### The dangers of intuition
* Problem: intrinsic nonlinearities, unknown model structure
* Misuse of correlations (especially when analyzing snapshots)
* Misuse of confounders (e.g., shared risks for two strains)

### The biological basis of antigenic diversity
* Innate response
* Cellular response
* Humoral response

### Antigenically varying pathogens
* Neutral antigenic variation
* Static types: Pneumococcus, pertussis, choleras, RSV?
* Evolving types: Influenza, HIV, malaria, enteroviruses
* Competition between different "species"
* Challenge: Heterogeneity in host response

### Mechanistic models
* Compartment models (v. statistical or agent-based)
* History v. status-based approaches
* Coinfection, superinfection, “neutral null models”
* Strength, time scale, breadth
* Antigenic drift as loss of immunity
* Solving for equilibrium states
* When we need numerical integration
* *Lab 1: Simulate from a mechanistic model with independent and competing strains. Create a bifurcation diagram, varying the strength of competition.*

### Fitting mechanistic models
* Fit to deterministic skeletons
* Likelihood with case (population) data
* *Lab 2: Inference of SIR model and/or longitudinal model with Stan*
* Likelihood with longitudinal models
* Epidemiological approach: GLMs
* Stan: HPV
* Probes and arbitrary metrics
* Pneumo as case example
* Insufficient approaches: wavelet analysis...
  
### When do we trust a model? Issues fitting.
* Non-identifiability
* Problems with model structure and bias (He et al. 2011)
* Work from simulated data?
* *Lab 3: When to trust a model. Do we require prediction?*

### Other tips & tricks: Insights from natural experiments
* Vaccination can reveal competition: pneumo, human papillomavirus Evolution/Immigration: Similar shifts in competition
* Influenza subtypes (and A v. B)
* Seasonal influenza (H3N2, H1N1, B)

### Attractor reconstruction & "empirical dynamical modeling"
* State-space reconstruction, attractors, Takens theorem
* Convergent cross-mapping for causal inference
* Limitations: nonstationarity, correlated noise
* *Lab 4: Attractor reconstruction and convergent cross-mapping. Generate time series (from Lab 1 code), look at impact on convergent cross-mapping.*

## Day 2: Evolution and selection

### [Wright-Fisher Dynamics](wright-fisher)

* Introduction to Wright-Fisher model
* Wright-Fisher with mutation and genetic drift
* *Exercise 1: Effects of mutation and population size on population dynamics*
* Neutral expectations for population summary statistics
* Wright-Fisher with mutation, genetic drift and selection
* *Exercise 2: Effects of positive and negative selection on population dynamics*
* Analysis of influenza sequence data

## Day 3: Immunity
