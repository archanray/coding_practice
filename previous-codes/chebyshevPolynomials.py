"""
Original inspiration: https://mathworld.wolfram.com/ChebyshevPolynomialoftheFirstKind.html
Polar code adapted from: https://gist.github.com/Panadestein/c9cda01fc24a3463871006914ed5f3a4
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import chebyshev
import sys

def ChebyshevPolynomial(x, n):
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return x
    return 2*np.multiply(x, ChebyshevPolynomial(x, n-1)) - ChebyshevPolynomial(x, n-2)

def ChebyshevWrapper(x, n, coefficients=None):
    m = len(x)
    y = np.zeros((n, m))
    for i in range(0, n+1):
        y[i,:] = ChebyshevPolynomial(x, i)
    if coefficients == None:
        coefficients = np.ones(n+1)
    elif len(coefficients) < n+1:
        print("coefficients needs to be of length n")
        sys.exit(1)
    coefficients = np.tile(coefficients, (1, m))
    weighedPolynomial = np.multiply(coefficients, y)
    summedPolynomial = np.sum(weighedPolynomial, axis=0) # axis 0 results in row sums
    return summedPolynomial

def polarChebyshev(thetas, degrees):
    """
    computes polar chebyshev function
    """
    print("thetas and degrees:", thetas, degrees)
    coeffs = degrees * [0] + [1]
    print("Coefficients:", coeffs)
    xvals = thetas / np.pi - 1
    print("Chebval:", chebyshev.chebval(xvals, coeffs), chebyshev.chebval(xvals, coeffs)+ degrees)
    # return ChebyshevWrapper(xvals, len(coeffs), coeffs) + degrees
    return chebyshev.chebval(xvals, coeffs) + degrees

def polarChebyshevGenerator(thetas, degrees):
    """
    generates polar chebyshev values
    """
    chebyPol = []
    for th in thetas:
        thCheby = []
        for dg in degrees:
            thCheby.append(polarChebyshev(th, dg))
        chebyPol.append(thCheby)
    return chebyPol

################ FIGURE PARAMS ######################################
params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#######################################################################

# for linear plot
# define variables
x = np.linspace(-1, 1, 1000)
minDegree = 1
maxDegree = 5
for i in range(minDegree,maxDegree+1):
    y = ChebyshevPolynomial(x, i)
    ax.plot(x, y, label="$T_{"+str(i)+"}(x)$")
plt.legend()
plt.title("Linear plot of Chebyshev's polynomials")
plt.show()

# # for polar plot
# # define variables
# thetas = np.linspace(0, 2 * np.pi, num=1000)
# degrees = np.arange(0, 40, 2)
# CHEBSPOL = np.array(polarChebyshevGenerator(thetas, degrees)).T
# # Plot Chebyshev spiral
# fig = plt.figure()
# ax1 = plt.subplot(121, projection='polar')
# ax2 = plt.subplot(122, projection='polar')

# ax1.grid(False)
# ax1.set_yticklabels([])
# ax1.set_thetagrids([])
# ax1.spines['polar'].set_visible(False)

# ax2.grid(False)
# ax2.set_yticklabels([])
# ax2.set_thetagrids([])
# ax2.spines['polar'].set_visible(False)

# for cpol in CHEBSPOL:
#     ax1.plot(thetas, cpol)

# for pla, plb in CHEBSPOL.reshape(-1, 2, 1000):
#     ax2.fill_between(thetas, pla, plb, facecolor='black')

# plt.show()