# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:44:37 2021

@author: juan
"""

def marg_future(x,spl,yg, yr, plt, np,mk, e):
   
    cont=0
    conth=0
    ap=[]
    c=[]
    for i in x:
        c.append(cont)
        if not(np.isnan(i)):
            if abs((yg[cont]-yr[cont])/yr[cont])<e:
                ap.append(1)
                conth=conth+1
            else:
                ap.append(2)
            print(cont+1,i,abs((yg[cont]-yr[cont])/yr[cont]))
            #plt.plot(cont,ap[cont], marker=mk)
            plt.bar(c[cont], ap[cont])
            cont=cont+1
            
            
    print(conth,'/',cont,'=',conth/cont)




def marg(x,spl, yr, plt, np,mk, e):
   
    cont=0
    conth=0
    yg=spl(x)
    ap=[]
    c=[]
    for i in x:
        c.append(cont)
        if not(np.isnan(i)):
            if abs((yg[cont]-yr[cont])/yr[cont])<e:
                ap.append(1)
                conth=conth+1
            else:
                ap.append(2)
            print(cont+1,i,abs((yg[cont]-yr[cont])/yr[cont]))
            #plt.plot(cont,ap[cont], marker=mk)
            cont=cont+1
    count=[] 
    cont=0       
    for j in ap:
        count.append(c[cont])
        cont=cont+1;
        
    print(len(count), len(ap))
    print(conth,'/',len(count),'=',conth/len(count))
    plt.bar(count, ap)
            
    
    



def comparision(x,spl, yr, plt, np,mk):
    print("Valor               Posible valor    Valor real      Error")
    cont=0
    yg=spl(x)
    for i in x:
        if not(np.isnan(i)):
      
            print(i,yg[cont],yr[cont], abs((yg[cont]-yr[cont])/yr[cont]))
            plt.plot(x[cont],yr[cont], marker=mk)
            cont=cont+1


def begin(l1,np):    
    l2=[]
    for i in l1:
        if not(np.isnan(i)):
            l2.append(i)
    
    return l2

            
def posible_values(x,spl,plt,np,mk):
    cont=0
    yg=spl(x)
    for i in x:
        if not(np.isnan(i)):
      
            print(i,yg[cont])
            #plt.plot(x[cont],yr[cont], marker=mk)
            cont=cont+1
            
def error(x,spl, yr, plt, np,mk):
  cont=0
  yg=spl(x)
  ap=[]
  for i in x:
      if not(np.isnan(i)):
          ap.append(abs((yg[cont]-yr[cont])/yr[cont]))
          print(i,ap[cont])
          plt.plot(x[cont],ap[cont], marker=mk)
      cont=cont+1
  print(max(ap))
  return ap

def error_future(x,spl,yg ,yr, plt, np,mk):
  cont=0
  ap=[]
  for i in x:
      if not(np.isnan(i)):
          ap.append(abs((yg[cont]-yr[cont])/yr[cont]))
          print(i,ap[cont])
          plt.plot(x[cont],ap[cont], marker=mk)
      cont=cont+1
  print(max(ap))
  return ap
            
    
    
    