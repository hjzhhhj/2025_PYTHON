import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element('movie')
title = SubElement(root, 'title')
title.text = '트랜스포머'
genre = SubElement(root, 'genre')
genre.text = 'SF'
rating = SubElement(root, 'rating')
rating.text = '8'

ET.ElementTree(root).write('./파일처리/movie.xml', encoding='utf-8', xml_declaration=True)

# <?xml version='1.0' encoding='utf-8'?>
# <movie><title>트랜스포머</title><genre>SF</genre><rating>8</rating></movie>