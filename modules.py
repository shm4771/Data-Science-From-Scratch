#we can use broad range of features and functions by importing inbuilt or 3rd party modules

#regular expression modules to find pattern and work with text data
import re  
my_regex = re.compile("[0-9]+", re.I)

print(my_regex)

##we can import module with other name
# such as import re as regex

import matplotlib.pyplot as pylot

#importing full content of module
from re import *