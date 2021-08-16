import numpy as np
import pandas as pd
from niapy.task import Task


def to_latex(df, filename=None, caption=None, label=None):
    return df.to_latex(buf=filename, bold_rows=True, column_format='llcccc', multirow=True, escape='', longtable=True,
                       label=label, caption=caption)


def run(algorithms, problems, runs=25, dim=2, max_iters=1000):
    # functions = ['$f_{{{}}}$'.format(i + 1) for i in range(len(problems))]
    iterables = [problems, ['Min', 'Max', 'Avg', 'Std']]
    index = pd.MultiIndex.from_product(iterables, names=['Fukcija', ''])
    columns = [algorithm.Name[1] for algorithm in algorithms]
    df = pd.DataFrame(np.zeros((len(problems) * len(algorithms), len(algorithms))), index=index, columns=columns)
    for problem in problems:
        for algorithm in algorithms:
            fitness = []
            for i in range(runs):
                task = Task(problem, dimension=dim, max_iters=max_iters)
                _, best_fitness = algorithm.run(task)
                fitness.append(best_fitness)
            df[algorithm.Name[1]][problem] = (np.min(fitness), np.max(fitness), np.mean(fitness), np.std(fitness))

    return df
