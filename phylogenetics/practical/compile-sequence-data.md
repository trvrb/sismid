## Compile sequence data

I started by downloading sequences of the HA segment of H3N2 influenza from the [Influenza Research Database](http://www.fludb.org) sampled after 1994.
I cleaned up these sequences to keep only strains with at least 900 bases and to keep strains with more antigenic data.
These strains are the same as was used in the [Integrating influenza antigenic dynamics with molecular evolution](http://bedford.io/papers/bedford-flux/) paper, except restricted to 1994 to 2011.
This left 244 sequences.
These sequences were tagged with inferred H3N2 antigenic cluster by [Charles Cheung](http://bedford.io/team/charles-cheung/) (more on antigenic inference and cartography tomorrow).
There were 8 total antigenic phenotypes in the dataset. 

BEAST accepts either [NEXUS](http://en.wikipedia.org/wiki/Nexus_file) or [FASTA](http://en.wikipedia.org/wiki/FASTA_format) format for sequence data.
Metadata about antigenic phenotype and date of sampling can be kept as separate tab-delimited files, however, I find it easier to incorporate metadata into sequence names, i.e. `A/Brazil/1742/2005|c6|2005` where pipes (`|`) are used to separate fields.

I then used [MUSCLE](http://www.drive5.com/muscle/) to align sequences and trimmed the ends of alignments to remove uncertain sites.
I've included the final aligned dataset as `data/H3N2.fasta`.

### Next section

* [Prepare BEAST analysis](prepare-beast-analysis.md)