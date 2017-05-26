#!/usr/bin/env python

#import os
from wisdata import allWisconsinAirportsList
from geopy.distance import great_circle, vincenty
import numpy, itertools

def allWisconsinPoints(latlong=True, shortList=False):
    '''Return every possible latitude and longitude coordinate occurring in Wisconsin's bounding box.
    Ordinarily returns lat/long, but passing reversed=True returns long/lat
    Passing shortList only returns a handful of points, for testing purposes
    TODO: Make this function not return coordinates that don't satisfy inWisconsinBorders()
    '''

    latstep = 1.0 if shortList else 0.1
    lonstep = -1.0 if shortList else -0.1

    wisLatitudes = numpy.arange(42,44,latstep)
    wisLongitudes = numpy.arange(-87,-90,lonstep)
    return itertools.product(wisLatitudes,wisLongitudes) if latlong else itertools.product(wisLongitudes,wisLatitudes)

def distanceToNearestAirport(point, allAirports):
    '''Given a point, determine the distance to the nearest airport'''
    return min( [getDistance(point, eachAirport) for eachAirport in allAirports] )

def getDistance(point, airport):
    # print(point, airport,vincenty(point,airport).nautical)
    return great_circle(point,airport).nautical

def main():
    # myButt = allWisconsinAirportsList(True)
    # reversedButt = allWisconsinAirportsList(False)
    # print(myButt[4])
    # print(reversedButt[4])
    # print(myButt[52])
    # print(reversedButt[52])
    # print( vincenty(reversedButt[52],reversedButt[4]).nautical )

    # print( getDistance(reversedButt[52],reversedButt[4] ) )

    allAirports = allWisconsinAirportsList()

    # point = (45.0,-89.0)
    # point2 = allAirports[3]

    # print( getDistance(point,point2))

    # print( min([getDistance(point, eachAirport) for eachAirport in allAirports] ) )

    print( max( [distanceToNearestAirport(eachpoint, allAirports) for eachpoint in allWisconsinPoints()] ) )



    

main()
