# Regression Study Notes

This is a collection of notes on regression analysis. We will cover the following topics:

- Simple linear regression with Simulated data
- Assumptions of linear regression
- Basic concepts of regression analysis
- Feature selection
- Model evaluation


## Simple Linear Regression with Simulated Data

We want to simulate the relationship between two variables, height and weight. We assume that there is a linear relationship between height and weight. This relationship follows the equation:

$$
\text{weight} = \beta_0 + \beta_1 \times \text{height} + \epsilon
$$

We will assume that the error term, $\epsilon$, follows a normal distribution with mean 0 and standard deviation 7. We will generate 500 samples of height and weight data and fit a linear regression model to the data.

