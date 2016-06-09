from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.gis.maps.google.gmap import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GEvent


def googleMapShowUtils(points):
    markers = []
    for point in points:
        marker = GMarker('POINT(%s %s)' % (point['lng'], point['lat']))
        event = GEvent('click', 'function() { location.href = "%s"}' % point['href'])
        marker.add_event(event)
        markers.append(marker)
    google = GoogleMap(center=(0,0), zoom=1, markers=markers,
                       key=settings.GOOGLE_MAPS_API_PASSWORD)
    return google
    
#add search utility here