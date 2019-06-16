from xml.etree import ElementTree as et
import math

def deg2rad(a):
    return a / (180 / math.pi)

EARTH_RADIUS = 6378137

def lat2y_m(lat):
    return math.log(math.tan( deg2rad(lat) / 2 + math.pi/4 )) * EARTH_RADIUS
def lon2x_m(lon):
    return deg2rad(lon) * EARTH_RADIUS

doc = et.parse("boundaries.kml")
root = doc.getroot()
for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
    code = placemark.find('.//{http://www.opengis.net/kml/2.2}SimpleData[@name="ctyua16cd"]').text
    latlons = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates').text
    points = ''
    minx = miny = float("inf")
    maxx = maxy = float("-inf")
    for latlon in latlons.split(' '):
        lon,lat = latlon.split(',')
        x = int(lon2x_m(float(lon)))
        y = -1 * int(lat2y_m(float(lat)))
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        points = points + ' ' + str(x) + ',' + str(y)
    
    width = maxx-minx
    height = maxy-miny
    
    svg = et.Element('svg', width='220', height='115', viewBox=str(minx) + ' ' + str(miny) + ' ' + str(width) + ' ' + str(height), version='1.1', xmlns='http://www.w3.org/2000/svg')
    polygon = et.SubElement(svg, 'polygon', stroke='#003087', fill='#003087', points=points)
    polygon.set('stroke-width', str((width + height)/1000))
    
    # ElementTree 1.2 doesn't write the SVG file header errata, so do that manually
    f = open('./maps/' + code + '.svg', 'w')
    f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
    f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
    f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
    f.write(et.tostring(svg).decode())
    f.close()
    
    print code, minx, miny, maxx, maxy, points
