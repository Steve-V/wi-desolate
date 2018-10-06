#!/usr/bin/env python

from geopy.distance import great_circle
from shapely.geometry import Polygon, Point
import numpy, itertools

def buildGrid():
    '''Return a grid of all latitude and longitude coordinates in the state, at whatever resolution. One of these will be our solution point.
    '''

    # Use shapely to build a polygon representing the land area of the state
    # For states like Colorado this is trivial but for non-square states we would import the coordinate list from a separate file
    stateBorders = [
        (-109.0448,37.0004), 
        (-102.0424,36.9949), 
        (-102.0534,41.0006), 
        (-109.0489, 40.9996), 
        (-109.0448, 37.0004)]
    borders = Polygon( stateBorders )

    # This represents the bounding latitude and longitude of the state. With a state like Colorado this approximates the actual borders, but with a state such as Florida this would also contain much ocean.
    # Step by a full degree for a coarse grid or less (such as a tenth of a degree) for a finer solution
    latstep = 1.0
    lonstep = -1.0
    latitudeBox = numpy.arange(35,43,latstep)
    longitudeBox = numpy.arange(-101,-110,lonstep)

    # Return all points that meet the criteria for being within the actual state borders.  For example, remove all ocean from Florida, leaving only land area.
    return (i for i in itertools.product(latitudeBox,longitudeBox) if Point(i[1],i[0]).within(borders) )

def distanceToNearestAirport(point, allAirports):
    '''Given a point, determine the distance to the nearest airport
    Point is a tuple of the following format: (latitude, longitude)
    allAirports is an OrderedDict containing at least value['lat'] and value['long']
    See here for more on OrderedDicts: https://docs.python.org/3/library/csv.html
    great_circle is provided by geopy, nautical is to make the answer easy to verify using standard aeronautical charts'''
    return min( [great_circle(point, (eachAirport['lat'],eachAirport['long'])).nautical for eachAirport in allAirports] )

def main():

    '''Figure out the place in a state that is furthest from the nearest airport'''

    # Airport data would be stored on disk as a pickled OrderedDict in the working directory. This is a small subset.
    allAirports = [
        {'long': -104.8493156, 'lat': 39.57013424, 'code': 'APA'},
        {'long': -104.6731767, 'lat': 39.86167312, 'code': 'DEN'},
        {'long': -104.5376322, 'lat': 39.78420646, 'code': 'FTG'},
        {'long': -105.1172046, 'lat': 39.90881199, 'code': 'BJC'}
    ]

    # this list comprehension walks through the grid of points and creates a list of tuples: (the distance from a provided point to the nearest airport, and the point itself)
    # the max function takes the highest-distance value from the list of tuples, which is our answer

    howfar, furthestpoint = (max(
        ((distanceToNearestAirport(eachpoint, allAirports), eachpoint )
        for eachpoint in buildGrid() ) ) ) 

    #Since i also want to know which airport is nearest to the point, we run our known furthest point back through the distance algorithm again. 
    # It outputs a tuple of the following format: (distance, airportname)
    result = min( [
        (great_circle(furthestpoint, (eachAirport['lat'], eachAirport['long']) ).nautical, eachAirport['code'])
        for eachAirport in allAirports] )

    # Output!
    print("Latitude of most desolate point: {} \n"
            "Longitude of furthest point: {} \n"
            "Nearest airport to point: {}\n"
            "Distance from point to airport: {}\n"
            .format( furthestpoint[0] , furthestpoint[1] , result[1] , result[0]) )

main()
