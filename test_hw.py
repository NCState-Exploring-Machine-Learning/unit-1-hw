'''





Do NOT edit this file unless told to do so by your instructor.









'''


import random

import string
import statistics
import sys

import test_utils
sys.meta_path.append(test_utils.NotebookFinder())
loaded = test_utils.NotebookLoader("./unit_1_hw.ipynb")
loaded.load_module("unit_1_hw")

import unit_1_hw

def test_some_test():
    return False

'''
Unit 1 Hw 

Hidden tests should take up about 20%
of the score. 
- How much repetition do I want there to be?
- How do I set the score, based on function calls and
keep each call by itself. 

Numpy

- Create an array from a list 
- Create an array of 1s of a specific size
- Return the shape of an array
- Return the 2nd dimension of an array
- Perform math on the array
	- add 
	- subtract
	- multiply
	- change data type
- Grap specific indexes from an existing list
- Use documentation 
	- check if an array is empty
	- all 
	- any
	- reshape an array
	- transpose an array
Secret Tests
- Take average
- Take variance 
- Read from a file
- Concat arrays
- Write to a file


Pandas 
- Create a series from a list
- Create a dataframe from a numpy array
- Categorize the arrays
- Call the arrays based on the categories
- Viewing the data
- Removing missing data

Hidden Tests
- Manipulating the data - tranpose, sort, 
- Replace missing data with average of other data
set


Matplotlib
- How do I test this? I like the idea of trying to replicate the graphic. 
	- Can make a rubric for this too
	- This is acutally a great idea, I can cross check
	the values as well. 


'''