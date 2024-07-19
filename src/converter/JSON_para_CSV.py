import json

if __name__ == "__main__":
    try:
        with open("caminho_do_arquivo.json", "r") as f:
            data = json.loads(f.read())
        convertido = ",".join([*data[0]])
        for obj in data:
            convertido += f'\n{obj["info_UM"]},{obj["info_DOIS"]},{obj["info_TRES"]}'
        with open("convertido.csv", "w") as f:
            f.write(convertido)
    except Exception as ex:
        print(f"Erro: {str(ex)}")
