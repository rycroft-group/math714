# Finite volume methods examples

This directory contains several introductory examples used in Lectures 16, 17, 18, and 19 on finite volume methods.

## The `fvolume.ipynb` notebook

The Python notebook contains the same code and functionality in the Python scripts below. It combines the scripts into an interactive format, making it easier to run, visualize results, and make modifications directly within the notebook environment. 

## The `fd_fv_comp.py` example

The program `fd_fv_comp.py` compares the numerical flux conservation between finite difference and finite volume methods. The program can be run by typing the following command in the terminal:

```Shell
python3 fd_fv_comp.py
```

## The `ho_fvolume.py` example

The program `ho_fvolume.py` demonstrates different higher-order methods such as Lax–Wendroff and Beam–Warming. The program can be run by typing the following command in the terminal:

```Shell
python3 ho_fvolume.py
```

## The `limiters.py` example

The program `limiters.py` shows how spurious oscillations can be reduced by adding limiters, such as minmod and superbee. The program can be run by typing the following command in the terminal:

```Shell
python3 limiters.py
```

## The `eno2.py` example

The program `eno2.py` shows how the second-order essentially non-oscillatory (ENO) method can also mitigate spurious oscillations. The program can be run by typing the following command in the terminal:

```Shell
python3 eno2.py
```

## The `van_visc.py` example

The program `van_visc.py` demonstrates how to simulate propagating shocks by adding in small viscosity to the transport equation. The program can be run by typing the following command in the terminal:

```Shell
python3 van_visc.py
```

## The `t_solve.py` example

The program `t_solve.py` demonstrates how to properly simulate the traffic equation with the REA algorithm. The program can be run by typing the following command in the terminal:

```Shell
python3 t_solve.py
```