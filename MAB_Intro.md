# [4.0] Multi-Arm Bandit Problem
In this section of the course we get introduced to the explore-exploit dilemma and the Multi-Arm bandit problem.

#### Explore-Exploit dilemma

The Explore-Exploit dilemma can be best understood with the casino example. Let's say you walk into a casino and find two slot machines. You either win or lose, there is no in between. The reward is either \$1 or \$0.

<span class = 'hital'>At this moment there is no real advantage of choosing one slot machine over another because there is no prior information.</span>

Let’s say we picked slot machine 1 and lost. At this point we still do not have any information about slot 2. Think about which slot machine would you pick during the second try and why? We would pick slot 2 right? This is partly because of probability.

$$P(\text{success}) = \frac{\text{Number of successful events}}{\text{Total events}}$$

For slot 1 → P = 0

For slot 2 → P = undefined.

Our gut says that somehow undefined is better than 0 and we want to explore the other slot machine, although you cannot compare them numerically.

Let’s say you picked slot 2 and won. Which one do we play next? We would pick slot 2 as $P(2) =1$ and $P(0) = 0$. <span class = 'nital'>In terms of probability, these estimates are what we call Maximum likelihood estimates and the process of picking the slot machine with maximum likelihood is called ‘Greedy approach’.</span>

Is there something wrong with this method of choosing? Consider we played slot machine 2 ten times and won only once, there would be more disagreement about which machine to choose next and something tells us to choose slot 1 instead of quantitative proof that slot 2 is better. Is there a way to algorithmically model this intuition?

#### Statistical approach towards choosing slot machines.

Statisticians would say that the above approach is totally wrong. One would say that the ‘correct’ way is to decide ‘How much data to collect before walking into the casino?’, the statistical power of the experiment and the effect size. However, one major question here is that ‘How do you know the effect size without playing the machines?’

Let’s say you decided to play each machine 10000 times and slot machine 1 → 3 rewards and slot machine 2 → 4000 times, but you cannot stop the experiment and play each slot 10,000 times. This would result in the loss of several coins just to understand the reward approximation by slot machines.

#### Adaptation

Thus, we require a new method that can adapt based on recent findings and estimates of probability of slot machines. This the exact intuition that we initially had while choosing slot machines. In this section, we shall model the intuition algorithmically.

We have two opposing forces (kind of):

1. To be a good statistician and collect as much data as possible (exploration)
2. Pick the machine with highest probability estimate (exploitation)

As these two forces oppose each other, we call this as the explore-exploit dilemma.

Rest of the section deals about ways to overcome this explore-exploit dilemma using several algorithms including,

1. Epsilon-greedy method
2. Optimistic Initial Values
3. UCB1
4. Thompson Sampling (Bayesian Bandit)

These methods can be used in A/B testing. These methods are adaptive.

#### Applications of Explore-Exploit Dilemma

The concept of comparing things to see which one is better can be applied to any business. Let's say a mobile manufacturing company made a brand new phone and their designer has created two ads and wants to decide on which ad is better. You have to choose the ad which the user is most likely to click and buy your phone. One way to decide is using “Click-Through Rate” of each ad.

$$\text{CTR} = \frac{\text{Number of clicks}}{\text{Total number of impressions}}$$

Doing an experiment seems to be the best choice to decide which ad to choose, but as per probability ‘to reach absolute precision is to collect infinite samples.’ However, if I show the worse advertisement 1 million times, that means I have wasted 1 million impressions to get a sub-optimal CTR.

<span class = 'hital'>In other words, my desire to show the best advertisement always is fundamentally at odds with my desire to find accurate CTRs for each advertisement.</span>

Numerous online businesses have advertisements at their core and these concepts can be applied to almost all of such businesses. One need not even be an established business to apply these techniques. Assuming you have traffic and one or more choices to choose from, the concept of Multi-Arm Bandit (MAB) can be applied to many applications including the following:

- Compare viewing time on old design vs new design
- Is “Buy Now” button better at the top or bottom of sales pages?
- Which “price ending” leads to the most conversions? \$20 vs \$19.99 vs \$19.98?

For practice both CTR and conversion rate are calculate similarly because they are a generic measure of “success rate”.

Another example is the news feed recommendation for apps like Facebook, New York Times. When people click on feed they see more ads, with more ads, more products can be bought and hence more conversion rate. This is the cycle of life ;) 

#### Summary

This section is to introduce you to the explore-exploit dilemma and how its applications are used in almost all business. These concepts can be used to decide between items such as ‘which headline?’, ‘which post?’, ‘which ad?’ and so on.
