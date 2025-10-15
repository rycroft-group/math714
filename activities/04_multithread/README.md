# Introduction to multithreading
This git repository contains the Jupyter notebook and code presented at the "Introduction to multithreading" workshop. It covers the basics of using ```OpenMP``` in C++, ```joblib``` in Python, and vectorized ```NumPy``` to parallelize a program.

## Repo organization
In order to run the example code, we need to first compile the executables. Run the following commands in your terminal:
```sh
make
```
>Note: ```Makefile``` automatically sets the compiler and flags based on the operating system. If you are running on Linux, the default GNU compiler will work out of the box. If you are running on a Mac, you will need to install a C++ compiler (preferably gcc) with ```OpenMP``` support from [MacPorts](https://www.macports.org/) or [Homebrew](https://brew.sh/). This is a [tutorial](http://www.mathcancer.org/blog/setting-up-gcc-openmp-on-osx-homebrew-edition/). If you are using a higher version of gcc, you can swap out the ```g++-mp14``` for Mac or ```g++-14``` for Linux with your gcc version.

### Monitoring core usage
[htop](https://htop.dev/) is a handy utility to visualize core usage. It can really help us understand multithreading and how to parallelize our code better. Highly recommend to install it if you are a Mac or Linux user. For Windows user, you can directly use the [Get-Process Cmdlet](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-powershell-1.0/ee176855(v=technet.10)?redirectedfrom=MSDN) or try some [alternative](https://technet.microsoft.com/en-us/sysinternals/bb842062) tools.

### Selected examples
1. ```openmp_example2.cc```: print out "Hello world" from each thread on your computer
   ```sh
   ./openmp_example2
   ```
2. ```race_condition.cc```: examine the different ways to prevent race condition in multithreaded code
   ```sh
   ./race_condition <keyword>
   ```
3. ```happy.cc``` and ```happy.py```: in-workshop example to use either ```OpenMP``` in C++ or ```joblib``` in Python to find the happy numbers
   ```sh
   ./happy
   python3 happy.py
   ```
   >Note: Currently the ```Makefile``` does not compile this example. Full code will be posted once the workshop has ended. You also need to [install](https://joblib.readthedocs.io/en/latest/installing.html) ```joblib``` on your computer to run the Python script.
4. ```numpy_jax.ipynb```: Some simple ```NumPy``` and ```JAX``` examples on parallelized code