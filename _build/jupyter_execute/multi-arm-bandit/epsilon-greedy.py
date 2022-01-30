#!/usr/bin/env python
# coding: utf-8

# # 4.1. Epsilon-Greedy
# 
# Epsilon-Greedy is the most important algorithm of this section as the subsequent solutions use epsilon-greedy inherently. While methods like UCB perform better than epsilon-greedy in most cases, the structure of the algorithms remaining mostly the same.
# 
# #### Need of epsilon-greedy.
# 
# In our previous casino example with 2 slot machines, we have observed how a naive greedy approach of choosing a slot with maximum likelihood can yield detrimental results.
# 
# <span class = "hital">Greedy approach</span>
# 
# - Roughly means being short-sighted
# - Using only immediate available information as a heuristic.
# 
# In our case being greedy is to pick the slot machine with highest “Maximum Likelihood Estimate” without any regard to how much data we collect or about the confidence of selection.
# 
# Epsilon-greedy is an approach that says “instead of going the greedy approach every single time, we shall have a small probability and explore slot machines at random.” without any regard to its win-rate.
# 
# This small probability is denoted by $\epsilon$ and its value is typically 5%, 10%

# The reason we explore is to collect more information about each bandit so that the probability estimates of each bandit can be closer to the their actual probability values.
# 
# Let’s say we have two slots with probability of rewards 0.9 and 0.8 respectively, then by using epsilon-greedy approach our estimated reward becomes:
# 
# $$\mathbb{E}(R) = (1-\epsilon)0.9 + \epsilon(\frac{0.8+0.9}{2})$$
# 
# One option to improve this behavior is to have a decaying epsilon over the time.
# 
# $$\epsilon(t) \propto 1/t, \enspace \epsilon(t) = max(\epsilon_0-kt, \epsilon_{min}), \enspace \epsilon(t) = \epsilon_0 \alpha^t, \enspace \epsilon(t)=\frac{a}{log(bt+c)}$$
# 
# ### Calculating a Sample Mean
# 
# Sample mean: 
# 
# $$\bar{X}_N = \frac{1}{N}\sum_{i=1}^{N}X_i$$
# 
# If the values of a random variable can only be 0 or 1 then the resultant distribution is bernoulli distribution and the sample mean is equal to the maximum likelihood estimate of the bernoulli parameter.
# 
# ### How to calculate sample mean?
# 
# One might suggest to take all the values of $x_i$ and sum over them to find $\bar{X}$. However, there is a problem here, we have to store all the values and the complexity of this calculation becomes $O(n)$. There is a way to make this calculation to O(1) complexity no matter how much data is collected.
# 
# This is done by storing previous sample mean.
# 
# $$
# \begin{align}
# \bar{X}_N &= \frac{1}{N}(\sum_{i=1}^{N}X_i+X_N) \\
# &= \frac{1}{N}((N-1)\bar X_{N-1}+X_N)
# \end{align}
# $$
# 
# This reduces the time complexity of finding sample mean at every step. We only need to store the previous sample mean, number of samples, newest sample at every step of sample mean calculation.

# In[1]:


## Multi-Arm Bandit code
import numpy as np
import matplotlib.pyplot as plt
Bandit_probs= [0.9,0.8,0.5]
epsilon = 0.01
num_trails = 10000

class Bandit:
    def __init__(self, prob):
        self.actual_prob = prob
        self.prob_estimate = 0
        self.N = 0
    def pull(self):
        return np.random.random()<self.actual_prob
    def update(self,x):
        self.N+=1
        self.prob_estimate+=(1/self.N)*(x-self.prob_estimate)
    
def experiment():
    bandits = [Bandit(p) for p in Bandit_probs]
    rewards = np.zeros(num_trails)
    num_explored = 0
    num_exploited = 0
    num_optimal = 0
    optimal_j = np.argmax([b.actual_prob for b in bandits])
    for i in range(num_trails):
        if np.random.random()<epsilon:
            num_explored +=1
            j = np.random.choice(len(bandits))
        else:
            num_exploited +=1
            j = np.argmax([b.prob_estimate for b in bandits])
            if j == optimal_j:
                num_optimal+=1
        
        rewards[i] = bandits[j].pull()
        bandits[j].update(rewards[i])
    for b in bandits:
        print("Estimated probabilities", b.prob_estimate)
        
    print("Total reward earned = ", rewards.sum())
    print("Overall win rate = ", rewards.sum()/num_trails)
    print("Number of times explored = ", num_explored)
    print("Number of times exploited = ", num_exploited)
    print("Number of optimal pulls = ", num_optimal)
    
    #plot the results
    cummulative_rewards = np.cumsum(rewards)
    win_rates = cummulative_rewards/(np.arange(num_trails)+1)
    plt.plot(win_rates, label = "predicted estimates")
    plt.plot(np.ones(num_trails)*np.max(Bandit_probs), label = 'actual probability')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    experiment()


# ### Rewards for different epsilon values

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

class Bandit:
  def __init__(self, m):
    self.m = m
    self.mean = 0
    self.N = 0

  def pull(self):
    return np.random.randn() + self.m

  def update(self, x):
    self.N += 1
    self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N*x

def run_experiment(m1, m2, m3, eps, N):
  bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

  data = np.empty(N)
  
  for i in range(N):
    # epsilon greedy
    p = np.random.random()
    if p < eps:
      j = np.random.choice(3)
    else:
      j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)
    
    # for the plot
    data[i] = x
  cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

  # plot moving average ctr
  # for b in bandits:
  #   print(b.mean)

  return cumulative_average

if __name__ == '__main__':
  c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000)
  c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000)
  c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)

  # log scale plot
  plt.plot(c_1, label='eps = 0.1')
  plt.plot(c_05, label='eps = 0.05')
  plt.plot(c_01, label='eps = 0.01')
  plt.legend()
  plt.xscale('log')
  plt.title("Comparing rewards for different epsilon values (log scale)")
  plt.show()

  # linear plot
  plt.plot(c_1, label='eps = 0.1')
  plt.plot(c_05, label='eps = 0.05')
  plt.plot(c_01, label='eps = 0.01')
  plt.title("Comparing rewards for different epsilon values (linear scale)")
  plt.legend()
  plt.show()


# From the above graphs it can be inferred that for large values of epsilon, the model tries to explore more and as a result, larger initial rewards can be received. However, smaller epsilon means less exploring and the final estimates will be very closer to the actual probabilities. Using these results, epsilon values can be selected as required.
