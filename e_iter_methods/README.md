# Iterative methods examples

This directory contains several introductory examples used in Lectures 6 and 7 on iterative methods.

## The `iter_methods.ipynb` notebook

The Python notebook contains the same code and functionality in `s_descent.py`, `simple_cg.py`, and `poisson_cg.py`. It combines the scripts into an interactive format, making it easier to run, visualize results, and make modifications directly within the notebook environment. 

## The `poisson_time.py` example

The program `poisson_time.py` measures the time taken to solve the [`poisson2.py`](https://github.com/rycroft-group/math714/blob/main/d_elliptic/poisson2.py) test code. It uses two different measures of time. The program can be run by typing the following command in the terminal:

```Shell
python3 poisson_time.py
```

## The `s_descent.py` example

The **s_descent.py** implements the steepest descent algorithm, reaching a tolerance of $10^{-10}$ in 43 iterations. It takes a zig-zag path to reach the solution. The program can be run by typing the following command in the
terminal:

```Shell
python3 s_descent.py
```

## The `simple_cg.py` example

The **simple_cg.py** uses CG to solve the one-dimensional Poisson equation. The program can be run by typing the following command in the terminal:

```Shell
python3 simple_cg.py
```

## The `poisson_cg.py` example

The **poisson_cg.py** uses CG to solve the two-dimensional Poisson equation. The program can be run by typing the following command in the terminal:

```Shell
python3 poisson_cg.py
```
