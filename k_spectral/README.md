# Spectral methods examples

This directory contains several introductory examples used in Lectures 23 and 24 on spectral methods.

## The `spectral.ipynb` notebook

The Python notebook contains the same code and functionality in the Python scripts below. It combines the scripts into an interactive format, making it easier to run, visualize results, and make modifications directly within the notebook environment. 

## The `spec_diff.py` example

The program `spec_diff.py` demonstrates the accuracy of a spectral derivative compared to second-order and fourth-order finite difference computations. The program can be run by typing the following command in the terminal:

```Shell
python3 spec_diff.py
```

## The `spec_conv.py` example

The program `spec_conv.py` examines the convergence rate of the finite-difference and spectral derivatives. The program can be run by typing the following command in the terminal:

```Shell
python3 spec_conv.py
```

## The `fderiv_time.py` example

The program `fderiv_time.py` measures the time to compute a spectral derivative across a wide range of grid sizes,  and demonstrates the $O(N\log N)$ scaling. The program can be run by typing the following command in the terminal:

```Shell
python3 fderiv_time.py
```

## The `spec_transp.py` example

The program `spec_transp.py` uses spectral derivatives in space and the leapfrog method in time to solve for the transport equation. The program can be run by typing the following command in the terminal:

```Shell
python3 spec_transp.py
```

## The `spec_bvp1d.py` example

The program `spec_bvp1d.py` uses the Chebyshev spectral method to solve for the 1D Poisson problem. The program can be run by typing the following command in the terminal:

```Shell
python3 spec_bvp1d.py
```

## The `spec_bvp2d.py` example

The program `spec_bvp2d.py` uses the Chebyshev spectral method to solve for the 2D Poisson problem. The program can be run by typing the following command in the terminal:

```Shell
python3 spec_bvp2d.py
```
