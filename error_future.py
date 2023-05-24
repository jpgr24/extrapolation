# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy.interpolate import CubicSpline

import numpy as np
import matplotlib.pyplot as plt

from comparison import marg_future
from comparison import begin
from comparison import posible_values
plt.style.use('seaborn-poster')





data = pd.read_excel(r'data.xlsx')


d=time = pd.DataFrame(data, columns=['Time','Value'])
time = pd.DataFrame(data, columns=['Time'])

t=time.Time

value=pd.DataFrame(data, columns=['Value'])
v=value.Value
t2=begin(t,np)


v2=begin(v,np)


p = CubicSpline(t2, v2, bc_type='natural')
t_new = np.linspace(t2[0], t2[len(t2)-1], 100)

v_new = p(t_new)
tshow=pd.DataFrame(data, columns=['time_help_future'])
ts=tshow.time_help_future

vgot=pd.DataFrame(data, columns=['Value_future_got'])
vreal=pd.DataFrame(data, columns=['Real_value_future'])
vg=vgot.Value_future_got
vr=vreal.Real_value_future
vh=pd.DataFrame(data, columns=['help_value'])
vhelp=vh.help_value
error=abs(vh-vr)
plt.figure(figsize = (9,5))

marg_future(ts,p,vg, vr, plt, np,'.',0.01)
tpred=pd.DataFrame(data, columns=['timepred'])
tp=tpred.timepred
#posible_values(tp,p,plt,np,'#')

print(error)

plt.title('Cubic Spline Interpolation')
plt.xlabel('t')
plt.ylabel('v')










plt.show()



