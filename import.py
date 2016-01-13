from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import os, xml

dir = './roms/mame'
fileList = os.listdir(dir)

tree = ET.parse('data/MAME.xml')

for file in fileList:
    filename, fileExt = os.path.splitext(file)
    print(filename)
    cases = tree.findall(".//game[@name='" + filename + "']")
    for item in cases:
        print(xml.etree.ElementTree.dump(item))

# dom = parse('data/MAME.xml') # parse an XML file by name

# def getGameElements(domRoot):
#     return domRoot.getElementsByTagName('game')

# for game in getGameElements(dom):
#     print game.toxml()
