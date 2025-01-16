# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 08:47:08 2024

@author: HP
"""

import pandas as pd
from matplotlib import pyplot as plot

# read by default 1st sheet of an excel file
df = pd.read_excel('plot.xlsx')

df.plot(kind = 'line', x= 'A', y= 'B', color = 'red')

# set the title
plot.title('Line')
plot.savefig('line.pdf')
# show the plot
plot.show()