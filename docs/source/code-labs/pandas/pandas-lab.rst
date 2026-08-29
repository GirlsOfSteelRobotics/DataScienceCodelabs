
Intro to Pandas Codelab
=======================

`Pandas <https://pandas.pydata.org/>`_ is a data analysis and manipulation tool. We use it on the data science
team to look at certain pieces of data, look at averages, plot it, and more.

Pandas works with dataframes, which feel very similar to an Excel Spreadsheet / Google Sheets table. Dataframes
are often organized into rows and columns.


Introduction
------------

.. code-block:: python

    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Sam', 'Charlie', 'Tom'],
        'Age': [25, 30, 35, 30, 42],
        'City': ['New York', 'London', 'Paris', 'Pittsburgh', "Rochester"]
    })

.. TODO: insert rendered image of df

Quering Data
------------

We can query the dataframe for a **query where** something something is :code:`true`

For example:

.. code-block:: pycon

    >>> df["Age"] == 30  # Which rows have the an age of 30?

    0    False
    1     True
    2    False
    3     True
    4    False
    Name: Age, dtype: bool

A more common usage is to **filter** the data based on your conditional:

.. code-block:: pycon

    >>> indices = df["Age"] > 30  # Which rows have the an age of over 30?
    >>> df[indices]

        Name  Age        City
    2    Sam   35       Paris
    4    Tom   42   Rochester

You can of course also do it without making the :code:`indices` local variable and do it all in one line:

.. code-block:: pycon

    >>> df[df["Age"] == 30]

          Name  Age        City
    1      Bob   30      London
    3  Charlie   30  Pittsburgh


Manipulating Columns
---------------------

We can also rename columns:

.. code-block:: pycon

    >>> df["Name"].rename("First Name")

      First Name  Age        City
    0      Alice   25    New York
    1        Bob   30      London
    2        Sam   35       Paris
    3    Charlie   30  Pittsburgh
    4        Tom   42   Rochester

And make new columns:

.. code-block:: python

    # Make a new column from scratch:
    df["Favorite Color"] = ["Red", "Green", "Blue", "Pink", "Yellow"]

    # Or using existing data
    df["Dog Years"] = df["Age"] / 7.0

    df

Data Aggregation
-----------------

We can also aggregate the data. The most common aggregation for us would be calculating averages
(:code:`mean`), but others like sum, median, etc are available too.

.. code-block:: pycon

    >>> df.mean(numeric_only=True)

    Age          32.400000
    Dog Years     4.628571
    dtype: float64

Note the :code:`numeric_only=True`. Our dataframe has columns that contain strings, which don't make sense to
average and would cause the program to crash. By adding :code:`numeric_only=True` pandas will filter out
string columns before performing the average.

In the case of our scouting data, we often want to calculate averages **per team**, and not simply a global
average for all teams. We can do that by grouping by a column first:

.. code-block:: pycon

    >>> df.groupby("Name").mean(numeric_only=True)

              Age
    Name
    Alice    25.0
    Bob      25.5
    Charlie  30.0
    Sam      35.0
    Tom      42.0


Exercises
_________

Now that you've seen the core pandas concepts, put them to use on real data. Open
:code:`source/CL1_pandas_codelab.ipynb`, which loads actual FRC scouting data from
:code:`source/data/scouted_data.csv`, and fill in each numbered cell as described below.
