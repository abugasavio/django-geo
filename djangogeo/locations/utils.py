import csv
from .models import Location


def dms2dec(value):
    """
    Degres Minutes Seconds to Decimal degres
    """
    degres, minutes, seconds = value.split()
    seconds, direction = seconds[:-1], seconds[-1]
    dec = float(degres) + float(minutes)/60 + float(seconds)/3600
    if direction in ('S', 'W'):
        return -dec
    return dec


def data():
    csv_file = 'new.flatfile.txt'

    reader = csv.DictReader(open(csv_file, 'rb'), delimiter="\t")
    for line in reader:
        lng = dms2dec(line.pop('Longitude'))
        lat = dms2dec(line.pop('Latitude'))
        wmoid = int(line.pop('StationId'))
        name = line.pop('StationName').title()
        geom = dict(type='Point',
                coordinates=[lng, lat])
        Location(wmoid=wmoid, name=name, geom=geom).save()