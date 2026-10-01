
Intro to Plotly Codelab
=======================

`Plotly <https://plotly.com/python/>`_ is a graphing library. Unlike a picture of a graph, plotly graphs are
interactive: you can hover over a point to see its exact values, click and drag to zoom in, and click on a legend
entry to hide or show it. All of the graphs in our scouting app are made with plotly.

For the most part, we use `Plotly Express <https://plotly.com/python/plotly-express/>`_, which works well with 
pandas dataframes. You can also use `Plotly Graph Objects <https://plotly.com/python/graph-objects/>`_ which is
a more manual version if you need more customization or features.


The Dataset
-----------

Plotly comes with a few built in datasets that are handy for practicing. We will use the **tips** dataset for all
of the examples on this page as opposed to scouted data:

.. code-block:: pycon

    >>> df.head()

       total_bill   tip     sex smoker  day    time  size
    0       16.99  1.01  Female     No  Sun  Dinner     2
    1       10.34  1.66    Male     No  Sun  Dinner     3
    2       21.01  3.50    Male     No  Sun  Dinner     3
    3       23.68  3.31    Male     No  Sun  Dinner     2
    4       24.59  3.61  Female     No  Sun  Dinner     4

Each row is one meal at a restaurant: how big the bill was, how much the customer tipped, what day it was, and
some info about the party. There are 244 meals spread across 4 days.


Scatter Plots
-------------

A scatter plot draws one dot for each row, with one column on the x axis and another on the y axis.

.. code-block:: python

    fig = px.scatter(df, x="total_bill", y="tip", color="time", title="Tip vs. Total Bill")

.. raw:: html
    :file: figures/scatter.html

The :code:`color` argument gives each dot a color based on another column. It works on almost every plotly express
function.

Scatter Plot of Averages
________________________

Plotting every row can get busy. Usually in charts like this we care about a teams average performance

.. code-block:: python

    day_averages = df.groupby("day").mean(numeric_only=True).reset_index()

    fig = px.scatter(day_averages, x="total_bill", y="tip", text="day", title="Average Tip vs. Average Bill per Day")
    fig.update_traces(textposition="top center")

.. raw:: html
    :file: figures/scatter_average.html

Note:

* :code:`text="day"` writes the day next to each dot, so you can tell which dot is which without hovering.
  :code:`update_traces(textposition="top center")` moves the label so it isn't on top of the dot.


Box and Whisker Plots
---------------------

Sometimes we do want to see a representation of a teams representation across matches, rather than just their average.
A box and whisker plot shows the spread of the data, and can tell you what a teams ceiling, floor, mean values are, and
illustrate their consistency across matches

.. code-block:: python

    fig = px.box(df, x="day", y="tip", points="all", title="Tips per Day")

.. raw:: html
    :file: figures/box.html

Note:

* :code:`points="all"` draws every row next to the box, which is can be nice when there are only a few rows per group


Bar Charts
----------

.. code-block:: python

    day_averages = df.groupby("day").mean(numeric_only=True).reset_index()
    day_averages = day_averages.sort_values("tip", ascending=False)

    fig = px.bar(day_averages, x="day", y="tip", title="Average Tip per Day")

.. raw:: html
    :file: figures/bar.html


Stacked Bar Charts
------------------

A stacked bar chart is a bar chart where each bar is split into colored pieces.

Counting
________

To count how often something happened, group by **both** columns and use :code:`size()`:

.. code-block:: python

    smoker_counts = df.groupby(["day", "smoker"]).size().reset_index(name="count")

    fig = px.bar(smoker_counts, x="day", y="count", color="smoker", title="Number of Meals per Day")

.. raw:: html
    :file: figures/stacked_count.html

.. tip::

    Plotly can do the counting for you. :code:`px.histogram(df, x="day", color="smoker")` makes the same graph
    without the :code:`groupby`.

If you'd rather see the bars next to each other instead of stacked, add :code:`barmode="group"` to :code:`px.bar`.

Counts vs. Totals
_________________

Swap :code:`size()` for :code:`sum()` of a column and the same chart now shows how much each group added up to
instead of how often it happened:

.. code-block:: python

    smoker_tips = df.groupby(["day", "smoker"])["tip"].sum().reset_index()

    fig = px.bar(smoker_tips, x="day", y="tip", color="smoker", title="Total Tips per Day")

.. raw:: html
    :file: figures/stacked_sum.html


Stacking Columns
________________

Sometimes the pieces of the bar are different columns instead of the values in one column. In that case, pass a
list of columns as :code:`y`:

.. code-block:: python

    day_averages = df.groupby("day").mean(numeric_only=True).reset_index()

    fig = px.bar(day_averages, x="day", y=["total_bill", "tip"], title="Average Amount Paid per Day")

.. raw:: html
    :file: figures/stacked_columns.html


Pie Charts
----------

If you only give :code:`names`, plotly counts how many rows fall into each group:

.. code-block:: python

    fig = px.pie(df, names="day", title="Number of Meals per Day")

.. raw:: html
    :file: figures/pie_count.html

If you also give :code:`values`, plotly adds up that column for each group instead:

.. code-block:: python

    fig = px.pie(df, names="day", values="tip", title="Total Tips per Day")

.. raw:: html
    :file: figures/pie_values.html



Making It Look Nice
-------------------

Every plotly express function takes the same handful of arguments to clean up a graph:

* :code:`title` puts a title on top
* :code:`labels` renames columns in the axes, legend and hover text, so people see "Tip ($)" instead of :code:`tip`
* :code:`hover_data` adds more columns to what you see when you hover over a point
* :code:`category_orders` sets the order of the groups, instead of the order they show up in the data

Anything else can be changed afterwards with :code:`fig.update_layout(...)`:

.. code-block:: python

    fig = px.box(
        df,
        x="day",
        y="tip",
        color="time",
        points="all",
        hover_data=["total_bill", "size"],
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        labels={"day": "Day of the Week", "tip": "Tip ($)", "time": "Meal", "total_bill": "Bill ($)", "size": "Party Size"},
        title="Tips per Day, Split by Meal",
    )
    fig.update_layout(legend_title_text="Which Meal?")

.. raw:: html
    :file: figures/customized.html

When you're working in a notebook, having :code:`fig` as the last line of a cell displays it. Anywhere else, call
:code:`fig.show()`.


Exercises
_________

Now that you've seen the core plotly concepts, put them to use on real data. Open
:code:`source/CL4_plotly_codelab.ipynb`, which loads actual FRC scouting data from
:code:`source/data/scouted_data.csv`, and fill in each numbered cell as described in its comment.
