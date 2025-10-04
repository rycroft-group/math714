# Iterative methods examples

This directory contains several introductory examples used in Lectures 6 and 7 on iterative methods.

## The `iter_methods.ipynb` notebook

The Python notebook contains the same code and functionality in the Python scripts below. It combines the scripts into an interactive format, making it easier to run, visualize results, and make modifications directly within the notebook environment. 

## The `rossler_trap.py` example

The program `rossler_trap.py` numerically integrate the Rossler ODE system using the trapezoid method. Root-finding is performed via Newton's method. The program can be run by typing the following command in the terminal:

```Shell
python3 rossler_trap.py
```

## The `z_stability.py` example

The program `z_stability.py` numerically integrate a test ODE with three multistep methods with varying stability. The program can be run by typing the following command in the terminal:

```Shell
python3 z_stability.py
```

## The `stab_region.py` example

The program `stab_region.py` calculates the stability region of several multi-step methods. The program can be run by typing the following command in the terminal:

```Shell
python3 stab_region.py
```

## The `stiff.py/stiff2.py` example

The program `stiff.py/stiff2.py` integrates a stiff system using explicit/implicit methods. The program can be run by typing the following command in the terminal:

```Shell
python3 stiff.py/stiff2.py
```

## The `stiff3.py` example

The program `stiff3.py` integrates the example ODE with the trapezoid method. The program can be run by typing the following command in the terminal:

```Shell
python3 stiff3.py
```