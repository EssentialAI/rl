#!/usr/bin/env python
# coding: utf-8

# # [0.2] Probability Review
# The language of this course is going to be probability. Everything we discuss in this course will be based on undergraduate level probability. Probability is the study of uncertainty. The mathematical theory of probability is very sophisticated, and delves into a branch of analysis known as measure theory. In these notes, we provide a basic treatment of probability that does not address these finer details.
# 
# ## [0.2.1] Elements of Probability
# The basic setting for a probability model is the random experiment or random trial. This is your mental model of what is going on.<br>
# 
# ### Sample Space $S$ :
# 
# The set of all the outcomes of a random experiment. Here, each outcome $\omega \in S$ can be thought of as a complete description of the state of the real world at the end of the experiment.
# ```{admonition} Further reading 
# :class: dropdown, tip
# The sample space $S$ is the set of all possible oucomes of a random experiment.
# 
# Depending on the random experiment, $S$ may be finite, countably infinite and uncountably infinite. For a random coin toss, $S =\{H,T\}$ so $|S|=2$.
# 
# <span class = 'hital'>Other examples:</span>
# 
# (1) Roll a die: the outcome is the number on the upturned face, so $S = {1, 2, 3, 4, 5, 6}, |S| = 6.$
# 
# (2) Toss a coin until Heads appears: the outcome is the number of tosses required, so $S = {1, 2, 3, . . . }, |S| = ∞.$
# 
# (3) Choose a random number between 0 and 1: $S = [0, 1].$ (This is the first example of an uncountable sample space).
# 
# (4) Throw a dart at a circular dartboard: $S = \{(x, y) \in \mathbb{R}^2 | x^2 + y^2 \leq 1\}$
# 
# For this review of elementary probability we will restrict ourselves to finite and countably infinite sample spaces.
# ```
# 
# ### Set of events (or event space) $\mathcal{F}:$
# 
# A set whose elements, $A \in \mathcal{F}$ (called events) are subsets of $S$.
# 
# An event is a collection of possible outcomes of a random experiment. Usually write $A, B, . . .$ to denote events. So an event $A$ is a subset of $S$, the sample space, that is $A ⊂ S$. Usually an event contains the set of outcomes which make the answer to a question ‘Yes’. Saying ‘the outcome is in $A$’ is the same as saying ‘the event A is true’. There are two special events: the whole sample space S is called the certain or the sure event. The empty set ∅ is the null event.
# 
# ```{admonition} Further reading 
# :class: dropdown, tip
# We often want to combine events in various ways. There are 3 basic operations for combining events.
# 
# <span class = 'hital'>Complement:</span>
# 
# $E^c$ = not $E$ = collection of outcome not in $E$
# 
# <span class = 'hital'>Intersection:</span>
# 
# $E \cap F$ = $E$ and $F$ = collection of outcomes in both $E$ and $F$
# 
# <span class = 'hital'>Union:</span>
# 
# $E \cup F$ = $E$ or $F$ = collection of outcomes in either $E$ or $F$ or both
# ```
# ### Probaility measure :
# 
# A function $P:\mathcal{F} \rightarrow \mathbb{R}$ that satisfies the following properties,
# 
# <span class = 'hital'>$P(A) \geq 0$</span>, for all $A \in \mathcal{F}$.
# 
# <span class = 'hital'>$P(S) = 1$.</span>
# 
# If $A_1, A_2,..$ are disjoint events (i.e.,) $A_i \cap A_j = \phi$ whenever $i \neq j$, then:
# 
# <span class = 'hital'>$P(\cup_iA_i) = \sum_iP(A_i)$</span>
# 
# These three properties are called <span class = 'blue'>Axioms of Probability.</span>
# ```{admonition} Further reading
# :class: dropdown, tip 
# <span class = 'hital'>Consistency relations to be satisfied:</span>
# The basic step is that every event $E$ is assigned a probability $P(E)$. This is a number satisfying:
# 
# $0 \leq P(E) \leq 1$
# 
# <span class = 'hital'>Other consistency relations:</span>
# 
# (1) $P(E^c)=1-P(E)$
# 
# (2) $P(S)=1$
# 
# (3) if $E \subset F$ then $P(E) \leq P(F)$
# 
# <span class = 'nital'>if $E \cap F = \phi$ (aka $E$ and $F$ are disjoint) then:
# 
# (4) $P(E \cup F) = P(E)+P(F)$
# 
# (5) $P(E \cup F) = P(E)+P(F)-P(E \cap F)$
# 
# (6) if $E_1, E_2,...,E_n,..$ is a sequence of pairwise disjoint events, then
# 
# $$P(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^{\infty}P(E_n)$$
# 
# 
# The last property cannot be deduced from the previous relations which involve only finitely many sets. This property is called countable additivity.
# ```
# ### Conditional Probability:
# 
# Let $B$ be an event with non-zero probability. The conditional probability of any event $A$ given $B$ is defined as,
# 
# $$P(A|B) \doteq \frac{P(A \cap B)}{P(B)}$$
# 
# In other words, $P(A|B)$ is the probability measure of the event $A$ after observing the occurence of $B$.
# 
# ### Independence:
# 
# Two events are called independent if and only if $P(A \cap B) = P(A) \cdot P(B)$ (or equivalently, $P(A|B)=P(A)$). Therefore, independence is equivalent to saying that observing $B$ does not have any effect on the probability of $A$.
# ```{admonition} Further reading
# :class: dropdown, tip 
# Imagine the following 2-step thought experiment: you toss a coin; if it comes up Heads, you draw one card at random from a standard deck of cards; if it comes up Tails you draw two cards at random (without replacement). 
# 
# Let $A$ be the event that you get Heads on the coin toss, and let $B$ be the event that you draw at least one Ace from the deck. Then $P(B|A)$ is clearly $4/52 = 1/13$. What about $P(A \cap B)$? Imagine lining up all your many repeated experiments, then for approximately one-half of them the event $A$ will be true.
# 
# Out of these approximately, $1/13$ will have $B$ also true. So we expect $P(A \cap B) = (1/2)(1/13) = P(A) \cdot P(B|A)$. This line of reasoning leads to the result shown in the above equation.
# 
# It is important to note that $P(B|A)$ is defined only is $P(A) \neq 0$
# ```
