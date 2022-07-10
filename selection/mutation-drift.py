"""
Simulate Wright-Fisher population dynamics
"""

import argparse
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

try:
    import itertools.izip as zip
except ImportError:
    import itertools

# global variables
pop_size = 200
seq_length = 100
alphabet = ['A', 'T', 'G', 'C']
mutation_rate = 0.000025 # per gen per individual per site
generations = 1000

# population
base_haplotype = ''.join(["A" for i in range(seq_length)])
pop = {}
pop[base_haplotype] = pop_size
history = []

# mutation
def get_mutation_count():
    mean = mutation_rate * pop_size * seq_length
    return np.random.poisson(mean)

def get_random_haplotype():
	haplotypes = list(pop.keys())
	frequencies = [x/float(pop_size) for x in pop.values()]
	total = sum(frequencies)
	frequencies = [x / total for x in frequencies]
	return np.random.choice(haplotypes, p=frequencies)

def get_mutant(haplotype):
    site = np.random.randint(seq_length)
    possible_mutations = list(alphabet)
    possible_mutations.remove(haplotype[site])
    mutation = np.random.choice(possible_mutations)
    new_haplotype = haplotype[:site] + mutation + haplotype[site+1:]
    return new_haplotype

def mutation_event():
    haplotype = get_random_haplotype()
    if pop[haplotype] > 1:
        pop[haplotype] -= 1
        new_haplotype = get_mutant(haplotype)
        if new_haplotype in pop:
            pop[new_haplotype] += 1
        else:
            pop[new_haplotype] = 1

def mutation_step():
    mutation_count = get_mutation_count()
    for i in range(mutation_count):
        mutation_event()

# genetic drift
def get_offspring_counts():
	haplotypes = list(pop.keys())
	frequencies = [x/float(pop_size) for x in pop.values()]
	total = sum(frequencies)
	frequencies = [x / total for x in frequencies]
	return list(np.random.multinomial(pop_size, frequencies))

def offspring_step():
    counts = get_offspring_counts()
    for (haplotype, count) in zip(list(pop.keys()), counts):
        if (count > 0):
            pop[haplotype] = count
        else:
            del pop[haplotype]

# simulate
def time_step():
    mutation_step()
    offspring_step()

def simulate():
    clone_pop = dict(pop)
    history.append(clone_pop)
    for i in range(generations):
        time_step()
        clone_pop = dict(pop)
        history.append(clone_pop)

# plot diversity
def get_distance(seq_a, seq_b):
    diffs = 0
    length = len(seq_a)
    assert len(seq_a) == len(seq_b)
    for chr_a, chr_b in zip(seq_a, seq_b):
        if chr_a != chr_b:
            diffs += 1
    return diffs / float(length)

def get_diversity(population):
    haplotypes = list(population.keys())
    haplotype_count = len(haplotypes)
    diversity = 0
    for i in range(haplotype_count):
        for j in range(haplotype_count):
            haplotype_a = haplotypes[i]
            haplotype_b = haplotypes[j]
            frequency_a = population[haplotype_a] / float(pop_size)
            frequency_b = population[haplotype_b] / float(pop_size)
            frequency_pair = frequency_a * frequency_b
            diversity += frequency_pair * get_distance(haplotype_a, haplotype_b)
    return diversity

def get_diversity_trajectory():
    trajectory = [get_diversity(generation) for generation in history]
    return trajectory

def diversity_plot(xlabel="generation"):
    mpl.rcParams['font.size']=14
    trajectory = get_diversity_trajectory()
    plt.plot(trajectory, "#447CCD")
    plt.ylabel("diversity")
    plt.xlabel(xlabel)

# plot divergence
def get_divergence(population):
    haplotypes = population.keys()
    divergence = 0
    for haplotype in haplotypes:
        frequency = population[haplotype] / float(pop_size)
        divergence += frequency * get_distance(base_haplotype, haplotype)
    return divergence

def get_divergence_trajectory():
    trajectory = [get_divergence(generation) for generation in history]
    return trajectory

def divergence_plot(xlabel="generation"):
    mpl.rcParams['font.size']=14
    trajectory = get_divergence_trajectory()
    plt.plot(trajectory, "#447CCD")
    plt.ylabel("divergence")
    plt.xlabel(xlabel)

