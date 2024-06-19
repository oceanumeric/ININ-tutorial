# Importance of Innovation

This is my lecture script for expaining the importance of innovation to my students. The lecture will be organized in the following manner:

- **Introduction**: I will introduce the concept of innovation and explain why it is important.
- **Types of Innovation**: I will explain the different types of innovation that exist.
- **Innovation in Business**: I will discuss how innovation is important in the business world.


Give me equation of normal distribution.

# Normal Distribution

The normal distribution is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. The normal distribution is also known as the Gaussian distribution.

$$
f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$


Give me a table that shows with four columns and three rows

# Table Example

| Column 1 | Column 2 | Column 3 | Column 4 |
|----------|----------|----------|----------|
| A1       | B1       | C1       | D1       |
| A2       | B2       | C2       | D2       |
| A3       | B3       | C3       | D3       |


Give me python code to simulate the normal distribution.

# Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, density=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.show()
```



