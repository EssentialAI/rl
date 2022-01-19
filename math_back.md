# [2.0] Mathematical Background

This chapter discusses the essential mathematics for Reinforcement Learning and Data Science. Jumping directly into coding RL agents without strong mathematical background is never recommended.

While there are multiple definitions for Data Science (and Reinforcement Learning) from several perspectives like Software Engineer, Machine Learning Scientist, the core concept of <span class = 'high'>Uncertainty</span> remains common.

We choose to learn from data because we believe that the latent information is embedded in the data — unprocessed, contains noise, and could have missing entries. If there is no randomness, all data scientists can close their business because there is simply no problem to solve. Therefore, data science is the subject of making decisions in uncertainty.

```{admonition} Note
:class: tip
See [Multi-Arm Bandit Chapter](MAB_Intro.md) for details about "Decision making under Uncertainty"
```

The mathematics of analyzing uncertainty is <span class = 'high'>Probability.</span> It is the tool to help us model, analyze, and predict random events. Probability is a vast topic and certainly deserves it's own chapter in this book. (See table of contents).

The topics in this chapter are meant to review familiar concepts of undergraduate algebra and calculus. These topics are meant to warm up your mathematics background so that you can follow the subsequent chapters. This chapter starts with details about [Infinite Series](MAB_Intro.md), something that will be used frequently to evaluate the expectation and variance of random variables. Next we move on to [Taylor Approximation](MAB_Intro.md), which will be helpful when we discuss continuous random variables. The next section deals with review of integration alongside providing several tricks to make integration easy. The last two sections of the chapter deal with [Linear Algebra](math_back.md) and details about [Permutations and Combinations](math_back.md), basic techniques to count events.


