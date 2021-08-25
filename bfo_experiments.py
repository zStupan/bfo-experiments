import multiprocessing as mp
import numpy as np
import pandas as pd
from niapy.task import Task
from niapy.algorithms.basic import (
    BacterialForagingOptimization,
    DifferentialEvolution,
    ParticleSwarmAlgorithm,
    BatAlgorithm,
)
from niapy.algorithms.basic.de import cross_rand1


def to_latex(df, filename=None, caption=None, label=None):
    return df.to_latex(buf=filename, bold_rows=True, column_format='llcccc', multirow=True, longtable=True,
                       label=label, caption=caption)


def run(algorithms, problems, runs=25, dim=10, max_iters=10000):
    functions = [problem[0] for problem in problems]
    iterables = [functions, ('Min', 'Max', 'Avg', 'Std')]
    index = pd.MultiIndex.from_product(iterables, names=['Function', ''])
    columns = [algorithm.Name[1] for algorithm in algorithms]
    df = pd.DataFrame(np.zeros((len(problems) * len(algorithms), len(algorithms))), index=index, columns=columns)
    for problem in problems:
        name, lb, ub = problem
        for algorithm in algorithms:
            fitness = []
            for i in range(runs):
                task = Task(name, lower=lb, upper=ub, dimension=dim, max_iters=max_iters)
                _, best_fitness = algorithm.run(task)
                fitness.append(best_fitness)
            df[algorithm.Name[1]][name] = (np.min(fitness), np.max(fitness), np.mean(fitness), np.std(fitness))
    df.to_pickle('results/{}d.pkl'.format(dim))
    to_latex(df, 'results/{}d.tex'.format(dim))


if __name__ == '__main__':
    problems = (
        ('sphere', -5.12, 5.12),
        ('rosenbrock', -2.048, 2.048),
        ('rastrigin', -5.12, 5.12),
        ('griewank', -600, 600),
        ('ackley', -32.768, 32.768),
        ('schwefel', -500, 500),
        ('alpine1', -10, 10),
        ('whitley', -10, 10),
        ('csendes', -1, 1),
        ('dixon_price', -10, 10),
    )

    de = DifferentialEvolution(population_size=100, strategy=cross_rand1, differential_weight=0.8,
                               crossover_probability=0.9, seed=12345)
    pso = ParticleSwarmAlgorithm(population_size=100, w=0.9, c1=0.5, c2=0.3, min_velocity=-1, max_velocity=1,
                                 seed=12345)
    ba = BatAlgorithm(population_size=100, seed=12345)
    bfo_10d = BacterialForagingOptimization(population_size=100, n_chemotactic=1000, n_reproduction=5, seed=12345)
    bfo_20d = BacterialForagingOptimization(population_size=100, n_chemotactic=2000, n_reproduction=5, seed=12345)
    bfo_30d = BacterialForagingOptimization(population_size=100, n_chemotactic=3000, n_reproduction=5, seed=12345)

    dims = [10, 20, 30]
    iters = [10000, 20000, 30000]
    algorithms = [(bfo_10d, de, pso, ba), (bfo_20d, de, pso, ba), (bfo_30d, de, pso, ba)]

    processes = [mp.Process(target=run, args=(algorithms[i], problems, 25, dims[i], iters[i])) for i in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