# plot trajectories
def get_frequency(haplotype, generation):
    pop_at_generation = history[generation]
    if haplotype in pop_at_generation:
        return pop_at_generation[haplotype]/float(pop_size)
    else:
        return 0

def get_trajectory(haplotype):
    trajectory = [get_frequency(haplotype, gen) for gen in range(generations)]
    return trajectory

def get_all_haplotypes():
    haplotypes = set()
    for generation in history:
        for haplotype in generation:
            haplotypes.add(haplotype)
    return haplotypes

def stacked_trajectory_plot(xlabel="generation"):
	colors_lighter = ["#A567AF", "#8F69C1", "#8474D1", "#7F85DB", "#7F97DF", "#82A8DD", "#88B5D5", "#8FC0C9", "#97C8BC", "#A1CDAD", "#ACD1A0", "#B9D395", "#C6D38C", "#D3D285", "#DECE81", "#E8C77D", "#EDBB7A", "#EEAB77", "#ED9773", "#EA816F", "#E76B6B"]
	mpl.rcParams['font.size']=18
	haplotypes = get_all_haplotypes()
	trajectories = [get_trajectory(haplotype) for haplotype in haplotypes]
	plt.stackplot(range(generations), trajectories, colors=colors_lighter)
	plt.ylim(0, 1)
	plt.ylabel("frequency")
	plt.xlabel(xlabel)

# plot snp trajectories
def get_snp_frequency(site, generation):
    minor_allele_frequency = 0.0
    pop_at_generation = history[generation]
    for haplotype in pop_at_generation.keys():
        allele = haplotype[site]
        frequency = pop_at_generation[haplotype] / float(pop_size)
        if allele != "A":
            minor_allele_frequency += frequency
    return minor_allele_frequency

def get_snp_trajectory(site):
    trajectory = [get_snp_frequency(site, gen) for gen in range(generations)]
    return trajectory

def get_all_snps():
    snps = set()
    for generation in history:
        for haplotype in generation:
            for site in range(seq_length):
                if haplotype[site] != "A":
                    snps.add(site)
    return snps

def snp_trajectory_plot(xlabel="generation"):
	colors = ["#781C86", "#571EA2", "#462EB9", "#3F47C9", "#3F63CF", "#447CCD", "#4C90C0", "#56A0AE", "#63AC9A", "#72B485", "#83BA70", "#96BD60", "#AABD52", "#BDBB48", "#CEB541", "#DCAB3C", "#E49938", "#E68133", "#E4632E", "#DF4327", "#DB2122"]
	mpl.rcParams['font.size']=18
	snps = get_all_snps()
	trajectories = [get_snp_trajectory(snp) for snp in snps]
	data = []
	for trajectory, color in zip(trajectories, itertools.cycle(colors)):
		data.append(range(generations))
		data.append(trajectory)
		data.append(color)
	plt.plot(*data)
	plt.ylim(0, 1)
	plt.ylabel("frequency")
	plt.xlabel(xlabel)

if __name__=="__main__":
	parser = argparse.ArgumentParser(description = "run wright-fisher simulation with mutation and genetic drift")
	parser.add_argument('--pop_size', type = int, default = 200, help = "population size")
	parser.add_argument('--mutation_rate', type = float, default = 0.000025, help = "mutation rate")
	parser.add_argument('--seq_length', type = int, default = 100, help = "sequence length")
	parser.add_argument('--generations', type = int, default = 1000, help = "generations")
	parser.add_argument('--summary', action = "store_true", default = False, help = "don't plot trajectories")
	parser.add_argument('--output', type = str, default = "fig_mutation_drift.png", help = "file name for figure output")

	params = parser.parse_args()
	pop_size = params.pop_size
	mutation_rate = params.mutation_rate
	seq_length = params.seq_length
	generations = params.generations
	output = params.output

	simulate()

	plt.figure(num=None, figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')
	if params.summary:
		plt.subplot2grid((2,1), (0,0))
		diversity_plot()
		plt.subplot2grid((2,1), (1,0))
		divergence_plot()
	else:
		plt.subplot2grid((3,2), (0,0), colspan=2)
		stacked_trajectory_plot(xlabel="")
		plt.subplot2grid((3,2), (1,0), colspan=2)
		snp_trajectory_plot(xlabel="")
		plt.subplot2grid((3,2), (2,0))
		diversity_plot()
		plt.subplot2grid((3,2), (2,1))
		divergence_plot()
	plt.savefig(output, dpi=150)
