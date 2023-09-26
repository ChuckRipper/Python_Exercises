import xml.etree.ElementTree as ET

tree = ET.parse('wejscie.xml')
root = tree.getroot()

args = []
for child in root:
    class_name = child.tag
    kwargs = child.attrib
    args.append(globals()[class_name](*child.text.split(), **kwargs))

wyjscie = globals()[root.tag](*args)
