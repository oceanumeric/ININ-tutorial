# Tutorial 2 

Today I am taking the second tutorial of the course. The goal of this tutorial is to learn basics of regression analysis.^

Here is the outline of the tutorial:

1. Simulate data
2. Fit a linear regression model
3. Evaluate the model


## 1. Simulate data

We will simulate a simple linear regression model. The model is to simulate people's weight based on their height. The model is defined as:

$$
\text{weight} = 50 + 0.5 \times \text{height} + \epsilon
$$

where $\epsilon$ is a random noise term. 

```python
import numpy as np
import pandas as pd

np.random.seed(0)
n = 100
height = np.random.normal(160, 10, n)
weight = 50 + 0.5 * height + np.random.normal(0, 5, n)

data = pd.DataFrame({'height': height, 'weight': weight})
data.head()
```

Now I want the code that could be used to plot the histogram of the height and weight.

```python
import matplotlib.pyplot as plt

plt.hist(data['height'], bins=20)
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()
```


Now, I want to plot the scatter plot of height and weight.

```python
plt.scatter(data['height'], data['weight'])
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
```

Now, I want to the data to csv file.

```python
data.to_csv('data.csv', index=False)
```