import xml.etree.ElementTree as ET
import codecs

f = codecs.open("./파일처리/movie.xml", "r", "utf-8")
str = f.read()
tree = ET.ElementTree(ET.fromstring(str))
root = tree.getroot()
print(root.tag)

for child in root:
    print("tag:", child.tag, ", ", child.text)

f.close()    

# movie
# tag: title ,  트랜스포머
# tag: genre ,  SF
# tag: rating ,  8