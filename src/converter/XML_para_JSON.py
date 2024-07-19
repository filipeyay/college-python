import json
import xmltodict

with open("converter.xml") as arquivo_xml:
    data = xmltodict.parse(arquivo_xml.read)
    arquivo_xml.close()
    json_convertido = json.dumps(data)

    with open("convertido.json", "w") as arquivo_json:
        arquivo_json.write(json_convertido)
        arquivo_json.close()
