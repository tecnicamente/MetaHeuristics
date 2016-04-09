# -*- coding: utf-8 -*-
"""
	A simple implementation of simulated annealing for the minimization of 2D function.
"""
	
import matplotlib.pyplot as plt
import math
import numpy as np
import random


def f(x):
	""" funzione da minimizzare"""
	return x**4 - 4*x**2 + 2*x -1
	#return (x**2 +1)/x
	
def Prob(ActualSolution, ProposedSolution,t):
	"""Calcolo probabilita' di accettare una soluzzione peggiorativa """
	"""prob(deltaE) = exp(-DeltaE/(k*t))							"""
	"""E -> Enegy level												"""
	"""k -> Iteration at same temperature							"""
	ProbValue = math.exp(-(f(ProposedSolution) - f(ActualSolution))/t)
	return ProbValue

# MAIN 

# Proces parameters
t       = 500		# Starting temperatures
nrep    = 3			# Number of repetitions for each temperature
LowerBound 	= -100000
UpperBound 	= 100000

StartingSolution 	= random.randint(LowerBound,UpperBound)
Solution			= StartingSolution
E					= f(StartingSolution)

k=0
z=0

plt.plot(np.linspace(LowerBound, UpperBound, 1000),f(np.linspace(LowerBound, UpperBound, 1000)))

	
while t>1:
	for i in range(1,nrep+1):
		x = random.randint(LowerBound, UpperBound)
		delta = f(x) - E
		z=z+1
		if delta > 0:
			if (random.random() < Prob(Solution,x,t)):
				Solution = x
				E = f(x)
		else:
			Solution = x
			E = f(x)
	k=k+1
	t = t - 1/(math.log(1+k))

	plt.plot(Solution,E,'bo')

plt.plot(Solution,E,'bo')

plt.show()
