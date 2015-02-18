from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView


class LocationView(TemplateView):
    template_name = 'locations.html'


class LocationGeoJSONLayerView(GeoJSONLayerView):
    model =