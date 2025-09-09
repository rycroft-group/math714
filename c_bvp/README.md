# Boundary value problems examples

This directory contains several introductory examples used in Lectures 2 and 3 on boundary value problems.

## The `c_bvp.ipynb` notebook

The Python notebook contains the same code and functionality as the three `.py` files below. It combines the scripts into an interactive format, making it easier to run, visualize results, and make modifications directly within the notebook environment. 

## The `bvp1.py` example

The **bvp1.py** showcases how to solve a 1D BVP with the method of manufactured solutions. The program can be run by typing the following command in the
terminal:

```Shell
python3 bvp1.py
```

The program outputs the results to the terminal. It also computes the infinity-norm error.

## The `newton.py` example

The **newton.py** performs linear root-finding of a given function. It demonstrates how 1D Newton's method works. The program can be run by typing the following command in the terminal:

```Shell
python3 deriv_gen.py
```

The program outputs each Newton iterate to the terminal.

## The `gq_solve.py` example

The **gq_solve.py** derives the two-point
Gaussian quadrature points and weights. It also demonstrates how to use `fsolve` for Newton's method. The program can be run by typing the following command in the terminal:

```Shell
python3 gq_solve.py
```

The program outputs the derived quadrature points and weights.