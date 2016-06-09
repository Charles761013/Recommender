from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from rango.forms import UserProfileForm
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.gis.maps.google.gmap import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GEvent

def about(request):
    return render(request, 'rango/about.html', {})
    #return HttpResponse("This is the about page.")

@login_required    
def index(request):
    if request.method == 'POST':
        #handle search result here!
        current_user = request.user
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = current_user
            profile.history = request.POST['history']
            profile.save()
            #call search utility function!
            return redirect('/rango/map')
        else:
            print form.errors  
        
    else:
        form = UserProfileForm()
        #also give query history
    context_dict = {'form':form}
    return render(request, 'rango/index.html', context_dict)
        
    
#for test    
def google_map(request):
    points = [
        {'lat':'35.42',     'lng': '139.42', 'href':'http://en.wikipedia.org/wiki/Tokyo'},
        {'lat':'51.30',     'lng':   '0.73', 'href':'http://en.wikipedia.org/wiki/London'},
        {'lat':'40.43',     'lng': '-74.0',  'href':'http://en.wikipedia.org/wiki/New_York_City'},
        {'lat':'34.03',     'lng':'-118.15', 'href':'http://en.wikipedia.org/wiki/Los_Angeles'},
        {'lat':'36.774402', 'lng':'-119.755405', 'href':'http://en.wikipedia.org/wiki/Fresno'},]
    markers = []
    for point in points:
        marker = GMarker('POINT(%s %s)' % (point['lng'], point['lat']))
        event = GEvent('click', 'function() { location.href = "%s"}' % point['href'])
        marker.add_event(event)
        markers.append(marker)
    google = GoogleMap(center=(0,0), zoom=1, markers=markers,
                       key=settings.GOOGLE_MAPS_API_PASSWORD)
    return render(request, 'rango/google_map.html', {'google': google})
    
