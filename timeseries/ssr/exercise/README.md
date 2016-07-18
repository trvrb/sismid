# Exercise

In this exercise, we'll test the ability of convergent cross-mapping to infer interactions. 
With our code* (mostly by Ed Baskerville), this requires a few steps:

1. Prepare the inputs. Convert a csv file of the time series to a sqlite database using [`csv2sqlite.py`](https://github.com/trvrb/sismid/blob/master/ssr/exercise/csv2sqlite.py). The first column of the csv file must be time, and the second two are observations. The first row should be the column labels (starting with 'time'). The sqlite database can be generated with `csv2sqlite.py input.csv input.sqlite time_series`. (The last argument creates a table called 'time_series' in the database.)

2. Run CCM on the inputs using [`ccm.py`](https://github.com/trvrb/sismid/blob/master/ssr/exercise/ccm.py), specifying the embedding dimension (`E`), lag (`t`), library lengths at which to calculate the correlation (`L`), the number of replicates per library length (`R`), the columns to use (`C`), the causality tests to run (`V`), the input databases and relevant table, and the output database. Example: `
ccm.py --n-cores 4 -E 4 -t 1 -L "5:50:5" -R 100 -C "x,y" -V "x:y,y:x" input.sqlite time_series output.sqlite`. Note that we're not trying to identify the best embedding dimension or lag at this point, although this is an important step in state-space reconstruction. For now, estimate reasonable values for `E` and `t`.

3. Plot the results using [`plot_rhos.py`](https://github.com/trvrb/sismid/blob/master/ssr/exercise/plot_rhos.py). Specify the database with the CCM results and the name of the file where the plot will be saved, e.g., `plot_rhos.py input_db.sqlite outputfile.png`.

As a test, run CCM on prepared inputs with:

```
python ccm.py --n-cores 4 -E 4 -t 1 -L "10:50:10" -R 100 -C "measles,chickenpox" -V "measles:chickenpox,chickenpox:measles" measles_chickenpox.sqlite time_series output.sqlite
```

And then visualize the results with:

```
python plot_rhos.py output.sqlite output.png
```

Several of the pathogens below, which we saw in the morning, are reputed to interact ([Rohani et al. 2003](http://www.ncbi.nlm.nih.gov/pubmed/12712203), [Mina et al. 2015](http://www.sciencemag.org/content/348/6235/694)).

![](../images/seattle_ts.png)

What happens when we run CCM on them? We might obtain something like this:

![](../images/chickenpox_measles.png)

What should we make of these trends? Let's work with simulated time series to get a better grasp of the  method.

> (1) Start with perfect and abundant observations of a deterministic system. Generate time series using the code from the first exercise. First simulate strains that are not interacting, and then simulate strains that are. When you run CCM, what do you obtain in each case? What happens if you remove seasonal forcing?

> (2) Now let's assume we have observations that contain a little bit of measurement error. Add white noise to these time series--you choose the strength. Before examining the results, think about how observation error should affect the correlations.

> (3) Now let's analyze a system that is perfectly observed but contains some process error in the transmission term. We can simulate stochastic differential equations by using the Euler method with process noise, i.e., the [Euler-Maruyama method](https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method). Add some process noise to the transmission rate. How does process noise affect inference?

> (4) Finally, let's assume our system is deterministic but starts away from equilibrium. 
(We might also ask what happens if one of the parameters is nonstationary.) How does this change affect the results?

> (Optional) See how changing the embedding dimension and lag affect your results.

> (Optional) Reconstruct some of the trajectories in state-space.

\* Unfortunately, this exercise requires the Anaconda distribution of Python 2.7.x to run (type `$ python --version` to see if you have it). We'll be working through this mostly as a class.