<!-- #region -->
# Notations

* <span style="color:blue;">**Overall notations**</span>

\begin{align}
\doteq \enspace & \leftarrow \enspace \textrm{equivalent relationship that is true by definition}\\
\approx \enspace & \leftarrow \enspace \textrm{approximately equal}\\
\propto \enspace & \leftarrow \enspace \textrm{proportional to}\\
P(X=x) \enspace & \leftarrow \enspace \textrm{Probability that a random variable $X$ takes on the value $x$}\\
\mathbb{E}[X] \enspace & \leftarrow \enspace \textrm{Expectation of a random variable $X$, $\mathbb{E}[X] \doteq \sum_{x}p(x)x$}\\
argmax_a f(a) \enspace & \leftarrow \enspace \textrm{a value of $a$ at which $f(a)$ takes its maximum value}\\
lnx \enspace & \leftarrow \enspace \textrm{natural logarithm of $x$}\\
e^x \enspace & \leftarrow \enspace \textrm{the base of the natural logarithm, $e \approx 2.718$}\\
\mathbb{R} \enspace & \leftarrow \enspace \textrm{set of real numbers}\\
f:X \rightarrow y  \enspace & \leftarrow \enspace \textrm{function $f$ from elements of set $X$ to elements of set $y$}\\
\leftarrow \enspace & \leftarrow \enspace \textrm{assignment}\\
(a,b] \enspace & \leftarrow \enspace \textrm{the real interval between $a$ and $b$ including $b$ but not $a$}\\
\varepsilon \enspace & \leftarrow \enspace \textrm{probability of taking a random action in an $\varepsilon$ - greedy policy}\\
\alpha , \beta \enspace & \leftarrow \enspace \textrm{step-size parameters}\\
\gamma \enspace & \leftarrow \enspace \textrm{discount-rate parameter}\\
\lambda \enspace & \leftarrow \enspace \textrm{decay-rate parameter for eligibility traces}\\


\end{align}
* <span style="color:blue;">**In a multi-arm bandit problem**</span>

\begin{align}
k \enspace & \leftarrow \enspace \textrm{number of actions (arms)}\\
t \enspace & \leftarrow \enspace \textrm{discrete time step or play number}\\
q_*(a) \enspace & \leftarrow \enspace \textrm{true value (expected reward) of action $a$}\\
Q_t(a) \enspace & \leftarrow \enspace \textrm{estimate at timme $t$ of $q_*(a)$}\\
N_t(a) \enspace & \leftarrow \enspace \textrm{number of times action $a$ has been selected up prior time $t$}\\
H_t(a) \enspace & \leftarrow \enspace \textrm{learned preference for selecting action $a$ at time $t$}\\
\pi_t(a) \enspace & \leftarrow \enspace \textrm{probability of selecting action $a$ at time $t$}\\
R_t \enspace & \leftarrow \enspace \textrm{estimate at time $t$ of the expected reward given $\pi_t$}\\
\end{align}

