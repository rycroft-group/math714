# Detect the operating system
detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')

# Set the compiler and flags based on the operating system
# Supported OS are Mac OSX ("Darwin") and Linux ("Linux")

# Is the OS Mac?
ifeq ($(detected_OS), Darwin)
cxx := g++-mp-14 -O3
cflags := -fopenmp -Wall -ansi -pedantic
lp_lflags := -llapack -lblas
endif

# Is the OS Linux?
ifeq ($(detected_OS), Linux)
cxx := g++-14 -O3
cflags := -fopenmp -Wall -ansi -pedantic
lp_lflags := -llapack -lblas
endif

# Lists of files to be built
execs=openmp_example1 openmp_example2 openmp_example2b race_condition ridders_array diffuse false_sharing happy

all: $(execs)

# A Makefile target to remove all the built files
clean:
	rm -f $(execs)
	
# Makefile rule to build an executable. Note $@ is a shorthand for the file to
# be built and $^ is a shorthand for all the dependencies. (Can also use $< to
# mean the first dependency only.)
openmp_example1: openmp_example1.cc
	$(cxx) $(cflags) -o $@ $^

openmp_example2: openmp_example2.cc
	$(cxx) $(cflags) -o $@ $^

openmp_example2b: openmp_example2b.cc
	$(cxx) $(cflags) -o $@ $^

race_condition: race_condition.cc
	$(cxx) $(cflags) -o $@ $^

ridders_array: ridders_array.cc
	$(cxx) $(cflags) -o $@ $^

diffuse: diffuse.cc
	$(cxx) $(cflags) -o $@ $^

false_sharing: false_sharing.cc
	$(cxx) $(cflags) -o $@ $^

happy: happy.cc
	$(cxx) $(cflags) -o $@ $^

# The PHONY command tells GNU Make than "clean" is a phony target, which means
# that it doesn't correspond to an actual file called "clean'.
.PHONY: clean