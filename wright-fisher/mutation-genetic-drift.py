# packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse

# global variables
pop_size = 100
seq_length = 10
alphabet = ['A', 'T', 'G', 'C']
mutation_rate = 0.002 # per gen per individual per site
generations = 200

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
    haplotypes = pop.keys() 
    frequencies = [x/float(pop_size) for x in pop.values()]
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
    haplotypes = pop.keys() 
    frequencies = [x/float(pop_size) for x in pop.values()]
    return list(np.random.multinomial(pop_size, frequencies))

def offspring_step():
    counts = get_offspring_counts()
    for (haplotype, count) in zip(pop.keys(), counts):
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

# plotting
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

def stacked_trajectory_plot():
	colors = ["#781C86", "#571EA2", "#462EB9", "#3F47C9", "#3F63CF", "#447CCD", "#4C90C0", "#56A0AE", "#63AC9A", "#72B485", "#83BA70", "#96BD60", "#AABD52", "#BDBB48", "#CEB541", "#DCAB3C", "#E49938", "#E68133", "#E4632E", "#DF4327", "#DB2122"]
	mpl.rcParams['font.size']=18
	plt.figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
	haplotypes = get_all_haplotypes()
	trajectories = [get_trajectory(haplotype) for haplotype in haplotypes]
	plt.stackplot(range(generations), trajectories, colors=colors)
	plt.ylim(0, 1)
	plt.ylabel("frequency")
	plt.xlabel("generation")
	plt.show()

if __name__=="__main__":
	parser = argparse.ArgumentParser(description = "run wright-fisher simulation with mutation and genetic drift")
	parser.add_argument('--pop_size', type = int, default = 100.0, help = "population size")
	parser.add_argument('--mutation_rate', type = float, default = 0.002, help = "mutation rate")
	parser.add_argument('--seq_length', type = int, default = 10, help = "sequence length")
	parser.add_argument('--generations', type = int, default = 200, help = "generations")	
	
	params = parser.parse_args()	
	pop_size = params.pop_size
	mutation_rate = params.mutation_rate
	seq_length = params.seq_length
	generations = params.generations		
	
	simulate()
	stacked_trajectory_plot()
	