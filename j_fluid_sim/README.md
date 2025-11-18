# Fluid simulation examples

This directory contains a C++ implementation of Chorin's projection method for simulating incompressible Navier–Stokes equations.

## Compiling the code
The code is written in C++ and uses the OpenMP library for multithreading. It has
been tested on Linux, MacOS, and Windows (via [Cygwin](https://www.cygwin.com)).

- The code requires on TGMG, a C++ library for solving linear systems using the
  geometric multigrid method, which is available as a
  [separate repository on GitHub](http:/github.com/chr1shr/tgmg). A copy of the library is provided in the [math714/tgmg](https://github.com/rycroft-group/math714/tree/main/tgmg) directory. 

- The code outputs data in a binary format that can be read by the freeware
  plotting program [Gnuplot](http://www.gnuplot.info). The code uses a Perl script to process and analyze Gnuplot output
  files using gp-headers.

- The gp-headers directory requires [libpng](http://www.libpng.org/pub/png/) for
  making for full functionality, but this dependency can be omitted. To make
  movies of the simulation output [FFmpeg](https://ffmpeg.org) is needed.

By default the code assumes that the **fluid_sim** and **tgmg**
repositories are placed in the same parent directory.

To compile the code it is necessary to create a common configuration file
called **config.mk** in the parent directory, which can be used by all three
repositories. Several templates are provided in the **config** directory. To
use, copy one of the templates into the parent directory. From the incrmt
directory, on a Linux computer, type
```Shell
cp config/config.mk.linux ../config.mk
```
On a Mac using GCC 14 installed via [MacPorts](http://www.macports.org), type
```Shell
cp config/config.mk.mac_mp ../config.mk
```
On a Mac using GCC installed via [Homebrew](http://brew.sh), type
```Shell
cp config/config.mk.mac_hb ../config.mk
```
On a Windows computer with Cygwin installed, type
```Shell
cp config/config.mk.win_cw ../config.mk
```
After this, the code can be compiled by typing
```Shell
make
```
This will build several executables such as **fluid_test**.

> **Note:** If you encounter warnings of deprecated declaration of `sprint` in `fluid_2d.cc`, or warnings of template-id not allowed for constructor in C++20 in `tgmg.hh`, you can ignore them.

## Example
The program `fluid test.cc` is a front-end that runs a simple test case where several
fluid vortices move around and interact. It saves snapshots of the fields at regular
intervals. It can be run using 8 threads on a 256&nbsp;&times;&nbsp;256 grid
with the following command:
```Shell
OMP_NUM_THREADS=8 ./fluid_test
```
The code will create a directory called **ftest.out** for the simulation
output.
The output directory contains files of different types:

- **p**.*<n>*, the pressure field at frame *n*;
- **u**.*<n>* and **v**.*<n>*, the components of the velocity field at frame *n*;
- **trace**.*<n>*, the fluid tracer positions at frame *n* stored in binary format;
- **header**, a small text file containing the number of simulation frames and
  the time interval simulated.

If FFmpeg is installed, then the following command can be used to generate a
movie of the pressure field with tracers:
```Shell
./gnuplot_movie.pl -t ftest.out p
```
This will generate a QuickTime movie using the H.265 codec called
**ftest_p.mov**. Alternatively, to just make the frames without making
a movie, the command
```Shell
./gnuplot_movie.pl -t -w ftest.out p
```
can be used. This will create a directory called **ftest_p.frames** that
contains the movie frames as PNG images.

The Perl script supports several other options, which can be seen by typing:
```Shell
./gnuplot_movie.pl -h
```


## Code structure
The code is structured around several C++ classes:

- The **fluid_2d** class contains the core routines for running a simulation.
  It allocates memory for the fluid field, and contains the main
  routines for updating these.

- The **field** data structure contains all of the fields required to simulate
  the fluid in one grid cell. The **fluid_2d** class allocates a
  two-dimensional array of the **field** data structure to perform the
  simulation.

The simulation method requires one linear system to be solved during each
timestep: the approximate projection
using the finite-element method (FEM). The code contains classes that describe
these linear systems, which are used by the TGMG library:

- **mgs_fem**, containing data that is common for all FEM systems
    