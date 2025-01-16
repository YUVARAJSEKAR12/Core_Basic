# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:10:42 2024

@author: HP
"""

#scatter
from matplotlib import pyplot as plot
x = [10, 20, 30,40,50,60]
y = [100, 200, 300,400,500,600]

#plot- line ,  scatter, 
plot.bar(x, y,color='red')
plot.title('s graph')
plot.ylabel('Y axis')
plot.xlabel('X axis')
plot.show()