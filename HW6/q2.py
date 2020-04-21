import math
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Part A
variance = 9
n = 100
se2 = variance / n
a, b2 = 0, 1
with open('q2_sigma3.dat') as file:
	for line in file.readlines():
		sample = [float(i) for i in line.strip().split(', ')]
		sample_mean = sum(sample) / n
		x = ((b2 * sample_mean) + (se2 * a)) / (b2 + se2)
		y2 = (b2 * se2) / (b2 + se2)
		a, b2 = x, y2
		print('{}\t{}'.format(a, b2))
		sigma = math.sqrt(b2)
		x_points = np.linspace(a - 3*sigma, a + 3*sigma, 100)
		plt.plot(x_points, stats.norm.pdf(x_points, a, sigma), label='\u03BC={:.2f} \u03C3={:.2f}'.format(a, sigma))

plt.title("q2_sigma3.dat")
plt.xlabel("x")
plt.ylabel("pdf(x)")
plt.legend(loc='upper left')
plt.show()