#!/usr/bin/env python

#import os
from wisdata import wisconsinBorders
from geopy.distance import great_circle
from tqdm import tqdm
from shapely.geometry import Polygon, Point
import numpy, itertools, pickle

def allWisconsinPoints(shortList=False):
    '''Return every possible latitude and longitude coordinate occurring in Wisconsin.
    Passing shortList results in a much coarser grid, for testing purposes
    '''

    # What should we use for latitude/longitude increments?
    latstep = 1.0 if shortList else 0.1
    lonstep = -1.0 if shortList else -0.1

    # Use shapely to build a polygon representing the land area of Wisconsin
    # I used Google Earth to get a KML polygon of Wisconsin's borders and then manually edited the file to get just the coordinates out of the KML. A utility to do this wouldn't be a bad thing.
    borders = Polygon(wisconsinBorders())

    # Don't forget to update this to be the actual bounding lat/long box for the state
    wisLatitudes = numpy.arange(42,47,latstep)
    wisLongitudes = numpy.arange(-87,-93,lonstep)

    # Return all points that meet the criteria for being in Wisconsin
    return (i for i in itertools.product(wisLatitudes,wisLongitudes) if Point(i[0],i[1]).within(borders) )

def distanceToNearestAirport(point, allAirports):
    '''Given a point, determine the distance to the nearest airport
    Point is a tuple of the following format: (latitude, longitude)
    allAirports is an OrderedDict containing at least value['lat'] and value['long']
    See here for more on OrderedDicts: https://docs.python.org/3/library/csv.html
    great_circle is provided by geopy, nautical is unnecessary but nice for verification'''
    return min( [great_circle(point, (eachAirport['lat'],eachAirport['long'])).nautical for eachAirport in allAirports] )

def main():

    '''Figure out the place in Wisconsin that is furthest from the nearest airport'''

    # Airport data is stored on disk as a pickled OrderedDict in the working directory
    allAirports = pickle.load(open('airportpickle','rb'))

    # this list comprehension walks through allWisconsinPoints and returns a list of tuples: (the distance from a point to the nearest airport, and the point itself)
    # the max function pulls out only the highest-distance value from the list of tuples
    # tqdm is for timing the loop and showing a progress bar
    # When this listcomp finishes, we have our desired point.
    # This listcomp is where all of the slowdown happens
    howfar, furthestpoint = ( max( ((distanceToNearestAirport(eachpoint, allAirports), eachpoint ) for eachpoint in tqdm( allWisconsinPoints(), total=1675 ) ) ) ) 

    #Since i want to know which airport is nearest to the point, we run our known furthest point back through the distance algorithm again. 
    # This listcomp takes our known furthest point and runs the calculation once more to find the nearest airport.
    # It outputs a tuple of the following format: (airportname, distance)
    # key=lambda item:item[1] is used to tell min to sort based on the second item in the tuple, in this case, distance
    closestairport = min( [(eachAirport['name'],great_circle(furthestpoint,(eachAirport['lat'],eachAirport['long'])).nautical) for eachAirport in allAirports], key=lambda item: item[1] )

    # Output!
    print("Latitude of most desolate point: {} \n"
            "Longitude of furthest point: {} \n"
            "Nearest airport to point: {}\n"
            "Distance from point to airport: {}\n"
            .format( furthestpoint[0] , furthestpoint[1] , closestairport[0] , closestairport[1]) )

main()
