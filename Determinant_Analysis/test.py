# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:08:18 2016

@author: mct00
"""

for i in range(5):
    f = open("output"+str(i)+".txt", "w")
    f.write(str(i))
    f.close()