#!/bin/bash
# Plot memory and CPU usage over time
set -m 
set -x

# sudo apt-get install gnuplot

gnuplot --persist -c plot.gp top.dat top.png 
 
