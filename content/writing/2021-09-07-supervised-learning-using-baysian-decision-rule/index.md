---
title: Supervised Learning Using Baysian Decision Rule
subtitle: Python Functions for Bayesian Learning (COSC 522 Project)
summary: Python Functions for Bayesian Learning (COSC 522 Project)
author: Harshvardhan
date: '2021-09-07'
slug: supervised-learning-using-baysian-decision-rule
tags:
- data-science
- machine-learning
- python
- r
cover:
  image: og.png
  hidden: true
---
In this project, I applied Bayesian decision theory for classification problem. The datasets used were from Ripley's Pattern Recognition and Neural Networks. The first dataset has two features and has a balanced class portfolio. The second dataset is for diabetes in Pima Indians with seven features where the number of diabetic patients is much less than the number of normal patients.

Codes to perform these calculations are in [this Github repository](https://github.com/harshvardhaniimi/cosc522-utk/tree/main/projects/Project%201).

The heart of this project was in three functions.

1.  **Euclidean Classifier**
2.  **Mahalanobis Classifier**
3.  **Bayesian Quadratic Classifier**

# Euclidean Classifier

-   The features are assumed to be statistically independent of each other (strictly speaking, no correlation) and have the same variance.

-   Geometrically, the samples would fall in a equal-radii hyperspherical cluster.

-   The decision boundary for a two class problem would be a hyperplane `\(d\)`-dimensions.

$$
\Sigma = 
\begin{bmatrix}
\sigma^2 \dots 0 \\
\vdots \ddots \vdots \\
0 \dots \sigma^2
\end{bmatrix}.
$$

$$
g_i(\vec{x}) = - \frac{||\vec{x} - \vec{\mu_i}||}{2\sigma^2} + \ln{P(\omega_i)}.
$$

## Python Function


```python
def euclid_classifier(xtrain, ytrain, xtest, ytest, pw):
    t1 = t.time()
    
    pw0 = pw
    pw1 = 1-pw

    nn, nf = xtest.shape

    # for class 0
    arr = xtrain[ytrain == 0]
    covs0 = np.cov(np.transpose(arr))
    means0 = np.mean(arr, axis = 0)

    # for class 1
    arr = xtrain[ytrain == 1]
    covs1 = np.cov(np.transpose(arr))
    means1 = np.mean(arr, axis = 0)

    # for euclidean distance
    covavg = (covs0+covs1)/2
    avg_var = np.mean(np.diagonal(covavg))

    # initialising yhat array
    yhat = np.ones(len(ytest))
    
    for i in range(len(ytest)):
        #for class 0
        d = np.dot(xtest[i]-means0, xtest[i]-means0)
        g0 = -d/(2*avg_var) + np.log(pw0)
        
        # for class 1
        d = np.dot(xtest[i]-means1, xtest[i]-means1)
        g1 = -d/(2*avg_var) + np.log(pw1)
        
        # if g0>g1, then i belongs to 0, else to 1
        if(g0>g1):
            yhat[i] = 0
            
    overall_acc = np.sum(yhat == ytest)/len(ytest)
    class0_acc = np.sum(yhat[ytest == 0] == 0)/np.sum(ytest == 0)
    class1_acc = np.sum(yhat[ytest == 1] == 1)/np.sum(ytest == 1)
    
    t2 = t.time()
    tt = t2-t1
    
    return yhat, overall_acc, class0_acc, class1_acc, tt
```

# Mahalanobis Classifier

-   The covariance matrices for all classes are identical but not identity (times `\(\sigma^2\)`). There is a constant variance.

-   Geometrically, the samples fall in a hyperellipsoidal shape.

-   Decision boundary is a hyperplane of `\(d\)`-dimensions.

$$
g_i(\vec{x}) = - \frac{1}{2}(\vec{x} - \vec{\mu_i})'\Sigma_i (\vec{x} - \vec{\mu_i}) + \ln{P(\omega_i)},
$$

where `\(\Sigma_i = \Sigma\)`.

## Python Function


```python
def maha_classifier(xtrain, ytrain, xtest, ytest, pw):
    t1 = t.time()
    
    pw0 = pw
    pw1 = 1-pw

    nn, nf = xtest.shape

    # for class 0
    arr = xtrain[ytrain == 0]
    covs0 = np.cov(np.transpose(arr))
    means0 = np.mean(arr, axis = 0)

    # for class 1
    arr = xtrain[ytrain == 1]
    covs1 = np.cov(np.transpose(arr))
    means1 = np.mean(arr, axis = 0)

    # for Mahalanobis distance, avg of the two covariance matrix is chosen
    covavg = (covs0+covs1)/2

    # initialising yhat array
    yhat = np.ones(len(ytest))
    
    for i in range(len(ytest)):
        #for class 0
        d = np.matmul(np.matmul(xtest[i]-means0, np.linalg.inv(covavg)), xtest[i]-means0)
        g0 = -d + np.log(pw0)
        
        # for class 1
        d = np.matmul(np.matmul(xtest[i]-means1, np.linalg.inv(covavg)), xtest[i]-means1)
        g1 = -d + np.log(pw1)
        
        # if g0>g1, then i belongs to 0, else to 1
        if(g0>g1):
            yhat[i] = 0
            
    overall_acc = np.sum(yhat == ytest)/len(ytest)
    class0_acc = np.sum(yhat[ytest == 0] == 0)/np.sum(ytest == 0)
    class1_acc = np.sum(yhat[ytest == 1] == 1)/np.sum(ytest == 1)

    t2 = t.time()
    tt = t2-t1
    
    return yhat, overall_acc, class0_acc, class1_acc, tt
```

# Bayesian (Quadratic) Classifier

-   The covariance matrix is different for different categories.

-   It is a quadratic classifier.

$$
g_i(\vec{x}) = -\frac{1}{2} (\vec{x} - \vec{\mu_i})'\Sigma_i (\vec{x} - \vec{\mu_i}) - \frac{1}{2} \ln{|\Sigma_i|} + \ln{P(\omega_i)}.
$$

## Python Function


```python
def bayes_classifier(xtrain, ytrain, xtest, ytest, pw):
    t1 = t.time()
    
    pw0 = pw
    pw1 = 1-pw

    nn, nf = xtest.shape

    # for class 0
    arr = xtrain[ytrain == 0]
    covs0 = np.cov(np.transpose(arr))
    means0 = np.mean(arr, axis = 0)

    # for class 1
    arr = xtrain[ytrain == 1]
    covs1 = np.cov(np.transpose(arr))
    means1 = np.mean(arr, axis = 0)

    # initialising yhat array
    yhat = np.ones(len(ytest))
    
    for i in range(len(ytest)):
        d = np.matmul(np.matmul(xtest[i]-means0, np.linalg.inv(covs0)), xtest[i]-means0) * -0.5
        g0 = -0.5*np.log(np.linalg.det(covs0)) + d + np.log(pw0)
        
        d = np.matmul(np.matmul(xtest[i]-means1, np.linalg.inv(covs1)), xtest[i]-means1) * -0.5
        g1 = -0.5*np.log(np.linalg.det(covs1)) + d + np.log(pw1)        
        
        # if g0>g1, then i belongs to 0, else to 1
        if(g0>g1):
            yhat[i] = 0
            
    overall_acc = np.sum(yhat == ytest)/len(ytest)
    class0_acc = np.sum(yhat[ytest == 0] == 0)/np.sum(ytest == 0)
    class1_acc = np.sum(yhat[ytest == 1] == 1)/np.sum(ytest == 1)
    
    t2 = t.time()
    tt = t2-t1
    
    return yhat, overall_acc, class0_acc, class1_acc, tt
```
