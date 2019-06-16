import os
from xml.etree import ElementTree as et
dataFile = input('What file do you want to use for data? ')
while not os.path.isfile(dataFile):
    dataFile = input('What file do you want to use for data? ')
file = open(dataFile, 'r')
n = 0
headers = []

# Colour schemes #
# background = '#009639'
# mapBackground = '#E8EDEE'
# mapColour = '#006747'
# titleBar = '#006747'
# scoreBox = '#78BE20'
# titleText = 'white'
# scoreText = '#231F20'

background = '#005EB8'
mapBackground = 'white'
mapColour = '#003087'
titleBar = '#003087'
scoreBox = '#41B6E6'
titleText = 'white'
scoreText = 'white'

if input('Do you want to use your own colour scheme? (y or n) ') == 'y':
    background = input('What colour ')

for line in file.read().splitlines():
    n = n + 1
    if n == 1:
        headers = line.split(',')
    else:
        data = line.split(',')
        code = data[0]
        name = data[1]
        print(code)
        f = open('cards/' + code + '.svg', 'w')
        f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
        f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
        f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
        f.write('<svg height="1800" version="1.1" width="1800" xmlns="http://www.w3.org/2000/svg">')
        f.write('<defs>')
        f.write('<style type="text/css">')
        f.write('@font-face {')
        f.write('font-family: \'Frutiger\';')
        f.write('font-style: normal;')
        f.write('font-weight: normal;')
        f.write('src: local(\'Frutiger\'), url(\'../fonts/Frutiger.woff\') format(\'woff\');')
        f.write('}')
        f.write('@font-face {')
        f.write('font-family: \'Frutiger Bold\';')
        f.write('font-style: normal;')
        f.write('font-weight: normal;')
        f.write('src: local(\'Frutiger Bold\'), url(\'../fonts/Frutiger_bold.woff\') format(\'woff\');')
        f.write('}')
        f.write('        </style>')
        f.write('    </defs>')
        f.write('    <rect x="20" y="20"  width="250" height="350" rx="15" fill="' + background + '" />')
        f.write('    <rect x="35" y="35"  width="220" height="145" rx="15" fill="' + mapBackground + '" />')
        
        tree = et.parse('maps/' + code + '.svg')
        svg = tree.getroot()
        svg.set('x','35')
        svg.set('y','50')
        polygon = svg.find('{http://www.w3.org/2000/svg}polygon')
        polygon.set('fill', mapColour)
        polygon.set('stroke', mapColour)
        f.write(et.tostring(svg).decode())
        
        if len(name) <= 15:
            fontsize = 30
        elif len(name) <= 25:
            fontsize = 20
        else:
            fontsize = 16
        f.write('    <rect x="20" y="50"  width="250" height="25"  rx="0"  fill="' + titleBar + '" fill-opacity="0.8" />')
        f.write('    <text x="145" y="70" text-anchor="middle" font-family="Frutiger" font-weight="bold" font-size="'+str(fontsize)+'" fill="' + titleText + '">' + name + '</text>')
        f.write('    <rect x="35" y="195" width="220" height="160" rx="15" fill="' + scoreBox +  '"/>')
        f.write('    <g font-family="Frutiger" font-size="15" fill="' + scoreText + '">')
        f.write('        <g> <text x="45" y="218">' + headers[2] + '</text> <text x="245" y="218" text-anchor="end">' + data[2] + '</text> </g>')
        f.write('        <g> <text x="45" y="243">' + headers[3] + '</text> <text x="245" y="243" text-anchor="end">' + data[3] + '</text> </g>')
        f.write('        <g> <text x="45" y="268">' + headers[4] + '</text> <text x="245" y="268" text-anchor="end">' + data[4] + '</text> </g>')
        f.write('        <g> <text x="45" y="293">' + headers[5] + '</text> <text x="245" y="293" text-anchor="end">' + data[5] + '</text> </g>')
        f.write('        <g> <text x="45" y="318">' + headers[6] + '</text> <text x="245" y="318" text-anchor="end">' + data[6] + '</text> </g>')
        f.write('        <g> <text x="45" y="343">' + headers[7] + '</text> <text x="245" y="343" text-anchor="end">' + data[7] + '</text> </g>')
        f.write('    </g>')
        f.write('</svg>')
        f.close()

file.close()

print(headers)
print("Done " + str(n))

