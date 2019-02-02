import random
import matplotlib.pyplot as pt
import numpy
def f(n):
   b=[]
   li=[1,3,5,7,8,10,12]
   li1=[]
   dic={}
   i=0
   while i<n:
      y=random.randint(1895,2017)
      if y%4==0 and y%100==0 or y%400==0:
         l=1
      else:
         l=0
      m=random.randint(1,12)
      if l==0 and m==2:
         d=random.randint(1,28)
      if l==1 and m==2:
         d=random.randint(1,29)
      if m in li:
         d=random.randint(1,31)
      if m not in li and m!=2:
         d=random.randint(1,30)
      li1.append(str(d)+str(m))
      i+=1
   for x in li1:
      dic[x]=dic.get(x,0)+1
   count=0
   for i,z in dic.items():
      if z>1:
         count+=1
   return count
t=numpy.arange(100,10000,100)
col=[]
for x in t:
   col.append(f(x))
pt.plot(t,col,'r--')
pt.ylabel("No of collisions")
pt.xlabel("No of Peoples")
pt.show()
