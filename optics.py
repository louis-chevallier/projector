import sympy
import numpy as np
from utillc import *
import sympy.abc as X
from sympy import Point2D, symbols, solve, cos, sin, lambdify
import os, sys
import random


# https://www.unige.ch/sciences/physique/tp/tpe/PDF/O1.pdf

a, ai, b, bi, fa, fb, h, i, aih, bih = symbols("a ai b bi fa fb h i aih bih")

eq1 = 1./fa -  (1/a + 1/ai)
ob = b - ai
eq2 = 1/fb - (1/ob + 1/bi)
eq3 = i - b + bi


eq4 = h / aih + ai/a
eq5 = aih / bih + bi / ai

s2 = solve([eq1, eq2, eq3, eq4, eq5], [ai, bi, i, aih, bih])
EKOX(len(s2))
EKOX(s2)
EKOX('\n'.join(map(str, s2[0])))
