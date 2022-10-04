# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy.interpolate import CubicSpline
from scipy.interpolate import interpolate


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt_error

from comparison import comparision
from comparison import begin
from comparison import posible_values
from polynomy import divided_diff
from polynomy import newton_poly
plt.style.use('seaborn-poster')

plt_error.style.use('seaborn-poster')



data = pd.read_excel(r'data.xlsx')


d=time = pd.DataFrame(data, columns=['Time','Value'])
time = pd.DataFrame(data, columns=['Time'])

t=time.Time

value=pd.DataFrame(data, columns=['Value'])
v=value.Value
t2=begin(t,np)


v2=begin(v,np)


p = CubicSpline(t2, v2, bc_type='natural')
t_new = np.linspace(t2[0], t2[len(t2)-1], 3000)

v_new = p(t_new)
a_s = divided_diff(t2, v2)[0, :]
x_new = np.arange(t2[0], t2[len(t2)-1], .1)
y_new = newton_poly(a_s, t2, x_new)
tshow=pd.DataFrame(data, columns=['Timeshow'])
ts=tshow.Timeshow

vreal=pd.DataFrame(data, columns=['Real_Value'])
vr=vreal.Real_Value
plt.figure(figsize = (30,5))

comparision(ts,p, vr, plt ,np,'.')
tpred=pd.DataFrame(data, columns=['timepred'])
tp=tpred.timepred
#posible_values(tp,p,plt,np,'#')
plt.plot(t_new, v_new, 'b')
#plt.plot(ts, vr, 'yellow')

plt.plot(t, v, 'ro')


plt.title('Cubic Spline Interpolation')
plt.xlabel('t')
plt.ylabel('v')

print('Posibles valores')
tfuture=pd.DataFrame(data, columns=['Tfuture'])
Tf=tfuture.Tfuture
Tf=begin(Tf,np)
cont=0

for i in Tf:
    print(Tf[cont],p(Tf[cont]))
    cont=cont+1
    








