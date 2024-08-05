# Optimization

The Steepest Descent Algorithm or the Gradient Descent Algorithm is a method for solving general unconstrained optimization problems, i.e., minimizing a general nonlinear function.

Here we employ two functions:

## 1. Rosenbrock function

f(x,y) = (a - x)^2 + b(y - (x^2))^2

where I take a = 1, b = 100

## 2. Himmelblau's function

f(x,y) = ((x^2) + y - 11)^2 + (x + (y)^2 - 7)^2

I have considered two starting points:

a. (0,0)^T
b. (pi + 1, pi - 1)^T

I try and reach their points of minima emplying the gradient descent algorithm. Now, the algorithm requires step-sizes, and I utilised three of them:

### 1. Wolfe-Powell step size
### 2. Armijo step size
### 3. constant step size

In the end, I try and compare the behaviour of the two functions with respect to the starting points and step sizes.

## References

1. Meza, J.C., 2010. Steepest descent. Wiley Interdisciplinary Reviews: Computational Statistics,2(6), pp.719-722.
2. Grad, S.M. Lecture Notes. Optimization[MAP554D].
3. scipy.optimize.minimize—SciPy v1.11.4 Manual. https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html.
4. differential evolution https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html
5. Campbell, S. (2023) Python Timeit() with Examples. https://www.guru99.com/timeitpython-examples.html.
6. GeeksforGeeks (2022) Quiver Plot in Matplotlib. https://www.geeksforgeeks.org/quiverplot-in-matplotlib/.
7. Shi, Z.J. and Shen, J., 2005. Step-size estimation for unconstrained optimization methods.
8. Computational & Applied Mathematics, 24, pp.399-416.
9. Kia, S.S. Lecture 4. Optimization Methods
