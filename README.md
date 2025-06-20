# PyGAU

Tired of not having tools to debug easily in python? PyGAU (Python Grab And Use) is here to help!

## The objective

As it names suggests, it is a library that adds debug features that are as easy to deploy as puting decorators in the functions you want to debug.

## Features

Currently, in version 1.0, it contains the following

- Benchmarking:
  - "Timing" class -> measure how many time does take a function to execute, as simple as adding a decorator to the functions of interest.
- Debugging:
  - "Report" class -> trace all the stack of functions called, as simple as adding a decorator to the functions of interest.
