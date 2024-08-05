# -*- coding: utf-8 -*-
"""Optimization_Project_Himmelblau.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZBreaPTlpvp1gS7WtttCMLDjS-XuKzp2
"""

#importing necessary packages
from sympy import *
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import timeit
from scipy.optimize import differential_evolution
import sys
sys.set_int_max_str_digits(0)

def g(x1,x2): #defining Himelblau's function
  return ((x1**2 + x2 -11)**2+ (x1+(x2**2)-7)**2)

#defining the first component of the gradient as a function
def gradg1(x1,x2):
  y1=symbols('y1')
  y2=symbols('y2')
  g1=diff(g(y1,y2),y1)
  U=g1.subs({y1:x1,y2:x2})
  return U

#defining the second component of the gradient as a function
def gradg2(x1,x2):
  y1=symbols('y1')
  y2=symbols('y2')
  g2=diff(g(y1,y2),y2)
  U=g2.subs({y1:x1,y2:x2})
  return U

#defining the Armijo step size function
#with the starting value of t as the lower bound according to Armijo rule = sigma = 0.1
def armijo(x1,x2,sigma,delta,b1,b2):
  t=sigma
  while(g(x1-t*gradg1(x1,x2),x2-t*gradg2(x1,x2))>g(x1,x2)-t*delta*(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)):
    t=random.uniform(t*b1,t*b2)
  return t

armijo(0,0,0.1,0.01,0.1,0.5) #calculating the armijo step size for the starting point (0,0),
#and values of sigma=0.1, delta=0.01, b1=0.1 and b2=0.5

armijo(math.pi+1,math.pi-1,0.1,0.01,0.1,0.5) #calculating the armijo step size for the starting point (pi+1,pi-1),
#and values of sigma=0.1, delta=0.01, b1=0.1 and b2=0.5

#defining the function for the steepest descent algorithm that uses the armijo step size
def st_des_a(x1,x2): #(x1,x2) is the starting point x0
  epsilon=pow(10,-10)
  k=0
  while(sqrt(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)>epsilon):
    k+=1
    t=armijo(x1,x2,0.1,0.01,0.1,0.5)
    x1=x1-t*gradg1(x1,x2)
    x2=x2-t*gradg2(x1,x2)
  print("Number of iterations to reach minimum: ",k)
  print("Point of minima: ",(x1,x2))
  print("Minimum value of the function at the obtained point: ", g(x1,x2))

#running the steepest descent algorithm with the starting point x0=(0,0)
stmt_code = lambda: st_des_a(0, 0)
# Measure the execution time
timeit_result = timeit.timeit(stmt=stmt_code, number=1)
print(f"Execution time: {timeit_result} seconds")

#running the steepest descent algorithm with the starting point x0=(pi+1,pi-1)
stmt_code = lambda: st_des_a(math.pi+1,math.pi-1)
# Measure the execution time
timeit_result = timeit.timeit(stmt=stmt_code, number=1)
print(f"Execution time: {timeit_result} seconds")

#defining the wolfe-powell step size
def wolfe_pow(x1,x2,delta,b):
  t=1
  z=t+2
  for i in range(0,1000):
    if ((g(x1-t*gradg1(x1,x2),x2-t*gradg2(x1,x2))<=g(x1,x2)-delta*t*(gradg1(x1,x2)**2 + gradg2(x1,x2)**2))) :
      if ((gradg1(x1-t*gradg1(x1,x2),x2-t*gradg2(x1,x2))*gradg1(x1,x2))+(gradg2(x1-t*gradg1(x1,x2),x2-t*gradg2(x1,x2))*gradg2(x1,x2))
      <=b*(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)):
        return t
      else:
        t=np.random.uniform(t,z)
    else:
      z=t
      t=t/2
  return t

wolfe_pow(0,0,0.01,0.5)

wolfe_pow(math.pi+1,math.pi-1,0.01,0.5)

def st_des_wp(x1,x2):
  epsilon=pow(10,-10)
  k=0
  for i in range(0,10000):
    if(sqrt(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)>epsilon):
      k+=1
      t=wolfe_pow(x1,x2,0.01,0.5) #defining the wolfe-powell step size with values of delta=0.1, b=0.5
      x1=x1-t*gradg1(x1,x2)
      x2=x2-t*gradg2(x1,x2)
    else:
      break
  print("Number of iterations to reach minimum: ",k)
  print("Point of minima: ",(x1,x2))
  print("Minimum value of the function at the obtained point: ", g(x1,x2))

