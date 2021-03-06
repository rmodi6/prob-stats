import math
import numpy as np
import matplotlib.pyplot as plt

# Compute pdf of normal distribution
def normal_pdf(x, mu, sigma):
	return (1 / (np.sqrt(2 * np.pi * np.square(sigma)))) * (np.power(np.e, -(np.square((x - mu)) / (2 * np.square(sigma)))))


# Part A
variance = 9
a, b2 = 0, 1
with open('q2_sigma3.dat') as file:
	for line in file.readlines():
		sample = [float(i) for i in line.strip().split(', ')]
		n = len(sample)
		se2 = variance / n
		sample_mean = sum(sample) / n
		x = ((b2 * sample_mean) + (se2 * a)) / (b2 + se2)
		y2 = (b2 * se2) / (b2 + se2)
		a, b2 = x, y2
		print('{}\t{}'.format(a, b2))
		sigma = math.sqrt(b2)
		x_points = np.linspace(a - 3*sigma, a + 3*sigma, 100)
		plt.plot(x_points, normal_pdf(x_points, a, sigma), label='\u03BC={:.2f} \u03C3={:.2f}'.format(a, sigma))

plt.title("q2_sigma3.dat")
plt.xlabel("x")
plt.ylabel("pdf(x)")
plt.legend(loc='upper left')
plt.show()


# Part B
variance = 10000
a, b2 = 0, 1
with open('q2_sigma100.dat') as file:
	for line in file.readlines():
		sample = [float(i) for i in line.strip().split(', ')]
		n = len(sample)
		se2 = variance / n
		sample_mean = sum(sample) / n
		x = ((b2 * sample_mean) + (se2 * a)) / (b2 + se2)
		y2 = (b2 * se2) / (b2 + se2)
		a, b2 = x, y2
		print('{}\t{}'.format(a, b2))
		sigma = math.sqrt(b2)
		x_points = np.linspace(a - 3*sigma, a + 3*sigma, 100)
		plt.plot(x_points, normal_pdf(x_points, a, sigma), label='\u03BC={:.2f} \u03C3={:.2f}'.format(a, sigma))

plt.title("q2_sigma100.dat")
plt.xlabel("x")
plt.ylabel("pdf(x)")
plt.legend(loc='upper left')
plt.show()