# Mixed equations examples

This directory contains an example used in the lecture on mixed equations.

## The `mixed.ipynb` notebook

The Python notebook contains the same code and functionality in the Python scripts below. It combines the scripts into an interactive format, making it easier to run, visualize results, and make modifications directly within the notebook environment. 

## The `spinodal.py` example

The program `spinodal.py` simulates spinodal decomposition by solving the reaction–diffusion equation $u_t = \epsilon^2 \nabla^2 u + \beta u(1-u^2)$ on a periodic 80&nbsp;&times;&nbsp;80 grid, starting from a random initial condition. Here $\beta = 3$, and $\epsilon = h = 1/80$ is the grid spacing, so the diffusion coefficient is $\epsilon^2 = h^2$. It uses Strang splitting, where the diffusion term is integrated with the Crank–Nicolson method and the reaction term is integrated explicitly. The program can be run by typing the following command in the terminal:

```Shell
python3 spinodal.py
```

The program creates a directory called **spinodal.odr** and saves 201 snapshots of the solution, **u.0** to **u.200**, in Gnuplot binary matrix format. A snapshot can be viewed in Gnuplot with the following command:

```Shell
plot 'spinodal.odr/u.200' binary matrix with image
```

## The `movie.py` example

The program `movie.py` converts the snapshots in **spinodal.odr** into PNG images, running eight conversions in parallel, and then combines them into a movie called **spinodal.mov** using the H.265 codec. It requires [FFmpeg](https://ffmpeg.org) and the `bitmap_field` utility, which it expects to find at `../../utils-gp/bitmap_field`. After running `spinodal.py`, the program can be run by typing the following command in the terminal:

```Shell
python3 movie.py
```
