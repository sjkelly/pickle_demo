#! /usr/bin/env python

import pickle
from slidedata import * # Import SlideData class from slidedata.py

# Demonstrate how to pickle an object

f = open("slide_data.txt", "w") # Open dump file

mySlideData = SlideData([1.0102830, 6.000, 5.5, 7.7]) # Create a SlideData object

pickle.dump(mySlideData, f) # Dump the SlideData object we just created

f.close() # close file

