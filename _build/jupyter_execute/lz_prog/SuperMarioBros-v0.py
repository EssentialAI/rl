#!/usr/bin/env python
# coding: utf-8

# ### [0.2] RL Example

# In[ ]:


import tensorflow as tf
import random
import gym
from collections import deque
import gym_super_mario_bros
from gym_super_mario_bros.actions import RIGHT_ONLY
from nes_py.wrappers import JoypadSpace
from IPython.display import clear_output


# In[3]:


env = gym_super_mario_bros.make("SuperMarioBros-v0")
env = JoypadSpace(env, RIGHT_ONLY)


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
total_reward = 0
done = True

for step in range(1000):
    env.render()
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    print(info)
    total_reward+=reward
    clear_output(wait = True)
env.close()


# <img src="../images/mario.gif" align="center"/>
