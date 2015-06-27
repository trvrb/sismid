# Pathogen evolution, selection and immunity

Short course taught by [Sarah Cobey](http://cobeylab.uchicago.edu/) and [Trevor Bedford](http://bedford.io/) for [SISMID 2015](https://depts.washington.edu/sismid/general.html).

## Description
This module provides an introduction to modeling antigenically diverse pathogen populations.
The first part of the course will introduce multistrain compartmental models and potential mechanisms of competition.
These simple models will be contrasted with models with more complex assumptions (e.g., multiple forms of immunity and spatial structure).
We will review how to statistically fit multistrain models to longitudinal data from individuals and time series data from populations.
The second part of the course will show how, using the coalescent as a neutral expectation, evolutionary pressures can be quantified using sequence data.
We will detail bioinformatic methods to build phylogenies, quantify selective pressures and estimate pathogen population structure.
Methods to measure pathogen phenotypic similarity and antigenic evolution, such as antigenic cartography, will be introduced.
Assumes material from Module 2 (Mathematical Models of Infectious Diseases).
Material from Module 14 (Evolutionary Dynamics and Molecular Epidemiology of Viruses) would be helpful, but not required.

## Outline

## Day 1: Competitive dynamics

1. Strain dynamics are evolutionary dynamics
2. The dangers of intuition
  1. Problem: intrinsic nonlinearities, unknown model structure
  2. Misuse of correlations (especially when analyzing snapshots)
  3. Misuse of confounders (e.g., shared risks for two strains)
3. The biological basis of antigenic diversity
  1. Innate response
  2. Cellular response
  3. Humoral response
4. Antigenically varying pathogens
  1. Neutral antigenic variation
  2. Static types: Pneumococcus, pertussis, choleras, RSV?
  3. Evolving types: Influenza, HIV, malaria, enteroviruses
  4. Competition between different “species”
  5. Challenge: Heterogeneity in host response
5. Mechanistic models
  1. Compartment models (v. statistical or agent-based)
  2. History v. status-based approaches
  3. Coinfection, superinfection, “neutral null models”
  4. Strength, time scale, breadth
  5. Antigenic drift as loss of immunity
  6. Solving for equilibrium states
  7. When we need numerical integration
  8. *Lab 1: Simulate from a mechanistic model with independent and
competing strains. Create a bifurcation diagram, varying the strength of
competition.*
6. Fitting mechanistic models
  1. Fit to deterministic skeletons
  2. Likelihood with case (population) data
  3. *Lab 2: Inference of SIR model and/or longitudinal model with Stan*
  4. Likelihood with longitudinal models
  5. Epidemiological approach: GLMs
  6. Stan: HPV
  7. Probes and arbitrary metrics
  8. Pneumo as case example
  9. Insufficient approaches: wavelet analysis...
7. When do we trust a model? Issues fitting.
  1. Non-identifiability
  2. Problems with model structure and bias (He et al. 2011)
  3. Work from simulated data?
  4. *Lab 3: When to trust a model. Do we require prediction?*
8. Other tips & tricks: Insights from natural experiments
  1. Vaccination can reveal competition: pneumo, human papillomavirus Evolution/Immigration: Similar shifts in competition
  2. Influenza subtypes (and A v. B)
  3. Seasonal influenza (H3N2, H1N1, B)
9. Attractor reconstruction & “empirical dynamical modeling”
  1. State-space reconstruction, attractors, Takens theorem
  2. Convergent cross-mapping for causal inference
  3. Limitations: nonstationarity, correlated noise
  4. *Lab 4: Attractor reconstruction and convergent cross-mapping. Generate time series (from Lab 1 code), look at impact on convergent cross-mapping.*

## Day 2: Evolution and selection

1. [Wright-Fisher Dynamics](wright-fisher)
  1. Introduction to Wright-Fisher model
  2. Wright-Fisher with mutation and genetic drift
  3. *Exercise 1: Effects of mutation and population size on population dynamics*
  4. Neutral expectations for population summary statistics
  5. Wright-Fisher with mutation, genetic drift and selection
  6. *Exercise 2: Effects of positive and negative selection on population dynamics*
  7. Analysis of influenza sequence data

## Day 3: Modeling immunity
