# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 08:55:23 2024

@author: HP
"""

import pandas as pd
from matplotlib import pyplot as plot

# read by default 1st sheet of an excel file
df = pd.read_excel('plot.xlsx')

df.plot(kind = 'line', x= 'A', y= 'B', color = 'magenta')

# set the title
plot.title('Line')
plot.savefig('line1.pdf')
# show the plot
plot.show()