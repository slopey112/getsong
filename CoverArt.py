from urllib.request import urlopen
from urllib.parse import quote
import xml.etree.ElementTree as ET
from json import loads
from sys import argv

artist = argv[1]
album = argv[2]

def main():
    query = 'title:{}%20AND%20artist:{}'.format(quote(album), quote(artist))
    xml_response = urlopen('http://musicbrainz.org/ws/2/release/?query=' + query).read()
    root = ET.fromstring(xml_response)
    for release in root[0]:
        if release[0].text == album:
            mbid = release.attrib['id']
            break

    json_response = urlopen('http://coverartarchive.org/release/' + mbid).read()
    parsed_json = loads(json_response)
    cover_art = parsed_json['images'][0]['thumbnails']['large']
    print(cover_art)

if __name__ == '__main__':
    main()
