#!/usr/bin/env python
# coding: utf-8

# # Content with notebooks
# 
# You can also create content with Jupyter Notebooks. This means that you can include
# code blocks and their outputs in your book.
# 
# ## Markdown + notebooks
# 
# As it is markdown, you can embed images, HTML, etc into your posts!
# 
# You can also $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# or
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# 
# ## MyST markdown
# 
# MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# ## Code blocks and outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[10]:


import plotly.express as px
data = px.data.iris()
data.head()


# In[20]:


# import altair as alt
# alt.Chart(data=data).mark_point().encode(
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     size='sepal_length'
# )


# In[19]:


# import plotly.io as pio
# import plotly.express as px
# import plotly.offline as py

# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="sepal_length")
# fig


# In[21]:


# p = figure()
# p.circle(data["sepal_width"], data["sepal_length"], fill_color=data["species"], size=data["sepal_length"])
# show(p)


# In[22]:


# import ipywidgets as widgets
# widgets.IntSlider(
#     value=7,
#     min=0,
#     max=10,
#     step=1,
#     description='Test:',
#     disabled=False,
#     continuous_update=False,
#     orientation='horizontal',
#     readout=True,
#     readout_format='d'
# )


# In[23]:


# tab_contents = ['P0', 'P1', 'P2', 'P3', 'P4']
# children = [widgets.Text(description=name) for name in tab_contents]
# tab = widgets.Tab()
# tab.children = children
# for ii in range(len(children)):
#     tab.set_title(ii, f"tab_{ii}")
# tab


# In[8]:


from bokeh.plotting import figure, show, output_notebook
output_notebook()


# In[24]:


# p = figure()
# p.circle(data["sepal_width"], data["sepal_length"], fill_color=data["species"], size=data["sepal_length"])
# show(p)


# In[25]:


# from matplotlib import rcParams, cycler
# import matplotlib.pyplot as plt
# import numpy as np
# plt.ion()
# plt.show()


# ```

# 

# In[18]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
