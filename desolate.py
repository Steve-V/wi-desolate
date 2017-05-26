#!/usr/bin/env python

#import os
from wisdata import allWisconsinAirportsList
from geopy.distance import great_circle, vincenty

def allWisconsinPoints():
    wisLatitudes = np.arange(42,44,0.01)
    wisLongitudes = np.arange(-87,-90,-0.01)
    return itertools.product(wisLongitudes,wisLatitudes)

def main():
    myButt = allWisconsinAirportsList()
    reversedButt = [(b,a) for a,b in myButt]
    print(myButt[4])
    print(reversedButt[4])
    print(myButt[52])
    print(reversedButt[52])
    print( vincenty(reversedButt[52],reversedButt[4]).miles )


main()
