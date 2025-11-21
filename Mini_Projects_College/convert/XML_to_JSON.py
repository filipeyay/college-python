import json
import xmltodict

with open("converted.xml") as file_xml:
    data = xmltodict.parse(file_xml.read)
    file_xml.close()
    json_converted = json.dumps(data)

    with open("converted.json", "w") as file_json:
        file_json.write(json_converted)
        file_json.close()
