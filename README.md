# bfo-experiments

## Description

As a part of my bachelor's thesis, I extended the NiaPy microframework [1],
adding to it, the Bacterial Foraging Optimization algorithm as proposed by
K. M. Passino in 2002 [2]. This repository contains the various experiments I ran,
comparing the performance of BFO with other popular nature-inspired algorithms,
specifically Differential Evolution, Particle Swarm Optimization and the Bat Algorithm.

The details of the experiments are described in the jupyter notebook `bfo_experiments.ipynb`.
The code used to run the experiments is in the `bfo_experiments.py` module, which contains two
functions: run and to_latex. The run function takes an iterable of `niapy.algorithms.Algorithm` 
instances, and an iterable of problems in the form of
`{'problem': <problem_name>, 'lower': <lower_bounds>, 'lower': <lower_bounds>, 'upper': <upper_bounds>}`.
It also accepts the number of independent `runs`, the dimension of the problems `dim` and the maximum number of
iterations, `max_iters`. It returns a pandas DataFrame with the
best, worst and mean values of the runs for each problem and algorithm.

The module also contains a `to_latex` function which can be used to export
the resulting DataFrame from the run function to a LaTeX table.

## Usage

For viewing purposes, the notebook can be viewed in github directly or with a third party tool,
like [nbviewer](https://nbviewer.jupyter.org/).

If you want to edit the notebook and run your own experiments follow the instructions below:

1. Clone this repository:
    ```shell
    git clone https://github.com/zStupan/bfo-experiments
    cd bfo-experiments
    ```
2. Create and activate a virtual environment:
   ```shell
    python3 -m venv venv
    . venv/bin/activate # or "source venv/bin/activate"
    ```
   
3. Install requirements:
   ```shell
    pip install -r requirements.txt
    ```
   
4. Start the jupyter notebook and start experimenting:
   ```shell
    jupyter notebook
    ```

5. Alternatively you could also just use the functions in the bfo_experiments module directly
   by modifying the file and running it or importing the file and calling the run function.

**Warning**: running the experiments in the notebook takes a very long time.

## References
[1] G. Vrbančič, L. Brezočnik, U. Mlakar, D. Fister in I. Fister, “NiaPy: Python microframework for building nature-inspired algorithms”, Journal of Open Source Software, vol. 3, no. 23, pp. 613, 2018.

[2] K. M. Passino, “Biomimicry of bacterial foraging for distributed optimization and control”, IEEE Control Systems Magazine, vol. 22, no. 3, pp. 52–67, 2002.