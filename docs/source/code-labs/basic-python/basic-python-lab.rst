
Intro to Python Codelab
=======================

In this codelab you will make a basic calculator app in a Jupyter Notebook

.. note:: If you have not set up PyCharm or cloned the mono repo you can use this `online editor <https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb>`_ and copy and paste the code below


.. collapse:: Click to reveal the code

    
    .. code-block::
        
        class Calculator:

            def add(x, y):
                return x + y


        def main():
            number = input("Input a number: ")
            print(f"You entered {number}")

        main()




Part One
________

1. Run the existing calculator
------------------------------

2. Edit the line printed. 
-------------------------
Change the line in the code to anything else. For example, to print `Alex typed in the number`

3. Create a calculator object
-----------------------------
Python uses objects, which are structures that contain data and perform functions.

In Python, the syntax (pattern of typing code that can be read by what builds it) of creating an object is
:code:`nameOfMyObject = new Object()`

The object you will create is a :code:`Calculator`. Follow the pattern above to create a :code:`Calculator`
called `myCalculator`.

5. Use the add function of the calculator
-----------------------------------------
Objects can call methods, which are functions that operate on inputs. We call the inputs arguments. 
To call a function, type a dot after the object name, and then put the inputs in the parentheses. 
:code:`myCalculator.add(3,4)`

Try adding 5+6 using myCalculator. Print out the result. 


6. Add functions to Calculator.java
-----------------------------------
Following the pattern of :code:`add` add more useful functions to :code:`Calculator.java`. Java operators are similar 
to what you use on your graphing calculator. Ex:

1. subtract: x-y

2. multiply: x*y

3. divide: x/y


Bonus: Call your functions in RunCalculator.java 
------------------------------------------------
This can potentially be a challenging exercise as it involves putting together several concepts
If you find yourself stuck, either ask for help from your fellow students, mentors, or move onto the Part 2 and come back later. 
Useful concepts:


1. conditions: a statement that is either true or false. To check equality, Java uses two equal signs :code:`(==)` Ex)

2. :code:`(3 == 4)` a false statement

3. :code:`(4 == 4)` a true statement

4. :code:`('a' == 'b')` a false statement
