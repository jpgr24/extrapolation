# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy.interpolate import CubicSpline

import numpy as np
import matplotlib.pyplot as plt

from comparison import marg
from comparison import begin
from comparison import posible_values
from comparison import error
plt.style.use('seaborn-poster')





data = pd.read_excel(r'data.xlsx')


d=time = pd.DataFrame(data, columns=['Time','Value'])
time = pd.DataFrame(data, columns=['Time'])

t=time.Time
print(d)
value=pd.DataFrame(data, columns=['Value'])
v=value.Value
t2=begin(t,np)


v2=begin(v,np)


p = CubicSpline(t2, v2, bc_type='natural')
t_new = np.linspace(t2[0], t2[len(t2)-1], 100)

v_new = p(t_new)
tshow=pd.DataFrame(data, columns=['Timeshow'])
ts=tshow.Timeshow

vreal=pd.DataFrame(data, columns=['Real_Value'])
vr=vreal.Real_Value
plt.figure(figsize = (9,3))

error(ts,p, vr, plt, np,'.')
tpred=pd.DataFrame(data, columns=['timepred'])
tp=tpred.timepred
#posible_values(tp,p,plt,np,'#')



plt.title('Cubic Spline Interpolation')
plt.xlabel('t')
plt.ylabel('v')










plt.show()



