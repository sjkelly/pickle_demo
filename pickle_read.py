#! /usr/bin/env python

import pickle
from slidedata import * # Import SlideData class from slidedata.py

f = open("slide_data.txt", "r") # Open file to read

mySlideData = pickle.load(f) # load pickle data

print(mySlideData.profiles) # This should be the data we input on line 10 of pickle_write.py