* <span style="color:blue;">**In a Markov Decision Process**</span>
\begin{align}
s, {s}' \enspace & \leftarrow \enspace \textrm{states}\\
a \enspace & \leftarrow \enspace \textrm{an action}\\
r \enspace & \leftarrow \enspace \textrm{a reward}\\
\mathcal{S} \enspace & \leftarrow \enspace \textrm{set of all nonterminal states}\\
\mathcal{S}^+ \enspace & \leftarrow \enspace \textrm{set of all states, including the terminal state}\\
\mathcal{A}(s) \enspace & \leftarrow \enspace \textrm{set of all actions available in state $s$}\\
\mathcal{R} \enspace & \leftarrow \enspace \textrm{set of all possible rewards, a finite subset of $\mathbb{R}$}\\
\subset \enspace & \leftarrow \enspace \textrm{subset of, e.g., $\mathcal{R} \subset \mathbb{R}$}\\
\in \enspace & \leftarrow \enspace \textrm{is an element of; e.g., $s \in \mathcal{S}$}\\
|\mathcal{S}| \enspace & \leftarrow \enspace \textrm{number of elements in set $\mathcal{S}$}\\
t \enspace & \leftarrow \enspace \textrm{discrete time step}\\
T, T_t \enspace & \leftarrow \enspace \textrm{final time step of an episode, or of the episode including time step $t$}\\
A_t \enspace & \leftarrow \enspace \textrm{action at time $t$}\\
S_t \enspace & \leftarrow \enspace \textrm{state at time $t$, typically due, stochastically, to $S_{t-1}$ and $A_{t-1}$}\\
R_t \enspace & \leftarrow \enspace \textrm{reward at time $t$, typically due, stochastically, to $S_{t-1}$ and $A_{t-1}$}\\
\pi \enspace & \leftarrow \enspace \textrm{Policy (decision-making rule)}\\
\pi(s) \enspace & \leftarrow \enspace \textrm{action taken in state $s$ under $deterministic$ policy $\pi$}\\
\pi(a|s) \enspace & \leftarrow \enspace \textrm{probability of taking action $a$ in state $s$ under $stochastic$ policy $\pi$}\\
G_t \enspace & \leftarrow \enspace \textrm{return following time $t$}\\
h \enspace & \leftarrow \enspace \textrm{horizon, the time step one looks up to in a forward view}\\
G_{t:t+n}, G_{t:h} \enspace & \leftarrow \enspace \textrm{$n$-step return from $t+1$ to $t+n$, or to $h$ (discounted and corrected)}\\
\bar{G_{t:h}} \enspace & \leftarrow \enspace \textrm{flat return (undiscounted and uncorrected) from $t+1$ to $h$}\\
{G_t}^{\lambda} \enspace & \leftarrow \enspace \textrm{$\lambda$-return}\\
{G_{t:h}}^{\lambda} \enspace & \leftarrow \enspace \textrm{truncated, corrected $\lambda$-return}\\
{G_t}^{\lambda s}, {G_t}^{\lambda a} \enspace & \leftarrow \enspace \textrm{$\lambda$-return, corrected by estimate state, or action, values}\\
p({s}',r|a,a) \enspace & \leftarrow \enspace \textrm{probability of transition to state ${s}'$ with reward $r$, from state $s$ and action $a$}\\
p({s}'|s,a) \enspace & \leftarrow \enspace \textrm{probability of transition to state {s}', from state $s$ taking action $a$}\\
r(s,a) \enspace & \leftarrow \enspace \textrm{expected immediate reward from state $s$ after action $a$}\\
r(s,a,{s}') \enspace & \leftarrow \enspace \textrm{expected immediate reward on transition from $s$ to ${s}'$ under action $a$}\\
v_{\pi}(s) \enspace & \leftarrow \enspace \textrm{value of state $s$ under policy $\pi$ (expected return)}\\
v_*(s) \enspace & \leftarrow \enspace \textrm{value of state $s$ under the optimal policy}\\
q_{\pi}(s,a) \enspace & \leftarrow \enspace \textrm{value of taking action $a$ in state $s$ under policy $\pi$}\\
q_{*}(s,a) \enspace & \leftarrow \enspace \textrm{value of taking action $a$ in state $s$ under the optimal policy}\\
V, V_t \enspace & \leftarrow \enspace \textrm{array estimate of state-value function $v_{\pi}$ or $v_{*}$}\\
Q, Q_t \enspace & \leftarrow \enspace \textrm{array estimates of action-value function $q_{\pi}$ or $q_*$}\\
V_t(s) \enspace & \leftarrow \enspace \textrm{expected approximate action value, e.g., $V_t(s) \doteq \sum_a \pi(a|s)Q_t(s,a)$}\\
U_t \enspace & \leftarrow \enspace \textrm{target for estimate at time $t$}\\
\delta_t \enspace & \leftarrow \enspace \textrm{temporal-difference (TD) error at $t$ (a random variable)}\\
{\delta_t}^s,{\delta_t}^a \enspace & \leftarrow \enspace \textrm{state-and action-specific forms of the TD error}\\
n \enspace & \leftarrow \enspace \textrm{in $n$-step methods, $n$ is the number of steps of bootstrapping}\\
d \enspace & \leftarrow \enspace \textrm{dimensionality-the number of components of $w$}\\
{d}' \enspace & \leftarrow \enspace \textrm{alternate dimensionality-the number of components of $\theta$}\\
\textbf{w},\textbf{w}_t \enspace & \leftarrow \enspace \textrm{$d$-vector of weights underlying an approximate value function }\\
w_i, w_{t,i} \enspace & \leftarrow \enspace \textrm{$i^{th}$ component of learnable weight vector}\\
\hat{v}(s, \textbf{w}) \enspace & \leftarrow \enspace \textrm{approximate value of state $s$ given weight vector $\textbf{w}$}\\
v_{\textbf{w}}(s) \enspace & \leftarrow \enspace \textrm{alternative notation for $\hat{v}(s, \textbf{w})$}\\
\hat{q}(s,a,\textbf{w}) \enspace & \leftarrow \enspace \textrm{approximate value of state-action pair $s,a$ given weight vector $\textbf{w}$}\\
\nabla \hat{v}(s,\textbf{w}) \enspace & \leftarrow \enspace \textrm{column vector of partial derivatives of $\hat{v}(s, \textbf{w})$ with respect to $\textbf{w}$ }\\
\nabla \hat{q}(s,a,\textbf{w}) \enspace & \leftarrow \enspace \textrm{column vector of partial derivatives of $\hat{q}(s,a,\textbf{w})$ with respect to $\textbf{w}$}\\
\textbf{x}(s) \enspace & \leftarrow \enspace \textrm{vector of features visible when in state $s$}\\
\textbf{x}(s,a) \enspace & \leftarrow \enspace \textrm{vector of features when in state $s$ taking action $a$}\\
x_i(s), x_i(s,a) \enspace & \leftarrow \enspace \textrm{$i^{th}$ component of vector $\textbf{x}(s)$ or $\textbf{x}(s,a)$}\\
\textbf{x}_t \enspace & \leftarrow \enspace \textrm{shorthand for $\textbf{x}(S_t)$ or $\textbf{x}(S_t,A_t)$}\\
\textbf{w}^T \textbf{x} \enspace & \leftarrow \enspace \textrm{inner product of vectors, $w^Tx \doteq \sum_i w_ix_i$}\\
\textbf{v}, \textbf{v}_t \enspace & \leftarrow \enspace \textrm{secondary $d$-vector of weights, used to learn $\textbf{w}$}\\
\textbf{z}_t \enspace & \leftarrow \enspace \textrm{$d$-vector of eligibility traces at time $t$}\\
\theta, \theta_t \enspace & \leftarrow \enspace \textrm{parameter vector of target policy}\\
\pi (a|s, \theta) \enspace & \leftarrow \enspace \textrm{probability of taking action $a$ in state $s$ given parameter vector $\theta$}\\
\pi_{\theta} \enspace & \leftarrow \enspace \textrm{policy corresponding to parameter $\theta$}\\
\nabla_{\pi}(a|s,\theta) \enspace & \leftarrow \enspace \textrm{column vector of partial derivatives of $\pi (a|s, \theta)$ with respect to $\theta$}\\
J(\theta) \enspace & \leftarrow \enspace \textrm{performance measure for the policy $\pi_{\theta}$}\\
\nabla J(\theta) \enspace & \leftarrow \enspace \textrm{column vector of partial derivatives of $J(\theta)$ with respect to $\theta$}\\
h(s,a,\theta) \enspace & \leftarrow \enspace \textrm{preference for selecting action $a$ in state $s$ based on $\theta$}\\
b(a|s) \enspace & \leftarrow \enspace \textrm{behavior policy used to select actions while learning about target policy $\pi$}\\
b(s) \enspace & \leftarrow \enspace \textrm{a baseline function $b:\mathcal{S}\rightarrow \mathbb{R}$ for policy-gradient methods}\\
b \enspace & \leftarrow \enspace \textrm{branching factor for an MDP or search tree}\\
\rho_{t:h} \enspace & \leftarrow \enspace \textrm{importance sampling ratio for time $t$ through time $h$}\\
\rho_t \enspace & \leftarrow \enspace \textrm{importance sampling ratio for time $t$ alone, $\rho_t \doteq \rho_{t:t}$}\\
r(\pi) \enspace & \leftarrow \enspace \textrm{average reward (reward rate) for policy $\pi$}\\
\bar{R}_t \enspace & \leftarrow \enspace \textrm{estimate of $r(\pi)$ at time $t$}\\
\mu(s) \enspace & \leftarrow \enspace \textrm{on-policy distribution over states}\\
\mu \enspace & \leftarrow \enspace \textrm{$|\mathcal{S}|$-vector of the $\mu(s)$ for all $s \in \mathcal{S}$}\\
\textbf{A} \enspace & \leftarrow \enspace \textrm{$d \times d$ matrix}\\
\textbf{b} \enspace & \leftarrow \enspace \textrm{$d$-dimensional vector}\\
\textbf{w}_{TD} \enspace & \leftarrow \enspace \textrm{TD fixed point $\textbf{w}_{TD} \doteq \textbf{A}^{-1}\textbf{b}$}\\
\textbf{I} \enspace & \leftarrow \enspace \textrm{Identity matrix}\\
\textbf{P} \enspace & \leftarrow \enspace \textrm{$|\mathcal{S}| \times |\mathcal{S}|$ matrix of state-transition probabilities under $\pi$}\\
\textbf{D} \enspace & \leftarrow \enspace \textrm{$|\mathcal{S}| \times |\mathcal{S}|$ diagonal matrix with $\mu$ on its diagonal}\\
\textbf{X} \enspace & \leftarrow \enspace \textrm{$|\mathcal{S}| \times d$ matrix with the $\textbf{x}(s)$ as rows}\\
{{||v||}_{\mu}}^2 \enspace & \leftarrow \enspace \textrm{$\mu$-weighted squared norm of the value function $v$, i.e., ${{||v||}_{\mu}}^2 \doteq \sum_{s \in \mathcal{S}} \mu(s)v(s)^2$}\\
\eta (s) \enspace & \leftarrow \enspace \textrm{expected number of visits to state $s$ per episode}\\
\prod \enspace & \leftarrow \enspace \textrm{projection operator for value functions}\\
B_{\pi} \enspace & \leftarrow \enspace \textrm{Bellaman operator for value functions}\\

\bar{\delta_w}(s) \enspace & \leftarrow \enspace \textrm{Bellman error}\\
\bar{\delta_w}, BE \enspace & \leftarrow \enspace \textrm{Bellman error vector}\\
\bar{VE}(\textbf{w}) \enspace & \leftarrow \enspace \textrm{mean square value error}\\
\bar{BE}(\textbf{w}) \enspace & \leftarrow \enspace \textrm{mean square Bellman error}\\
\bar{PBE}(\textbf{w}) \enspace & \leftarrow \enspace \textrm{mean square projected Bellman error}\\
\bar{TDE}(\textbf{w}) \enspace & \leftarrow \enspace \textrm{mean square }\\
\bar{RE}(\textbf{w}) \enspace & \leftarrow \enspace \textrm{mean square return error}
\end{align}
<!-- #endregion -->
