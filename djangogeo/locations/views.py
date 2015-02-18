from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Location


class LocationView(TemplateView):
    template_name = 'locations.html'


class LocationGeoJSONLayerView(GeoJSONLayerView):
    model = Location
    properties = ['wmoid', 'name']