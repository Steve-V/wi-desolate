#!/usr/bin/env python

#import os
from wisdata import allWisconsinAirportsList, wisconsinBorders
from geopy.distance import great_circle, vincenty
from tqdm import tqdm
from shapely.geometry import Polygon, Point, shape
import numpy, itertools

def allWisconsinPoints(shortList=False):
    '''Return every possible latitude and longitude coordinate occurring in Wisconsin.
    Passing shortList only returns a handful of points, for testing purposes
    '''

    latstep = 1.0 if shortList else 0.1
    lonstep = -1.0 if shortList else -0.1
    borders = Polygon(wisconsinBorders())

    wisLatitudes = numpy.arange(42,47,latstep)
    wisLongitudes = numpy.arange(-87,-93,lonstep)
    return (i for i in itertools.product(wisLatitudes,wisLongitudes) if Point(i[0],i[1]).within(borders) )
    # return itertools.product(wisLatitudes,wisLongitudes)
    # return tertools.product(wisLongitudes,wisLatitudes) # if for some reason we ever want to use long-lat ordering

def distanceToNearestAirport(point, allAirports):
    '''Given a point, determine the distance to the nearest airport'''
    return min( [great_circle(point,eachAirport).nautical for eachAirport in allAirports] )

def main():

    allAirports = allWisconsinAirportsList()

    print( max( [(eachpoint, distanceToNearestAirport(eachpoint, allAirports) ) for eachpoint in tqdm( allWisconsinPoints(), total=325 ) ], key=lambda item: item[1] ) ) 

main()
