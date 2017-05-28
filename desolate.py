#!/usr/bin/env python

#import os
from wisdata import allWisconsinAirportsList
from geopy.distance import great_circle, vincenty
from tqdm import tqdm
import numpy, itertools

def allWisconsinPoints(shortList=False):
    '''Return every possible latitude and longitude coordinate occurring in Wisconsin's bounding box.
    Ordinarily returns lat/long, but passing reversed=True returns long/lat
    Passing shortList only returns a handful of points, for testing purposes
    TODO: Make this function not return coordinates that don't satisfy inWisconsinBorders()
    '''

    latstep = 1.0 if shortList else 0.1
    lonstep = -1.0 if shortList else -0.1

    wisLatitudes = numpy.arange(42,44,latstep)
    wisLongitudes = numpy.arange(-87,-90,lonstep)
    return itertools.product(wisLatitudes,wisLongitudes) 
    # return tertools.product(wisLongitudes,wisLatitudes) # if for some reason we ever want to use long-lat ordering

def distanceToNearestAirport(point, allAirports):
    '''Given a point, determine the distance to the nearest airport'''
    return min( [great_circle(point,eachAirport).nautical for eachAirport in allAirports] )

def getDistance(point, airport):
    return great_circle(point,airport).nautical

def main():

    allAirports = allWisconsinAirportsList()

    print( max( [(eachpoint, distanceToNearestAirport(eachpoint, allAirports) ) for eachpoint in tqdm( allWisconsinPoints(), total=600 ) ], key=lambda item: item[1] ) ) 



    

main()
