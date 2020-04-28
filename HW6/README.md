# Assignment 6

### Question 2
The conjugate prior for θ is taken to be Standard Normal (mean 0, variance 1). The mean and variance of the posterior distribution in each step is calculated using the results of Q1 (a).

(a)

| mean        | variance      |
|-------------|---------------|
| 4.590762414 | 0.08256880734 |
| 4.813523613 | 0.04306220096 |
| 4.921256878 | 0.02912621359 |
| 4.972837412 | 0.02200488998 |
| 4.983966098 | 0.01768172888 |

![q2_sigma3.png](https://raw.githubusercontent.com/rmodi6/CSE544/master/HW6/q2_sigma3.png)

We can observe that for the initial steps the variance is high meaning the bayesian inference is  less confident for the mean value but as we see more data with each step the bayesian inference gets more and more confident about the mean value (converging towards a particular value) and the variance of the posterior distribution keeps on decreasing. So with each progressing step, the estimate for the θ value is better with a smaller posterior interval.

(b)

| mean          | variance     |
|---------------|--------------|
| 0.05871624148 | 0.9900990099 |
| 0.09500866962 | 0.9803921569 |
| 0.1382262615  | 0.9708737864 |
| 0.1712188335  | 0.9615384615 |
| 0.218918245   | 0.9523809524 |

![q2_sigma100.png](https://raw.githubusercontent.com/rmodi6/CSE544/master/HW6/q2_sigma100.png)

We can observe that for each step the mean keeps on increasing constantly by ~0.04 (does not seem to be converging) and variance of the posterior distribution does not decrease much. The pdf of the posterior distribution of step 5 is very similar to that of step 1 just moved slightly towards right. The confidence (posterior interval) for the estimate of θ is pretty much the same for each step.

(c) Comparing (a) and (b) we observe that bayesian inference works well when the variance (std. dev.) of the distribution of the samples is low with a converging value for mean with each progressing step. Incase of high variance of the samples’ distribution, the mean computed from the bayesian inference does not converge. 
