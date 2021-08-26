# bfo-experiments

## Description

As a part of my bachelor's thesis, I extended the NiaPy microframework [1],
adding to it, the Bacterial Foraging Optimization algorithm as proposed by
K. M. Passino in 2002 [2]. This repository contains the various experiments I ran,
comparing the performance of BFO with other popular nature-inspired algorithms,
specifically Differential Evolution, Particle Swarm Optimization and the Bat Algorithm.

The details of the experiments are described in the jupyter notebook `bfo_experiments.ipynb`.
The results themselves can be found in the results directory in the form of pickled pandas dataframes and LaTeX tables.

The code used to run the experiments is located in `bfo_experiments.py`.

## Usage

For viewing purposes, the notebook can be viewed in github directly or with a third party tool,
like [nbviewer](https://nbviewer.jupyter.org/).

If you want to edit and run the notebook follow the instructions below:

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
   
4. Start the jupyter notebook (should open browser tab):
   ```shell
    jupyter notebook
    ```

**Warning**: Running the experiments using `bfo_experiments.py` takes a very long time (a little over 3 days on my machine) so I wouldn't recommend it.

## References
[1] G. Vrbančič, L. Brezočnik, U. Mlakar, D. Fister in I. Fister, “NiaPy: Python microframework for building nature-inspired algorithms”, Journal of Open Source Software, vol. 3, no. 23, pp. 613, 2018.

[2] K. M. Passino, “Biomimicry of bacterial foraging for distributed optimization and control”, IEEE Control Systems Magazine, vol. 22, no. 3, pp. 52–67, 2002.
