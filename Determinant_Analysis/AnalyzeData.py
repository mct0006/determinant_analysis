# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:33:09 2016

@author: mct00
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

det_data = pd.read_csv('determinants.csv')


# The first histogram combines all of the data stored in determinants.csv from the 5 seperate experiments. 
# The remaining histograms display only the data from one experiment. 
# In each expermint, random 20x20 matrices A and B are fixed, and determinants of matrices of the form 
# WAX+YBZ are generated, where W, X, Y, and Z are orthogonal.
# Each experiment has 1000 data points.


plt.figure();
det_data.plot.hist(bins = 30)


plt.figure();
det_data['A'].plot.hist(bins = 30)

plt.figure();
det_data['B'].plot.hist(bins = 30)

plt.figure();
det_data['C'].plot.hist(bins = 30)

plt.figure();
det_data['D'].plot.hist(bins = 30)

plt.figure();
det_data['E'].plot.hist(bins = 30)


# Compute some basic statistics for each column.

print("Means:")
print(det_data.mean(0))
print("\n")
print("Standard Deviations:")
print(det_data.std(0))
print("\n")
print("Quartiles:")
print(det_data.quantile(.25))
print(det_data.quantile(.5))
print(det_data.quantile(.75))
print("\n")
print("1st-4th Moments:")
print(det_data.median(0))
print(det_data.var(0))
print(det_data.skew(0))
print(det_data.kurt(0))


