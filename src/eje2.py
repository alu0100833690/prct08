#! /usr/bin/python
import eje1

t_upla_intervalos=(10,100,1000,10000)
t_upla_umbrales=(0.1,0.01,0.001,0.0001,0.00001)

for i in t_upla_intervalos:
  for j in t_upla_umbrales:
    error(i,j,8)