#running the wolfe-powell steepest descent algorithm with the starting point x0=(0,0)
stmt_code = lambda: st_des_wp(0, 0)
# Measure the execution time
timeit_result = timeit.timeit(stmt=stmt_code, number=1)
print(f"Execution time: {timeit_result} seconds")

#running the wolfe-powell steepest descent algorithm with the starting point x0=(pi+1,pi-1)
stmt_code = lambda: st_des_wp(math.pi+1,math.pi-1)
# Measure the execution time
timeit_result = timeit.timeit(stmt=stmt_code, number=1)
print(f"Execution time: {timeit_result} seconds")

#defining the function for the steepest descent algorithm where the step sizes are constant values
def st_des_cst(x1,x2):
    t1=0.0001
    t2=0.001
    t3=0.1
    epsilon=pow(10,-10)
    k1=0
    k2=0
    k3=0
    print("Step Size","\t","Number of iterations","\t\t\t","Point of minima","\t\t\t\t","Min value of function" )
    for i in range(0,10000):
      if(sqrt(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)>epsilon):
        k1+=1
        x1=x1-t1*gradg1(x1,x2)
        x2=x2-t1*gradg2(x1,x2)
      else:
        break
    print(t1,"\t\t\t",k1,"\t\t\t",(x1,x2),"\t\t\t",g(x1,x2))
    x1=0
    x2=0
    for i in range(0,10000):
      if(sqrt(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)>epsilon):
        k2+=1
        x1=x1-t2*gradg1(x1,x2)
        x2=x2-t2*gradg2(x1,x2)
      else:
        break
    print(t2,"\t\t\t",k2,"\t\t\t",(x1,x2),"\t\t\t",g(x1,x2))
    x1=0
    x2=0
    for i in range(0,10000):
      if(sqrt(gradg1(x1,x2)**2 + gradg2(x1,x2)**2)>epsilon):
        k3+=1
        x1=x1-t3*gradg1(x1,x2)
        x2=x2-t3*gradg2(x1,x2)
      else:
        break
    print(t3,"\t\t\t",k3,"\t\t\t",(x1,x2),"\t\t\t",g(x1,x2))

#running the steepest descent algorithm with the starting point x0=(0,0)
stmt_code = lambda: st_des_cst(0,0)
# Measure the execution time
timeit_result = timeit.timeit(stmt=stmt_code, number=1)
print(f"Execution time: {timeit_result} seconds")

#running the steepest descent algorithm with the starting point x0=(pi+1,pi-1)
stmt_code = lambda: st_des_cst(math.pi+1,math.pi-1)
# Measure the execution time
timeit_result = timeit.timeit(stmt=stmt_code, number=1)
print(f"Execution time: {timeit_result} seconds")

#Plotting the graph of the Himmelblau's function
xpt=np.arange(-50.0,50.0,0.5)
ypt=np.arange(-50.0,50.0,0.5)
X,Y=np.meshgrid(xpt,ypt)
vector=np.vectorize(g)
Z=vector(X,Y)

plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='viridis')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()

#Plotting the gradient of the Himmelblau's function
xpt=np.arange(-10.0,10.0,1)
ypt=np.arange(-10.0,10.0,1)
X,Y=np.meshgrid(xpt,ypt)
y1=symbols('y1')
y2=symbols('y2')
grad1_func = lambdify((y1, y2), gradg1(y1, y2), 'numpy')
grad2_func = lambdify((y1, y2), gradg2(y1, y2), 'numpy')

# Compute the gradients using NumPy functions
grad1 = grad1_func(X, Y)
grad2 = grad2_func(X, Y)

fig, ax = plt.subplots(figsize=(9, 9))
ax.quiver(X, Y, grad1, grad2,alpha=0.8)
ax.set_aspect('equal')
plt.show()

#defining the bounds
bounds = [(-5,0), (-5,0)]

# Using Differential Evolution for global optimization
result = differential_evolution(lambda x: g(x[0], x[1]), bounds)
result

#defining the bounds
bounds = [(-5,0), (0,5)]

# Using Differential Evolution for global optimization
result = differential_evolution(lambda x: g(x[0], x[1]), bounds)
result

#defining the bounds
bounds = [(0,5), (-5,0)]

# Using Differential Evolution for global optimization
result = differential_evolution(lambda x: g(x[0], x[1]), bounds)
result

#defining the bounds
bounds = [(0,5), (0,5)]

# Using Differential Evolution for global optimization
result = differential_evolution(lambda x: g(x[0], x[1]), bounds)
result