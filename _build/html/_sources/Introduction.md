# Introduction
Add some introduction about Reinforcement Learning here. @Naresh Kumar Devulapally

#### Concepts' Warmup
The language of this course is going to be probability. Everything we discuss in this course will be based on undergraduate level probability.
```{admonition} Question 1
:class: tip
We have two probability distributions $P(A,B)$ and $P(A|B)$. What do we call these distributions?
```
```{admonition} Answer 1
:class: dropdown
$P(A,B)$ (also denoted as $P(A,B)$ is called **Joint Probability**. Joint Probability is a statistical measure that calculates the likelihood of two events occuring together and at the same point in time.

![](/images/p(a_and_b).png)

Joint probability is a measure of two events happening at the same time, and can only be applied to situations where more than one observation can occur at the same time. For example, from a deck of $52$ cards, the joint probability of picking up a card that is both red and $6$ is $P(6 ∩ red) = 2/52 = 1/26$, since a deck of cards has two red sixes—the six of hearts and the six of diamonds. Because the events "$6$" and "red" are independent in this example, you can also use the following formula to calculate the joint probability:

$$P(6 \cap red) = P(6) \times P(red) = 4/52 \times 26/52 = 1/26$$

**Joint probability should not be confused with conditional probability (denoted by $P(A|B)$), which is the probability that one event will happen given that another action or event happens.**
```

Duplicate Description

Joint probability is a measure of two events happening at the same time, and can only be applied to situations where more than one observation can occur at the same time. For example, from a deck of $52$ cards, the joint probability of picking up a card that is both red and $6$ is $P(6 ∩ red) = 2/52 = 1/26$, since a deck of cards has two red sixes—the six of hearts and the six of diamonds. Because the events "$6$" and "red" are independent in this example, you can also use the following formula to calculate the joint probability:

$$P(6 \cap red) = P(6) \times P(red) = 4/52 \times 26/52 = 1/26$$

**Joint probability should not be confused with conditional probability (denoted by $P(A|B)$), which is the probability that one event will happen given that another action or event happens.**
```

#### Using a directive

At its simplest, you can insert a directive into your book's content like so:

````
```{mydirectivename}
My directive content
```
````
<!-- ![](https://static.vecteezy.com/system/resources/previews/000/622/564/original/ai-concept-vector.jpg) -->
This will only work if a directive with name `mydirectivename` already exists
(which it doesn't). There are many pre-defined directives associated with
Jupyter Book. For example, to insert a note box into your content, you can
use the following directive:

````
```{note}
Here is a note
```
````

This results in:

```{note}
Here is a note
```

In your built book.

For more information on writing directives, see the
[MyST documentation](https://myst-parser.readthedocs.io/).


### Using a role

Roles are very similar to directives, but they are less-complex and written
entirely on one line. You can insert a role into your book's content with
this pattern:

```
Some content {rolename}`and here is my role's content!`
```

Again, roles will only work if `rolename` is a valid role's name. For example,
the `doc` role can be used to refer to another page in your book. You can
refer directly to another page by its relative path. For example, the
role syntax `` {doc}`intro` `` will result in: {doc}`intro`.

For more information on writing roles, see the
[MyST documentation](https://myst-parser.readthedocs.io/).


### Adding a citation

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

````
```{bibliography}
```
````

Resulting in a rendered bibliography that looks like:

```{bibliography}
```


### Executing code in your markdown files

If you'd like to include computational content inside these markdown files,
you can use MyST Markdown to define cells that will be executed when your
book is built. Jupyter Book uses *jupytext* to do this.

First, add Jupytext metadata to the file. For example, to add Jupytext metadata
to this markdown page, run this command:

```
jupyter-book myst init markdown.md
```

Once a markdown file has Jupytext metadata in it, you can add the following
directive to run the code at build time:

````
```{code-cell}
print("Here is some code to execute")
```
````

When your book is built, the contents of any `{code-cell}` blocks will be
executed with your default Jupyter kernel, and their outputs will be displayed
in-line with the rest of your content.

For more information about executing computational content with Jupyter Book,
see [The MyST-NB documentation](https://myst-nb.readthedocs.io/).
