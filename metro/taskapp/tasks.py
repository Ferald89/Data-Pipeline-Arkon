"""Celery django"""

# Celery
from celery.decorators import task, periodic_task

# Utils
from datetime import timedelta
import requests

# Models
from metro.location.models import Unit, District

# geopy
from geopy.geocoders import Nominatim

def getDistrict(point):
    geolocator = Nominatim(user_agent="hpp")
    location = geolocator.reverse(point, timeout=10)
    # Get a list of adress to get the district
    location_list = location.raw["display_name"].split(", ")
    # The district is localed in position before "Ciudad de México" or "Estado de México"
    if "Ciudad de México" in location_list:
        index = location_list.index('Ciudad de México') - 1
    if "Estado de México" in location_list:
        index = location_list.index('Estado de México') - 1
    district = location_list[index]
    return district

@periodic_task(name="fetch_data", run_every=timedelta(minutes=10))
def periodic_refresh():
    # Get data from API CDMX
    try:
        url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?' + \
            'resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=300'
        units_fetch = requests.get(url=url).json()['result']['records']
    except NameError:
        return("something's wrong "+ NameError)

    # iterate each data
    for unit_fetch in units_fetch:
        # if there is a data into "position_latitude" data can be use it
        if unit_fetch['position_latitude']:
            try:
                district_name = getDistrict(unit_fetch['geographic_point'])
            except NameError:
                return ("something's wrong "+ NameError)
            # Save data into DB
            # Get or create a Disctrict object
            district, created = District.objects.get_or_create(name=district_name)
            district.name = district_name
            district.save()
            # Get or create a Unit object
            unit, created = Unit.objects.get_or_create(id=unit_fetch['id'])
            unit.latitude = float(unit_fetch['position_latitude'])
            unit.longitude = float(unit_fetch['position_longitude'])
            unit.district = district
            unit.save()
    return "SUCCESS.!"
