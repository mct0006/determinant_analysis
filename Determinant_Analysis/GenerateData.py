# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:35:28 2016

@author: mct00
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import DeterminantCalculations as ddt

mat1 = ddt.genData()
mat2 = ddt.genData()
mat3 = ddt.genData()
mat4 = ddt.genData()
mat5 = ddt.genData()

df = pd.DataFrame({'A' : pd.Series(mat1),
                   'B' : pd.Series(mat2),
                   'C' : pd.Series(mat3),
                   'D' : pd.Series(mat4),
                   'E' : pd.Series(mat5)})

df.to_csv('determinants.csv')